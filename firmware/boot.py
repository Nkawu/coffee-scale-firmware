# uncomment to setup WiFi connection

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        # Enter WiFi parameters here
        wlan.connect('*SSID*', '*PASSWORD*')
        while not wlan.isconnected():
            pass
    print('Network config:', wlan.ifconfig())

do_connect()
