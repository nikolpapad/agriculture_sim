# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mini_ros/AgentData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class AgentData(genpy.Message):
  _md5sum = "eb20a647338517e50d32ae4353795371"
  _type = "mini_ros/AgentData"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 action0
float32 action1
float32 action2
float32 action3
float32 action4
float32 action5
float32 action6
float32 action7
float32 action8
float32 action9
float32 action10
float32 action11
float32 action12
float32 action13"""
  __slots__ = ['action0','action1','action2','action3','action4','action5','action6','action7','action8','action9','action10','action11','action12','action13']
  _slot_types = ['float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       action0,action1,action2,action3,action4,action5,action6,action7,action8,action9,action10,action11,action12,action13

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AgentData, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.action0 is None:
        self.action0 = 0.
      if self.action1 is None:
        self.action1 = 0.
      if self.action2 is None:
        self.action2 = 0.
      if self.action3 is None:
        self.action3 = 0.
      if self.action4 is None:
        self.action4 = 0.
      if self.action5 is None:
        self.action5 = 0.
      if self.action6 is None:
        self.action6 = 0.
      if self.action7 is None:
        self.action7 = 0.
      if self.action8 is None:
        self.action8 = 0.
      if self.action9 is None:
        self.action9 = 0.
      if self.action10 is None:
        self.action10 = 0.
      if self.action11 is None:
        self.action11 = 0.
      if self.action12 is None:
        self.action12 = 0.
      if self.action13 is None:
        self.action13 = 0.
    else:
      self.action0 = 0.
      self.action1 = 0.
      self.action2 = 0.
      self.action3 = 0.
      self.action4 = 0.
      self.action5 = 0.
      self.action6 = 0.
      self.action7 = 0.
      self.action8 = 0.
      self.action9 = 0.
      self.action10 = 0.
      self.action11 = 0.
      self.action12 = 0.
      self.action13 = 0.

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
      buff.write(_get_struct_14f().pack(_x.action0, _x.action1, _x.action2, _x.action3, _x.action4, _x.action5, _x.action6, _x.action7, _x.action8, _x.action9, _x.action10, _x.action11, _x.action12, _x.action13))
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
      end += 56
      (_x.action0, _x.action1, _x.action2, _x.action3, _x.action4, _x.action5, _x.action6, _x.action7, _x.action8, _x.action9, _x.action10, _x.action11, _x.action12, _x.action13,) = _get_struct_14f().unpack(str[start:end])
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
      buff.write(_get_struct_14f().pack(_x.action0, _x.action1, _x.action2, _x.action3, _x.action4, _x.action5, _x.action6, _x.action7, _x.action8, _x.action9, _x.action10, _x.action11, _x.action12, _x.action13))
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
      end += 56
      (_x.action0, _x.action1, _x.action2, _x.action3, _x.action4, _x.action5, _x.action6, _x.action7, _x.action8, _x.action9, _x.action10, _x.action11, _x.action12, _x.action13,) = _get_struct_14f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_14f = None
def _get_struct_14f():
    global _struct_14f
    if _struct_14f is None:
        _struct_14f = struct.Struct("<14f")
    return _struct_14f