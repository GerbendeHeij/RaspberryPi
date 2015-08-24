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
    redpin = pin9.pwm
    greenpin = pin10.pwm
    bluepin = pin11.pwm

    running = True

    while running:
        Input_text =input("Give the collor rightness of red");
        if input == 'exit':
            running = False
        red = Input_text
        Input_text =input("Give the collor rightness of green");
        if input == 'exit':
            running = False
        green = Input_text
        Input_text =input("Give the collor rightness of blue");
        if input == 'exit':
            running = False
        blue = Input_text

        redpin.write_value(red)
        greenpin.write_value(green)
        bluepin.write_value(blue)

        print red
        print green
        print blue