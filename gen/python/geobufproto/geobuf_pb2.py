# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geobufproto/geobuf.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18geobufproto/geobuf.proto\x12\x0bgeobufproto\"\xea\n\n\x04\x44\x61ta\x12\x12\n\x04keys\x18\x01 \x03(\tR\x04keys\x12!\n\ndimensions\x18\x02 \x01(\r:\x01\x32R\ndimensions\x12\x1f\n\tprecision\x18\x03 \x01(\r:\x01\x36R\tprecision\x12T\n\x12\x66\x65\x61ture_collection\x18\x04 \x01(\x0b\x32#.geobufproto.Data.FeatureCollectionH\x00R\x11\x66\x65\x61tureCollection\x12\x35\n\x07\x66\x65\x61ture\x18\x05 \x01(\x0b\x32\x19.geobufproto.Data.FeatureH\x00R\x07\x66\x65\x61ture\x12\x38\n\x08geometry\x18\x06 \x01(\x0b\x32\x1a.geobufproto.Data.GeometryH\x00R\x08geometry\x1a\xfd\x01\n\x07\x46\x65\x61ture\x12\x36\n\x08geometry\x18\x01 \x02(\x0b\x32\x1a.geobufproto.Data.GeometryR\x08geometry\x12\x10\n\x02id\x18\x0b \x01(\tH\x00R\x02id\x12\x17\n\x06int_id\x18\x0c \x01(\x12H\x00R\x05intId\x12/\n\x06values\x18\r \x03(\x0b\x32\x17.geobufproto.Data.ValueR\x06values\x12\"\n\nproperties\x18\x0e \x03(\rB\x02\x10\x01R\nproperties\x12/\n\x11\x63ustom_properties\x18\x0f \x03(\rB\x02\x10\x01R\x10\x63ustomPropertiesB\t\n\x07id_type\x1a\x96\x03\n\x08Geometry\x12\x33\n\x04type\x18\x01 \x02(\x0e\x32\x1f.geobufproto.Data.Geometry.TypeR\x04type\x12\x1c\n\x07lengths\x18\x02 \x03(\rB\x02\x10\x01R\x07lengths\x12\x1a\n\x06\x63oords\x18\x03 \x03(\x12\x42\x02\x10\x01R\x06\x63oords\x12:\n\ngeometries\x18\x04 \x03(\x0b\x32\x1a.geobufproto.Data.GeometryR\ngeometries\x12/\n\x06values\x18\r \x03(\x0b\x32\x17.geobufproto.Data.ValueR\x06values\x12/\n\x11\x63ustom_properties\x18\x0f \x03(\rB\x02\x10\x01R\x10\x63ustomProperties\"}\n\x04Type\x12\t\n\x05POINT\x10\x00\x12\x0e\n\nMULTIPOINT\x10\x01\x12\x0e\n\nLINESTRING\x10\x02\x12\x13\n\x0fMULTILINESTRING\x10\x03\x12\x0b\n\x07POLYGON\x10\x04\x12\x10\n\x0cMULTIPOLYGON\x10\x05\x12\x16\n\x12GEOMETRYCOLLECTION\x10\x06\x1a\xac\x01\n\x11\x46\x65\x61tureCollection\x12\x35\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x19.geobufproto.Data.FeatureR\x08\x66\x65\x61tures\x12/\n\x06values\x18\r \x03(\x0b\x32\x17.geobufproto.Data.ValueR\x06values\x12/\n\x11\x63ustom_properties\x18\x0f \x03(\rB\x02\x10\x01R\x10\x63ustomProperties\x1a\xed\x01\n\x05Value\x12#\n\x0cstring_value\x18\x01 \x01(\tH\x00R\x0bstringValue\x12#\n\x0c\x64ouble_value\x18\x02 \x01(\x01H\x00R\x0b\x64oubleValue\x12$\n\rpos_int_value\x18\x03 \x01(\x04H\x00R\x0bposIntValue\x12$\n\rneg_int_value\x18\x04 \x01(\x04H\x00R\x0bnegIntValue\x12\x1f\n\nbool_value\x18\x05 \x01(\x08H\x00R\tboolValue\x12\x1f\n\njson_value\x18\x06 \x01(\tH\x00R\tjsonValueB\x0c\n\nvalue_typeB\x0b\n\tdata_typeBl\n\x0f\x63om.geobufprotoB\x0bGeobufProtoH\x01P\x01\xa2\x02\x03GXX\xaa\x02\x0bGeobufproto\xca\x02\x0bGeobufproto\xe2\x02\x17Geobufproto\\GPBMetadata\xea\x02\x0bGeobufproto')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'geobufproto.geobuf_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.geobufprotoB\013GeobufProtoH\001P\001\242\002\003GXX\252\002\013Geobufproto\312\002\013Geobufproto\342\002\027Geobufproto\\GPBMetadata\352\002\013Geobufproto'
  _DATA_FEATURE.fields_by_name['properties']._options = None
  _DATA_FEATURE.fields_by_name['properties']._serialized_options = b'\020\001'
  _DATA_FEATURE.fields_by_name['custom_properties']._options = None
  _DATA_FEATURE.fields_by_name['custom_properties']._serialized_options = b'\020\001'
  _DATA_GEOMETRY.fields_by_name['lengths']._options = None
  _DATA_GEOMETRY.fields_by_name['lengths']._serialized_options = b'\020\001'
  _DATA_GEOMETRY.fields_by_name['coords']._options = None
  _DATA_GEOMETRY.fields_by_name['coords']._serialized_options = b'\020\001'
  _DATA_GEOMETRY.fields_by_name['custom_properties']._options = None
  _DATA_GEOMETRY.fields_by_name['custom_properties']._serialized_options = b'\020\001'
  _DATA_FEATURECOLLECTION.fields_by_name['custom_properties']._options = None
  _DATA_FEATURECOLLECTION.fields_by_name['custom_properties']._serialized_options = b'\020\001'
  _DATA._serialized_start=42
  _DATA._serialized_end=1428
  _DATA_FEATURE._serialized_start=338
  _DATA_FEATURE._serialized_end=591
  _DATA_GEOMETRY._serialized_start=594
  _DATA_GEOMETRY._serialized_end=1000
  _DATA_GEOMETRY_TYPE._serialized_start=875
  _DATA_GEOMETRY_TYPE._serialized_end=1000
  _DATA_FEATURECOLLECTION._serialized_start=1003
  _DATA_FEATURECOLLECTION._serialized_end=1175
  _DATA_VALUE._serialized_start=1178
  _DATA_VALUE._serialized_end=1415
# @@protoc_insertion_point(module_scope)
