
### Partial copyright for spi code extracted from http://abyz.co.uk/rpi/pigpio/code/test-APA102_py.zip
# test-APA102.py
# 2017-03-28
# Public Domain

### Partial copyright from Pimoroni (MIT licence) for the Blinkt! interface and some unmodifed code

### Mix & Match to use spi code inside Blinkt! API by David Glaude (MIT licence)

import atexit
import spidev

__version__ = '0.1.1'

DAT=10
CLK=11
CE=1

DATB=(1<<DAT)
CLKB=(1<<CLK)

NUM_PIXELS = 8
BRIGHTNESS = 7


apa102_cmd=[0]*4 + [0xe0+BRIGHTNESS, 0, 0, 0]*NUM_PIXELS + [255]*4

_gpio_setup = False
_clear_on_exit = True

### inspiring version ###
def _exit():
    if _clear_on_exit:
        clear()
        show()
    spi.close()


### inspiring version ###
def set_brightness(brightness):
    """Set the brightness of all pixels

    :param brightness: Brightness: 0.0 to 1.0
    """

    if brightness < 0 or brightness > 1:
        raise ValueError("Brightness should be between 0.0 and 1.0")

    for led in range(NUM_PIXELS):
        offset = (led*4) +4
        apa102_cmd[offset  ] = 0xE0 + ( int(31.0 * brightness) & 0b11111 )


### inspiring version ###
def clear():
    """Clear the pixel buffer"""
    for led in range(NUM_PIXELS):
        offset = (led*4) +4
        apa102_cmd[offset+1] = 0
        apa102_cmd[offset+2] = 0
        apa102_cmd[offset+3] = 0


### inspiring version ###
def show():
    """Output the buffer to Blinkt!"""
    global _gpio_setup

    if not _gpio_setup:
        global spi
        spi = spidev.SpiDev()
        spi.open(0, CE)
        spi.max_speed_hz = int(2e6)
        _gpio_setup = True

    spi.xfer(apa102_cmd)


### inspiring version ### NO CHANGE ###
def set_all(r, g, b, brightness=None):
    """Set the RGB value and optionally brightness of all pixels

    If you don't supply a brightness value, the last value set for each pixel be kept.

    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    for x in range(NUM_PIXELS):
        set_pixel(x, r, g, b, brightness)


### inspiring version ###
def get_pixel(x):
    """Get the RGB and brightness value of a specific pixel"""

    offset = (x*4) +4
    brightness = apa102_cmd[offset  ] & 0b11111
    b = apa102_cmd[offset+1]
    g = apa102_cmd[offset+2]
    r = apa102_cmd[offset+3]
    brightness /= 31.0

    return r, g, b, round(brightness, 3)


### inspiring version ###
def set_pixel(x, r, g, b, brightness=None):
    """Set the RGB value, and optionally brightness, of a single pixel

    If you don't supply a brightness value, the last value will be kept.

    :param x: The horizontal position of the pixel: 0 to 7
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    offset = (x*4) +4
    if brightness is not None:
        apa102_cmd[offset  ] = 0xE0 + ( int(31.0 * brightness) & 0b11111 )
    apa102_cmd[offset+1] = b
    apa102_cmd[offset+2] = g
    apa102_cmd[offset+3] = r


### inspiring version ### NO CHANGE ###
def set_clear_on_exit(value=True):
    """Set whether Blinkt! should be cleared upon exit

    By default Blinkt! will turn off the pixels on exit, but calling::

        blinkt.set_clear_on_exit(False)

    Will ensure that it does not.

    :param value: True or False (default True)
    """
    global _clear_on_exit
    _clear_on_exit = value


atexit.register(_exit)

