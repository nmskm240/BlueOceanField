# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/process.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'feature/process.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66\x65\x61ture/process.proto\x12\x1e\x62lueOceanField.feature.process\"k\n\x0e\x46\x65\x61tureProcess\x12\x0c\n\x04type\x18\x01 \x01(\t\x12K\n\nparameters\x18\x02 \x03(\x0b\x32\x37.blueOceanField.feature.process.FeatureProcessParameter\"\xc0\x01\n\x17\x46\x65\x61tureProcessParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12=\n\x05value\x18\x03 \x01(\x0b\x32..blueOceanField.feature.process.ParameterValue\x12\x43\n\x0b\x63onstraints\x18\x04 \x03(\x0b\x32..blueOceanField.feature.process.ConstraintInfo\"\xf2\x01\n\x0eParameterValue\x12\x13\n\tint_value\x18\x01 \x01(\x05H\x00\x12\x15\n\x0b\x66loat_value\x18\x02 \x01(\x02H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12?\n\nlist_value\x18\x05 \x01(\x0b\x32).blueOceanField.feature.process.ListValueH\x00\x12=\n\tmap_value\x18\x06 \x01(\x0b\x32(.blueOceanField.feature.process.MapValueH\x00\x42\x06\n\x04kind\"J\n\tListValue\x12=\n\x05items\x18\x01 \x03(\x0b\x32..blueOceanField.feature.process.ParameterValue\"\xac\x01\n\x08MapValue\x12\x42\n\x05items\x18\x01 \x03(\x0b\x32\x33.blueOceanField.feature.process.MapValue.ItemsEntry\x1a\\\n\nItemsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..blueOceanField.feature.process.ParameterValue:\x02\x38\x01\"\x81\x02\n\x0e\x43onstraintInfo\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.blueOceanField.feature.process.Constraint\x12@\n\x06target\x18\x02 \x01(\x0e\x32\x30.blueOceanField.feature.process.ConstraintTarget\x12\x46\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\x38.blueOceanField.feature.process.ConstraintInfo.ArgsEntry\x1a+\n\tArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\x8b\x01\n\nConstraint\x12\x1a\n\x16\x43ONSTRAINT_UNSPECIFIED\x10\x00\x12\t\n\x05REGEX\x10\x01\x12\x0f\n\x0bUPPER_LIMIT\x10\x02\x12\x0f\n\x0bLOWER_LIMIT\x10\x03\x12\r\n\tINCLUSION\x10\x04\x12\r\n\tEXCLUSION\x10\x05\x12\n\n\x06LENGTH\x10\x06\x12\n\n\x06UNIQUE\x10\x07*H\n\x10\x43onstraintTarget\x12\x16\n\x12TARGET_UNSPECIFIED\x10\x00\x12\x08\n\x04SELF\x10\x01\x12\x07\n\x03KEY\x10\x02\x12\t\n\x05VALUE\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.process_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MAPVALUE_ITEMSENTRY']._loaded_options = None
  _globals['_MAPVALUE_ITEMSENTRY']._serialized_options = b'8\001'
  _globals['_CONSTRAINTINFO_ARGSENTRY']._loaded_options = None
  _globals['_CONSTRAINTINFO_ARGSENTRY']._serialized_options = b'8\001'
  _globals['_CONSTRAINT']._serialized_start=1118
  _globals['_CONSTRAINT']._serialized_end=1257
  _globals['_CONSTRAINTTARGET']._serialized_start=1259
  _globals['_CONSTRAINTTARGET']._serialized_end=1331
  _globals['_FEATUREPROCESS']._serialized_start=57
  _globals['_FEATUREPROCESS']._serialized_end=164
  _globals['_FEATUREPROCESSPARAMETER']._serialized_start=167
  _globals['_FEATUREPROCESSPARAMETER']._serialized_end=359
  _globals['_PARAMETERVALUE']._serialized_start=362
  _globals['_PARAMETERVALUE']._serialized_end=604
  _globals['_LISTVALUE']._serialized_start=606
  _globals['_LISTVALUE']._serialized_end=680
  _globals['_MAPVALUE']._serialized_start=683
  _globals['_MAPVALUE']._serialized_end=855
  _globals['_MAPVALUE_ITEMSENTRY']._serialized_start=763
  _globals['_MAPVALUE_ITEMSENTRY']._serialized_end=855
  _globals['_CONSTRAINTINFO']._serialized_start=858
  _globals['_CONSTRAINTINFO']._serialized_end=1115
  _globals['_CONSTRAINTINFO_ARGSENTRY']._serialized_start=1072
  _globals['_CONSTRAINTINFO_ARGSENTRY']._serialized_end=1115
# @@protoc_insertion_point(module_scope)
