# This file automatically generated by protocol-compiler from quality/labels/proto/google-label-data.proto
# DO NOT EDIT!

from google3.net.proto import ProtocolBuffer
import array
import thread
from google3.net.proto import _net_proto___parse__python

__pychecker__ = """maxreturns=0 maxbranches=0 no-callinit
                   unusednames=printElemNumber,debug_strs no-special"""

class GoogleLabelData_LabelProvider(ProtocolBuffer.ProtocolMessage):
  def __init__(self, contents=None):
    self.id_ = 0
    self.name_ = ""
    self.label_value_ = 1.0
    self.label_bucket_ = 0
    self.feed_ = 0
    self.has_id_ = 0
    self.has_name_ = 0
    self.has_label_value_ = 0
    self.has_label_bucket_ = 0
    self.has_feed_ = 0
    if contents is not None: self.MergeFromString(contents)

  def id(self): return self.id_

  def set_id(self, x):
    self.has_id_ = 1
    self.id_ = x

  def clear_id(self):
    self.has_id_ = 0
    self.id_ = 0

  def has_id(self): return self.has_id_

  def name(self): return self.name_

  def set_name(self, x):
    self.has_name_ = 1
    self.name_ = x

  def clear_name(self):
    self.has_name_ = 0
    self.name_ = ""

  def has_name(self): return self.has_name_

  def label_value(self): return self.label_value_

  def set_label_value(self, x):
    self.has_label_value_ = 1
    self.label_value_ = x

  def clear_label_value(self):
    self.has_label_value_ = 0
    self.label_value_ = 1.0

  def has_label_value(self): return self.has_label_value_

  def label_bucket(self): return self.label_bucket_

  def set_label_bucket(self, x):
    self.has_label_bucket_ = 1
    self.label_bucket_ = x

  def clear_label_bucket(self):
    self.has_label_bucket_ = 0
    self.label_bucket_ = 0

  def has_label_bucket(self): return self.has_label_bucket_

  def feed(self): return self.feed_

  def set_feed(self, x):
    self.has_feed_ = 1
    self.feed_ = x

  def clear_feed(self):
    self.has_feed_ = 0
    self.feed_ = 0

  def has_feed(self): return self.has_feed_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_id()): self.set_id(x.id())
    if (x.has_name()): self.set_name(x.name())
    if (x.has_label_value()): self.set_label_value(x.label_value())
    if (x.has_label_bucket()): self.set_label_bucket(x.label_bucket())
    if (x.has_feed()): self.set_feed(x.feed())

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'quality_labels.GoogleLabelData', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'quality_labels.GoogleLabelData')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'quality_labels.GoogleLabelData', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'quality_labels.GoogleLabelData', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'quality_labels.GoogleLabelData', s)


  def Equals(self, x):
    if x is self: return 1
    if self.has_id_ != x.has_id_: return 0
    if self.has_id_ and self.id_ != x.id_: return 0
    if self.has_name_ != x.has_name_: return 0
    if self.has_name_ and self.name_ != x.name_: return 0
    if self.has_label_value_ != x.has_label_value_: return 0
    if self.has_label_value_ and self.label_value_ != x.label_value_: return 0
    if self.has_label_bucket_ != x.has_label_bucket_: return 0
    if self.has_label_bucket_ and self.label_bucket_ != x.label_bucket_: return 0
    if self.has_feed_ != x.has_feed_: return 0
    if self.has_feed_ and self.feed_ != x.feed_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_id_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: id not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.id_)
    if (self.has_name_): n += 1 + self.lengthString(len(self.name_))
    if (self.has_label_value_): n += 5
    if (self.has_label_bucket_): n += 1 + self.lengthVarInt64(self.label_bucket_)
    if (self.has_feed_): n += 2
    return n + 1

  def Clear(self):
    self.clear_id()
    self.clear_name()
    self.clear_label_value()
    self.clear_label_bucket()
    self.clear_feed()

  def OutputUnchecked(self, out):
    out.putVarInt32(56)
    out.putVarUint64(self.id_)
    if (self.has_name_):
      out.putVarInt32(66)
      out.putPrefixedString(self.name_)
    if (self.has_label_value_):
      out.putVarInt32(85)
      out.putFloat(self.label_value_)
    if (self.has_label_bucket_):
      out.putVarInt32(96)
      out.putVarInt32(self.label_bucket_)
    if (self.has_feed_):
      out.putVarInt32(104)
      out.putBoolean(self.feed_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 52: break
      if tt == 56:
        self.set_id(d.getVarUint64())
        continue
      if tt == 66:
        self.set_name(d.getPrefixedString())
        continue
      if tt == 85:
        self.set_label_value(d.getFloat())
        continue
      if tt == 96:
        self.set_label_bucket(d.getVarInt32())
        continue
      if tt == 104:
        self.set_feed(d.getBoolean())
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_id_: res+=prefix+("id: %s\n" % self.DebugFormatInt64(self.id_))
    if self.has_name_: res+=prefix+("name: %s\n" % self.DebugFormatString(self.name_))
    if self.has_label_value_: res+=prefix+("label_value: %s\n" % self.DebugFormatFloat(self.label_value_))
    if self.has_label_bucket_: res+=prefix+("label_bucket: %s\n" % self.DebugFormatInt32(self.label_bucket_))
    if self.has_feed_: res+=prefix+("feed: %s\n" % self.DebugFormatBool(self.feed_))
    return res

class GoogleLabelData_Label(ProtocolBuffer.ProtocolMessage):
  def __init__(self, contents=None):
    self.label_id_ = 0
    self.label_name_ = ""
    self.confidence_ = 1.0
    self.global_label_value_ = 0.0
    self.global_label_bucket_ = 0
    self.provider_id_ = []
    self.provider_ = []
    self.has_label_id_ = 0
    self.has_label_name_ = 0
    self.has_confidence_ = 0
    self.has_global_label_value_ = 0
    self.has_global_label_bucket_ = 0
    if contents is not None: self.MergeFromString(contents)

  def label_id(self): return self.label_id_

  def set_label_id(self, x):
    self.has_label_id_ = 1
    self.label_id_ = x

  def clear_label_id(self):
    self.has_label_id_ = 0
    self.label_id_ = 0

  def has_label_id(self): return self.has_label_id_

  def label_name(self): return self.label_name_

  def set_label_name(self, x):
    self.has_label_name_ = 1
    self.label_name_ = x

  def clear_label_name(self):
    self.has_label_name_ = 0
    self.label_name_ = ""

  def has_label_name(self): return self.has_label_name_

  def confidence(self): return self.confidence_

  def set_confidence(self, x):
    self.has_confidence_ = 1
    self.confidence_ = x

  def clear_confidence(self):
    self.has_confidence_ = 0
    self.confidence_ = 1.0

  def has_confidence(self): return self.has_confidence_

  def global_label_value(self): return self.global_label_value_

  def set_global_label_value(self, x):
    self.has_global_label_value_ = 1
    self.global_label_value_ = x

  def clear_global_label_value(self):
    self.has_global_label_value_ = 0
    self.global_label_value_ = 0.0

  def has_global_label_value(self): return self.has_global_label_value_

  def global_label_bucket(self): return self.global_label_bucket_

  def set_global_label_bucket(self, x):
    self.has_global_label_bucket_ = 1
    self.global_label_bucket_ = x

  def clear_global_label_bucket(self):
    self.has_global_label_bucket_ = 0
    self.global_label_bucket_ = 0

  def has_global_label_bucket(self): return self.has_global_label_bucket_

  def provider_id_size(self): return len(self.provider_id_)
  def provider_id_list(self): return self.provider_id_

  def provider_id(self, i):
    return self.provider_id_[i]

  def set_provider_id(self, i, x):
    self.provider_id_[i] = x

  def add_provider_id(self, x):
    self.provider_id_.append(x)

  def clear_provider_id(self):
    self.provider_id_ = []

  def provider_size(self): return len(self.provider_)
  def provider_list(self): return self.provider_

  def provider(self, i):
    return self.provider_[i]

  def mutable_provider(self, i):
    return self.provider_[i]

  def add_provider(self):
    x = GoogleLabelData_LabelProvider()
    self.provider_.append(x)
    return x

  def clear_provider(self):
    self.provider_ = []

  def MergeFrom(self, x):
    assert x is not self
    if (x.has_label_id()): self.set_label_id(x.label_id())
    if (x.has_label_name()): self.set_label_name(x.label_name())
    if (x.has_confidence()): self.set_confidence(x.confidence())
    if (x.has_global_label_value()): self.set_global_label_value(x.global_label_value())
    if (x.has_global_label_bucket()): self.set_global_label_bucket(x.global_label_bucket())
    for i in xrange(x.provider_id_size()): self.add_provider_id(x.provider_id(i))
    for i in xrange(x.provider_size()): self.add_provider().CopyFrom(x.provider(i))

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'quality_labels.GoogleLabelData', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'quality_labels.GoogleLabelData')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'quality_labels.GoogleLabelData', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'quality_labels.GoogleLabelData', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'quality_labels.GoogleLabelData', s)


  def Equals(self, x):
    if x is self: return 1
    if self.has_label_id_ != x.has_label_id_: return 0
    if self.has_label_id_ and self.label_id_ != x.label_id_: return 0
    if self.has_label_name_ != x.has_label_name_: return 0
    if self.has_label_name_ and self.label_name_ != x.label_name_: return 0
    if self.has_confidence_ != x.has_confidence_: return 0
    if self.has_confidence_ and self.confidence_ != x.confidence_: return 0
    if self.has_global_label_value_ != x.has_global_label_value_: return 0
    if self.has_global_label_value_ and self.global_label_value_ != x.global_label_value_: return 0
    if self.has_global_label_bucket_ != x.has_global_label_bucket_: return 0
    if self.has_global_label_bucket_ and self.global_label_bucket_ != x.global_label_bucket_: return 0
    if len(self.provider_id_) != len(x.provider_id_): return 0
    for e1, e2 in zip(self.provider_id_, x.provider_id_):
      if e1 != e2: return 0
    if len(self.provider_) != len(x.provider_): return 0
    for e1, e2 in zip(self.provider_, x.provider_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    for i in xrange(len(self.provider_)):
      if (not self.provider_[i].IsInitialized(debug_strs)): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    if (self.has_label_id_): n += 1 + self.lengthVarInt64(self.label_id_)
    if (self.has_label_name_): n += 1 + self.lengthString(len(self.label_name_))
    if (self.has_confidence_): n += 5
    if (self.has_global_label_value_): n += 5
    if (self.has_global_label_bucket_): n += 1 + self.lengthVarInt64(self.global_label_bucket_)
    n += 1 * len(self.provider_id_)
    for i in xrange(len(self.provider_id_)): n += self.lengthVarInt64(self.provider_id_[i])
    n += 2 * len(self.provider_)
    for i in xrange(len(self.provider_)): n += self.provider_[i].ByteSize()
    return n + 0

  def Clear(self):
    self.clear_label_id()
    self.clear_label_name()
    self.clear_confidence()
    self.clear_global_label_value()
    self.clear_global_label_bucket()
    self.clear_provider_id()
    self.clear_provider()

  def OutputUnchecked(self, out):
    if (self.has_label_id_):
      out.putVarInt32(16)
      out.putVarInt32(self.label_id_)
    if (self.has_confidence_):
      out.putVarInt32(29)
      out.putFloat(self.confidence_)
    for i in xrange(len(self.provider_id_)):
      out.putVarInt32(32)
      out.putVarUint64(self.provider_id_[i])
    if (self.has_label_name_):
      out.putVarInt32(42)
      out.putPrefixedString(self.label_name_)
    for i in xrange(len(self.provider_)):
      out.putVarInt32(51)
      self.provider_[i].OutputUnchecked(out)
      out.putVarInt32(52)
    if (self.has_global_label_value_):
      out.putVarInt32(77)
      out.putFloat(self.global_label_value_)
    if (self.has_global_label_bucket_):
      out.putVarInt32(88)
      out.putVarInt32(self.global_label_bucket_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 12: break
      if tt == 16:
        self.set_label_id(d.getVarInt32())
        continue
      if tt == 29:
        self.set_confidence(d.getFloat())
        continue
      if tt == 32:
        self.add_provider_id(d.getVarUint64())
        continue
      if tt == 42:
        self.set_label_name(d.getPrefixedString())
        continue
      if tt == 51:
        self.add_provider().TryMerge(d)
        continue
      if tt == 77:
        self.set_global_label_value(d.getFloat())
        continue
      if tt == 88:
        self.set_global_label_bucket(d.getVarInt32())
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_label_id_: res+=prefix+("label_id: %s\n" % self.DebugFormatInt32(self.label_id_))
    if self.has_label_name_: res+=prefix+("label_name: %s\n" % self.DebugFormatString(self.label_name_))
    if self.has_confidence_: res+=prefix+("confidence: %s\n" % self.DebugFormatFloat(self.confidence_))
    if self.has_global_label_value_: res+=prefix+("global_label_value: %s\n" % self.DebugFormatFloat(self.global_label_value_))
    if self.has_global_label_bucket_: res+=prefix+("global_label_bucket: %s\n" % self.DebugFormatInt32(self.global_label_bucket_))
    cnt=0
    for e in self.provider_id_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("provider_id%s: %s\n" % (elm, self.DebugFormatInt64(e)))
      cnt+=1
    cnt=0
    for e in self.provider_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Provider%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    return res

class GoogleLabelData(ProtocolBuffer.ProtocolMessage):
  def __init__(self, contents=None):
    self.label_ = []
    if contents is not None: self.MergeFromString(contents)

  def label_size(self): return len(self.label_)
  def label_list(self): return self.label_

  def label(self, i):
    return self.label_[i]

  def mutable_label(self, i):
    return self.label_[i]

  def add_label(self):
    x = GoogleLabelData_Label()
    self.label_.append(x)
    return x

  def clear_label(self):
    self.label_ = []

  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.label_size()): self.add_label().CopyFrom(x.label(i))

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'quality_labels.GoogleLabelData', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'quality_labels.GoogleLabelData')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'quality_labels.GoogleLabelData', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'quality_labels.GoogleLabelData', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'quality_labels.GoogleLabelData', s)


  def Equals(self, x):
    if x is self: return 1
    if len(self.label_) != len(x.label_): return 0
    for e1, e2 in zip(self.label_, x.label_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    for i in xrange(len(self.label_)):
      if (not self.label_[i].IsInitialized(debug_strs)): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += 2 * len(self.label_)
    for i in xrange(len(self.label_)): n += self.label_[i].ByteSize()
    return n + 0

  def Clear(self):
    self.clear_label()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.label_)):
      out.putVarInt32(11)
      self.label_[i].OutputUnchecked(out)
      out.putVarInt32(12)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 11:
        self.add_label().TryMerge(d)
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.label_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Label%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    return res

  kLabelGroup = 1
  kLabellabel_id = 2
  kLabellabel_name = 5
  kLabelconfidence = 3
  kLabelglobal_label_value = 9
  kLabelglobal_label_bucket = 11
  kLabelprovider_id = 4
  kLabelProviderGroup = 6
  kLabelProviderid = 7
  kLabelProvidername = 8
  kLabelProviderlabel_value = 10
  kLabelProviderlabel_bucket = 12
  kLabelProviderfeed = 13

  _TEXT = (
   "ErrorCode",  #   0
   "Label",  #   1
   "label_id",  #   2
   "confidence",  #   3
   "provider_id",  #   4
   "label_name",  #   5
   "Provider",  #   6
   "id",  #   7
   "name",  #   8
   "global_label_value",  #   9
   "label_value",  #  10
   "global_label_bucket",  #  11
   "label_bucket",  #  12
   "feed",  #  13
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,  #   0
   ProtocolBuffer.Encoder.STARTGROUP,  #   1

   ProtocolBuffer.Encoder.NUMERIC,  #   2

   ProtocolBuffer.Encoder.FLOAT,  #   3

   ProtocolBuffer.Encoder.NUMERIC,  #   4

   ProtocolBuffer.Encoder.STRING,  #   5

   ProtocolBuffer.Encoder.STARTGROUP,  #   6

   ProtocolBuffer.Encoder.NUMERIC,  #   7

   ProtocolBuffer.Encoder.STRING,  #   8

   ProtocolBuffer.Encoder.FLOAT,  #   9

   ProtocolBuffer.Encoder.FLOAT,  #  10

   ProtocolBuffer.Encoder.NUMERIC,  #  11

   ProtocolBuffer.Encoder.NUMERIC,  #  12

   ProtocolBuffer.Encoder.NUMERIC,  #  13

  )

  # stylesheet for XML output
  _STYLE = \
   """"""
  _STYLE_CONTENT_TYPE = \
   """"""
  _SERIALIZED_DESCRIPTOR = array.array('B', [
    0x5a,
    0x2c,
    0x71,
    0x75,
    0x61,
    0x6c,
    0x69,
    0x74,
    0x79,
    0x2f,
    0x6c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x73,
    0x2f,
    0x70,
    0x72,
    0x6f,
    0x74,
    0x6f,
    0x2f,
    0x67,
    0x6f,
    0x6f,
    0x67,
    0x6c,
    0x65,
    0x2d,
    0x6c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2d,
    0x64,
    0x61,
    0x74,
    0x61,
    0x2e,
    0x70,
    0x72,
    0x6f,
    0x74,
    0x6f,
    0x0a,
    0x1e,
    0x71,
    0x75,
    0x61,
    0x6c,
    0x69,
    0x74,
    0x79,
    0x5f,
    0x6c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x73,
    0x2e,
    0x47,
    0x6f,
    0x6f,
    0x67,
    0x6c,
    0x65,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x44,
    0x61,
    0x74,
    0x61,
    0x13,
    0x1a,
    0x05,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x20,
    0x01,
    0x28,
    0x03,
    0x30,
    0x0a,
    0x38,
    0x03,
    0x14,
    0x13,
    0x1a,
    0x0e,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x6c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x5f,
    0x69,
    0x64,
    0x20,
    0x02,
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
    0x10,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x6c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x5f,
    0x6e,
    0x61,
    0x6d,
    0x65,
    0x20,
    0x05,
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
    0x10,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x63,
    0x6f,
    0x6e,
    0x66,
    0x69,
    0x64,
    0x65,
    0x6e,
    0x63,
    0x65,
    0x20,
    0x03,
    0x28,
    0x05,
    0x30,
    0x02,
    0x38,
    0x01,
    0x42,
    0x03,
    0x31,
    0x2e,
    0x30,
    0x60,
    0x00,
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
    0x03,
    0x31,
    0x2e,
    0x30,
    0xa4,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x18,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x67,
    0x6c,
    0x6f,
    0x62,
    0x61,
    0x6c,
    0x5f,
    0x6c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x5f,
    0x76,
    0x61,
    0x6c,
    0x75,
    0x65,
    0x20,
    0x09,
    0x28,
    0x05,
    0x30,
    0x02,
    0x38,
    0x01,
    0x60,
    0x00,
    0x14,
    0x13,
    0x1a,
    0x19,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x67,
    0x6c,
    0x6f,
    0x62,
    0x61,
    0x6c,
    0x5f,
    0x6c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x5f,
    0x62,
    0x75,
    0x63,
    0x6b,
    0x65,
    0x74,
    0x20,
    0x0b,
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
    0x11,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x70,
    0x72,
    0x6f,
    0x76,
    0x69,
    0x64,
    0x65,
    0x72,
    0x5f,
    0x69,
    0x64,
    0x20,
    0x04,
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
    0x0e,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x50,
    0x72,
    0x6f,
    0x76,
    0x69,
    0x64,
    0x65,
    0x72,
    0x20,
    0x06,
    0x28,
    0x03,
    0x30,
    0x0a,
    0x38,
    0x03,
    0x60,
    0x00,
    0x14,
    0x13,
    0x1a,
    0x11,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x50,
    0x72,
    0x6f,
    0x76,
    0x69,
    0x64,
    0x65,
    0x72,
    0x2e,
    0x69,
    0x64,
    0x20,
    0x07,
    0x28,
    0x00,
    0x30,
    0x04,
    0x38,
    0x02,
    0x60,
    0x07,
    0x14,
    0x13,
    0x1a,
    0x13,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x50,
    0x72,
    0x6f,
    0x76,
    0x69,
    0x64,
    0x65,
    0x72,
    0x2e,
    0x6e,
    0x61,
    0x6d,
    0x65,
    0x20,
    0x08,
    0x28,
    0x02,
    0x30,
    0x09,
    0x38,
    0x01,
    0x60,
    0x07,
    0x14,
    0x13,
    0x1a,
    0x1a,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x50,
    0x72,
    0x6f,
    0x76,
    0x69,
    0x64,
    0x65,
    0x72,
    0x2e,
    0x6c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x5f,
    0x76,
    0x61,
    0x6c,
    0x75,
    0x65,
    0x20,
    0x0a,
    0x28,
    0x05,
    0x30,
    0x02,
    0x38,
    0x01,
    0x42,
    0x03,
    0x31,
    0x2e,
    0x30,
    0x60,
    0x07,
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
    0x03,
    0x31,
    0x2e,
    0x30,
    0xa4,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x1b,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x50,
    0x72,
    0x6f,
    0x76,
    0x69,
    0x64,
    0x65,
    0x72,
    0x2e,
    0x6c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x5f,
    0x62,
    0x75,
    0x63,
    0x6b,
    0x65,
    0x74,
    0x20,
    0x0c,
    0x28,
    0x00,
    0x30,
    0x05,
    0x38,
    0x01,
    0x60,
    0x07,
    0x14,
    0x13,
    0x1a,
    0x13,
    0x4c,
    0x61,
    0x62,
    0x65,
    0x6c,
    0x2e,
    0x50,
    0x72,
    0x6f,
    0x76,
    0x69,
    0x64,
    0x65,
    0x72,
    0x2e,
    0x66,
    0x65,
    0x65,
    0x64,
    0x20,
    0x0d,
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
    0x60,
    0x07,
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

__all__ = ['GoogleLabelData','GoogleLabelData_LabelProvider','GoogleLabelData_Label']
