# DIY Smart Coffee and Espresso Scale

This is a modified version of the amazing project by **Valentin Bersier**, original repo at https://github.com/beeb/coffee-scale-app. This repo only contains the firmware for the **ESP32 microcontroller**, go to the original repo for the rest of the software.

## Documentation
Refer to the [Wiki](https://github.com/Nkawu/coffee-scale-firmware/wiki) for detailed instructions on how to install this firmware on your scale

## Modification details
For this version of the scale, the 3D printed housing was completely redesigned to fit on a Breville Dual Boiler espresso machine. The 3D printable parts are available from [Printables - Bluetooth Espresso Scale ESP32 Feather based](https://www.printables.com/model/213101-bluetooth-espresso-scale-esp32-feather-based)

An ESP32-based **Feather** microcontroller board is used in place of the **ESP32 Thing** of the original. This board is available from [EzSBC.com](https://www.ezsbc.com/product/esp32-feather/) and vastly reduces the original Adafruit Feather's high deepsleep current draw of 160mA (IIRC) down to 10uA.

The power switch is removed from the housing to free up space in the scale body, and now uses the ESP32 deepsleep mode instead to preserve battery life. An additional button is added to the front panel, with both buttons activating tactile switches mounted inside the body. Holding the left button down > 1sec puts the ESP32 into deepsleep mode. The right button wakes the ESP32 from deepsleep, and while powered on tares/resets the scale. Both buttons use internal pull-up/down resistors in the ESP32, so no extra components are required.

The `firmware` folder contains the `.py` files that need to be uploaded into the root of the ESP32 running the [MicroPython](https://micropython.org/) interpreter.

## Modified Espresso Workflow

- Power on the scale by pressing the right button. It should take a few seconds to start up and enable the display.
- Place a measuring cup on the scale and tare with the right button.
- Place the desired amount of coffee beans into the measuring cup.
- Grind the beans in your grinder.
- Place the empty portafiler on the scale and tare. If you grind directly into the portafilter, do this before grinding the beans.
- Place the portafilter filled with ground coffee back on the portafilter, adjust the required coffee dose, e.g. 18g
- Connect to the [Scale Web App](http://beeb.li/coffee) on your phone or tablet as prompted. If it's an Apple device, you may need to use [Bluefy – Web BLE Browser](https://apps.apple.com/us/app/bluefy-web-ble-browser/id1492822055).
- Enter the parameters for your shot in the app:
  - My espresso machine has automatic pre-infusion, so I just set `Pre-infusion time` to 0 and `Total time` to my required shot time.
  - The "Read" button next to the "Coffee Weight" input can be clicked to read the current scale value into it.
- Place a cup on the scale and tare with the right button
- Press the "Start recording" button (only available when the scale reads ~0g). The app now waits for an increase in weight.
- Start the shot extraction on your espresso machine.
- As soon as the weight exceeds 0.5g, the timer starts counting from the pre-infusion time (default 5s).
- The extraction can be followed in real time and should match the grey reference curve.
- Stop the shot extraction when the required extracted coffee weight is shown on the scale.
- Lift the cup from the scale to stop the recording.

## License

Distributed under the MIT License
