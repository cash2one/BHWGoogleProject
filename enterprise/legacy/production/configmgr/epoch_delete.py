#!/usr/bin/python2.4
# (c) 2002 Google inc
# cpopescu@google.com
#
# This contains the code to send an epoch limit delete command to
# the specified rtserver types
#
import string
import sys

from google3.pyglib import flags
from google3.enterprise.legacy.production.configmgr import server_requests

from google3.enterprise.legacy.production.babysitter import config_factory
from google3.enterprise.legacy.production.configmgr import configmgr_request

FLAGS = flags.FLAGS

flags.DEFINE_string("config_file", "", "The configuration file")
flags.DEFINE_string("epoch_list", "", "The repr of list with epoch"\
                    " numbers to delete")
flags.DEFINE_string("server_types", "", "The repr of server types to"\
                    "send the command to")
flags.DEFINE_integer("no_extra_req", None, "Do not write subsequent "\
                     "config manager requests (good for testing")

def execute(flag_config_file, flag_epoch_list, flag_server_types,
            flag_no_extra_req):

  if not flag_config_file: sys.exit("Must specify a config file")

  server_types = None
  epoch_list = None
  try:
    exec("server_types = %s" % flag_server_types)
    exec("epoch_list = %s" % flag_epoch_list)
  except:
    sys.exit("Invalid value %s or %s" % (flag_server_types, flag_epoch_list))

  cp = config_factory.ConfigFactory().CreateConfig(flag_config_file)
  if not cp.Load():
    sys.exit("Unable to load config file  %s" % (cp.GetConfigFileName()))

  # Register requests per machine

  # Prepare adummy request to send server command
  req = server_requests.SendServerCommandRequest()
  req.Set("dummy", 1,
          "GET /update?%s HTTP/1.0\r\n\r\n" % \
          (string.join(map(lambda e: "EpochDelete=%d" % e, epoch_list), "&")),
          "HTTP/1.0 200 OK",
          cp.GetConfigFileName())

  requests = []
  # The actual requests that registers req for each machine:port
  # for all server types
  for stype in server_types:
    the_req = configmgr_request.MultiRequestCreateRequest()
    the_req.Set(req.datadict, stype,
                server_requests.MACHINE, server_requests.PORT,
                cp.GetConfigFileName())
    if not flag_no_extra_req and not cp.WriteConfigManagerRequest(the_req):
      sys.exit("Cannot save subsequent request to update param on machine")
    requests.append(the_req)

  cp.DistributeAll()

  return requests

def main(argv):
  try:
    argv = FLAGS(argv)  # parse flags
  except flags.FlagsError, e:
    print "%s\nUsage: %s ARGS\n%s" % (e, sys.argv[0], FLAGS)
    sys.exit(1)

  return execute(FLAGS.config_file, FLAGS.epoch_list, FLAGS.server_types,
                 FLAGS.no_extra_req)

if __name__ == '__main__':
  main(sys.argv)
