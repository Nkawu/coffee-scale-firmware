import network
import esp

# station interface is not active by default
def connect_sta():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print('Connecting to network...')
        # Enter WiFi parameters here
        sta_if.connect('*SSID*', '*PASSWORD*')
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())

# access point interface is enabled by default
def disable_ap():
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)

esp.osdebug(None)
disable_ap()

# Uncomment the following line to setup WiFi connection
# connect_sta()
