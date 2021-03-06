# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: matrix_op.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='matrix_op.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0fmatrix_op.proto\"!\n\tOpRequest\x12\t\n\x01\x61\x18\x01 \x02(\x0c\x12\t\n\x01\x62\x18\x02 \x01(\x0c\"\x16\n\x07OpReply\x12\x0b\n\x03res\x18\x01 \x02(\x0c\x32-\n\x08MatrixOp\x12!\n\x07MatMult\x12\n.OpRequest\x1a\x08.OpReply\"\x00'
)




_OPREQUEST = _descriptor.Descriptor(
  name='OpRequest',
  full_name='OpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='OpRequest.a', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='OpRequest.b', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=52,
)


_OPREPLY = _descriptor.Descriptor(
  name='OpReply',
  full_name='OpReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='OpReply.res', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=76,
)

DESCRIPTOR.message_types_by_name['OpRequest'] = _OPREQUEST
DESCRIPTOR.message_types_by_name['OpReply'] = _OPREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpRequest = _reflection.GeneratedProtocolMessageType('OpRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPREQUEST,
  '__module__' : 'matrix_op_pb2'
  # @@protoc_insertion_point(class_scope:OpRequest)
  })
_sym_db.RegisterMessage(OpRequest)

OpReply = _reflection.GeneratedProtocolMessageType('OpReply', (_message.Message,), {
  'DESCRIPTOR' : _OPREPLY,
  '__module__' : 'matrix_op_pb2'
  # @@protoc_insertion_point(class_scope:OpReply)
  })
_sym_db.RegisterMessage(OpReply)



_MATRIXOP = _descriptor.ServiceDescriptor(
  name='MatrixOp',
  full_name='MatrixOp',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=78,
  serialized_end=123,
  methods=[
  _descriptor.MethodDescriptor(
    name='MatMult',
    full_name='MatrixOp.MatMult',
    index=0,
    containing_service=None,
    input_type=_OPREQUEST,
    output_type=_OPREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MATRIXOP)

DESCRIPTOR.services_by_name['MatrixOp'] = _MATRIXOP

# @@protoc_insertion_point(module_scope)
