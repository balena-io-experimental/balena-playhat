from __future__ import absolute_import

import time
import random
from neopixel import *

# LED strip configuration:
LED_COUNT = 9  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 40  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)

# Define list of Dice configurations
digits = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 0, 0, 0, 1, 0, 0, 0, 0],  # 1
    [1, 0, 0, 0, 0, 0, 0, 0, 1],  # 2
    [1, 0, 0, 0, 1, 0, 0, 0, 1],  # 3
    [1, 0, 1, 0, 0, 0, 1, 0, 1],  # 4
    [1, 0, 1, 0, 1, 0, 1, 0, 1],  # 5
    [1, 1, 1, 0, 0, 0, 1, 1, 1],  # 6
]


def clearStrip(strip):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, 0)
    strip.show()


def doDigit(strip, digit, colour):
    for i in range(9):
        if digits[digit][i] > 0:
            strip.setPixelColor(i, colour)
        else:
            strip.setPixelColor(i, 0)
    strip.show()


def main():
    strip = Adafruit_NeoPixel(
        LED_COUNT,
        LED_PIN,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS
    )
    strip.begin()

    try:
        while True:
            num = 0
            for i in range(1, 30):
                num = random.randrange(1, 7)
                doDigit(strip, num, Color(255, 0, 0))
                time.sleep(0.1)
            doDigit(strip, num, Color(0, 255, 0))
            time.sleep(3)

    except KeyboardInterrupt:
        print

    finally:
        clearStrip(strip)
