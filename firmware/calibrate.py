"""Calibrate HX711 on ESP32"""
from hx711 import HX711
from machine import Pin
from debounce import DebouncedSwitch
from micropython import const
import time

_HX711_DOUT = const(14)
_HX711_SCK  = const(13)
_XH711_GAIN = const(64)
_RESET_BUTTON_PIN = const(15) # short press to tare scale
_SLEEP_BUTTON_PIN = const(27) # press 1s to deepsleep, short press to wake
_SAMPLES = const(10)
_TEST_WEIGHT = 100 # grams

# buttons
left_button = Pin(_SLEEP_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)
right_button = Pin(_RESET_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

### callback functions ###

def left_callback(arg):
    global scale_factor
    scale_factor -= 1
    print("Decrease sscale factor to {}".format(scale_factor))
    hx.set_scale(scale_factor)

def right_callback(arg):
    global scale_factor
    scale_factor += 1
    print("Increase sscale factor to {}".format(scale_factor))
    hx.set_scale(scale_factor)

### interrupts ###

left_sw = DebouncedSwitch(sw=left_button, cb=left_callback)
right_sw = DebouncedSwitch(sw=right_button, cb=right_callback)

# hx711 load cell amp
hx = HX711(dout = _HX711_DOUT, pd_sck = _HX711_SCK, gain = _XH711_GAIN)
hx.set_scale(0)
hx.tare()

## START ##

def wait_dot(n=5):
    for i in range(n):
        print("{}".format(n-i), end='')
        time.sleep(1)
    else:
        print("\n")

# first get 10 readings with scale empty
print("***** Remove weight")
wait_dot(5)

empty_total = 0
for i in range(_SAMPLES):
    empty_read = hx.read_average(times = 100)
    print(">>> Empty reading [{}]: {}".format(i+1, empty_read))
    empty_total += empty_read
else:
    print("\n*** Empty average: {}".format(empty_total / _SAMPLES))

# now get 10 readings with 100g weight on scale
print("\n*** Place 100g weight")
wait_dot(5)

wt_total = 0
for i in range(_SAMPLES):
    wt_read = hx.read_average(times = 100)
    print(">>> {}g reading [{}]: {}".format(_TEST_WEIGHT, i+1, wt_read))
    wt_total += wt_read
else:
    print("\n*** {}g average: {}".format(_TEST_WEIGHT, wt_total / _SAMPLES))

# remove weight
print("\n*** Remove weight")
wait_dot(5)

# set scale factor
scale_factor = (wt_total - empty_total) / _SAMPLES / _TEST_WEIGHT
hx.set_scale(scale_factor)
hx.tare()
print("\n*** Calculated sscale factor is {}".format(scale_factor))
wait_dot(5)

print("\n*** Replace 100g weight: L- R+ buttons adjust sscale factor")
wait_dot(5)

while True:
    # read weight
    print("\n>>> Measured weight is {}g".format(hx.get_units(5)))
    time.sleep(3)
