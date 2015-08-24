from nanpy.arduinotree import ArduinoTree

__author__ = 'gcdeh_000'

from nanpy.pwm import ArduinoPwmPin
from nanpy.serialmanager import SerialManager


if __name__ == '__main__':
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    pin9 = a.pin.get(9)
    pin10 = a.pin.get(9)
    pin11 = a.pin.get(9)
    pin9.mode = 1
    pin10.mode = 1
    pin11.mode = 1
    pin9.write_digital_value(1)
    pin10.write_digital_value(1)
    pin11.write_digital_value(1)
    red = pin9.pwm
    red.write_value(self,1)

    running = true

    while running:
        input = input("Give the collor in the following format: red,green,blue")
        if input == 'exit':
            running = false
        red = input[0:3]
        green = input[5:8]
        blue = input[10:13]
        print (red)
        print (blue)
        print (red)