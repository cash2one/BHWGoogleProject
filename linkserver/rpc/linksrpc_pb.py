# This file automatically generated by protocol-compiler from linkserver/rpc/linksrpc.proto
# DO NOT EDIT!

from google3.net.proto import ProtocolBuffer
import array
import thread
from google3.net.proto import _net_proto___parse__python

__pychecker__ = """maxreturns=0 maxbranches=0 no-callinit
                   unusednames=printElemNumber,debug_strs no-special"""

class LinksCommandProto(ProtocolBuffer.ProtocolMessage):
  def __init__(self, contents=None):
    self.docid_ = 0
    self.wantforwardlinks_ = 0
    self.numlinkswanted_ = 0
    self.samplelinks_ = 0
    self.dataversion_ = ""
    self.wantasciiresults_ = 0
    self.timeoutinms_ = 0
    self.resultsformat_ = 20
    self.has_docid_ = 0
    self.has_wantforwardlinks_ = 0
    self.has_numlinkswanted_ = 0
    self.has_samplelinks_ = 0
    self.has_dataversion_ = 0
    self.has_wantasciiresults_ = 0
    self.has_timeoutinms_ = 0
    self.has_resultsformat_ = 0
    if contents is not None: self.MergeFromString(contents)

  def docid(self): return self.docid_

  def set_docid(self, x):
    self.has_docid_ = 1
    self.docid_ = x

  def clear_docid(self):
    self.has_docid_ = 0
    self.docid_ = 0

  def has_docid(self): return self.has_docid_

  def wantforwardlinks(self): return self.wantforwardlinks_

  def set_wantforwardlinks(self, x):
    self.has_wantforwardlinks_ = 1
    self.wantforwardlinks_ = x

  def clear_wantforwardlinks(self):
    self.has_wantforwardlinks_ = 0
    self.wantforwardlinks_ = 0

  def has_wantforwardlinks(self): return self.has_wantforwardlinks_

  def numlinkswanted(self): return self.numlinkswanted_

  def set_numlinkswanted(self, x):
    self.has_numlinkswanted_ = 1
    self.numlinkswanted_ = x

  def clear_numlinkswanted(self):
    self.has_numlinkswanted_ = 0
    self.numlinkswanted_ = 0

  def has_numlinkswanted(self): return self.has_numlinkswanted_

  def samplelinks(self): return self.samplelinks_

  def set_samplelinks(self, x):
    self.has_samplelinks_ = 1
    self.samplelinks_ = x

  def clear_samplelinks(self):
    self.has_samplelinks_ = 0
    self.samplelinks_ = 0

  def has_samplelinks(self): return self.has_samplelinks_

  def dataversion(self): return self.dataversion_

  def set_dataversion(self, x):
    self.has_dataversion_ = 1
    self.dataversion_ = x

  def clear_dataversion(self):
    self.has_dataversion_ = 0
    self.dataversion_ = ""

  def has_dataversion(self): return self.has_dataversion_

  def wantasciiresults(self): return self.wantasciiresults_

  def set_wantasciiresults(self, x):
    self.has_wantasciiresults_ = 1
    self.wantasciiresults_ = x

  def clear_wantasciiresults(self):
    self.has_wantasciiresults_ = 0
    self.wantasciiresults_ = 0

  def has_wantasciiresults(self): return self.has_wantasciiresults_

  def timeoutinms(self): return self.timeoutinms_

  def set_timeoutinms(self, x):
    self.has_timeoutinms_ = 1
    self.timeoutinms_ = x

  def clear_timeoutinms(self):
    self.has_timeoutinms_ = 0
    self.timeoutinms_ = 0

  def has_timeoutinms(self): return self.has_timeoutinms_

  def resultsformat(self): return self.resultsformat_

  def set_resultsformat(self, x):
    self.has_resultsformat_ = 1
    self.resultsformat_ = x

  def clear_resultsformat(self):
    self.has_resultsformat_ = 0
    self.resultsformat_ = 20

  def has_resultsformat(self): return self.has_resultsformat_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_docid()): self.set_docid(x.docid())
    if (x.has_wantforwardlinks()): self.set_wantforwardlinks(x.wantforwardlinks())
    if (x.has_numlinkswanted()): self.set_numlinkswanted(x.numlinkswanted())
    if (x.has_samplelinks()): self.set_samplelinks(x.samplelinks())
    if (x.has_dataversion()): self.set_dataversion(x.dataversion())
    if (x.has_wantasciiresults()): self.set_wantasciiresults(x.wantasciiresults())
    if (x.has_timeoutinms()): self.set_timeoutinms(x.timeoutinms())
    if (x.has_resultsformat()): self.set_resultsformat(x.resultsformat())

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'LinksCommandProto', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'LinksCommandProto')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'LinksCommandProto', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'LinksCommandProto', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'LinksCommandProto', s)


  def Equals(self, x):
    if x is self: return 1
    if self.has_docid_ != x.has_docid_: return 0
    if self.has_docid_ and self.docid_ != x.docid_: return 0
    if self.has_wantforwardlinks_ != x.has_wantforwardlinks_: return 0
    if self.has_wantforwardlinks_ and self.wantforwardlinks_ != x.wantforwardlinks_: return 0
    if self.has_numlinkswanted_ != x.has_numlinkswanted_: return 0
    if self.has_numlinkswanted_ and self.numlinkswanted_ != x.numlinkswanted_: return 0
    if self.has_samplelinks_ != x.has_samplelinks_: return 0
    if self.has_samplelinks_ and self.samplelinks_ != x.samplelinks_: return 0
    if self.has_dataversion_ != x.has_dataversion_: return 0
    if self.has_dataversion_ and self.dataversion_ != x.dataversion_: return 0
    if self.has_wantasciiresults_ != x.has_wantasciiresults_: return 0
    if self.has_wantasciiresults_ and self.wantasciiresults_ != x.wantasciiresults_: return 0
    if self.has_timeoutinms_ != x.has_timeoutinms_: return 0
    if self.has_timeoutinms_ and self.timeoutinms_ != x.timeoutinms_: return 0
    if self.has_resultsformat_ != x.has_resultsformat_: return 0
    if self.has_resultsformat_ and self.resultsformat_ != x.resultsformat_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_docid_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: docid not set.')
    if (not self.has_wantforwardlinks_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: wantforwardlinks not set.')
    if (not self.has_numlinkswanted_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: numlinkswanted not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.docid_)
    n += self.lengthVarInt64(self.numlinkswanted_)
    if (self.has_samplelinks_): n += 2
    if (self.has_dataversion_): n += 1 + self.lengthString(len(self.dataversion_))
    if (self.has_wantasciiresults_): n += 2
    if (self.has_timeoutinms_): n += 1 + self.lengthVarInt64(self.timeoutinms_)
    if (self.has_resultsformat_): n += 2 + self.lengthVarInt64(self.resultsformat_)
    return n + 4

  def Clear(self):
    self.clear_docid()
    self.clear_wantforwardlinks()
    self.clear_numlinkswanted()
    self.clear_samplelinks()
    self.clear_dataversion()
    self.clear_wantasciiresults()
    self.clear_timeoutinms()
    self.clear_resultsformat()

  def OutputUnchecked(self, out):
    out.putVarInt32(8)
    out.putVarUint64(self.docid_)
    out.putVarInt32(16)
    out.putBoolean(self.wantforwardlinks_)
    out.putVarInt32(24)
    out.putVarInt32(self.numlinkswanted_)
    if (self.has_samplelinks_):
      out.putVarInt32(32)
      out.putBoolean(self.samplelinks_)
    if (self.has_dataversion_):
      out.putVarInt32(42)
      out.putPrefixedString(self.dataversion_)
    if (self.has_wantasciiresults_):
      out.putVarInt32(48)
      out.putBoolean(self.wantasciiresults_)
    if (self.has_timeoutinms_):
      out.putVarInt32(56)
      out.putVarInt32(self.timeoutinms_)
    if (self.has_resultsformat_):
      out.putVarInt32(808)
      out.putVarInt32(self.resultsformat_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.set_docid(d.getVarUint64())
        continue
      if tt == 16:
        self.set_wantforwardlinks(d.getBoolean())
        continue
      if tt == 24:
        self.set_numlinkswanted(d.getVarInt32())
        continue
      if tt == 32:
        self.set_samplelinks(d.getBoolean())
        continue
      if tt == 42:
        self.set_dataversion(d.getPrefixedString())
        continue
      if tt == 48:
        self.set_wantasciiresults(d.getBoolean())
        continue
      if tt == 56:
        self.set_timeoutinms(d.getVarInt32())
        continue
      if tt == 808:
        self.set_resultsformat(d.getVarInt32())
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_docid_: res+=prefix+("Docid: %s\n" % self.DebugFormatInt64(self.docid_))
    if self.has_wantforwardlinks_: res+=prefix+("WantForwardLinks: %s\n" % self.DebugFormatBool(self.wantforwardlinks_))
    if self.has_numlinkswanted_: res+=prefix+("NumLinksWanted: %s\n" % self.DebugFormatInt32(self.numlinkswanted_))
    if self.has_samplelinks_: res+=prefix+("SampleLinks: %s\n" % self.DebugFormatBool(self.samplelinks_))
    if self.has_dataversion_: res+=prefix+("DataVersion: %s\n" % self.DebugFormatString(self.dataversion_))
    if self.has_wantasciiresults_: res+=prefix+("WantAsciiResults: %s\n" % self.DebugFormatBool(self.wantasciiresults_))
    if self.has_timeoutinms_: res+=prefix+("TimeoutInMs: %s\n" % self.DebugFormatInt32(self.timeoutinms_))
    if self.has_resultsformat_: res+=prefix+("ResultsFormat: %s\n" % self.DebugFormatInt32(self.resultsformat_))
    return res

  kDocid = 1
  kWantForwardLinks = 2
  kNumLinksWanted = 3
  kSampleLinks = 4
  kDataVersion = 5
  kWantAsciiResults = 6
  kTimeoutInMs = 7
  kResultsFormat = 101

  _TEXT = (
   "ErrorCode",  #   0
   "Docid",  #   1
   "WantForwardLinks",  #   2
   "NumLinksWanted",  #   3
   "SampleLinks",  #   4
   "DataVersion",  #   5
   "WantAsciiResults",  #   6
   "TimeoutInMs",  #   7
   None,  #   8
   None,  #   9
   None,  #  10
   None,  #  11
   None,  #  12
   None,  #  13
   None,  #  14
   None,  #  15
   None,  #  16
   None,  #  17
   None,  #  18
   None,  #  19
   None,  #  20
   None,  #  21
   None,  #  22
   None,  #  23
   None,  #  24
   None,  #  25
   None,  #  26
   None,  #  27
   None,  #  28
   None,  #  29
   None,  #  30
   None,  #  31
   None,  #  32
   None,  #  33
   None,  #  34
   None,  #  35
   None,  #  36
   None,  #  37
   None,  #  38
   None,  #  39
   None,  #  40
   None,  #  41
   None,  #  42
   None,  #  43
   None,  #  44
   None,  #  45
   None,  #  46
   None,  #  47
   None,  #  48
   None,  #  49
   None,  #  50
   None,  #  51
   None,  #  52
   None,  #  53
   None,  #  54
   None,  #  55
   None,  #  56
   None,  #  57
   None,  #  58
   None,  #  59
   None,  #  60
   None,  #  61
   None,  #  62
   None,  #  63
   None,  #  64
   None,  #  65
   None,  #  66
   None,  #  67
   None,  #  68
   None,  #  69
   None,  #  70
   None,  #  71
   None,  #  72
   None,  #  73
   None,  #  74
   None,  #  75
   None,  #  76
   None,  #  77
   None,  #  78
   None,  #  79
   None,  #  80
   None,  #  81
   None,  #  82
   None,  #  83
   None,  #  84
   None,  #  85
   None,  #  86
   None,  #  87
   None,  #  88
   None,  #  89
   None,  #  90
   None,  #  91
   None,  #  92
   None,  #  93
   None,  #  94
   None,  #  95
   None,  #  96
   None,  #  97
   None,  #  98
   None,  #  99
   None,  # 100
   "ResultsFormat",  # 101
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,  #   0
   ProtocolBuffer.Encoder.NUMERIC,  #   1

   ProtocolBuffer.Encoder.NUMERIC,  #   2

   ProtocolBuffer.Encoder.NUMERIC,  #   3

   ProtocolBuffer.Encoder.NUMERIC,  #   4

   ProtocolBuffer.Encoder.STRING,  #   5

   ProtocolBuffer.Encoder.NUMERIC,  #   6

   ProtocolBuffer.Encoder.NUMERIC,  #   7

   ProtocolBuffer.Encoder.MAX_TYPE,  #   8

   ProtocolBuffer.Encoder.MAX_TYPE,  #   9

   ProtocolBuffer.Encoder.MAX_TYPE,  #  10

   ProtocolBuffer.Encoder.MAX_TYPE,  #  11

   ProtocolBuffer.Encoder.MAX_TYPE,  #  12

   ProtocolBuffer.Encoder.MAX_TYPE,  #  13

   ProtocolBuffer.Encoder.MAX_TYPE,  #  14

   ProtocolBuffer.Encoder.MAX_TYPE,  #  15

   ProtocolBuffer.Encoder.MAX_TYPE,  #  16

   ProtocolBuffer.Encoder.MAX_TYPE,  #  17

   ProtocolBuffer.Encoder.MAX_TYPE,  #  18

   ProtocolBuffer.Encoder.MAX_TYPE,  #  19

   ProtocolBuffer.Encoder.MAX_TYPE,  #  20

   ProtocolBuffer.Encoder.MAX_TYPE,  #  21

   ProtocolBuffer.Encoder.MAX_TYPE,  #  22

   ProtocolBuffer.Encoder.MAX_TYPE,  #  23

   ProtocolBuffer.Encoder.MAX_TYPE,  #  24

   ProtocolBuffer.Encoder.MAX_TYPE,  #  25

   ProtocolBuffer.Encoder.MAX_TYPE,  #  26

   ProtocolBuffer.Encoder.MAX_TYPE,  #  27

   ProtocolBuffer.Encoder.MAX_TYPE,  #  28

   ProtocolBuffer.Encoder.MAX_TYPE,  #  29

   ProtocolBuffer.Encoder.MAX_TYPE,  #  30

   ProtocolBuffer.Encoder.MAX_TYPE,  #  31

   ProtocolBuffer.Encoder.MAX_TYPE,  #  32

   ProtocolBuffer.Encoder.MAX_TYPE,  #  33

   ProtocolBuffer.Encoder.MAX_TYPE,  #  34

   ProtocolBuffer.Encoder.MAX_TYPE,  #  35

   ProtocolBuffer.Encoder.MAX_TYPE,  #  36

   ProtocolBuffer.Encoder.MAX_TYPE,  #  37

   ProtocolBuffer.Encoder.MAX_TYPE,  #  38

   ProtocolBuffer.Encoder.MAX_TYPE,  #  39

   ProtocolBuffer.Encoder.MAX_TYPE,  #  40

   ProtocolBuffer.Encoder.MAX_TYPE,  #  41

   ProtocolBuffer.Encoder.MAX_TYPE,  #  42

   ProtocolBuffer.Encoder.MAX_TYPE,  #  43

   ProtocolBuffer.Encoder.MAX_TYPE,  #  44

   ProtocolBuffer.Encoder.MAX_TYPE,  #  45

   ProtocolBuffer.Encoder.MAX_TYPE,  #  46

   ProtocolBuffer.Encoder.MAX_TYPE,  #  47

   ProtocolBuffer.Encoder.MAX_TYPE,  #  48

   ProtocolBuffer.Encoder.MAX_TYPE,  #  49

   ProtocolBuffer.Encoder.MAX_TYPE,  #  50

   ProtocolBuffer.Encoder.MAX_TYPE,  #  51

   ProtocolBuffer.Encoder.MAX_TYPE,  #  52

   ProtocolBuffer.Encoder.MAX_TYPE,  #  53

   ProtocolBuffer.Encoder.MAX_TYPE,  #  54

   ProtocolBuffer.Encoder.MAX_TYPE,  #  55

   ProtocolBuffer.Encoder.MAX_TYPE,  #  56

   ProtocolBuffer.Encoder.MAX_TYPE,  #  57

   ProtocolBuffer.Encoder.MAX_TYPE,  #  58

   ProtocolBuffer.Encoder.MAX_TYPE,  #  59

   ProtocolBuffer.Encoder.MAX_TYPE,  #  60

   ProtocolBuffer.Encoder.MAX_TYPE,  #  61

   ProtocolBuffer.Encoder.MAX_TYPE,  #  62

   ProtocolBuffer.Encoder.MAX_TYPE,  #  63

   ProtocolBuffer.Encoder.MAX_TYPE,  #  64

   ProtocolBuffer.Encoder.MAX_TYPE,  #  65

   ProtocolBuffer.Encoder.MAX_TYPE,  #  66

   ProtocolBuffer.Encoder.MAX_TYPE,  #  67

   ProtocolBuffer.Encoder.MAX_TYPE,  #  68

   ProtocolBuffer.Encoder.MAX_TYPE,  #  69

   ProtocolBuffer.Encoder.MAX_TYPE,  #  70

   ProtocolBuffer.Encoder.MAX_TYPE,  #  71

   ProtocolBuffer.Encoder.MAX_TYPE,  #  72

   ProtocolBuffer.Encoder.MAX_TYPE,  #  73

   ProtocolBuffer.Encoder.MAX_TYPE,  #  74

   ProtocolBuffer.Encoder.MAX_TYPE,  #  75

   ProtocolBuffer.Encoder.MAX_TYPE,  #  76

   ProtocolBuffer.Encoder.MAX_TYPE,  #  77

   ProtocolBuffer.Encoder.MAX_TYPE,  #  78

   ProtocolBuffer.Encoder.MAX_TYPE,  #  79

   ProtocolBuffer.Encoder.MAX_TYPE,  #  80

   ProtocolBuffer.Encoder.MAX_TYPE,  #  81

   ProtocolBuffer.Encoder.MAX_TYPE,  #  82

   ProtocolBuffer.Encoder.MAX_TYPE,  #  83

   ProtocolBuffer.Encoder.MAX_TYPE,  #  84

   ProtocolBuffer.Encoder.MAX_TYPE,  #  85

   ProtocolBuffer.Encoder.MAX_TYPE,  #  86

   ProtocolBuffer.Encoder.MAX_TYPE,  #  87

   ProtocolBuffer.Encoder.MAX_TYPE,  #  88

   ProtocolBuffer.Encoder.MAX_TYPE,  #  89

   ProtocolBuffer.Encoder.MAX_TYPE,  #  90

   ProtocolBuffer.Encoder.MAX_TYPE,  #  91

   ProtocolBuffer.Encoder.MAX_TYPE,  #  92

   ProtocolBuffer.Encoder.MAX_TYPE,  #  93

   ProtocolBuffer.Encoder.MAX_TYPE,  #  94

   ProtocolBuffer.Encoder.MAX_TYPE,  #  95

   ProtocolBuffer.Encoder.MAX_TYPE,  #  96

   ProtocolBuffer.Encoder.MAX_TYPE,  #  97

   ProtocolBuffer.Encoder.MAX_TYPE,  #  98

   ProtocolBuffer.Encoder.MAX_TYPE,  #  99

   ProtocolBuffer.Encoder.MAX_TYPE,  # 100

   ProtocolBuffer.Encoder.NUMERIC,  # 101

  )

  # stylesheet for XML output
  _STYLE = \
   """"""
  _STYLE_CONTENT_TYPE = \
   """"""
  _SERIALIZED_DESCRIPTOR = array.array('B', [
    0x5a,
    0x1d,
    0x6c,
    0x69,
    0x6e,
    0x6b,
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
    0x6c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x72,
    0x70,
    0x63,
    0x2e,
    0x70,
    0x72,
    0x6f,
    0x74,
    0x6f,
    0x0a,
    0x11,
    0x4c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x43,
    0x6f,
    0x6d,
    0x6d,
    0x61,
    0x6e,
    0x64,
    0x50,
    0x72,
    0x6f,
    0x74,
    0x6f,
    0x13,
    0x1a,
    0x05,
    0x44,
    0x6f,
    0x63,
    0x69,
    0x64,
    0x20,
    0x01,
    0x28,
    0x00,
    0x30,
    0x04,
    0x38,
    0x02,
    0x14,
    0x13,
    0x1a,
    0x10,
    0x57,
    0x61,
    0x6e,
    0x74,
    0x46,
    0x6f,
    0x72,
    0x77,
    0x61,
    0x72,
    0x64,
    0x4c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x20,
    0x02,
    0x28,
    0x00,
    0x30,
    0x08,
    0x38,
    0x02,
    0x14,
    0x13,
    0x1a,
    0x0e,
    0x4e,
    0x75,
    0x6d,
    0x4c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x57,
    0x61,
    0x6e,
    0x74,
    0x65,
    0x64,
    0x20,
    0x03,
    0x28,
    0x00,
    0x30,
    0x05,
    0x38,
    0x02,
    0x14,
    0x13,
    0x1a,
    0x0b,
    0x53,
    0x61,
    0x6d,
    0x70,
    0x6c,
    0x65,
    0x4c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x20,
    0x04,
    0x28,
    0x00,
    0x30,
    0x08,
    0x38,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x0b,
    0x44,
    0x61,
    0x74,
    0x61,
    0x56,
    0x65,
    0x72,
    0x73,
    0x69,
    0x6f,
    0x6e,
    0x20,
    0x05,
    0x28,
    0x02,
    0x30,
    0x09,
    0x38,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x10,
    0x57,
    0x61,
    0x6e,
    0x74,
    0x41,
    0x73,
    0x63,
    0x69,
    0x69,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x73,
    0x20,
    0x06,
    0x28,
    0x00,
    0x30,
    0x08,
    0x38,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x0b,
    0x54,
    0x69,
    0x6d,
    0x65,
    0x6f,
    0x75,
    0x74,
    0x49,
    0x6e,
    0x4d,
    0x73,
    0x20,
    0x07,
    0x28,
    0x00,
    0x30,
    0x05,
    0x38,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x0d,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x73,
    0x46,
    0x6f,
    0x72,
    0x6d,
    0x61,
    0x74,
    0x20,
    0x65,
    0x28,
    0x00,
    0x30,
    0x05,
    0x38,
    0x01,
    0x42,
    0x02,
    0x32,
    0x30,
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
    0x02,
    0x32,
    0x30,
    0xa4,
    0x01,
    0x14,
    ])
  _net_proto___parse__python.RegisterType(_SERIALIZED_DESCRIPTOR.tostring())
class LinksResultsProto_Links(ProtocolBuffer.ProtocolMessage):
  def __init__(self, contents=None):
    self.docid_ = 0
    self.pagerank_ = 0.0
    self.has_docid_ = 0
    self.has_pagerank_ = 0
    if contents is not None: self.MergeFromString(contents)

  def docid(self): return self.docid_

  def set_docid(self, x):
    self.has_docid_ = 1
    self.docid_ = x

  def clear_docid(self):
    self.has_docid_ = 0
    self.docid_ = 0

  def has_docid(self): return self.has_docid_

  def pagerank(self): return self.pagerank_

  def set_pagerank(self, x):
    self.has_pagerank_ = 1
    self.pagerank_ = x

  def clear_pagerank(self):
    self.has_pagerank_ = 0
    self.pagerank_ = 0.0

  def has_pagerank(self): return self.has_pagerank_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_docid()): self.set_docid(x.docid())
    if (x.has_pagerank()): self.set_pagerank(x.pagerank())

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'LinksResultsProto', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'LinksResultsProto')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'LinksResultsProto', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'LinksResultsProto', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'LinksResultsProto', s)


  def Equals(self, x):
    if x is self: return 1
    if self.has_docid_ != x.has_docid_: return 0
    if self.has_docid_ and self.docid_ != x.docid_: return 0
    if self.has_pagerank_ != x.has_pagerank_: return 0
    if self.has_pagerank_ and self.pagerank_ != x.pagerank_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_docid_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: docid not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.docid_)
    if (self.has_pagerank_): n += 5
    return n + 1

  def Clear(self):
    self.clear_docid()
    self.clear_pagerank()

  def OutputUnchecked(self, out):
    out.putVarInt32(24)
    out.putVarUint64(self.docid_)
    if (self.has_pagerank_):
      out.putVarInt32(37)
      out.putFloat(self.pagerank_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 20: break
      if tt == 24:
        self.set_docid(d.getVarUint64())
        continue
      if tt == 37:
        self.set_pagerank(d.getFloat())
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_docid_: res+=prefix+("Docid: %s\n" % self.DebugFormatInt64(self.docid_))
    if self.has_pagerank_: res+=prefix+("Pagerank: %s\n" % self.DebugFormatFloat(self.pagerank_))
    return res

class LinksResultsProto(ProtocolBuffer.ProtocolMessage):
  def __init__(self, contents=None):
    self.totallinks_ = 0
    self.links_ = []
    self.has_totallinks_ = 0
    if contents is not None: self.MergeFromString(contents)

  def totallinks(self): return self.totallinks_

  def set_totallinks(self, x):
    self.has_totallinks_ = 1
    self.totallinks_ = x

  def clear_totallinks(self):
    self.has_totallinks_ = 0
    self.totallinks_ = 0

  def has_totallinks(self): return self.has_totallinks_

  def links_size(self): return len(self.links_)
  def links_list(self): return self.links_

  def links(self, i):
    return self.links_[i]

  def mutable_links(self, i):
    return self.links_[i]

  def add_links(self):
    x = LinksResultsProto_Links()
    self.links_.append(x)
    return x

  def clear_links(self):
    self.links_ = []

  def MergeFrom(self, x):
    assert x is not self
    if (x.has_totallinks()): self.set_totallinks(x.totallinks())
    for i in xrange(x.links_size()): self.add_links().CopyFrom(x.links(i))

  def _CMergeFromString(self, s):
    _net_proto___parse__python.MergeFromString(self, 'LinksResultsProto', s)

  def _CEncode(self):
    return _net_proto___parse__python.Encode(self, 'LinksResultsProto')

  def _CToASCII(self, output_format):
    return _net_proto___parse__python.ToASCII(self, 'LinksResultsProto', output_format)


  def ParseASCII(self, s):
    _net_proto___parse__python.ParseASCII(self, 'LinksResultsProto', s)


  def ParseASCIIIgnoreUnknown(self, s):
    _net_proto___parse__python.ParseASCIIIgnoreUnknown(self, 'LinksResultsProto', s)


  def Equals(self, x):
    if x is self: return 1
    if self.has_totallinks_ != x.has_totallinks_: return 0
    if self.has_totallinks_ and self.totallinks_ != x.totallinks_: return 0
    if len(self.links_) != len(x.links_): return 0
    for e1, e2 in zip(self.links_, x.links_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_totallinks_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: totallinks not set.')
    for i in xrange(len(self.links_)):
      if (not self.links_[i].IsInitialized(debug_strs)): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.totallinks_)
    n += 2 * len(self.links_)
    for i in xrange(len(self.links_)): n += self.links_[i].ByteSize()
    return n + 1

  def Clear(self):
    self.clear_totallinks()
    self.clear_links()

  def OutputUnchecked(self, out):
    out.putVarInt32(8)
    out.putVarInt64(self.totallinks_)
    for i in xrange(len(self.links_)):
      out.putVarInt32(19)
      self.links_[i].OutputUnchecked(out)
      out.putVarInt32(20)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.set_totallinks(d.getVarInt64())
        continue
      if tt == 19:
        self.add_links().TryMerge(d)
        continue
      # tag 0 is special: it's used to indicate an error.
      # so if we see it we raise an exception.
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_totallinks_: res+=prefix+("TotalLinks: %s\n" % self.DebugFormatInt64(self.totallinks_))
    cnt=0
    for e in self.links_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Links%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    return res

  kTotalLinks = 1
  kLinksGroup = 2
  kLinksDocid = 3
  kLinksPagerank = 4

  _TEXT = (
   "ErrorCode",  #   0
   "TotalLinks",  #   1
   "Links",  #   2
   "Docid",  #   3
   "Pagerank",  #   4
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,  #   0
   ProtocolBuffer.Encoder.NUMERIC,  #   1

   ProtocolBuffer.Encoder.STARTGROUP,  #   2

   ProtocolBuffer.Encoder.NUMERIC,  #   3

   ProtocolBuffer.Encoder.FLOAT,  #   4

  )

  # stylesheet for XML output
  _STYLE = \
   """"""
  _STYLE_CONTENT_TYPE = \
   """"""
  _SERIALIZED_DESCRIPTOR = array.array('B', [
    0x5a,
    0x1d,
    0x6c,
    0x69,
    0x6e,
    0x6b,
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
    0x6c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x72,
    0x70,
    0x63,
    0x2e,
    0x70,
    0x72,
    0x6f,
    0x74,
    0x6f,
    0x0a,
    0x11,
    0x4c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x52,
    0x65,
    0x73,
    0x75,
    0x6c,
    0x74,
    0x73,
    0x50,
    0x72,
    0x6f,
    0x74,
    0x6f,
    0x13,
    0x1a,
    0x0a,
    0x54,
    0x6f,
    0x74,
    0x61,
    0x6c,
    0x4c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x20,
    0x01,
    0x28,
    0x00,
    0x30,
    0x03,
    0x38,
    0x02,
    0x14,
    0x13,
    0x1a,
    0x05,
    0x4c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x20,
    0x02,
    0x28,
    0x03,
    0x30,
    0x0a,
    0x38,
    0x03,
    0x14,
    0x13,
    0x1a,
    0x0b,
    0x4c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x2e,
    0x44,
    0x6f,
    0x63,
    0x69,
    0x64,
    0x20,
    0x03,
    0x28,
    0x00,
    0x30,
    0x04,
    0x38,
    0x02,
    0x60,
    0x01,
    0x14,
    0x13,
    0x1a,
    0x0e,
    0x4c,
    0x69,
    0x6e,
    0x6b,
    0x73,
    0x2e,
    0x50,
    0x61,
    0x67,
    0x65,
    0x72,
    0x61,
    0x6e,
    0x6b,
    0x20,
    0x04,
    0x28,
    0x05,
    0x30,
    0x02,
    0x38,
    0x01,
    0x60,
    0x01,
    0x14,
    ])
  _net_proto___parse__python.RegisterType(_SERIALIZED_DESCRIPTOR.tostring())

__all__ = ['LinksCommandProto','LinksResultsProto','LinksResultsProto_Links']
