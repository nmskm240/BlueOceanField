# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: market.proto
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
    'market.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmarket.proto\x12\x15\x62lueOceanField.market\x1a\x1bgoogle/protobuf/empty.proto\"\x1d\n\rExchangePlace\x12\x0c\n\x04name\x18\x01 \x01(\t\"N\n\x0e\x45xchangePlaces\x12<\n\x0e\x65xchangePlaces\x18\x01 \x03(\x0b\x32$.blueOceanField.market.ExchangePlace\"\\\n\x06Symbol\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x36\n\x08\x65xchange\x18\x03 \x01(\x0b\x32$.blueOceanField.market.ExchangePlace\"9\n\x07Symbols\x12.\n\x07symbols\x18\x01 \x03(\x0b\x32\x1d.blueOceanField.market.Symbol2\xf8\x01\n\rMarketService\x12O\n\x0cGetExchanges\x12\x16.google.protobuf.Empty\x1a%.blueOceanField.market.ExchangePlaces\"\x00\x12T\n\nGetSymbols\x12$.blueOceanField.market.ExchangePlace\x1a\x1e.blueOceanField.market.Symbols\"\x00\x12@\n\x05\x46\x65tch\x12\x1d.blueOceanField.market.Symbol\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'market_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EXCHANGEPLACE']._serialized_start=68
  _globals['_EXCHANGEPLACE']._serialized_end=97
  _globals['_EXCHANGEPLACES']._serialized_start=99
  _globals['_EXCHANGEPLACES']._serialized_end=177
  _globals['_SYMBOL']._serialized_start=179
  _globals['_SYMBOL']._serialized_end=271
  _globals['_SYMBOLS']._serialized_start=273
  _globals['_SYMBOLS']._serialized_end=330
  _globals['_MARKETSERVICE']._serialized_start=333
  _globals['_MARKETSERVICE']._serialized_end=581
# @@protoc_insertion_point(module_scope)
