# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blob_storage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='blob_storage.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x62lob_storage.proto\"2\n\x11OpenReaderRequest\x12\r\n\x05Type_\x18\x01 \x01(\t\x12\x0e\n\x06\x43onfig\x18\x02 \x01(\t\"!\n\x12OpenReaderResponse\x12\x0b\n\x03Res\x18\x01 \x01(\x03\"2\n\x11OpenWriterRequest\x12\r\n\x05Type_\x18\x01 \x01(\t\x12\x0e\n\x06\x43onfig\x18\x02 \x01(\t\"!\n\x12OpenWriterResponse\x12\x0b\n\x03Res\x18\x01 \x01(\x03\x62\x06proto3')
)




_OPENREADERREQUEST = _descriptor.Descriptor(
  name='OpenReaderRequest',
  full_name='OpenReaderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type_', full_name='OpenReaderRequest.Type_', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Config', full_name='OpenReaderRequest.Config', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=72,
)


_OPENREADERRESPONSE = _descriptor.Descriptor(
  name='OpenReaderResponse',
  full_name='OpenReaderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Res', full_name='OpenReaderResponse.Res', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=107,
)


_OPENWRITERREQUEST = _descriptor.Descriptor(
  name='OpenWriterRequest',
  full_name='OpenWriterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type_', full_name='OpenWriterRequest.Type_', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Config', full_name='OpenWriterRequest.Config', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=159,
)


_OPENWRITERRESPONSE = _descriptor.Descriptor(
  name='OpenWriterResponse',
  full_name='OpenWriterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Res', full_name='OpenWriterResponse.Res', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=194,
)

DESCRIPTOR.message_types_by_name['OpenReaderRequest'] = _OPENREADERREQUEST
DESCRIPTOR.message_types_by_name['OpenReaderResponse'] = _OPENREADERRESPONSE
DESCRIPTOR.message_types_by_name['OpenWriterRequest'] = _OPENWRITERREQUEST
DESCRIPTOR.message_types_by_name['OpenWriterResponse'] = _OPENWRITERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpenReaderRequest = _reflection.GeneratedProtocolMessageType('OpenReaderRequest', (_message.Message,), dict(
  DESCRIPTOR = _OPENREADERREQUEST,
  __module__ = 'blob_storage_pb2'
  # @@protoc_insertion_point(class_scope:OpenReaderRequest)
  ))
_sym_db.RegisterMessage(OpenReaderRequest)

OpenReaderResponse = _reflection.GeneratedProtocolMessageType('OpenReaderResponse', (_message.Message,), dict(
  DESCRIPTOR = _OPENREADERRESPONSE,
  __module__ = 'blob_storage_pb2'
  # @@protoc_insertion_point(class_scope:OpenReaderResponse)
  ))
_sym_db.RegisterMessage(OpenReaderResponse)

OpenWriterRequest = _reflection.GeneratedProtocolMessageType('OpenWriterRequest', (_message.Message,), dict(
  DESCRIPTOR = _OPENWRITERREQUEST,
  __module__ = 'blob_storage_pb2'
  # @@protoc_insertion_point(class_scope:OpenWriterRequest)
  ))
_sym_db.RegisterMessage(OpenWriterRequest)

OpenWriterResponse = _reflection.GeneratedProtocolMessageType('OpenWriterResponse', (_message.Message,), dict(
  DESCRIPTOR = _OPENWRITERRESPONSE,
  __module__ = 'blob_storage_pb2'
  # @@protoc_insertion_point(class_scope:OpenWriterResponse)
  ))
_sym_db.RegisterMessage(OpenWriterResponse)


# @@protoc_insertion_point(module_scope)