# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exa/diff_action_pb/diff_action.proto
"""Generated protocol buffer code."""
from Codeium.google.protobuf import descriptor as _descriptor
from Codeium.google.protobuf import descriptor_pool as _descriptor_pool
from Codeium.google.protobuf import symbol_database as _symbol_database
from Codeium.google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Codeium.exa.codeium_common_pb import codeium_common_pb2 as exa_dot_codeium__common__pb_dot_codeium__common__pb2
from Codeium.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$exa/diff_action_pb/diff_action.proto\x12\x12\x65xa.diff_action_pb\x1a*exa/codeium_common_pb/codeium_common.proto\x1a\x17validate/validate.proto\"\xb8\x01\n\x0bUnifiedDiff\x12\x45\n\x05lines\x18\x03 \x03(\x0b\x32/.exa.diff_action_pb.UnifiedDiff.UnifiedDiffLineR\x05lines\x1a\x62\n\x0fUnifiedDiffLine\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12;\n\x04type\x18\x02 \x01(\x0e\x32\'.exa.diff_action_pb.UnifiedDiffLineTypeR\x04type\"\x9a\x02\n\tDiffBlock\x12&\n\nstart_line\x18\x01 \x01(\x05\x42\x07\xfa\x42\x04\x1a\x02 \x00R\tstartLine\x12\x19\n\x08\x65nd_line\x18\x02 \x01(\x05R\x07\x65ndLine\x12\x42\n\x0cunified_diff\x18\x03 \x01(\x0b\x32\x1f.exa.diff_action_pb.UnifiedDiffR\x0bunifiedDiff\x12\x44\n\rfrom_language\x18\x04 \x01(\x0e\x32\x1f.exa.codeium_common_pb.LanguageR\x0c\x66romLanguage\x12@\n\x0bto_language\x18\x05 \x01(\x0e\x32\x1f.exa.codeium_common_pb.LanguageR\ntoLanguage*\xa9\x01\n\x13UnifiedDiffLineType\x12&\n\"UNIFIED_DIFF_LINE_TYPE_UNSPECIFIED\x10\x00\x12!\n\x1dUNIFIED_DIFF_LINE_TYPE_INSERT\x10\x01\x12!\n\x1dUNIFIED_DIFF_LINE_TYPE_DELETE\x10\x02\x12$\n UNIFIED_DIFF_LINE_TYPE_UNCHANGED\x10\x03\x42\x37Z5github.com/Exafunction/Exafunction/exa/diff_action_pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exa.diff_action_pb.diff_action_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/Exafunction/Exafunction/exa/diff_action_pb'
  _DIFFBLOCK.fields_by_name['start_line']._options = None
  _DIFFBLOCK.fields_by_name['start_line']._serialized_options = b'\372B\004\032\002 \000'
  _globals['_UNIFIEDDIFFLINETYPE']._serialized_start=602
  _globals['_UNIFIEDDIFFLINETYPE']._serialized_end=771
  _globals['_UNIFIEDDIFF']._serialized_start=130
  _globals['_UNIFIEDDIFF']._serialized_end=314
  _globals['_UNIFIEDDIFF_UNIFIEDDIFFLINE']._serialized_start=216
  _globals['_UNIFIEDDIFF_UNIFIEDDIFFLINE']._serialized_end=314
  _globals['_DIFFBLOCK']._serialized_start=317
  _globals['_DIFFBLOCK']._serialized_end=599
# @@protoc_insertion_point(module_scope)
