# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from unitree_legged_msgs/HighState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import unitree_legged_msgs.msg

class HighState(genpy.Message):
  _md5sum = "ecc2950a071fd456ed31756d75114627"
  _type = "unitree_legged_msgs/HighState"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 levelFlag
uint16 commVersion                  # Old version Aliengo does not have
uint16 robotID                      # Old version Aliengo does not have
uint32 SN                           # Old version Aliengo does not have
uint8 bandWidth                     # Old version Aliengo does not have
uint8 mode
IMU imu
float32 forwardSpeed
float32 sideSpeed
float32 rotateSpeed
float32 bodyHeight
float32 updownSpeed
float32 forwardPosition       # (will be float type next version)   # Old version Aliengo is different
float32 sidePosition          # (will be float type next version)   # Old version Aliengo is different
Cartesian[4] footPosition2Body
Cartesian[4] footSpeed2Body
int16[4] footForce                  # Old version Aliengo is different
int16[4] footForceEst               # Old version Aliengo does not have
uint32 tick               
uint8[40] wirelessRemote
uint32 reserve                      # Old version Aliengo does not have
uint32 crc

# Under are not defined in SDK yet. # Old version Aliengo does not have
Cartesian[4] eeForce            # It's a 1-DOF force in real robot, but 3-DOF is better for visualization.
float32[12] jointP              # for visualization
================================================================================
MSG: unitree_legged_msgs/IMU
float32[4] quaternion
float32[3] gyroscope
float32[3] accelerometer
float32[3] rpy
int8 temperature
================================================================================
MSG: unitree_legged_msgs/Cartesian
float32 x
float32 y
float32 z"""
  __slots__ = ['levelFlag','commVersion','robotID','SN','bandWidth','mode','imu','forwardSpeed','sideSpeed','rotateSpeed','bodyHeight','updownSpeed','forwardPosition','sidePosition','footPosition2Body','footSpeed2Body','footForce','footForceEst','tick','wirelessRemote','reserve','crc','eeForce','jointP']
  _slot_types = ['uint8','uint16','uint16','uint32','uint8','uint8','unitree_legged_msgs/IMU','float32','float32','float32','float32','float32','float32','float32','unitree_legged_msgs/Cartesian[4]','unitree_legged_msgs/Cartesian[4]','int16[4]','int16[4]','uint32','uint8[40]','uint32','uint32','unitree_legged_msgs/Cartesian[4]','float32[12]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       levelFlag,commVersion,robotID,SN,bandWidth,mode,imu,forwardSpeed,sideSpeed,rotateSpeed,bodyHeight,updownSpeed,forwardPosition,sidePosition,footPosition2Body,footSpeed2Body,footForce,footForceEst,tick,wirelessRemote,reserve,crc,eeForce,jointP

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HighState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.levelFlag is None:
        self.levelFlag = 0
      if self.commVersion is None:
        self.commVersion = 0
      if self.robotID is None:
        self.robotID = 0
      if self.SN is None:
        self.SN = 0
      if self.bandWidth is None:
        self.bandWidth = 0
      if self.mode is None:
        self.mode = 0
      if self.imu is None:
        self.imu = unitree_legged_msgs.msg.IMU()
      if self.forwardSpeed is None:
        self.forwardSpeed = 0.
      if self.sideSpeed is None:
        self.sideSpeed = 0.
      if self.rotateSpeed is None:
        self.rotateSpeed = 0.
      if self.bodyHeight is None:
        self.bodyHeight = 0.
      if self.updownSpeed is None:
        self.updownSpeed = 0.
      if self.forwardPosition is None:
        self.forwardPosition = 0.
      if self.sidePosition is None:
        self.sidePosition = 0.
      if self.footPosition2Body is None:
        self.footPosition2Body = [unitree_legged_msgs.msg.Cartesian() for _ in range(4)]
      if self.footSpeed2Body is None:
        self.footSpeed2Body = [unitree_legged_msgs.msg.Cartesian() for _ in range(4)]
      if self.footForce is None:
        self.footForce = [0] * 4
      if self.footForceEst is None:
        self.footForceEst = [0] * 4
      if self.tick is None:
        self.tick = 0
      if self.wirelessRemote is None:
        self.wirelessRemote = b'\0'*40
      if self.reserve is None:
        self.reserve = 0
      if self.crc is None:
        self.crc = 0
      if self.eeForce is None:
        self.eeForce = [unitree_legged_msgs.msg.Cartesian() for _ in range(4)]
      if self.jointP is None:
        self.jointP = [0.] * 12
    else:
      self.levelFlag = 0
      self.commVersion = 0
      self.robotID = 0
      self.SN = 0
      self.bandWidth = 0
      self.mode = 0
      self.imu = unitree_legged_msgs.msg.IMU()
      self.forwardSpeed = 0.
      self.sideSpeed = 0.
      self.rotateSpeed = 0.
      self.bodyHeight = 0.
      self.updownSpeed = 0.
      self.forwardPosition = 0.
      self.sidePosition = 0.
      self.footPosition2Body = [unitree_legged_msgs.msg.Cartesian() for _ in range(4)]
      self.footSpeed2Body = [unitree_legged_msgs.msg.Cartesian() for _ in range(4)]
      self.footForce = [0] * 4
      self.footForceEst = [0] * 4
      self.tick = 0
      self.wirelessRemote = b'\0'*40
      self.reserve = 0
      self.crc = 0
      self.eeForce = [unitree_legged_msgs.msg.Cartesian() for _ in range(4)]
      self.jointP = [0.] * 12

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
      buff.write(_get_struct_B2HI2B().pack(_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth, _x.mode))
      buff.write(_get_struct_4f().pack(*self.imu.quaternion))
      buff.write(_get_struct_3f().pack(*self.imu.gyroscope))
      buff.write(_get_struct_3f().pack(*self.imu.accelerometer))
      buff.write(_get_struct_3f().pack(*self.imu.rpy))
      _x = self
      buff.write(_get_struct_b7f().pack(_x.imu.temperature, _x.forwardSpeed, _x.sideSpeed, _x.rotateSpeed, _x.bodyHeight, _x.updownSpeed, _x.forwardPosition, _x.sidePosition))
      if len(self.footPosition2Body) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.footPosition2Body), 'self.footPosition2Body')))
      for val1 in self.footPosition2Body:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      if len(self.footSpeed2Body) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.footSpeed2Body), 'self.footSpeed2Body')))
      for val1 in self.footSpeed2Body:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      buff.write(_get_struct_4h().pack(*self.footForce))
      buff.write(_get_struct_4h().pack(*self.footForceEst))
      _x = self.tick
      buff.write(_get_struct_I().pack(_x))
      _x = self.wirelessRemote
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_40B().pack(*_x))
      else:
        buff.write(_get_struct_40s().pack(_x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.reserve, _x.crc))
      if len(self.eeForce) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.eeForce), 'self.eeForce')))
      for val1 in self.eeForce:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      buff.write(_get_struct_12f().pack(*self.jointP))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.imu is None:
        self.imu = unitree_legged_msgs.msg.IMU()
      if self.footPosition2Body is None:
        self.footPosition2Body = None
      if self.footSpeed2Body is None:
        self.footSpeed2Body = None
      if self.eeForce is None:
        self.eeForce = None
      end = 0
      _x = self
      start = end
      end += 11
      (_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth, _x.mode,) = _get_struct_B2HI2B().unpack(str[start:end])
      start = end
      end += 16
      self.imu.quaternion = _get_struct_4f().unpack(str[start:end])
      start = end
      end += 12
      self.imu.gyroscope = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.imu.accelerometer = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.imu.rpy = _get_struct_3f().unpack(str[start:end])
      _x = self
      start = end
      end += 29
      (_x.imu.temperature, _x.forwardSpeed, _x.sideSpeed, _x.rotateSpeed, _x.bodyHeight, _x.updownSpeed, _x.forwardPosition, _x.sidePosition,) = _get_struct_b7f().unpack(str[start:end])
      self.footPosition2Body = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.footPosition2Body.append(val1)
      self.footSpeed2Body = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.footSpeed2Body.append(val1)
      start = end
      end += 8
      self.footForce = _get_struct_4h().unpack(str[start:end])
      start = end
      end += 8
      self.footForceEst = _get_struct_4h().unpack(str[start:end])
      start = end
      end += 4
      (self.tick,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 40
      self.wirelessRemote = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.reserve, _x.crc,) = _get_struct_2I().unpack(str[start:end])
      self.eeForce = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.eeForce.append(val1)
      start = end
      end += 48
      self.jointP = _get_struct_12f().unpack(str[start:end])
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
      buff.write(_get_struct_B2HI2B().pack(_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth, _x.mode))
      buff.write(self.imu.quaternion.tostring())
      buff.write(self.imu.gyroscope.tostring())
      buff.write(self.imu.accelerometer.tostring())
      buff.write(self.imu.rpy.tostring())
      _x = self
      buff.write(_get_struct_b7f().pack(_x.imu.temperature, _x.forwardSpeed, _x.sideSpeed, _x.rotateSpeed, _x.bodyHeight, _x.updownSpeed, _x.forwardPosition, _x.sidePosition))
      if len(self.footPosition2Body) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.footPosition2Body), 'self.footPosition2Body')))
      for val1 in self.footPosition2Body:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      if len(self.footSpeed2Body) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.footSpeed2Body), 'self.footSpeed2Body')))
      for val1 in self.footSpeed2Body:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      buff.write(self.footForce.tostring())
      buff.write(self.footForceEst.tostring())
      _x = self.tick
      buff.write(_get_struct_I().pack(_x))
      _x = self.wirelessRemote
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_40B().pack(*_x))
      else:
        buff.write(_get_struct_40s().pack(_x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.reserve, _x.crc))
      if len(self.eeForce) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.eeForce), 'self.eeForce')))
      for val1 in self.eeForce:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      buff.write(self.jointP.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.imu is None:
        self.imu = unitree_legged_msgs.msg.IMU()
      if self.footPosition2Body is None:
        self.footPosition2Body = None
      if self.footSpeed2Body is None:
        self.footSpeed2Body = None
      if self.eeForce is None:
        self.eeForce = None
      end = 0
      _x = self
      start = end
      end += 11
      (_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth, _x.mode,) = _get_struct_B2HI2B().unpack(str[start:end])
      start = end
      end += 16
      self.imu.quaternion = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=4)
      start = end
      end += 12
      self.imu.gyroscope = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.imu.accelerometer = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.imu.rpy = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      _x = self
      start = end
      end += 29
      (_x.imu.temperature, _x.forwardSpeed, _x.sideSpeed, _x.rotateSpeed, _x.bodyHeight, _x.updownSpeed, _x.forwardPosition, _x.sidePosition,) = _get_struct_b7f().unpack(str[start:end])
      self.footPosition2Body = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.footPosition2Body.append(val1)
      self.footSpeed2Body = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.footSpeed2Body.append(val1)
      start = end
      end += 8
      self.footForce = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=4)
      start = end
      end += 8
      self.footForceEst = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=4)
      start = end
      end += 4
      (self.tick,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 40
      self.wirelessRemote = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.reserve, _x.crc,) = _get_struct_2I().unpack(str[start:end])
      self.eeForce = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.eeForce.append(val1)
      start = end
      end += 48
      self.jointP = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=12)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_12f = None
def _get_struct_12f():
    global _struct_12f
    if _struct_12f is None:
        _struct_12f = struct.Struct("<12f")
    return _struct_12f
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_40B = None
def _get_struct_40B():
    global _struct_40B
    if _struct_40B is None:
        _struct_40B = struct.Struct("<40B")
    return _struct_40B
_struct_40s = None
def _get_struct_40s():
    global _struct_40s
    if _struct_40s is None:
        _struct_40s = struct.Struct("<40s")
    return _struct_40s
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
_struct_4h = None
def _get_struct_4h():
    global _struct_4h
    if _struct_4h is None:
        _struct_4h = struct.Struct("<4h")
    return _struct_4h
_struct_B2HI2B = None
def _get_struct_B2HI2B():
    global _struct_B2HI2B
    if _struct_B2HI2B is None:
        _struct_B2HI2B = struct.Struct("<B2HI2B")
    return _struct_B2HI2B
_struct_b7f = None
def _get_struct_b7f():
    global _struct_b7f
    if _struct_b7f is None:
        _struct_b7f = struct.Struct("<b7f")
    return _struct_b7f
