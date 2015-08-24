from nanpy.arduinotree import ArduinoTree

__author__ = 'gcdeh_000'

from nanpy.pwm import ArduinoPwmPin
from nanpy.serialmanager import SerialManager


if __name__ == '__main__':
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    pin9 = a.pin.get(9)
    pin9.mode = 1
    pin9.write_digital_value()
    pin9.pwm.write_value(255)
    print ('set  frequency=%s Hz' % 1000)
  
