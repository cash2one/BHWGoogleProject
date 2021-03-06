# This file automatically generated by protocol-compiler from rtserver/rpc/rtlookup.proto
# DO NOT EDIT!

from google3.net.proto import ProtocolBuffer
import array
import thread
from google3.net.proto import _net_proto___parse__python

__pychecker__ = """maxreturns=0 maxbranches=0 no-callinit
                   unusednames=printElemNumber,debug_strs no-special"""

class RTLookupCommand_PropertyLookup(ProtocolBuffer.ProtocolMessage):
  def __init__(self, contents=None):
    self.propertyname_ = ""
    self.propertynum_ = 0
    self.key_ = []
    self.rangecount_ = 0
    self.has_propertyname_ = 0
    self.has_propertynum_ = 0
    self.has_rangecount_ = 0
    if contents is not None: self.MergeFromString(contents)

  def propertyname(self): return self.propertyname_

  def set_propertyname(self, x):
    self.has_propertyname_ = 1
    self.propertyname_ = x

  def clear_propertyname(self):
    self.has_propertyname_ = 0
    self.propertyname_ = ""

  def has_propertyname(self): return self.has_propertyname_

  def propertynum(self): return self.propertynum_

  def set_propertynum(self, x):
    self.has_propertynum_ = 1
    self.propertynum_ = x

  def clear_propertynum(self):
    self.has_propertynum_ = 0
    self.propertynum_ = 0

  def has_propertynum(self): return self.has_propertynum_

  def key_size(self): return len(self.key_)
  def key_list(self): return self.key_

  def key(self, i):
    return self.key_[i]

  def set_key(self, i, x):
    self.key_[i] = x

  def add_key(self, x):
    self.key_.append(x)

  def clear_key(self):
    self.key_ = []

  def rangecount(self): return self.rangecount_

  def set_rangecount(self, x):
    self.has_rangecount_ = 1
    self.rangecount_ = x

  def clear_rangecount(self):
    self.has_rangecount_ = 0
    self.rangecount_ = 0

  def has_rangecount(self): return self.has_rangecount_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_propertyname()): self.set_propertyname(x.propertyname())
    if (x.has_propertynum()): self.set_propertynum(x.propertynum())
    for i in xrange(x.key_size()): self.add_key(x.key(i))
    if (x.has_rangecount()): self.set_rangecount(x.rangecount())

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'RTLookupCommand', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'RTLookupCommand')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'RTLookupCommand', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'RTLookupCommand', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'RTLookupCommand', s)


  def Equals(self, x):
    if x is self: return 1
    if self.has_propertyname_ != x.has_propertyname_: return 0
    if self.has_propertyname_ and self.propertyname_ != x.propertyname_: return 0
    if self.has_propertynum_ != x.has_propertynum_: return 0
    if self.has_propertynum_ and self.propertynum_ != x.propertynum_: return 0
    if len(self.key_) != len(x.key_): return 0
    for e1, e2 in zip(self.key_, x.key_):
      if e1 != e2: return 0
    if self.has_rangecount_ != x.has_rangecount_: return 0
    if self.has_rangecount_ and self.rangecount_ != x.rangecount_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    if (self.has_propertyname_): n += 1 + self.lengthString(len(self.propertyname_))
    if (self.has_propertynum_): n += 1 + self.lengthVarInt64(self.propertynum_)
    n += 1 * len(self.key_)
    for i in xrange(len(self.key_)): n += self.lengthVarInt64(self.key_[i])
    if (self.has_rangecount_): n += 1 + self.lengthVarInt64(self.rangecount_)
    return n + 0

  def Clear(self):
    self.clear_propertyname()
    self.clear_propertynum()
    self.clear_key()
    self.clear_rangecount()

  def OutputUnchecked(self, out):
    if (self.has_propertyname_):
      out.putVarInt32(50)
      out.putPrefixedString(self.propertyname_)
    if (self.has_propertynum_):
      out.putVarInt32(56)
      out.putVarInt32(self.propertynum_)
    for i in xrange(len(self.key_)):
      out.putVarInt32(64)
      out.putVarUint64(self.key_[i])
    if (self.has_rangecount_):
      out.putVarInt32(72)
      out.putVarInt64(self.rangecount_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 44: break
      if tt == 50:
        self.set_propertyname(d.getPrefixedString())
        continue
      if tt == 56:
        self.set_propertynum(d.getVarInt32())
        continue
      if tt == 64:
        self.add_key(d.getVarUint64())
        continue
      if tt == 72:
        self.set_rangecount(d.getVarInt64())
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_propertyname_: res+=prefix+("PropertyName: %s\n" % self.DebugFormatString(self.propertyname_))
    if self.has_propertynum_: res+=prefix+("PropertyNum: %s\n" % self.DebugFormatInt32(self.propertynum_))
    cnt=0
    for e in self.key_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Key%s: %s\n" % (elm, self.DebugFormatInt64(e)))
      cnt+=1
    if self.has_rangecount_: res+=prefix+("RangeCount: %s\n" % self.DebugFormatInt64(self.rangecount_))
    return res

class RTLookupCommand(ProtocolBuffer.ProtocolMessage):
  def __init__(self, contents=None):
    self.propertylookup_ = []
    self.suppresskeys_ = 0
    self.binaryresponse_ = 0
    self.has_suppresskeys_ = 0
    self.has_binaryresponse_ = 0
    if contents is not None: self.MergeFromString(contents)

  def propertylookup_size(self): return len(self.propertylookup_)
  def propertylookup_list(self): return self.propertylookup_

  def propertylookup(self, i):
    return self.propertylookup_[i]

  def mutable_propertylookup(self, i):
    return self.propertylookup_[i]

  def add_propertylookup(self):
    x = RTLookupCommand_PropertyLookup()
    self.propertylookup_.append(x)
    return x

  def clear_propertylookup(self):
    self.propertylookup_ = []
  def suppresskeys(self): return self.suppresskeys_

  def set_suppresskeys(self, x):
    self.has_suppresskeys_ = 1
    self.suppresskeys_ = x

  def clear_suppresskeys(self):
    self.has_suppresskeys_ = 0
    self.suppresskeys_ = 0

  def has_suppresskeys(self): return self.has_suppresskeys_

  def binaryresponse(self): return self.binaryresponse_

  def set_binaryresponse(self, x):
    self.has_binaryresponse_ = 1
    self.binaryresponse_ = x

  def clear_binaryresponse(self):
    self.has_binaryresponse_ = 0
    self.binaryresponse_ = 0

  def has_binaryresponse(self): return self.has_binaryresponse_


  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.propertylookup_size()): self.add_propertylookup().CopyFrom(x.propertylookup(i))
    if (x.has_suppresskeys()): self.set_suppresskeys(x.suppresskeys())
    if (x.has_binaryresponse()): self.set_binaryresponse(x.binaryresponse())

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'RTLookupCommand', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'RTLookupCommand')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'RTLookupCommand', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'RTLookupCommand', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'RTLookupCommand', s)


  def Equals(self, x):
    if x is self: return 1
    if len(self.propertylookup_) != len(x.propertylookup_): return 0
    for e1, e2 in zip(self.propertylookup_, x.propertylookup_):
      if e1 != e2: return 0
    if self.has_suppresskeys_ != x.has_suppresskeys_: return 0
    if self.has_suppresskeys_ and self.suppresskeys_ != x.suppresskeys_: return 0
    if self.has_binaryresponse_ != x.has_binaryresponse_: return 0
    if self.has_binaryresponse_ and self.binaryresponse_ != x.binaryresponse_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    for i in xrange(len(self.propertylookup_)):
      if (not self.propertylookup_[i].IsInitialized(debug_strs)): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += 2 * len(self.propertylookup_)
    for i in xrange(len(self.propertylookup_)): n += self.propertylookup_[i].ByteSize()
    if (self.has_suppresskeys_): n += 2
    if (self.has_binaryresponse_): n += 2
    return n + 0

  def Clear(self):
    self.clear_propertylookup()
    self.clear_suppresskeys()
    self.clear_binaryresponse()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.propertylookup_)):
      out.putVarInt32(43)
      self.propertylookup_[i].OutputUnchecked(out)
      out.putVarInt32(44)
    if (self.has_suppresskeys_):
      out.putVarInt32(80)
      out.putBoolean(self.suppresskeys_)
    if (self.has_binaryresponse_):
      out.putVarInt32(88)
      out.putBoolean(self.binaryresponse_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 43:
        self.add_propertylookup().TryMerge(d)
        continue
      if tt == 80:
        self.set_suppresskeys(d.getBoolean())
        continue
      if tt == 88:
        self.set_binaryresponse(d.getBoolean())
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.propertylookup_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("PropertyLookup%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    if self.has_suppresskeys_: res+=prefix+("SuppressKeys: %s\n" % self.DebugFormatBool(self.suppresskeys_))
    if self.has_binaryresponse_: res+=prefix+("BinaryResponse: %s\n" % self.DebugFormatBool(self.binaryresponse_))
    return res

  kPropertyLookupGroup = 5
  kPropertyLookupPropertyName = 6
  kPropertyLookupPropertyNum = 7
  kPropertyLookupKey = 8
  kPropertyLookupRangeCount = 9
  kSuppressKeys = 10
  kBinaryResponse = 11

  _TEXT = (
   "ErrorCode",  #   0
   None,  #   1
   None,  #   2
   None,  #   3
   None,  #   4
   "PropertyLookup",  #   5
   "PropertyName",  #   6
   "PropertyNum",  #   7
   "Key",  #   8
   "RangeCount",  #   9
   "SuppressKeys",  #  10
   "BinaryResponse",  #  11
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,  #   0
   ProtocolBuffer.Encoder.MAX_TYPE,  #   1

   ProtocolBuffer.Encoder.MAX_TYPE,  #   2

   ProtocolBuffer.Encoder.MAX_TYPE,  #   3

   ProtocolBuffer.Encoder.MAX_TYPE,  #   4

   ProtocolBuffer.Encoder.STARTGROUP,  #   5

   ProtocolBuffer.Encoder.STRING,  #   6

   ProtocolBuffer.Encoder.NUMERIC,  #   7

   ProtocolBuffer.Encoder.NUMERIC,  #   8

   ProtocolBuffer.Encoder.NUMERIC,  #   9

   ProtocolBuffer.Encoder.NUMERIC,  #  10

   ProtocolBuffer.Encoder.NUMERIC,  #  11

  )

  # stylesheet for XML output
  _STYLE = \
   """"""
  _STYLE_CONTENT_TYPE = \
   """"""
  _SERIALIZED_DESCRIPTOR = array.array('B', [
    0x5a,
    0x1b,
    0x72,
    0x74,
    0x73,
    0x65,
    0x72,
    0x76,
    0x65,
    0x72,
    0x2f,
    0x72,
    0x70,
    0x63,
    0x2f,
    0x72,
    0x74,
    0x6c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x2e,
    0x70,
    0x72,
    0x6f,
    0x74,
    0x6f,
    0x0a,
    0x0f,
    0x52,
    0x54,
    0x4c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x43,
    0x6f,
    0x6d,
    0x6d,
    0x61,
    0x6e,
    0x64,
    0x13,
    0x1a,
    0x0e,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x4c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x20,
    0x05,
    0x28,
    0x03,
    0x30,
    0x0a,
    0x38,
    0x03,
    0x14,
    0x13,
    0x1a,
    0x1b,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x4c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x2e,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x4e,
    0x61,
    0x6d,
    0x65,
    0x20,
    0x06,
    0x28,
    0x02,
    0x30,
    0x09,
    0x38,
    0x01,
    0x60,
    0x00,
    0x14,
    0x13,
    0x1a,
    0x1a,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x4c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x2e,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x4e,
    0x75,
    0x6d,
    0x20,
    0x07,
    0x28,
    0x00,
    0x30,
    0x05,
    0x38,
    0x01,
    0x60,
    0x00,
    0x14,
    0x13,
    0x1a,
    0x12,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x4c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x2e,
    0x4b,
    0x65,
    0x79,
    0x20,
    0x08,
    0x28,
    0x00,
    0x30,
    0x04,
    0x38,
    0x03,
    0x60,
    0x00,
    0x14,
    0x13,
    0x1a,
    0x19,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x4c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x2e,
    0x52,
    0x61,
    0x6e,
    0x67,
    0x65,
    0x43,
    0x6f,
    0x75,
    0x6e,
    0x74,
    0x20,
    0x09,
    0x28,
    0x00,
    0x30,
    0x03,
    0x38,
    0x01,
    0x60,
    0x00,
    0x14,
    0x13,
    0x1a,
    0x0c,
    0x53,
    0x75,
    0x70,
    0x70,
    0x72,
    0x65,
    0x73,
    0x73,
    0x4b,
    0x65,
    0x79,
    0x73,
    0x20,
    0x0a,
    0x28,
    0x00,
    0x30,
    0x08,
    0x38,
    0x01,
    0x42,
    0x05,
    0x66,
    0x61,
    0x6c,
    0x73,
    0x65,
    0xa3,
    0x01,
    0xaa,
    0x01,
    0x07,
    0x64,
    0x65,
    0x66,
    0x61,
    0x75,
    0x6c,
    0x74,
    0xb2,
    0x01,
    0x05,
    0x66,
    0x61,
    0x6c,
    0x73,
    0x65,
    0xa4,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x0e,
    0x42,
    0x69,
    0x6e,
    0x61,
    0x72,
    0x79,
    0x52,
    0x65,
    0x73,
    0x70,
    0x6f,
    0x6e,
    0x73,
    0x65,
    0x20,
    0x0b,
    0x28,
    0x00,
    0x30,
    0x08,
    0x38,
    0x01,
    0x42,
    0x05,
    0x66,
    0x61,
    0x6c,
    0x73,
    0x65,
    0xa3,
    0x01,
    0xaa,
    0x01,
    0x07,
    0x64,
    0x65,
    0x66,
    0x61,
    0x75,
    0x6c,
    0x74,
    0xb2,
    0x01,
    0x05,
    0x66,
    0x61,
    0x6c,
    0x73,
    0x65,
    0xa4,
    0x01,
    0x14,
    ])
  _net_proto___parse__python.RegisterType(_SERIALIZED_DESCRIPTOR.tostring())
class RTLookupResponse_PropertyResultElement(ProtocolBuffer.ProtocolMessage):
  def __init__(self, contents=None):
    self.stringvalue_ = ""
    self.intvalue_ = 0
    self.key_ = 0
    self.has_stringvalue_ = 0
    self.has_intvalue_ = 0
    self.has_key_ = 0
    if contents is not None: self.MergeFromString(contents)

  def stringvalue(self): return self.stringvalue_

  def set_stringvalue(self, x):
    self.has_stringvalue_ = 1
    self.stringvalue_ = x

  def clear_stringvalue(self):
    self.has_stringvalue_ = 0
    self.stringvalue_ = ""

  def has_stringvalue(self): return self.has_stringvalue_

  def intvalue(self): return self.intvalue_

  def set_intvalue(self, x):
    self.has_intvalue_ = 1
    self.intvalue_ = x

  def clear_intvalue(self):
    self.has_intvalue_ = 0
    self.intvalue_ = 0

  def has_intvalue(self): return self.has_intvalue_

  def key(self): return self.key_

  def set_key(self, x):
    self.has_key_ = 1
    self.key_ = x

  def clear_key(self):
    self.has_key_ = 0
    self.key_ = 0

  def has_key(self): return self.has_key_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_stringvalue()): self.set_stringvalue(x.stringvalue())
    if (x.has_intvalue()): self.set_intvalue(x.intvalue())
    if (x.has_key()): self.set_key(x.key())

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'RTLookupResponse', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'RTLookupResponse')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'RTLookupResponse', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'RTLookupResponse', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'RTLookupResponse', s)


  def Equals(self, x):
    if x is self: return 1
    if self.has_stringvalue_ != x.has_stringvalue_: return 0
    if self.has_stringvalue_ and self.stringvalue_ != x.stringvalue_: return 0
    if self.has_intvalue_ != x.has_intvalue_: return 0
    if self.has_intvalue_ and self.intvalue_ != x.intvalue_: return 0
    if self.has_key_ != x.has_key_: return 0
    if self.has_key_ and self.key_ != x.key_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    return initialized

  def ByteSize(self):
    n = 0
    if (self.has_stringvalue_): n += 1 + self.lengthString(len(self.stringvalue_))
    if (self.has_intvalue_): n += 1 + self.lengthVarInt64(self.intvalue_)
    if (self.has_key_): n += 1 + self.lengthVarInt64(self.key_)
    return n + 0

  def Clear(self):
    self.clear_stringvalue()
    self.clear_intvalue()
    self.clear_key()

  def OutputUnchecked(self, out):
    if (self.has_stringvalue_):
      out.putVarInt32(106)
      out.putPrefixedString(self.stringvalue_)
    if (self.has_intvalue_):
      out.putVarInt32(112)
      out.putVarInt64(self.intvalue_)
    if (self.has_key_):
      out.putVarInt32(120)
      out.putVarInt64(self.key_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 100: break
      if tt == 106:
        self.set_stringvalue(d.getPrefixedString())
        continue
      if tt == 112:
        self.set_intvalue(d.getVarInt64())
        continue
      if tt == 120:
        self.set_key(d.getVarInt64())
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_stringvalue_: res+=prefix+("StringValue: %s\n" % self.DebugFormatString(self.stringvalue_))
    if self.has_intvalue_: res+=prefix+("IntValue: %s\n" % self.DebugFormatInt64(self.intvalue_))
    if self.has_key_: res+=prefix+("Key: %s\n" % self.DebugFormatInt64(self.key_))
    return res

class RTLookupResponse_PropertyResult(ProtocolBuffer.ProtocolMessage):

  SUCCESS      =    0 
  PROPERTY_NOT_FOUND =    1 
  KEY_NOT_FOUND =    2 
  INVALID_KEY  =    3 

  _PropertyResultStatus_NAMES = {
    0: "SUCCESS",
    1: "PROPERTY_NOT_FOUND",
    2: "KEY_NOT_FOUND",
    3: "INVALID_KEY",
  }

  def PropertyResultStatus_Name(cls, x): return cls._PropertyResultStatus_NAMES.get(x, "")
  PropertyResultStatus_Name = classmethod(PropertyResultStatus_Name)

  def __init__(self, contents=None):
    self.responsecode_ = 0
    self.element_ = []
    self.has_responsecode_ = 0
    if contents is not None: self.MergeFromString(contents)

  def responsecode(self): return self.responsecode_

  def set_responsecode(self, x):
    self.has_responsecode_ = 1
    self.responsecode_ = x

  def clear_responsecode(self):
    self.has_responsecode_ = 0
    self.responsecode_ = 0

  def has_responsecode(self): return self.has_responsecode_

  def element_size(self): return len(self.element_)
  def element_list(self): return self.element_

  def element(self, i):
    return self.element_[i]

  def mutable_element(self, i):
    return self.element_[i]

  def add_element(self):
    x = RTLookupResponse_PropertyResultElement()
    self.element_.append(x)
    return x

  def clear_element(self):
    self.element_ = []

  def MergeFrom(self, x):
    assert x is not self
    if (x.has_responsecode()): self.set_responsecode(x.responsecode())
    for i in xrange(x.element_size()): self.add_element().CopyFrom(x.element(i))

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'RTLookupResponse', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'RTLookupResponse')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'RTLookupResponse', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'RTLookupResponse', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'RTLookupResponse', s)


  def Equals(self, x):
    if x is self: return 1
    if self.has_responsecode_ != x.has_responsecode_: return 0
    if self.has_responsecode_ and self.responsecode_ != x.responsecode_: return 0
    if len(self.element_) != len(x.element_): return 0
    for e1, e2 in zip(self.element_, x.element_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_responsecode_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: responsecode not set.')
    for i in xrange(len(self.element_)):
      if (not self.element_[i].IsInitialized(debug_strs)): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.responsecode_)
    n += 2 * len(self.element_)
    for i in xrange(len(self.element_)): n += self.element_[i].ByteSize()
    return n + 1

  def Clear(self):
    self.clear_responsecode()
    self.clear_element()

  def OutputUnchecked(self, out):
    out.putVarInt32(88)
    out.putVarInt32(self.responsecode_)
    for i in xrange(len(self.element_)):
      out.putVarInt32(99)
      self.element_[i].OutputUnchecked(out)
      out.putVarInt32(100)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 84: break
      if tt == 88:
        self.set_responsecode(d.getVarInt32())
        continue
      if tt == 99:
        self.add_element().TryMerge(d)
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_responsecode_: res+=prefix+("ResponseCode: %s\n" % self.DebugFormatInt32(self.responsecode_))
    cnt=0
    for e in self.element_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Element%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    return res

class RTLookupResponse(ProtocolBuffer.ProtocolMessage):

  SUCCESS      =    0 
  INTERNAL_ERROR =    1 
  PARSE_ERROR  =    2 

  _LookupStatus_NAMES = {
    0: "SUCCESS",
    1: "INTERNAL_ERROR",
    2: "PARSE_ERROR",
  }

  def LookupStatus_Name(cls, x): return cls._LookupStatus_NAMES.get(x, "")
  LookupStatus_Name = classmethod(LookupStatus_Name)

  def __init__(self, contents=None):
    self.responsecode_ = 0
    self.propertyresult_ = []
    self.has_responsecode_ = 0
    if contents is not None: self.MergeFromString(contents)

  def responsecode(self): return self.responsecode_

  def set_responsecode(self, x):
    self.has_responsecode_ = 1
    self.responsecode_ = x

  def clear_responsecode(self):
    self.has_responsecode_ = 0
    self.responsecode_ = 0

  def has_responsecode(self): return self.has_responsecode_

  def propertyresult_size(self): return len(self.propertyresult_)
  def propertyresult_list(self): return self.propertyresult_

  def propertyresult(self, i):
    return self.propertyresult_[i]

  def mutable_propertyresult(self, i):
    return self.propertyresult_[i]

  def add_propertyresult(self):
    x = RTLookupResponse_PropertyResult()
    self.propertyresult_.append(x)
    return x

  def clear_propertyresult(self):
    self.propertyresult_ = []

  def MergeFrom(self, x):
    assert x is not self
    if (x.has_responsecode()): self.set_responsecode(x.responsecode())
    for i in xrange(x.propertyresult_size()): self.add_propertyresult().CopyFrom(x.propertyresult(i))

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'RTLookupResponse', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'RTLookupResponse')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'RTLookupResponse', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'RTLookupResponse', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'RTLookupResponse', s)


  def Equals(self, x):
    if x is self: return 1
    if self.has_responsecode_ != x.has_responsecode_: return 0
    if self.has_responsecode_ and self.responsecode_ != x.responsecode_: return 0
    if len(self.propertyresult_) != len(x.propertyresult_): return 0
    for e1, e2 in zip(self.propertyresult_, x.propertyresult_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_responsecode_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: responsecode not set.')
    for i in xrange(len(self.propertyresult_)):
      if (not self.propertyresult_[i].IsInitialized(debug_strs)): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.responsecode_)
    n += 2 * len(self.propertyresult_)
    for i in xrange(len(self.propertyresult_)): n += self.propertyresult_[i].ByteSize()
    return n + 1

  def Clear(self):
    self.clear_responsecode()
    self.clear_propertyresult()

  def OutputUnchecked(self, out):
    out.putVarInt32(72)
    out.putVarInt32(self.responsecode_)
    for i in xrange(len(self.propertyresult_)):
      out.putVarInt32(83)
      self.propertyresult_[i].OutputUnchecked(out)
      out.putVarInt32(84)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 72:
        self.set_responsecode(d.getVarInt32())
        continue
      if tt == 83:
        self.add_propertyresult().TryMerge(d)
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_responsecode_: res+=prefix+("ResponseCode: %s\n" % self.DebugFormatInt32(self.responsecode_))
    cnt=0
    for e in self.propertyresult_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("PropertyResult%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    return res

  kResponseCode = 9
  kPropertyResultGroup = 10
  kPropertyResultResponseCode = 11
  kPropertyResultElementGroup = 12
  kPropertyResultElementStringValue = 13
  kPropertyResultElementIntValue = 14
  kPropertyResultElementKey = 15

  _TEXT = (
   "ErrorCode",  #   0
   None,  #   1
   None,  #   2
   None,  #   3
   None,  #   4
   None,  #   5
   None,  #   6
   None,  #   7
   None,  #   8
   "ResponseCode",  #   9
   "PropertyResult",  #  10
   "ResponseCode",  #  11
   "Element",  #  12
   "StringValue",  #  13
   "IntValue",  #  14
   "Key",  #  15
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,  #   0
   ProtocolBuffer.Encoder.MAX_TYPE,  #   1

   ProtocolBuffer.Encoder.MAX_TYPE,  #   2

   ProtocolBuffer.Encoder.MAX_TYPE,  #   3

   ProtocolBuffer.Encoder.MAX_TYPE,  #   4

   ProtocolBuffer.Encoder.MAX_TYPE,  #   5

   ProtocolBuffer.Encoder.MAX_TYPE,  #   6

   ProtocolBuffer.Encoder.MAX_TYPE,  #   7

   ProtocolBuffer.Encoder.MAX_TYPE,  #   8

   ProtocolBuffer.Encoder.NUMERIC,  #   9

   ProtocolBuffer.Encoder.STARTGROUP,  #  10

   ProtocolBuffer.Encoder.NUMERIC,  #  11

   ProtocolBuffer.Encoder.STARTGROUP,  #  12

   ProtocolBuffer.Encoder.STRING,  #  13

   ProtocolBuffer.Encoder.NUMERIC,  #  14

   ProtocolBuffer.Encoder.NUMERIC,  #  15

  )

  # stylesheet for XML output
  _STYLE = \
   """"""
  _STYLE_CONTENT_TYPE = \
   """"""
  _SERIALIZED_DESCRIPTOR = array.array('B', [
    0x5a,
    0x1b,
    0x72,
    0x74,
    0x73,
    0x65,
    0x72,
    0x76,
    0x65,
    0x72,
    0x2f,
    0x72,
    0x70,
    0x63,
    0x2f,
    0x72,
    0x74,
    0x6c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x2e,
    0x70,
    0x72,
    0x6f,
    0x74,
    0x6f,
    0x0a,
    0x10,
    0x52,
    0x54,
    0x4c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x52,
    0x65,
    0x73,
    0x70,
    0x6f,
    0x6e,
    0x73,
    0x65,
    0x13,
    0x1a,
    0x0c,
    0x52,
    0x65,
    0x73,
    0x70,
    0x6f,
    0x6e,
    0x73,
    0x65,
    0x43,
    0x6f,
    0x64,
    0x65,
    0x20,
    0x09,
    0x28,
    0x00,
    0x30,
    0x05,
    0x38,
    0x02,
    0x14,
    0x13,
    0x1a,
    0x0e,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x20,
    0x0a,
    0x28,
    0x03,
    0x30,
    0x0a,
    0x38,
    0x03,
    0x14,
    0x13,
    0x1a,
    0x1b,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x2e,
    0x52,
    0x65,
    0x73,
    0x70,
    0x6f,
    0x6e,
    0x73,
    0x65,
    0x43,
    0x6f,
    0x64,
    0x65,
    0x20,
    0x0b,
    0x28,
    0x00,
    0x30,
    0x05,
    0x38,
    0x02,
    0x60,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x16,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x2e,
    0x45,
    0x6c,
    0x65,
    0x6d,
    0x65,
    0x6e,
    0x74,
    0x20,
    0x0c,
    0x28,
    0x03,
    0x30,
    0x0a,
    0x38,
    0x03,
    0x60,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x22,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x2e,
    0x45,
    0x6c,
    0x65,
    0x6d,
    0x65,
    0x6e,
    0x74,
    0x2e,
    0x53,
    0x74,
    0x72,
    0x69,
    0x6e,
    0x67,
    0x56,
    0x61,
    0x6c,
    0x75,
    0x65,
    0x20,
    0x0d,
    0x28,
    0x02,
    0x30,
    0x09,
    0x38,
    0x01,
    0x60,
    0x03,
    0x14,
    0x13,
    0x1a,
    0x1f,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x2e,
    0x45,
    0x6c,
    0x65,
    0x6d,
    0x65,
    0x6e,
    0x74,
    0x2e,
    0x49,
    0x6e,
    0x74,
    0x56,
    0x61,
    0x6c,
    0x75,
    0x65,
    0x20,
    0x0e,
    0x28,
    0x00,
    0x30,
    0x03,
    0x38,
    0x01,
    0x60,
    0x03,
    0x14,
    0x13,
    0x1a,
    0x1a,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x2e,
    0x45,
    0x6c,
    0x65,
    0x6d,
    0x65,
    0x6e,
    0x74,
    0x2e,
    0x4b,
    0x65,
    0x79,
    0x20,
    0x0f,
    0x28,
    0x00,
    0x30,
    0x03,
    0x38,
    0x01,
    0x60,
    0x03,
    0x14,
    0x73,
    0x7a,
    0x0c,
    0x4c,
    0x6f,
    0x6f,
    0x6b,
    0x75,
    0x70,
    0x53,
    0x74,
    0x61,
    0x74,
    0x75,
    0x73,
    0x8b,
    0x01,
    0x92,
    0x01,
    0x07,
    0x53,
    0x55,
    0x43,
    0x43,
    0x45,
    0x53,
    0x53,
    0x98,
    0x01,
    0x00,
    0x8c,
    0x01,
    0x8b,
    0x01,
    0x92,
    0x01,
    0x0e,
    0x49,
    0x4e,
    0x54,
    0x45,
    0x52,
    0x4e,
    0x41,
    0x4c,
    0x5f,
    0x45,
    0x52,
    0x52,
    0x4f,
    0x52,
    0x98,
    0x01,
    0x01,
    0x8c,
    0x01,
    0x8b,
    0x01,
    0x92,
    0x01,
    0x0b,
    0x50,
    0x41,
    0x52,
    0x53,
    0x45,
    0x5f,
    0x45,
    0x52,
    0x52,
    0x4f,
    0x52,
    0x98,
    0x01,
    0x02,
    0x8c,
    0x01,
    0x74,
    0x73,
    0x7a,
    0x14,
    0x50,
    0x72,
    0x6f,
    0x70,
    0x65,
    0x72,
    0x74,
    0x79,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x53,
    0x74,
    0x61,
    0x74,
    0x75,
    0x73,
    0x80,
    0x01,
    0x01,
    0x8b,
    0x01,
    0x92,
    0x01,
    0x07,
    0x53,
    0x55,
    0x43,
    0x43,
    0x45,
    0x53,
    0x53,
    0x98,
    0x01,
    0x00,
    0x8c,
    0x01,
    0x8b,
    0x01,
    0x92,
    0x01,
    0x12,
    0x50,
    0x52,
    0x4f,
    0x50,
    0x45,
    0x52,
    0x54,
    0x59,
    0x5f,
    0x4e,
    0x4f,
    0x54,
    0x5f,
    0x46,
    0x4f,
    0x55,
    0x4e,
    0x44,
    0x98,
    0x01,
    0x01,
    0x8c,
    0x01,
    0x8b,
    0x01,
    0x92,
    0x01,
    0x0d,
    0x4b,
    0x45,
    0x59,
    0x5f,
    0x4e,
    0x4f,
    0x54,
    0x5f,
    0x46,
    0x4f,
    0x55,
    0x4e,
    0x44,
    0x98,
    0x01,
    0x02,
    0x8c,
    0x01,
    0x8b,
    0x01,
    0x92,
    0x01,
    0x0b,
    0x49,
    0x4e,
    0x56,
    0x41,
    0x4c,
    0x49,
    0x44,
    0x5f,
    0x4b,
    0x45,
    0x59,
    0x98,
    0x01,
    0x03,
    0x8c,
    0x01,
    0x74,
    ])
  _net_proto___parse__python.RegisterType(_SERIALIZED_DESCRIPTOR.tostring())

__all__ = ['RTLookupCommand','RTLookupCommand_PropertyLookup','RTLookupResponse','RTLookupResponse_PropertyResultElement','RTLookupResponse_PropertyResult']
