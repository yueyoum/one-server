# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: guide.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='guide.proto',
  package='Sanguo.protocol.guide',
  serialized_pb='\n\x0bguide.proto\x12\x15Sanguo.protocol.guide\"N\n\x0bGuideNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12.\n\x04step\x18\x02 \x02(\x0e\x32 .Sanguo.protocol.guide.GuideStep\"%\n\x12GuideFinishRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"3\n\x13GuideFinishResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c*\xba\x01\n\tGuideStep\x12\x10\n\x0cGUIDE_NORMAL\x10\x00\x12\x10\n\x0cGUIDE_FINISH\x10\x01\x12\x0f\n\x0bGUIDE_STORY\x10\x02\x12\x15\n\x11GUIDE_SHOW_BATTLE\x10\x03\x12\x11\n\rGUIDE_GETHERO\x10\x04\x12\x1b\n\x17GUIDE_HERO_IN_FORMATION\x10\x05\x12\x1c\n\x18GUIDE_EQUIP_IN_FORMATION\x10\x06\x12\x13\n\x0fGUIDE_FIRST_PVE\x10\x07')

_GUIDESTEP = _descriptor.EnumDescriptor(
  name='GuideStep',
  full_name='Sanguo.protocol.guide.GuideStep',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GUIDE_NORMAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUIDE_FINISH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUIDE_STORY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUIDE_SHOW_BATTLE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUIDE_GETHERO', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUIDE_HERO_IN_FORMATION', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUIDE_EQUIP_IN_FORMATION', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUIDE_FIRST_PVE', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=211,
  serialized_end=397,
)

GuideStep = enum_type_wrapper.EnumTypeWrapper(_GUIDESTEP)
GUIDE_NORMAL = 0
GUIDE_FINISH = 1
GUIDE_STORY = 2
GUIDE_SHOW_BATTLE = 3
GUIDE_GETHERO = 4
GUIDE_HERO_IN_FORMATION = 5
GUIDE_EQUIP_IN_FORMATION = 6
GUIDE_FIRST_PVE = 7



_GUIDENOTIFY = _descriptor.Descriptor(
  name='GuideNotify',
  full_name='Sanguo.protocol.guide.GuideNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.guide.GuideNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step', full_name='Sanguo.protocol.guide.GuideNotify.step', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=38,
  serialized_end=116,
)


_GUIDEFINISHREQUEST = _descriptor.Descriptor(
  name='GuideFinishRequest',
  full_name='Sanguo.protocol.guide.GuideFinishRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.guide.GuideFinishRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=118,
  serialized_end=155,
)


_GUIDEFINISHRESPONSE = _descriptor.Descriptor(
  name='GuideFinishResponse',
  full_name='Sanguo.protocol.guide.GuideFinishResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.guide.GuideFinishResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.guide.GuideFinishResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=157,
  serialized_end=208,
)

_GUIDENOTIFY.fields_by_name['step'].enum_type = _GUIDESTEP
DESCRIPTOR.message_types_by_name['GuideNotify'] = _GUIDENOTIFY
DESCRIPTOR.message_types_by_name['GuideFinishRequest'] = _GUIDEFINISHREQUEST
DESCRIPTOR.message_types_by_name['GuideFinishResponse'] = _GUIDEFINISHRESPONSE

class GuideNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUIDENOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.guide.GuideNotify)

class GuideFinishRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUIDEFINISHREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.guide.GuideFinishRequest)

class GuideFinishResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUIDEFINISHRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.guide.GuideFinishResponse)


# @@protoc_insertion_point(module_scope)
