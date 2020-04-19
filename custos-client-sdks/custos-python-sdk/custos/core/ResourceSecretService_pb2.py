# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ResourceSecretService.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ResourceSecretService.proto',
  package='org.apache.custos.resource.secret.service',
  syntax='proto3',
  serialized_options=b'P\001',
  serialized_pb=b'\n\x1bResourceSecretService.proto\x12)org.apache.custos.resource.secret.service\"\x9a\x02\n\x0eSecretMetadata\x12P\n\nowner_type\x18\x01 \x01(\x0e\x32<.org.apache.custos.resource.secret.service.ResourceOwnerType\x12N\n\rresource_type\x18\x02 \x01(\x0e\x32\x37.org.apache.custos.resource.secret.service.ResourceType\x12I\n\x06source\x18\x03 \x01(\x0e\x32\x39.org.apache.custos.resource.secret.service.ResourceSource\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\t\"\xab\x01\n\x10GetSecretRequest\x12K\n\x08metadata\x18\x01 \x01(\x0b\x32\x39.org.apache.custos.resource.secret.service.SecretMetadata\x12\x10\n\x08tenantId\x18\x02 \x01(\x03\x12\x10\n\x08\x63lientId\x18\x03 \x01(\t\x12\x11\n\tclientSec\x18\x04 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x05 \x01(\t*<\n\x11ResourceOwnerType\x12\x0f\n\x0bTENANT_USER\x10\x00\x12\n\n\x06\x43USTOS\x10\x01\x12\n\n\x06TENANT\x10\x02*D\n\x0cResourceType\x12\x16\n\x12SERVER_CERTIFICATE\x10\x00\x12\x07\n\x03RAW\x10\x01\x12\x13\n\x0fJWT_CERTIFICATE\x10\x02*D\n\x0eResourceSource\x12\x08\n\x04KUBE\x10\x00\x12\t\n\x05LOCAL\x10\x01\x12\x0c\n\x08\x45XTERNAL\x10\x02\x12\x0f\n\x0bLETSENCRYPT\x10\x03\x32\x9d\x01\n\x15ResourceSecretService\x12\x83\x01\n\tgetSecret\x12;.org.apache.custos.resource.secret.service.GetSecretRequest\x1a\x39.org.apache.custos.resource.secret.service.SecretMetadataB\x02P\x01\x62\x06proto3'
)

_RESOURCEOWNERTYPE = _descriptor.EnumDescriptor(
  name='ResourceOwnerType',
  full_name='org.apache.custos.resource.secret.service.ResourceOwnerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TENANT_USER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TENANT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=533,
  serialized_end=593,
)
_sym_db.RegisterEnumDescriptor(_RESOURCEOWNERTYPE)

ResourceOwnerType = enum_type_wrapper.EnumTypeWrapper(_RESOURCEOWNERTYPE)
_RESOURCETYPE = _descriptor.EnumDescriptor(
  name='ResourceType',
  full_name='org.apache.custos.resource.secret.service.ResourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SERVER_CERTIFICATE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JWT_CERTIFICATE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=595,
  serialized_end=663,
)
_sym_db.RegisterEnumDescriptor(_RESOURCETYPE)

ResourceType = enum_type_wrapper.EnumTypeWrapper(_RESOURCETYPE)
_RESOURCESOURCE = _descriptor.EnumDescriptor(
  name='ResourceSource',
  full_name='org.apache.custos.resource.secret.service.ResourceSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KUBE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LETSENCRYPT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=665,
  serialized_end=733,
)
_sym_db.RegisterEnumDescriptor(_RESOURCESOURCE)

ResourceSource = enum_type_wrapper.EnumTypeWrapper(_RESOURCESOURCE)
TENANT_USER = 0
CUSTOS = 1
TENANT = 2
SERVER_CERTIFICATE = 0
RAW = 1
JWT_CERTIFICATE = 2
KUBE = 0
LOCAL = 1
EXTERNAL = 2
LETSENCRYPT = 3



_SECRETMETADATA = _descriptor.Descriptor(
  name='SecretMetadata',
  full_name='org.apache.custos.resource.secret.service.SecretMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_type', full_name='org.apache.custos.resource.secret.service.SecretMetadata.owner_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='org.apache.custos.resource.secret.service.SecretMetadata.resource_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='org.apache.custos.resource.secret.service.SecretMetadata.source', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='org.apache.custos.resource.secret.service.SecretMetadata.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='org.apache.custos.resource.secret.service.SecretMetadata.value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=75,
  serialized_end=357,
)


_GETSECRETREQUEST = _descriptor.Descriptor(
  name='GetSecretRequest',
  full_name='org.apache.custos.resource.secret.service.GetSecretRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='org.apache.custos.resource.secret.service.GetSecretRequest.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenantId', full_name='org.apache.custos.resource.secret.service.GetSecretRequest.tenantId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='org.apache.custos.resource.secret.service.GetSecretRequest.clientId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientSec', full_name='org.apache.custos.resource.secret.service.GetSecretRequest.clientSec', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='org.apache.custos.resource.secret.service.GetSecretRequest.accessToken', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=360,
  serialized_end=531,
)

_SECRETMETADATA.fields_by_name['owner_type'].enum_type = _RESOURCEOWNERTYPE
_SECRETMETADATA.fields_by_name['resource_type'].enum_type = _RESOURCETYPE
_SECRETMETADATA.fields_by_name['source'].enum_type = _RESOURCESOURCE
_GETSECRETREQUEST.fields_by_name['metadata'].message_type = _SECRETMETADATA
DESCRIPTOR.message_types_by_name['SecretMetadata'] = _SECRETMETADATA
DESCRIPTOR.message_types_by_name['GetSecretRequest'] = _GETSECRETREQUEST
DESCRIPTOR.enum_types_by_name['ResourceOwnerType'] = _RESOURCEOWNERTYPE
DESCRIPTOR.enum_types_by_name['ResourceType'] = _RESOURCETYPE
DESCRIPTOR.enum_types_by_name['ResourceSource'] = _RESOURCESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SecretMetadata = _reflection.GeneratedProtocolMessageType('SecretMetadata', (_message.Message,), {
  'DESCRIPTOR' : _SECRETMETADATA,
  '__module__' : 'ResourceSecretService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.resource.secret.service.SecretMetadata)
  })
_sym_db.RegisterMessage(SecretMetadata)

GetSecretRequest = _reflection.GeneratedProtocolMessageType('GetSecretRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSECRETREQUEST,
  '__module__' : 'ResourceSecretService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.resource.secret.service.GetSecretRequest)
  })
_sym_db.RegisterMessage(GetSecretRequest)


DESCRIPTOR._options = None

_RESOURCESECRETSERVICE = _descriptor.ServiceDescriptor(
  name='ResourceSecretService',
  full_name='org.apache.custos.resource.secret.service.ResourceSecretService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=736,
  serialized_end=893,
  methods=[
  _descriptor.MethodDescriptor(
    name='getSecret',
    full_name='org.apache.custos.resource.secret.service.ResourceSecretService.getSecret',
    index=0,
    containing_service=None,
    input_type=_GETSECRETREQUEST,
    output_type=_SECRETMETADATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESOURCESECRETSERVICE)

DESCRIPTOR.services_by_name['ResourceSecretService'] = _RESOURCESECRETSERVICE

# @@protoc_insertion_point(module_scope)
