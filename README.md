# blinktspiring

Blinkt! compatible layer for InsPiRing driver

If you have an InsPiRing Straight-8 from rasp.io ( http://rasp.io/inspiring/ ) and want to use any of the example the Pimoroni Blinkt! ( https://github.com/pimoroni/blinkt ), this the BlinktSpiring project is for you.

## Instruction

Take any example code from here: https://github.com/pimoroni/blinkt/tree/master/examples
Copy blinkt.py file in the same folder.
Enjoy

## Copyright / LICENCE

This code is a mix between:
* Public Domain code extracted from http://abyz.co.uk/rpi/pigpio/code/test-APA102_py.zip # test-APA102.py # 2017-03-28 # Public Domain
* MIT code from the Blinkt! library from Pimoroni
* MIT code from David Glaude to use SPI code within Blinkt! API

No single piece of code from Alex Eames has been used to write this glue layer from Blinkt! to his hardware.
While there is no chinees wall in my head, I did not look at that code it while writing mine.

The partial reason for writing code is that I don't like the library offered Alex Eames to drive InsPiRing hardware.

In particular, [RasPiO InsPiRing Python driver class and example scripts is licensed under CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) and the **except for commercial purposes.** part make it incompatible with the Free Software and Open Source definition.

This make it incompatible with other pieces of software that you may want to use together.
For that matter, MIT licence is compatible with most use, including with commercial use of the software.

## TODO

Better support for more than 8 LEDs kind of hardware from Alex Eames.
This require playing around with NUM_PIXEL and more testing.
