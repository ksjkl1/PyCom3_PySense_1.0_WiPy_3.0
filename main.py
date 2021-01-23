#!/usr/bin/env python    
#
# Copyright (c) 2020, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

# See https://docs.pycom.io for more information regarding library specifics

import time
import pycom
from pysense import Pysense
import machine

from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

pycom.heartbeat(False)
#pycom.rgbled(0x0A0A08) # white

py = Pysense()

while True:
     print("")
     print("Reading Sensors")
     print("")
     pycom.rgbled(0x0000F7) # blue
     mp = MPL3115A2(py,mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
     print("MPL3115A2 temperature: " + str(mp.temperature()))
     print("Altitude: " + str(mp.altitude()))
     mpp = MPL3115A2(py,mode=PRESSURE) # Returns pressure in Pa. Mode may also be set to ALTITUDE, returning a value in meters
     print("Pressure: " + str(mpp.pressure()))
     si = SI7006A20(py)
     print("Temperature: " + str(si.temperature())+ " deg C and Relative Humidity: " + str(si.humidity()) + " %RH")
     print("Dew point: "+ str(si.dew_point()) + " deg C")
     t_ambient = 24.4
     print("Humidity Ambient for " + str(t_ambient) + " deg C is " + str(si.humid_ambient(t_ambient)) + "%RH")
     lt = LTR329ALS01(py)
     print("Light (channel Blue lux, channel Red lux): " + str(lt.light()))
     li = LIS2HH12(py)
     print("Acceleration: " + str(li.acceleration()))
     print("Roll: " + str(li.roll()))
     print("Pitch: " + str(li.pitch()))
     print("Battery voltage: " + str(py.read_battery_voltage()))
     pybytes.send_signal(0, str(mp.temperature()))
     pybytes.send_signal(1, str(si.temperature()))
     #pybytes.send_signal(2, str(mp.altitude()))
     pybytes.send_signal(3, str(mpp.pressure()))
     pybytes.send_signal(4, str(si.humidity()))
     pybytes.send_signal(5, str(si.dew_point()))
     pybytes.send_signal(6, str(si.humid_ambient(t_ambient)))
     pybytes.send_signal(7, str(lt.light()))
     pybytes.send_signal(8, str(py.read_battery_voltage()))
     pycom.rgbled(0x0A0A08) # white
     print("End Run")
     print("")
     print("PyCom3_PySense_1.0_WiPy_3.0")
     time.sleep(60)

print("sleep 60")
