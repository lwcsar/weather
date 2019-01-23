#!/usr/bin/env python3
# Portions copyright (c) 2014-18 Richard Hull and contributors

import os
import sys
import time

if os.name != 'posix':
    sys.exit('{} platform not supported'.format(os.name))

from demo_opts import get_device
from luma.core.render import canvas
from PIL import ImageFont

try:
    import psutil
except ImportError:
    print("The psutil library was not found. Run 'sudo -H pip install psutil' to install it.")
    sys.exit()

try:
    import smbus2
    import bme280
except ImportError:
    print("The psutil library was not found. Run 'sudo -H pip install RPi.bme280 smbus2' to install it.")
    sys.exit()

port = 4
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)


def date_time():
    f = os.popen('date +"%a %x %H:%M:%S"')
    dt = str(f.read())
    return "%s" % dt.rstrip('\r\n').rstrip(' ')

def lan_ip():
    cmd = 'hostname -I'
    f = os.popen(cmd)
    ip = str(f.read())
    return "IP: %s" % ip.rstrip('\r\n').rstrip(' ')


def temperature(type='temp'):
    # this will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, address, calibration_params)
    if type == 'humidity':
    	return "%0.2f%% rH" % \
           (data.humidity)
    elif type == 'pressure':
    	return "%0.2f hPa" % \
           (data.pressure)
    elif type == 'tempf':
    	return "%0.0fF" % \
           ((data.temperature * 9/5)+32)
    elif type == 'tempc':
    	return "%0.2f C" % \
           (data.temperature)
    else:
    	return "%0.2fC, %0.2fF" % \
           (data.temperature, (data.temperature * 9/5)+32)

def stats(device):
    # use custom font
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                'fonts', 'C&C Red Alert [INET].ttf'))
    font_sm = ImageFont.truetype(font_path, 12)
    font_lg = ImageFont.truetype(font_path, 18)
    font_xl = ImageFont.truetype(font_path, 32)

    with canvas(device) as draw:
        draw.text((0, 0), date_time(), font=font_sm, fill="white")
        draw.text((0, 14), lan_ip(), font=font_sm, fill="white")

        if device.height >= 64:
            try:
                draw.text((74, 10), temperature('tempf'),
                          font=font_xl, fill="white")
                draw.text((0, 30), "Temp:", font=font_sm, fill="white")
                draw.text((36, 30), temperature('tempc'), 
                          font=font_sm, fill="white")
                draw.text((0, 42), "Humidity:", font=font_sm, fill="white")
                draw.text((60, 42), temperature('humidity'), 
                          font=font_sm, fill="white")
                draw.text((0,54), "Pressure:", font=font_sm, fill="white")
                draw.text((60,54), temperature('pressure'), 
                          font=font_sm, fill="white")
            except KeyError:
                # no temp enabled/available
                pass


def main():
    while True:
        stats(device)
        time.sleep(5)


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
