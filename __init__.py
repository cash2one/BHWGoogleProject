# DO NOT EDIT THIS FILE EXCEPT AS //depot/google3/tools/google3__init__.py
# Once you edit there, make sure you copy it to //depot/google3/__init__.py
# and submit both files in the same change.

# Copyright 2006 Google Inc. All Rights Reserved.
#
# This file sets up import mechanisms for all Google3 programs.  Every
# Google3 program should import this file.  If the program uses
# third-party modules such as MySQLdb, it should import this file
# before importing any third-party code.
#
# The public API provided by this module:
#
#   basedir: The directory containing this file.
#
# Implementation notes:
#
# This module makes use of 'meta-import hooks', as described in PEP 302.

import os
import sys
import warnings

########################################################################
# Support "union" imports for thin clients, that merge together
# several directory trees into a single "virtual" directory tree for
# Python imports.
########################################################################

def _SetupPath(old_path, this_dir):
  """Setup package import path for Google3.

  old_path: List of directories.
  this_dir: Directory that this package is loaded from.

  Allow the google3 package to import subpackages and modules from
  several different directory trees: The standard perforce client, the
  READONLY directory maintained by gcheckout, and /home/build.

  TODO(dgreiman): /home/build is a bit of a can of worms: Sometimes
  you want to take things from /home/build and sometimes you don't.
  I.e. in a par file you don't.  In a release branch you don't.  On a
  production machine you don't.  Eventually we want to give people a
  way to conditionally add /home/build to their path, or not.  For
  now, we try to prevent the problem from getting any bigger without
  breaking the existing programs that depend on it.  For this reason,
  we don't take third-party modules from /home/build and we don't do
  directory merging with /home/build, but we do allow importing
  modules directly under google3 from /home/build.

  TODO(dgreiman): Add bin/ and genfiles/ once the build tree layout is
  rearranged to allow this to work.  Basically remove
  directory-doubling for .py generated files.

  This code sets the top-level path, and relies on
  Google3MetaImportHook to propagate the path to subpackages.

  Returns a list of three things:

  The first is the new package path, consisting of the old package
  path reordered and with extra directories inserted.

  The second is a subset of the first, consisting of all the google3
  directories that we might want to take third-party modules from.

  The third is a boolean saying whether a READONLY directory was
  found.  If true, the 'directory merging' functionality will be
  activated.  Note that this will never be true if running from a .par
  file, since 'client_root' will be '/somedir/somefile.par' and thus
  '/somedir/somefile.par/READONLY' will not be a directory.

  """

  # If running in a stateless client, take packages from
  # <clientroot>/READONLY/google3/.  If already in READONLY dir, take
  # packages from <clientroot>/google3/.  The read-write client should
  # always be first in precedence.
  this_dir = os.path.abspath(this_dir)
  parent_dir = os.path.dirname(this_dir)

  # If this program started inside the readonly tree, the path may
  # either be the "short" symlink
  # /home/<user>/<p4client>/READONLY/google3, or the actual "long"
  # directory name
  # /usr/local/google/home/<usr>/<p4client>/READONLY/stateless-client/google3
  # This code must match the paths used in
  # google3/tools/perforce/stateless_sync.py
  if os.path.basename(parent_dir) == 'READONLY':  # "short"
    client_root = os.path.dirname(parent_dir)
    readwrite_dir = os.path.join(client_root, 'google3')
    readonly_dir = os.path.join(client_root, 'READONLY', 'google3')
    have_readonly_dir = 1
  elif (parent_dir.endswith('/READONLY/stateless-client') and
        parent_dir.startswith('/usr/local/google/')):  # "long"
    # We make sure client_root starts with /
    client_root = parent_dir[len('/usr/local/google'):
                             -len('/READONLY/stateless-client')]
    readwrite_dir = os.path.join(client_root, 'google3')
    # Note that readonly and readwrite have different parents
    readonly_dir = os.path.join(parent_dir, 'google3')
    have_readonly_dir = 1
  else:
    client_root = parent_dir
    readwrite_dir = os.path.join(client_root, 'google3')
    readonly_dir = os.path.join(client_root, 'READONLY', 'google3')
    have_readonly_dir = os.path.isdir(readonly_dir)

  # The readwrite_dir may actually be in a zipfile, so we don't check
  # for existence.  We do however check the readonly dir, since it
  # will always be a real directory.
  google3_path = [readwrite_dir]
  if have_readonly_dir:
    google3_path.append(readonly_dir)

  package_path = google3_path[:]
  
  # Fall back to /home/build.
  #
  # We test for the existence of os.R_OK because the jython
  # implementation of os doesn't have it.
  if (not os.environ.get("GOOGLE3_NO_HOME_BUILD") and
      not _RunningProgramIsAParFile()):
    if not hasattr(os, 'R_OK') or os.access('/home/build/google3/.', os.R_OK):
      package_path.append('/home/build/google3')
    else:
      package_path.append('/home/build/nonconf/google3')

  # The existing path shouldn't have anything else, but just in case,
  # keep unexpected items.
  for pathdir in old_path:
    if pathdir not in package_path:
      package_path.append(pathdir)

  return (package_path, google3_path, have_readonly_dir)


#_A list of directories that should not be propagated to
# subpackages.  This is basically a hack while we figure out a good
# solution to /home/build.

_NO_INHERIT = [
  '/home/build/google3',
  '/home/build/nonconf/google3',
  ]


def _FixupParentPathByName(module_name):
  """Given a module name, find its parent package, and fix that package's path.

  module_name: Fully-qualified module name

  """

  # Find parent and grandparent package.
  lastdot = module_name.rfind('.')
  if lastdot == -1:
    return
  second_lastdot = module_name.rfind('.', 0, lastdot)
  if second_lastdot == -1:
    return
  parent_name = module_name[:lastdot]
  parent = sys.modules.get(parent_name)
  grandparent_name = module_name[:second_lastdot]
  grandparent = sys.modules.get(grandparent_name)

  if parent and grandparent:
    _MaybeInheritPath(parent_name, parent, grandparent)


def _FixupPackagePathByObject(package):
  """Given a package object, fixup its path if necessary.

  package: Module object

  A no-op if called on a non-package module.
  
  """

  # Is it even a package?
  if not hasattr(package, '__path__'):
    return
  
  package_name = getattr(package, '__name__', None)
  # Some special modules don't have names, ignore them
  if not package_name:
    return
  
  # Find package's parent if any
  lastdot = package_name.rfind('.')
  if lastdot == -1:
    return
  package_parent_name = package_name[:lastdot]
  package_parent = sys.modules.get(package_parent_name)

  if package_parent:
    _MaybeInheritPath(package_name, package, package_parent)


def _MaybeInheritPath(package_name, package, package_parent):
  """Given a package, fixup its path if necessary.

  package_name: Fully-qualified module name
  package, package_parent_name: Module objects
  """
  
  # Already did this one?
  if getattr(package, '_g_inherit_processed__', 0):
    return

  # Package has disabled inheritance?
  if not getattr(package, '_g_inherit_path__', 1):
    return

  # Package's parent hasn't enabled inheritance?
  if not getattr(package_parent, '_g_inherit_path__', 0):
    return

  # Propagate path down
  _InheritPath(package_name, package, package_parent)


def _InheritPath(package_name, package, package_parent):
  """Compute a path for a package, based on the path of its parent.
  
  If package is named spam.eggs, then for each entry D in
  package_parent's path, add D/eggs to package's path.

  package_name: Fully qualified package name
  package, package_parent: Module objects
  
  """

  basename = package_name.split('.')[-1]
  assert basename, "Contact build-grouplet@google.com"

  orig_package_path = getattr(package, '__path__', [])

  # Pull down each path item from parent
  new_path = []
  for pathdir in getattr(package_parent, '__path__', []):
    if pathdir not in _NO_INHERIT:
      newdir = os.path.join(pathdir, basename)

      # To save I/O, we only add directories that 1) actually exist,
      # or 2) were in the original path.  Condition #2 is present to
      # accomodate import hooks that might put arbitrary strings on
      # the __path__.
      if newdir in orig_package_path or os.path.isdir(newdir):
        new_path.append(newdir)

  # If path had pre-existing entries, keep them.
  for pathdir in orig_package_path:
    if pathdir not in new_path:
      new_path.append(pathdir)

  # We mutate the path in-place since we might be in the process of
  # using it to import something.
  package.__path__[:] = new_path
  package._g_inherit_path__ = 1
  package._g_inherit_processed__ = 1


class _Python23MergeImportsHook:
  """Propagate package search path to all subpackages of Google3.

  This class is a meta-import hook, as defined by Python 2.3 and
  above.  Instead of actually importing anything, it works like a
  pre-import hook to fix up the __path__ in a package object that has
  already been imported.

  Consider packages A, A.B, and A.B.C.  A's __path__ contains a list
  of directories.  We want A.B's __path__ to be set to the same list
  of directories, except with '/B' appended to each one.  We could
  update A.B's __path__ when A.B is first imported, but that is
  difficult to implement.  Instead, we allow A.B's path to be
  incorrect until A.B.C is imported.  When A.B.C is imported, this
  hook runs, looks at A's __path__, and copies it with modifications
  to A.B's __path__.  The updated __path__ is then used by the normal
  import mechanism to find A.B.C.

  """

  def find_module(self, module_name, unused):
    """Called by standard Python import mechanism.

    module_name: Fully-qualified module name
    unused: List of directories to search, from parent package.

    We use this as a signal that a module is about to be imported, and
    fixup its parent's path if necessary.

    We then return a failure notification (via 'return None'), so that
    the normal import process continues.

    """

    _FixupParentPathByName(module_name)
    return None  # import.c interprets this as failure to find
  

_real_import = None  # Saved value of __builtins__.__import__

def _Python22MergeImportsHook(name, globals=None, locals=None, fromlist=None):
  """A wrapper for __builtins__.__import__

  Returns module object, or raises ImportError
  """

  # First off, this might be a relative import.  So we figure out what
  # package we're currently importing from, and make sure its path is
  # setup.
  if globals:
    maybe_current_package_name = globals.get('__name__', None)
    if maybe_current_package_name:
      maybe_current_package = sys.modules.get(maybe_current_package_name, None)
      if maybe_current_package:
        _FixupPackagePathByObject(maybe_current_package)
  
  # Unlike Python 2.3, we can't get a callback for each individual
  # package that is imported. So we simulate this by manually
  # importing each subpackage in turn.  I.e. if the user asked for
  # a.b.c.d, we import a, then a.b, then a.b.c, then a.b.c.d
  #
  # Futhermore, we don't know whether 'name' is absolute or relative
  # to the current package.  And __import__ doesn't necessarily return
  # the module named "cur_name".  So we have to compute that
  # separately.
  components = name.split('.')
  cur_name = None
  prev_module = None  # Parent of cur_module
  for component in components:
    if not cur_name:
      cur_name = component
    else:
      cur_name = "%s.%s" % (cur_name, component)
      
    result_module = _real_import(cur_name, globals, locals, [])

    # Find the actual module named "cur_name" if we can
    if prev_module is not None:
      cur_module = getattr(prev_module, component, None)
    else:
      cur_module = result_module
    if cur_module:
      _FixupPackagePathByObject(cur_module)
    prev_module = cur_module

  # Now do fromlist if necessary
  if fromlist:
    result_module = _real_import(name, globals, locals, fromlist)
  return result_module


def _Python22FixFirstImport():
  """Find the first google3 import in this program and fix it up.

  In _SetupMergeImportsHook we replace __import__ with our own import
  hook.  However, this replacement doesn't affect the
  already-in-progress import.  So, we have to figure out what the
  first google3 import of the program is, and run the fixup code on
  it, while the program is already in the process of doing the import.

  The implementation is a heuristic.  Note also that f_lasti is broken
  on Python 2.2, so the heuristic is very loose since we can't use
  f_lasti to get exact byte-code instruction offsets.
  
  """

  # These contants defined in dis.py
  HAVE_ARGUMENT = 90
  IMPORT_NAME = 107
  EXTENDED_ARG = 143
  
  # Find outer-most execution frame of this program
  frame = sys._getframe()
  while frame.f_back:
    frame = frame.f_back

  # Scan the frame looking for 'import google3.something'
  code = frame.f_code.co_code
  names = frame.f_code.co_names
  n = len(code)
  i = 0
  name = None
  extended_arg = 0
  # This loop largely stolen from dis.py
  while i < n:
    op = ord(code[i])
    i = i+1
    if op >= HAVE_ARGUMENT:
      oparg = ord(code[i]) + ord(code[i+1])*256 + extended_arg
      extended_arg = 0
      i = i+2
      if op == EXTENDED_ARG:
        extended_arg = oparg*65536L
      elif op == IMPORT_NAME:
        name = names[oparg]
        if name.startswith('google3'):
          # Run this import manually
          _Python22MergeImportsHook(name)
          break


_merge_imports_hook_installed = 0

def _SetupMergeImportsHook(have_readonly_dir):
  """Enable hook to merge directory trees for imports

  have_readonly_dir: 1 if [p4 client]/READONLY exists
  """

  # Don't load the hook twice
  global _merge_imports_hook_installed
  if _merge_imports_hook_installed:
    return

  # If don't have readonly dir, then this merge functionality isn't
  # (currently) needed, so don't enable it.  Also provide environment
  # variable to disable functionality if something goes haywire.
  if not have_readonly_dir or os.environ.get('GOOGLE3_DISABLE_MERGE_IMPORTS'):
    return

  _merge_imports_hook_installed = 1
  
  if sys.version_info >= (2,3):
    meta_path = getattr(sys, 'meta_path', [])
    meta_path.append(_Python23MergeImportsHook())
  else:
    # For Python 2.2, override builtin __import__ if have a READONLY
    # client and not running as a .par file
    import __builtin__
    global _real_import
    _real_import = __builtin__.__import__
    __builtin__.__import__ = _Python22MergeImportsHook

    # Run the hook manually for the currently-in-progress import
    _Python22FixFirstImport()


def _RunningProgramIsAParFile():
  """Returns whether or not sys.argv[0] (the running program) is a par
     file.

     Sadly, copied from google3/pyglib/parinfo.py to avoid dependency probs.
  """
  loader = globals().get('__loader__', None)
  if not loader or not hasattr(loader, '__module__'):
    return 0
  module = sys.modules[loader.__module__]
  return hasattr(module, 'AUTOPAR_VERSION')


########################################################################
# Support third-party imports using standard names like mx
# instead of google3.third_party.python.mx
########################################################################

def _SetupThirdParty(sys_path, google3_path):
  """Setup import path to code in google3/third_party/py.

  sys_path: Original sys.path
  google3_path: Google3 dirs being added to sys.path

  Returns nothing, modifies sys_path in place.
  """
  
  third_party_path = [os.path.join(d, 'third_party', 'py')
                      for d in google3_path]

  # Add third_party dirs to import path
  found_site_packages = 0
  if os.environ.get('GOOGLE3_OLD_STYLE_THIRD_PARTY') != '1':
    # Insert immediately before the first site-package dir
    for idx in range(len(sys_path)):
      dirname = sys_path[idx]
      if dirname.find('site-packages') != -1:
        found_site_packages = 1
        break
      
  if found_site_packages:
    sys_path[idx:idx] = third_party_path
  else:
    # Append to end if no site-packages found
    sys_path.extend(third_party_path)

  # Check for import order mistakes
  # Note that sys.path_hooks doesn't exist in Python 2.2, so we look
  # for an Google-specific implementation in the autopar code.
  if sys.version_info >= (2, 3, 0):
    path_hooks = getattr(sys, 'path_hooks', [])
  else:
    path_hooks = []
    zi_module = sys.modules.get('zipimport_compat', None)
    if zi_module:
      zi_class = getattr(zi_module, 'ZipImporter', None)
      if zi_class:
        path_hooks = [zi_class]
  
  _CheckThirdParty(third_party_path, path_hooks, sys.modules)

  return None

 
def _CheckThirdParty(third_party_path, path_hooks, sys_modules):
  """Check for erroneous imports from site-packages directory.

  third_party_path: List of path entries.  Each is an absolute
                    directory name, but may be a pseudo-path formed by
                    concatenating a .par filename with a subdir.
                    E.g. '/home/zog/src1/google3/third_party/py' or
                    '/root/myprog.par/google3/third_party/py'.

  For each top-level module or package that was imported from Python's
  site-package directory, but should have been imported from
  [client]/google3/third_party/py instead, issue a warning message.

  We try to determine this with a minimum of I/O, and without fully
  reimplementing import().  So we use heuristics: We only look at top
  level modules or packages (no dots), and we assume that every file
  or directory in google3/third_party/py is a module or package name.
  Since we control google3/third_party/py, this is generally safe.

  Returns a list of problematic modules
  """

  # Examine third-party dirs.
  path_data = _ExaminePath(third_party_path, path_hooks)
  
  # Iterate over all top-level modules loaded from site-packages.
  problems = []
  for module_name, module in sys_modules.items():
    if module_name.find('.') == -1:
      # Is module from site-packages?
      fn = getattr(module, '__file__', None)
      if fn and fn.find('site-packages') != -1:
        # Look for same-named module in third_party
        third_party_fn = _FindInPath(module_name, path_data)
        if third_party_fn:
          msg = ("%s is deprecated, use %s instead.  To fix this, move "
                 "'import google3' or 'from google3... import ...' before "
                 "'import %s' in your main source file." % (
            fn, third_party_fn, module_name))
          warnings.warn(msg, DeprecationWarning, stacklevel=2)
          problems.append((fn, third_party_fn, module_name))

  return problems


def _ExaminePath(dirs, path_hooks):
  """Determine the type and contents of a list of import path entries.

  dirs:  List of path entries as above.
  path_hooks: Contents of sys.path_hooks
  
  We categorize each directory as 1) real directory or 2) zipfile.
  There is no usable Python-level API to access the import internals,
  so we have to reimplement sys.path_hooks
  processing. [imp.find_module() doesn't work because it wasn't
  updated when new-style import hooks were added to Python 2.3]

  Returns a list of (path, [dir contents if real dir], loader if zipfile)
  """

  path_data = []
  for dirname in dirs:
    # Get possible modules and packages in this dir
    files = []
    try:
      files = []
      for f in os.listdir(dirname):
        # Look for no extension (i.e. directory) or a .py* extension.
        # Note that some interpreters use things like foo.pyc-2.2.
        base, ext = os.path.splitext(f)
        if ext == '' or ext.startswith('.py'):
          files.append(base)
    except EnvironmentError:
      pass

    # Get new-style path hook object for this dir
    loader = None
    for path_hook in path_hooks:
      try:
        loader = path_hook(dirname)
        break  # Success if got this far
      except ImportError:
        pass

    path_data.append([dirname, files, loader])

  return path_data

  
def _FindInPath(module_name, path_data):
  """Heuristic search for a module in a set of directories.

  module_name: top-level module name.  E.g. 'MySQLdb'
  path_data: List of (path, [dir contents if real dir], loader if zipfile)

  Returns the filename to the module or package dir, or None if not found.
  """
  assert '.' not in module_name, "Contact build-grouplet@google.com"
  
  for path, files, loader in path_data:
    if module_name in files:
      # Look for __init__.py.  We delay this check until here to avoid
      # I/O in the common case.
      package_fn = os.path.join(path, module_name)
      init_fn = os.path.join(package_fn, '__init__.py')
      if os.path.exists(init_fn):
        return package_fn
    
    if loader and loader.find_module(module_name):
      return os.path.join(path, module_name)

  return None

    
########################################################################
# Support for Google extension modules.
########################################################################

def _SetupSwig():
  """Setup environment for SWIG'd extension modules.

  TODO(dgreiman): This functionality should be moved from here into
  the auto-generated .py files produced by swig, so that it only runs
  when swig is actually used.

  """

  # Some Python extension modules are built with the Python 2.2
  # headers right now, even when they're being built for a Python 2.3+
  # program. They are 100% forward-compatible, so we silence the
  # (harmless) warning Python gives.
  if sys.version_info >= (2, 3, 0):
    warnings.filterwarnings('ignore', 'Python C API version mismatch')

  # If we are running a program that uses SWIG, a special library
  # called "swigdeps.so" will have been created.  Its only purpose is
  # to include functionality indirectly needed by SWIG
  # modules. E.g. pywrapfile.so indirectly relies on code in
  # util/hash/hash.cc, so we put util/hash/hash.o into swigdeps.so.
  # We can't always use the exact name "swigdeps.so", in particular
  # when using multiple combinations of extension modules from the
  # same runfiles directory, which is convenient to do for, for
  # example, py_tests. The GOOGLE3_SWIGDEPS_MODULE environment variable,
  # if set, should be set to the module name (not filename) to import.
  # It can be a Python package path like 'google3.tools.autopar.swigdeps',
  # if necessary.
  swigdeps_name = os.environ.get('GOOGLE3_SWIGDEPS_MODULE', 'swigdeps')
  swigdeps_modulename = swigdeps_name.split('.')[-1]
  # As a further complication, because we're in google3/__init__.py,
  # and we are being executed while it is loading (and thus while
  # google3 is being imported) we can't always import things inside of
  # google3/ by referring to them as 'google3.foo.bar'. We have to use
  # the relative form, 'foo.bar'. That also means we need to pass
  # globals() to __import__(), below, or __import__() won't know what
  # package to take as the starting point for relative imports. Some
  # time after we stop supporting Python 2.4, we should make sure
  # these kinds of imports are explicitly relative (by passing a
  # proper 'level' argument to __import__()), but the implicit
  # relative import is supported until Python 2.7 or 3.0 at least.
  if swigdeps_name.startswith('google3.'):
    swigdeps_name = swigdeps_name[len('google3.'):]
  # If the module doesn't use swig then no swigdeps.so will be created
  # so we can safely ignore the 'no module' error.  Also, if an empty
  # swigdeps.so is created, which happens spuriously for py_extension
  # modules and for py_binaries with data dependencies on
  # cc_libraries, ignore the 'no init function' error. Try not to
  # catch any other errors, or we might hide legitimate problems.
  ok_msgs = ( 'no module named %s' % swigdeps_modulename,
              'dynamic module does not define init function (init%s)'
                % swigdeps_modulename,
             )
  try:
    __import__(swigdeps_name, globals())
  except ImportError, e:
    msg = str(e).lower()
    if msg not in ok_msgs:
      raise

########################################################################
# Code run at import time
########################################################################

# Only Python 2.4 is supported; issue a warning for other versions
if sys.version_info[:2] != (2, 4):
  _msg = "Python %d.%d is unsupported; use 2.4" % sys.version_info[:2]
  warnings.warn(_msg, DeprecationWarning, stacklevel=1)

# The google3 directory; for people who need to orient themselves.
basedir = os.path.dirname(os.path.abspath(__file__))

# Private variables used by meta import hook
_g_inherit_path__ = 1
_g_inherit_processed__ = 1

# Code executed at import time for all Google3 programs.
__path__ = globals().get('__path__', [])  # For pychecker
__path__, _google3_path, _have_readonly_dir = _SetupPath(__path__, basedir)
_SetupMergeImportsHook(_have_readonly_dir)
_SetupThirdParty(sys.path, _google3_path)
_SetupSwig()
