# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_CaboCha', [dirname(__file__)])
        except ImportError:
            import _CaboCha
            return _CaboCha
        if fp is not None:
            try:
                _mod = imp.load_module('_CaboCha', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _CaboCha = swig_import_helper()
    del swig_import_helper
else:
    import _CaboCha
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


CABOCHA_EUC_JP = _CaboCha.CABOCHA_EUC_JP
CABOCHA_CP932 = _CaboCha.CABOCHA_CP932
CABOCHA_UTF8 = _CaboCha.CABOCHA_UTF8
CABOCHA_ASCII = _CaboCha.CABOCHA_ASCII
CABOCHA_IPA = _CaboCha.CABOCHA_IPA
CABOCHA_JUMAN = _CaboCha.CABOCHA_JUMAN
CABOCHA_UNIDIC = _CaboCha.CABOCHA_UNIDIC
CABOCHA_FORMAT_TREE = _CaboCha.CABOCHA_FORMAT_TREE
CABOCHA_FORMAT_LATTICE = _CaboCha.CABOCHA_FORMAT_LATTICE
CABOCHA_FORMAT_TREE_LATTICE = _CaboCha.CABOCHA_FORMAT_TREE_LATTICE
CABOCHA_FORMAT_XML = _CaboCha.CABOCHA_FORMAT_XML
CABOCHA_FORMAT_NONE = _CaboCha.CABOCHA_FORMAT_NONE
CABOCHA_INPUT_RAW_SENTENCE = _CaboCha.CABOCHA_INPUT_RAW_SENTENCE
CABOCHA_INPUT_POS = _CaboCha.CABOCHA_INPUT_POS
CABOCHA_INPUT_CHUNK = _CaboCha.CABOCHA_INPUT_CHUNK
CABOCHA_INPUT_SELECTION = _CaboCha.CABOCHA_INPUT_SELECTION
CABOCHA_INPUT_DEP = _CaboCha.CABOCHA_INPUT_DEP
CABOCHA_OUTPUT_RAW_SENTENCE = _CaboCha.CABOCHA_OUTPUT_RAW_SENTENCE
CABOCHA_OUTPUT_POS = _CaboCha.CABOCHA_OUTPUT_POS
CABOCHA_OUTPUT_CHUNK = _CaboCha.CABOCHA_OUTPUT_CHUNK
CABOCHA_OUTPUT_SELECTION = _CaboCha.CABOCHA_OUTPUT_SELECTION
CABOCHA_OUTPUT_DEP = _CaboCha.CABOCHA_OUTPUT_DEP
CABOCHA_TRAIN_NE = _CaboCha.CABOCHA_TRAIN_NE
CABOCHA_TRAIN_CHUNK = _CaboCha.CABOCHA_TRAIN_CHUNK
CABOCHA_TRAIN_DEP = _CaboCha.CABOCHA_TRAIN_DEP
class Chunk(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Chunk, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Chunk, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["link"] = _CaboCha.Chunk_link_get
    if _newclass:link = _swig_property(_CaboCha.Chunk_link_get)
    __swig_getmethods__["head_pos"] = _CaboCha.Chunk_head_pos_get
    if _newclass:head_pos = _swig_property(_CaboCha.Chunk_head_pos_get)
    __swig_getmethods__["func_pos"] = _CaboCha.Chunk_func_pos_get
    if _newclass:func_pos = _swig_property(_CaboCha.Chunk_func_pos_get)
    __swig_getmethods__["token_size"] = _CaboCha.Chunk_token_size_get
    if _newclass:token_size = _swig_property(_CaboCha.Chunk_token_size_get)
    __swig_getmethods__["token_pos"] = _CaboCha.Chunk_token_pos_get
    if _newclass:token_pos = _swig_property(_CaboCha.Chunk_token_pos_get)
    __swig_getmethods__["score"] = _CaboCha.Chunk_score_get
    if _newclass:score = _swig_property(_CaboCha.Chunk_score_get)
    __swig_getmethods__["additional_info"] = _CaboCha.Chunk_additional_info_get
    if _newclass:additional_info = _swig_property(_CaboCha.Chunk_additional_info_get)
    __swig_getmethods__["feature_list_size"] = _CaboCha.Chunk_feature_list_size_get
    if _newclass:feature_list_size = _swig_property(_CaboCha.Chunk_feature_list_size_get)
    def feature_list(self, *args): return _CaboCha.Chunk_feature_list(self, *args)
Chunk_swigregister = _CaboCha.Chunk_swigregister
Chunk_swigregister(Chunk)

class Token(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Token, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Token, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["surface"] = _CaboCha.Token_surface_get
    if _newclass:surface = _swig_property(_CaboCha.Token_surface_get)
    __swig_getmethods__["normalized_surface"] = _CaboCha.Token_normalized_surface_get
    if _newclass:normalized_surface = _swig_property(_CaboCha.Token_normalized_surface_get)
    __swig_getmethods__["feature"] = _CaboCha.Token_feature_get
    if _newclass:feature = _swig_property(_CaboCha.Token_feature_get)
    __swig_getmethods__["feature_list_size"] = _CaboCha.Token_feature_list_size_get
    if _newclass:feature_list_size = _swig_property(_CaboCha.Token_feature_list_size_get)
    __swig_getmethods__["ne"] = _CaboCha.Token_ne_get
    if _newclass:ne = _swig_property(_CaboCha.Token_ne_get)
    __swig_getmethods__["additional_info"] = _CaboCha.Token_additional_info_get
    if _newclass:additional_info = _swig_property(_CaboCha.Token_additional_info_get)
    __swig_getmethods__["chunk"] = _CaboCha.Token_chunk_get
    if _newclass:chunk = _swig_property(_CaboCha.Token_chunk_get)
    def feature_list(self, *args): return _CaboCha.Token_feature_list(self, *args)
Token_swigregister = _CaboCha.Token_swigregister
Token_swigregister(Token)

EUC_JP = _CaboCha.EUC_JP
CP932 = _CaboCha.CP932
UTF8 = _CaboCha.UTF8
ASCII = _CaboCha.ASCII
IPA = _CaboCha.IPA
JUMAN = _CaboCha.JUMAN
UNIDIC = _CaboCha.UNIDIC
FORMAT_TREE = _CaboCha.FORMAT_TREE
FORMAT_LATTICE = _CaboCha.FORMAT_LATTICE
FORMAT_TREE_LATTICE = _CaboCha.FORMAT_TREE_LATTICE
FORMAT_XML = _CaboCha.FORMAT_XML
FORMAT_NONE = _CaboCha.FORMAT_NONE
INPUT_RAW_SENTENCE = _CaboCha.INPUT_RAW_SENTENCE
INPUT_POS = _CaboCha.INPUT_POS
INPUT_CHUNK = _CaboCha.INPUT_CHUNK
INPUT_SELECTION = _CaboCha.INPUT_SELECTION
INPUT_DEP = _CaboCha.INPUT_DEP
OUTPUT_RAW_SENTENCE = _CaboCha.OUTPUT_RAW_SENTENCE
OUTPUT_POS = _CaboCha.OUTPUT_POS
OUTPUT_CHUNK = _CaboCha.OUTPUT_CHUNK
OUTPUT_SELECTION = _CaboCha.OUTPUT_SELECTION
OUTPUT_DEP = _CaboCha.OUTPUT_DEP
TRAIN_NE = _CaboCha.TRAIN_NE
TRAIN_CHUNK = _CaboCha.TRAIN_CHUNK
TRAIN_DEP = _CaboCha.TRAIN_DEP
class Tree(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tree, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tree, name)
    __repr__ = _swig_repr
    def set_sentence(self, *args): return _CaboCha.Tree_set_sentence(self, *args)
    def sentence(self): return _CaboCha.Tree_sentence(self)
    def sentence_size(self): return _CaboCha.Tree_sentence_size(self)
    def chunk(self, *args): return _CaboCha.Tree_chunk(self, *args)
    def token(self, *args): return _CaboCha.Tree_token(self, *args)
    def read(self, *args): return _CaboCha.Tree_read(self, *args)
    def empty(self): return _CaboCha.Tree_empty(self)
    def clear(self): return _CaboCha.Tree_clear(self)
    def clear_chunk(self): return _CaboCha.Tree_clear_chunk(self)
    def chunk_size(self): return _CaboCha.Tree_chunk_size(self)
    def token_size(self): return _CaboCha.Tree_token_size(self)
    def size(self): return _CaboCha.Tree_size(self)
    def toString(self, *args): return _CaboCha.Tree_toString(self, *args)
    def charset(self): return _CaboCha.Tree_charset(self)
    def set_charset(self, *args): return _CaboCha.Tree_set_charset(self, *args)
    def posset(self): return _CaboCha.Tree_posset(self)
    def set_posset(self, *args): return _CaboCha.Tree_set_posset(self, *args)
    def output_layer(self): return _CaboCha.Tree_output_layer(self)
    def set_output_layer(self, *args): return _CaboCha.Tree_set_output_layer(self, *args)
    def what(self): return _CaboCha.Tree_what(self)
    def __init__(self): 
        this = _CaboCha.new_Tree()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _CaboCha.delete_Tree
    __del__ = lambda self : None;
Tree_swigregister = _CaboCha.Tree_swigregister
Tree_swigregister(Tree)

class Parser(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Parser, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Parser, name)
    __repr__ = _swig_repr
    def parseToString(self, *args): return _CaboCha.Parser_parseToString(self, *args)
    def parse(self, *args): return _CaboCha.Parser_parse(self, *args)
    def what(self): return _CaboCha.Parser_what(self)
    __swig_getmethods__["version"] = lambda x: _CaboCha.Parser_version
    if _newclass:version = staticmethod(_CaboCha.Parser_version)
    __swig_destroy__ = _CaboCha.delete_Parser
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _CaboCha.new_Parser(*args)
        try: self.this.append(this)
        except: self.this = this
Parser_swigregister = _CaboCha.Parser_swigregister
Parser_swigregister(Parser)

def Parser_version():
  return _CaboCha.Parser_version()
Parser_version = _CaboCha.Parser_version


def getLastError():
  return _CaboCha.getLastError()
getLastError = _CaboCha.getLastError
VERSION = _CaboCha.VERSION
# This file is compatible with both classic and new-style classes.


