# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drones.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x64rones.proto\"\x07\n\x05\x45mpty\"\x1c\n\x0cRegistration\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1c\n\x0eRegistrationId\x12\n\n\x02id\x18\x01 \x01(\x05\"/\n\x08Waypoint\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\"A\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x02\x32\x87\x01\n\x07Greeter\x12,\n\x08register\x12\r.Registration\x1a\x0f.RegistrationId\"\x00\x12$\n\rsend_position\x12\t.Position\x1a\x06.Empty\"\x00\x12(\n\x0flisten_waypoint\x12\x06.Empty\x1a\t.Waypoint\"\x00\x30\x01\x62\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_REGISTRATION = DESCRIPTOR.message_types_by_name['Registration']
_REGISTRATIONID = DESCRIPTOR.message_types_by_name['RegistrationId']
_WAYPOINT = DESCRIPTOR.message_types_by_name['Waypoint']
_POSITION = DESCRIPTOR.message_types_by_name['Position']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'drones_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

Registration = _reflection.GeneratedProtocolMessageType('Registration', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRATION,
  '__module__' : 'drones_pb2'
  # @@protoc_insertion_point(class_scope:Registration)
  })
_sym_db.RegisterMessage(Registration)

RegistrationId = _reflection.GeneratedProtocolMessageType('RegistrationId', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRATIONID,
  '__module__' : 'drones_pb2'
  # @@protoc_insertion_point(class_scope:RegistrationId)
  })
_sym_db.RegisterMessage(RegistrationId)

Waypoint = _reflection.GeneratedProtocolMessageType('Waypoint', (_message.Message,), {
  'DESCRIPTOR' : _WAYPOINT,
  '__module__' : 'drones_pb2'
  # @@protoc_insertion_point(class_scope:Waypoint)
  })
_sym_db.RegisterMessage(Waypoint)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'drones_pb2'
  # @@protoc_insertion_point(class_scope:Position)
  })
_sym_db.RegisterMessage(Position)

_GREETER = DESCRIPTOR.services_by_name['Greeter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=16
  _EMPTY._serialized_end=23
  _REGISTRATION._serialized_start=25
  _REGISTRATION._serialized_end=53
  _REGISTRATIONID._serialized_start=55
  _REGISTRATIONID._serialized_end=83
  _WAYPOINT._serialized_start=85
  _WAYPOINT._serialized_end=132
  _POSITION._serialized_start=134
  _POSITION._serialized_end=199
  _GREETER._serialized_start=202
  _GREETER._serialized_end=337
# @@protoc_insertion_point(module_scope)