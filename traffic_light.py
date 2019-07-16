from gpiozero import LED,Button
import time
from signal import pause


red = LED(18)
yellow = LED(4)
green = LED(21)


red.on()
time.sleep(5)
red.off()
yellow.on()
time.sleep(5)
yellow.off()
green.on()
time.sleep(5)
green.off()