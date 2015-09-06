__author__ = 'gcdeh_000'

from nanpy.arduinotree import ArduinoTree
from nanpy import onewire
from nanpy import dallastemperature

__author__ = 'gcdeh_000'

from nanpy.pwm import ArduinoPwmPin
from nanpy.serialmanager import SerialManager
import time


if __name__ == '__main__':
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    tempPin = a.pin.get(4)
    TempSensor = dallastemperature.DallasTemperature(tempPin,connection=connection)

    print "Start reading temp sensor"
    time.sleep(0.010)
    temp = TempSensor.getTempC
    print temp
