# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/api/request_log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$chirpstack-api/api/request_log.proto\x12\x03\x61pi\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"chirpstack-api/common/common.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto\"\x8f\x01\n\nRequestLog\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12/\n\x08metadata\x18\x03 \x03(\x0b\x32\x1d.api.RequestLog.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42g\n\x11io.chirpstack.apiB\x0fRequestLogProtoP\x01Z.github.com/chirpstack/chirpstack/api/go/v4/api\xaa\x02\x0e\x43hirpstack.Apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.api.request_log_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021io.chirpstack.apiB\017RequestLogProtoP\001Z.github.com/chirpstack/chirpstack/api/go/v4/api\252\002\016Chirpstack.Api'
  _REQUESTLOG_METADATAENTRY._options = None
  _REQUESTLOG_METADATAENTRY._serialized_options = b'8\001'
  _globals['_REQUESTLOG']._serialized_start=143
  _globals['_REQUESTLOG']._serialized_end=286
  _globals['_REQUESTLOG_METADATAENTRY']._serialized_start=239
  _globals['_REQUESTLOG_METADATAENTRY']._serialized_end=286
# @@protoc_insertion_point(module_scope)
