# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/process.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'feature/process.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66\x65\x61ture/process.proto\x12\x1e\x62lueOceanField.feature.process\"\xe4\x01\n\x0e\x46\x65\x61tureProcess\x12\x12\n\nclass_name\x18\x01 \x01(\t\x12R\n\nparameters\x18\x02 \x03(\x0b\x32>.blueOceanField.feature.process.FeatureProcess.ParametersEntry\x1aj\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x37.blueOceanField.feature.process.FeatureProcessParameter:\x02\x38\x01\"\x89\x01\n\x17\x46\x65\x61tureProcessParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12=\n\x05value\x18\x04 \x01(\x0b\x32..blueOceanField.feature.process.ParameterValue\"\xe2\x02\n\x0eParameterValue\x12I\n\x06nested\x18\x01 \x01(\x0b\x32\x37.blueOceanField.feature.process.FeatureProcessParameterH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x05H\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x02H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x05 \x01(\x08H\x00\x12L\n\x11string_list_value\x18\x06 \x01(\x0b\x32/.blueOceanField.feature.process.StringListValueH\x00\x12U\n\x16string_float_map_value\x18\x07 \x01(\x0b\x32\x33.blueOceanField.feature.process.StringFloatMapValueH\x00\x42\x06\n\x04kind\" \n\x0fStringListValue\x12\r\n\x05items\x18\x01 \x03(\t\"\x92\x01\n\x13StringFloatMapValue\x12M\n\x05items\x18\x01 \x03(\x0b\x32>.blueOceanField.feature.process.StringFloatMapValue.ItemsEntry\x1a,\n\nItemsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.process_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FEATUREPROCESS_PARAMETERSENTRY']._loaded_options = None
  _globals['_FEATUREPROCESS_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_STRINGFLOATMAPVALUE_ITEMSENTRY']._loaded_options = None
  _globals['_STRINGFLOATMAPVALUE_ITEMSENTRY']._serialized_options = b'8\001'
  _globals['_FEATUREPROCESS']._serialized_start=58
  _globals['_FEATUREPROCESS']._serialized_end=286
  _globals['_FEATUREPROCESS_PARAMETERSENTRY']._serialized_start=180
  _globals['_FEATUREPROCESS_PARAMETERSENTRY']._serialized_end=286
  _globals['_FEATUREPROCESSPARAMETER']._serialized_start=289
  _globals['_FEATUREPROCESSPARAMETER']._serialized_end=426
  _globals['_PARAMETERVALUE']._serialized_start=429
  _globals['_PARAMETERVALUE']._serialized_end=783
  _globals['_STRINGLISTVALUE']._serialized_start=785
  _globals['_STRINGLISTVALUE']._serialized_end=817
  _globals['_STRINGFLOATMAPVALUE']._serialized_start=820
  _globals['_STRINGFLOATMAPVALUE']._serialized_end=966
  _globals['_STRINGFLOATMAPVALUE_ITEMSENTRY']._serialized_start=922
  _globals['_STRINGFLOATMAPVALUE_ITEMSENTRY']._serialized_end=966
# @@protoc_insertion_point(module_scope)
