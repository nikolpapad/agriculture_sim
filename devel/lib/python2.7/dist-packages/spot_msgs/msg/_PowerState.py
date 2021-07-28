# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from spot_msgs/PowerState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import std_msgs.msg

class PowerState(genpy.Message):
  _md5sum = "1248df72d2f23288441e3a23d09bd4f0"
  _type = "spot_msgs/PowerState"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# MotorPowerState
uint8 STATE_UNKNOWN = 0
uint8 STATE_OFF = 1
uint8 STATE_ON = 2
uint8 STATE_POWERING_ON = 3
uint8 STATE_POWERING_OFF = 4
uint8 STATE_ERROR = 5

# ShorePowerState
uint8 STATE_UNKNOWN_SHORE_POWER = 0
uint8 STATE_ON_SHORE_POWER = 1
uint8 STATE_OFF_SHORE_POWER = 2

Header header
uint8 motor_power_state
uint8 shore_power_state
float64 locomotion_charge_percentage
duration locomotion_estimated_runtime

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  # Pseudo-constants
  STATE_UNKNOWN = 0
  STATE_OFF = 1
  STATE_ON = 2
  STATE_POWERING_ON = 3
  STATE_POWERING_OFF = 4
  STATE_ERROR = 5
  STATE_UNKNOWN_SHORE_POWER = 0
  STATE_ON_SHORE_POWER = 1
  STATE_OFF_SHORE_POWER = 2

  __slots__ = ['header','motor_power_state','shore_power_state','locomotion_charge_percentage','locomotion_estimated_runtime']
  _slot_types = ['std_msgs/Header','uint8','uint8','float64','duration']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,motor_power_state,shore_power_state,locomotion_charge_percentage,locomotion_estimated_runtime

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PowerState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.motor_power_state is None:
        self.motor_power_state = 0
      if self.shore_power_state is None:
        self.shore_power_state = 0
      if self.locomotion_charge_percentage is None:
        self.locomotion_charge_percentage = 0.
      if self.locomotion_estimated_runtime is None:
        self.locomotion_estimated_runtime = genpy.Duration()
    else:
      self.header = std_msgs.msg.Header()
      self.motor_power_state = 0
      self.shore_power_state = 0
      self.locomotion_charge_percentage = 0.
      self.locomotion_estimated_runtime = genpy.Duration()

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2Bd2i().pack(_x.motor_power_state, _x.shore_power_state, _x.locomotion_charge_percentage, _x.locomotion_estimated_runtime.secs, _x.locomotion_estimated_runtime.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.locomotion_estimated_runtime is None:
        self.locomotion_estimated_runtime = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 18
      (_x.motor_power_state, _x.shore_power_state, _x.locomotion_charge_percentage, _x.locomotion_estimated_runtime.secs, _x.locomotion_estimated_runtime.nsecs,) = _get_struct_2Bd2i().unpack(str[start:end])
      self.locomotion_estimated_runtime.canon()
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2Bd2i().pack(_x.motor_power_state, _x.shore_power_state, _x.locomotion_charge_percentage, _x.locomotion_estimated_runtime.secs, _x.locomotion_estimated_runtime.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.locomotion_estimated_runtime is None:
        self.locomotion_estimated_runtime = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 18
      (_x.motor_power_state, _x.shore_power_state, _x.locomotion_charge_percentage, _x.locomotion_estimated_runtime.secs, _x.locomotion_estimated_runtime.nsecs,) = _get_struct_2Bd2i().unpack(str[start:end])
      self.locomotion_estimated_runtime.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2Bd2i = None
def _get_struct_2Bd2i():
    global _struct_2Bd2i
    if _struct_2Bd2i is None:
        _struct_2Bd2i = struct.Struct("<2Bd2i")
    return _struct_2Bd2i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
