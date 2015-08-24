from nanpy.arduinotree import ArduinoTree

__author__ = 'gcdeh_000'

from nanpy.pwm import ArduinoPwmPin
from nanpy.serialmanager import SerialManager


if __name__ == '__main__':
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    pin9 = a.pin.get(9)
    pin9.mode = 1
    pin9.write_digital_value(1)
    pwm = pin9.pwm()
    print ('set  frequency=%s Hz' % 1000)
    pwm.set_high_freq_around(1000)
    print ('real frequency=%s Hz' % pwm.read_frequency())
