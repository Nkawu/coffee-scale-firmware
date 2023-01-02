"""Calibrate HX711 on ESP32"""
from hx711 import HX711

hx = HX711(dout = 14, pd_sck = 13, gain = 64)
hx.set_scale(0)
hx.tare()

while True:
    print(hx.read_average(times = 100))
