#!/usr/bin/python3

import smbus2
import bme280

port = 4
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)


# this will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# compensated_reading class has the following attributes
print(data.id)
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)

# Also a string representation
print(data)
