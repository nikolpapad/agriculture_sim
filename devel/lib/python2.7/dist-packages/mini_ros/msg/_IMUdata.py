# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mini_ros/IMUdata.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class IMUdata(genpy.Message):
  _md5sum = "3a27cb61fd87ce5110e1d6a4a68a0126"
  _type = "mini_ros/IMUdata"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 roll
float32 pitch
float32 acc_x
float32 acc_y
float32 acc_z
float32 gyro_x
float32 gyro_y
float32 gyro_z"""
  __slots__ = ['roll','pitch','acc_x','acc_y','acc_z','gyro_x','gyro_y','gyro_z']
  _slot_types = ['float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       roll,pitch,acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(IMUdata, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.roll is None:
        self.roll = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.acc_x is None:
        self.acc_x = 0.
      if self.acc_y is None:
        self.acc_y = 0.
      if self.acc_z is None:
        self.acc_z = 0.
      if self.gyro_x is None:
        self.gyro_x = 0.
      if self.gyro_y is None:
        self.gyro_y = 0.
      if self.gyro_z is None:
        self.gyro_z = 0.
    else:
      self.roll = 0.
      self.pitch = 0.
      self.acc_x = 0.
      self.acc_y = 0.
      self.acc_z = 0.
      self.gyro_x = 0.
      self.gyro_y = 0.
      self.gyro_z = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_8f().pack(_x.roll, _x.pitch, _x.acc_x, _x.acc_y, _x.acc_z, _x.gyro_x, _x.gyro_y, _x.gyro_z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.roll, _x.pitch, _x.acc_x, _x.acc_y, _x.acc_z, _x.gyro_x, _x.gyro_y, _x.gyro_z,) = _get_struct_8f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_8f().pack(_x.roll, _x.pitch, _x.acc_x, _x.acc_y, _x.acc_z, _x.gyro_x, _x.gyro_y, _x.gyro_z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.roll, _x.pitch, _x.acc_x, _x.acc_y, _x.acc_z, _x.gyro_x, _x.gyro_y, _x.gyro_z,) = _get_struct_8f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_8f = None
def _get_struct_8f():
    global _struct_8f
    if _struct_8f is None:
        _struct_8f = struct.Struct("<8f")
    return _struct_8f
