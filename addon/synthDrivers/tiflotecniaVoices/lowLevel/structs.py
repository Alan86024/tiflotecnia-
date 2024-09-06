from ctypes import *
from enum import IntEnum

VE_CURRENT_VERSION = 0x0520
VE_MAX_STRING_LENGTH = 128
VPLATFORM_CURRENT_VERSION = 0x0200

NUAN_OK = 0
NUAN_E_TTS_USERSTOP = 0x80000807
NUAN_E_WRONG_STATE = 0x80000011
NUAN_E_NOTFOUND = 0x80000014

PITCH_MAX = 200
PITCH_MIN = 50
RATE_MAX = 400
RATE_MIN = 50
VOLUME_MAX = 100
VOLUME_MIN = 0
WAITFACTOR_MAX = 9
WAITFACTOR_MIN = 0

VE_NORM_TEXT = 0
VE_SSML_TEXT = 1

class Param(IntEnum):
    LANGUAGE = 1
    VOICE                  = 2
    VOICE_OPERATING_POINT  = 3
    FREQUENCY              = 4
    EXTRAESCLANG           = 5
    EXTRAESCTN             = 6
    TYPE_OF_CHAR           = 7
    VOLUME                 = 8
    SPEECHRATE = 9
    PITCH                  = 10
    WAITFACTOR             = 11
    READMODE               = 12
    TEXTMODE               = 13 
    MAX_INPUT_LENGTH       = 14
    LIDSCOPE               = 15
    LIDVOICESWITCH         = 16
    LIDMODE                = 17
    LIDLANGUAGES           = 18
    MARKER_MODE            = 19
    INITMODE               = 20
    VOP_VERSION = 21
    DISABLE_FINAL_SILENCE = 22
    FOREIGN_LANGUAGES = 23
    TIMBRE = 24

VE_INITMODE_LOAD_ONCE_OPEN_ALL = 0xC
VE_INITMODE_LOAD_OPEN_ALL_EACH_TIME = 0x3

VE_TEXTMODE_STANDARD = 1
VE_TEXTMODE_SMS = 2

class ReadMode(IntEnum):
    SENT = 1
    CHAR = 2
    WORD = 3
    LINE = 4

VE_MRK_OFF = 0
VE_MRK_ON = 1

VE_LIDVOICESWITCH_OFF = 0
VE_LIDVOICESWITCH_ON = 1

VE_LIDMODE_MEMORY_BIASED = 0
VE_LIDMODE_FORCED_CHOICE = 1

VE_LIDSCOPE_NONE         = 0
VE_LIDSCOPE_USERDEFINED  = 1

VE_MSG_BEGINPROCESS   = 0x00000001
VE_MSG_ENDPROCESS     = 0x00000002
VE_MSG_PROCESS      = 0x00000004
VE_MSG_OUTBUFREQ      = 0x00000008
VE_MSG_OUTBUFDONE     = 0x00000010
VE_MSG_STOP           = 0x00000020
VE_MSG_PAUSE          = 0x00000040
VE_MSG_RESUME         = 0x00000080
VE_MSG_TAIBEGIN       = 0x00000100
VE_MSG_TAIEND         = 0x00000200
VE_MSG_TAIBUFREQ      = 0x00000400
VE_MSG_TAIBUFDONE     = 0x00000800

VE_MRK_TEXTUNIT = 0x0001
VE_MRK_WORD = 0x0002
VE_MRK_PHONEME = 0x0004
VE_MRK_BOOKMARK = 0x0008
VE_MRK_PROMPT = 0x0010

VE_TYPE_OF_CHAR_UTF16   = 1
VE_TYPE_OF_CHAR_UTF8    = 2

VE_PCMSTAT_TXTUNIT_NEW = 1
VE_PCMSTAT_TXTUNIT_MID = 2
VE_PCMSTAT_DONE = 0xFFFF

sampleRateConversions = {8 : 8000,
	11 : 11025,
	16 : 16000,
	22 : 22050}

class VE_HSAFE(Structure):
	_fields_ = (('pHandleData', c_void_p),
	('u32Check', c_uint))
	def __eq__(self, other):
		return addressof(self) == addressof(other) or self.pHandleData == other.pHandleData

	def __hash__(self):
		return addressof(self) ^ self.pHandleData

class VE_INSTALL(Structure):
	_fields_ = (('fmtVersion', c_ushort),
	('pBinBrokerInfo', c_char_p),
	('pIHeap', c_void_p),
	('hHeap', c_void_p),
	('pICritSec', c_void_p),
	('hCSClass', c_void_p),
	('pIDataStream', c_void_p),
	('pIDataMapping', c_void_p),
	('hDataClass', c_void_p),
	('pILog', c_void_p),
	('hLog', c_void_p),
	('pIClock', c_void_p),
	('hClock', c_void_p),
	('pIThread', c_void_p),
	('pISemaphore', c_void_p),
	('hThdClass', c_void_p))

class VPLATFORM_MEMBLOCK(Structure):
	_fields_ = [('start', c_void_p),
	('cByte', c_uint),
	('cFlags', c_uint)]

class VPLATFORM_RESOURCES(Structure):
	_fields_ = (('fmtVersion', c_ushort),
	('u16NbrOfDataInstall', c_ushort),
	('apDataInstall', POINTER(c_wchar_p)),
	('stHeap', VPLATFORM_MEMBLOCK),
	('pDatPtr_Table', c_void_p),
	('szBinaryBroker', c_wchar_p),
	('szFileListFile', c_wchar_p),
	('bFlags', c_uint),
	('rfu1', c_uint))

class VE_INTEXT(Structure):
	_fields_ = (('eTextFormat', c_int),
	('cntTextLength', c_size_t),
	('szInText', c_void_p))

class VE_LPARAM(Union):
	_fields_ = (('lValue', c_uint),
	('lError', c_uint))

class VE_PARAM_VALUE(Union):
	_fields_ = (('usValue', c_ushort),
	('szStringValue', (c_char * VE_MAX_STRING_LENGTH)))

class VE_PARAM(Structure):
	_fields_ = (('eID', c_uint),
	('uValue', VE_PARAM_VALUE))

class VE_CALLBACKMSG(Structure):
	_fields_ = (('eMessage', c_uint),
	('lValue', c_int),
	('pParam', c_void_p))

VE_CBOUTNOTIFY = CFUNCTYPE(c_uint, VE_HSAFE, c_void_p, POINTER(VE_CALLBACKMSG))

class VE_OUTDEVINFO(Structure):
	_fields_ = (('userData', c_void_p),
	('pfOutNotify', VE_CBOUTNOTIFY))

class VE_LANGUAGE(Structure):
	_fields_ = (('szLanguage', (c_char * VE_MAX_STRING_LENGTH)),
	('szLanguageTLW', (c_char * 4)),
	('szVersion', (c_char * VE_MAX_STRING_LENGTH)))

class VE_VOICEINFO(Structure):
	_fields_ = (('szVersion', (c_char * VE_MAX_STRING_LENGTH)),
	('szLanguage', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceName', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceAge', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceType', (c_char * VE_MAX_STRING_LENGTH)),
	('szForeignLanguages', (c_char * VE_MAX_STRING_LENGTH)))

	def __eq__(self, other):
		return isinstance(other, type(self)) and addressof(self) == addressof(other)

class VE_SPEECHDBINFO(Structure):
	_fields_ = (('szVersion', (c_char * VE_MAX_STRING_LENGTH)),
	('szLanguage', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceName', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceOperatingPoint', (c_char * VE_MAX_STRING_LENGTH)),
	('u16Freq', c_ushort))

class VE_MARKINFO(Structure):
	_fields_ = [('eMrkType', c_uint),
	('cntSrcPos', c_size_t),
	('cntSrcTextLen', c_size_t),
	('cntDestPos', c_size_t),
	('cntDestLen', c_uint),
	('usValue', c_uint),
	('ulValue', c_uint),
	('szValue', c_char_p)]

class VE_OUTDATA(Structure):
	_fields_ = (('eAudioFormat', c_uint),
	('cntPcmBufLen', c_size_t),
	('pOutPcmBuf', c_void_p),
	('cntMrkListLen', c_size_t),
	('pMrkList', POINTER(VE_MARKINFO)))

class VE_PRODUCT_VERSION(Structure):
	_fields_ = (('major', c_uint8),
		('minor', c_uint8),
		('maint', c_uint8))

class VE_ADDITIONAL_PRODUCTINFO(Structure):
	_fields_ = (('buildYar', c_uint16),
		('buildMonth', c_uint8),
		('buildDay', c_uint8),
		('buildInfoStr', (c_char * 256)))

pfErrorFuncType = CFUNCTYPE(None, VE_HSAFE, c_uint, c_uint, POINTER(c_char_p), POINTER(c_char_p))
pfDiagnosticFuncType = CFUNCTYPE(None, VE_HSAFE, c_uint, c_char_p)
class VE_LOG_INTERFACE_S(Structure):
	_fields_ = [('pfError', pfErrorFuncType),
	('pfDiagnostic', pfDiagnosticFuncType)]

class VeError(RuntimeError):
	def __init__(self, code, msg):
		self.code = code
		super(RuntimeError, self).__init__(msg)
