# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sitebots.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sitebots.proto',
  package='sitebots',
  syntax='proto3',
  serialized_pb=_b('\n\x0esitebots.proto\x12\x08sitebots\"<\n\x08Waypoint\x12\n\n\x02id\x18\x01 \x01(\t\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\x0e\n\x06map_id\x18\x04 \x01(\t\"Z\n\nConnection\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0fsource_waypoint\x18\x02 \x01(\t\x12\x17\n\x0ftarget_waypoint\x18\x03 \x01(\t\x12\x0e\n\x06map_id\x18\x04 \x01(\t\"8\n\x04Path\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x08waypoint\x18\x02 \x03(\x0b\x32\x12.sitebots.Waypoint\"u\n\x04\x41rea\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06map_id\x18\x02 \x01(\t\x12\x1f\n\x06\x62ounds\x18\x03 \x03(\x0b\x32\x0f.sitebots.Point\x12\"\n\twaypoints\x18\x04 \x03(\x0b\x32\x0f.sitebots.Point\x12\x0c\n\x04name\x18\x05 \x01(\t\"-\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0e\n\x06map_id\x18\x03 \x01(\t\"g\n\x07Vehicle\x12\n\n\x02id\x18\x01 \x01(\t\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\x0e\n\x06map_id\x18\x04 \x01(\t\x12*\n\x0f\x63urrent_mission\x18\x05 \x01(\x0b\x32\x11.sitebots.Mission\"o\n\x0bMissionItem\x12\x1c\n\x04path\x18\x01 \x01(\x0b\x32\x0e.sitebots.Path\x12\x1c\n\x04\x61rea\x18\x02 \x01(\x0b\x32\x0e.sitebots.Area\x12$\n\x08waypoint\x18\x03 \x01(\x0b\x32\x12.sitebots.Waypoint\";\n\x07Mission\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x05items\x18\x02 \x03(\x0b\x32\x15.sitebots.MissionItem\"m\n\x07Request\x12\x0c\n\x04type\x18\x01 \x01(\t\x12)\n\x10south_west_bound\x18\x02 \x01(\x0b\x32\x0f.sitebots.Point\x12)\n\x10north_east_bound\x18\x03 \x01(\x0b\x32\x0f.sitebots.Pointb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_WAYPOINT = _descriptor.Descriptor(
  name='Waypoint',
  full_name='sitebots.Waypoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sitebots.Waypoint.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='sitebots.Waypoint.x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='sitebots.Waypoint.y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='sitebots.Waypoint.map_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=88,
)


_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='sitebots.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sitebots.Connection.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_waypoint', full_name='sitebots.Connection.source_waypoint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_waypoint', full_name='sitebots.Connection.target_waypoint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='sitebots.Connection.map_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=180,
)


_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='sitebots.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sitebots.Path.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='waypoint', full_name='sitebots.Path.waypoint', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=238,
)


_AREA = _descriptor.Descriptor(
  name='Area',
  full_name='sitebots.Area',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sitebots.Area.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='sitebots.Area.map_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bounds', full_name='sitebots.Area.bounds', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='waypoints', full_name='sitebots.Area.waypoints', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='sitebots.Area.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=357,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='sitebots.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='sitebots.Point.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='sitebots.Point.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='sitebots.Point.map_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=404,
)


_VEHICLE = _descriptor.Descriptor(
  name='Vehicle',
  full_name='sitebots.Vehicle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sitebots.Vehicle.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='sitebots.Vehicle.x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='sitebots.Vehicle.y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='sitebots.Vehicle.map_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_mission', full_name='sitebots.Vehicle.current_mission', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=509,
)


_MISSIONITEM = _descriptor.Descriptor(
  name='MissionItem',
  full_name='sitebots.MissionItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='sitebots.MissionItem.path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area', full_name='sitebots.MissionItem.area', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='waypoint', full_name='sitebots.MissionItem.waypoint', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=622,
)


_MISSION = _descriptor.Descriptor(
  name='Mission',
  full_name='sitebots.Mission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sitebots.Mission.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='sitebots.Mission.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=624,
  serialized_end=683,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='sitebots.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sitebots.Request.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='south_west_bound', full_name='sitebots.Request.south_west_bound', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='north_east_bound', full_name='sitebots.Request.north_east_bound', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=685,
  serialized_end=794,
)

_PATH.fields_by_name['waypoint'].message_type = _WAYPOINT
_AREA.fields_by_name['bounds'].message_type = _POINT
_AREA.fields_by_name['waypoints'].message_type = _POINT
_VEHICLE.fields_by_name['current_mission'].message_type = _MISSION
_MISSIONITEM.fields_by_name['path'].message_type = _PATH
_MISSIONITEM.fields_by_name['area'].message_type = _AREA
_MISSIONITEM.fields_by_name['waypoint'].message_type = _WAYPOINT
_MISSION.fields_by_name['items'].message_type = _MISSIONITEM
_REQUEST.fields_by_name['south_west_bound'].message_type = _POINT
_REQUEST.fields_by_name['north_east_bound'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Waypoint'] = _WAYPOINT
DESCRIPTOR.message_types_by_name['Connection'] = _CONNECTION
DESCRIPTOR.message_types_by_name['Path'] = _PATH
DESCRIPTOR.message_types_by_name['Area'] = _AREA
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Vehicle'] = _VEHICLE
DESCRIPTOR.message_types_by_name['MissionItem'] = _MISSIONITEM
DESCRIPTOR.message_types_by_name['Mission'] = _MISSION
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST

Waypoint = _reflection.GeneratedProtocolMessageType('Waypoint', (_message.Message,), dict(
  DESCRIPTOR = _WAYPOINT,
  __module__ = 'sitebots_pb2'
  # @@protoc_insertion_point(class_scope:sitebots.Waypoint)
  ))
_sym_db.RegisterMessage(Waypoint)

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTION,
  __module__ = 'sitebots_pb2'
  # @@protoc_insertion_point(class_scope:sitebots.Connection)
  ))
_sym_db.RegisterMessage(Connection)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), dict(
  DESCRIPTOR = _PATH,
  __module__ = 'sitebots_pb2'
  # @@protoc_insertion_point(class_scope:sitebots.Path)
  ))
_sym_db.RegisterMessage(Path)

Area = _reflection.GeneratedProtocolMessageType('Area', (_message.Message,), dict(
  DESCRIPTOR = _AREA,
  __module__ = 'sitebots_pb2'
  # @@protoc_insertion_point(class_scope:sitebots.Area)
  ))
_sym_db.RegisterMessage(Area)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'sitebots_pb2'
  # @@protoc_insertion_point(class_scope:sitebots.Point)
  ))
_sym_db.RegisterMessage(Point)

Vehicle = _reflection.GeneratedProtocolMessageType('Vehicle', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLE,
  __module__ = 'sitebots_pb2'
  # @@protoc_insertion_point(class_scope:sitebots.Vehicle)
  ))
_sym_db.RegisterMessage(Vehicle)

MissionItem = _reflection.GeneratedProtocolMessageType('MissionItem', (_message.Message,), dict(
  DESCRIPTOR = _MISSIONITEM,
  __module__ = 'sitebots_pb2'
  # @@protoc_insertion_point(class_scope:sitebots.MissionItem)
  ))
_sym_db.RegisterMessage(MissionItem)

Mission = _reflection.GeneratedProtocolMessageType('Mission', (_message.Message,), dict(
  DESCRIPTOR = _MISSION,
  __module__ = 'sitebots_pb2'
  # @@protoc_insertion_point(class_scope:sitebots.Mission)
  ))
_sym_db.RegisterMessage(Mission)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'sitebots_pb2'
  # @@protoc_insertion_point(class_scope:sitebots.Request)
  ))
_sym_db.RegisterMessage(Request)


# @@protoc_insertion_point(module_scope)
