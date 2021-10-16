# A Quick D1 Mini Micropython Setup/Tutorial

Just my quick reference/cheat sheet for D1 Mini board resources and setting up micropython for updating main.py remotely

## Purchase Source
bought 10 off amazon at ~3 dollars a piece [here](<https://www.amazon.com/dp/B08QZ2887K?psc=1&ref=ppx_yo2_dt_b_product_details>)

## supposed schematic and potential pinout
- https://www.wemos.cc/en/latest/_static/files/sch_d1_mini_v3.0.0.pdf
- https://www.wemos.cc/en/latest/d1/d1_mini.html
- https://escapequotes.net/esp8266-wemos-d1-mini-pins-and-diagram/


## Flashing ESP8266 with Latest Micropython
[tutorial source](<https://www.wemos.cc/en/latest/tutorials/d1/get_started_with_micropython_d1.html>)

Find the latest micropython .bin file in the >4MB flash section and download it [here](<https://micropython.org/download/esp8266/>)
install esptool on your python with `pip install esptool` (github [here](<https://github.com/espressif/esptool>) if you want)

Plug in device via USB and check the port name in device manager (example: COM6)
Now swap PORT_NAME with your port and FIRMWARE.bin with the .bin file you just downloaded in the following commands:
```bash
# first erase flash
esptool.py --port PORT_NAME erase_flash

# then write flash with your preferred firmware .bin file 
esptool.py --port PORT_NAME --baud 115200 write_flash --flash_size=4MB -fm dio 0 FIRMWARE.bin

# here's the example command I used in powershell for the version in this repo. it assumes you're already in the software folder and COM6 is your device serial port
esptool.py --port COM6 --baud 115200 write_flash --flash_size=4MB -fm dio 0 .\esp8266-20210902-v1.17.bin
```

Open [realterm](https://sourceforge.net/projects/realterm/) and set baud to 115200 and open your port. you should be able to type help() and follow the first steps now

## First Steps
```python
# this is how to get help
help()

# this sets up a remote accessible micropython shell
# follow prompts after import to enable webrepl on boot (feel free to reboot)
import webrepl_setup

# this is how to check what files exist on the board
import os
os.listdir()
```

## Network Config
[tutorial source](<https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html>)
```python
# turn on client connection and turn off access point
import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active(True)
ap_if.active(False)

# check to be sure they're on/off
sta_if.active()
ap_if.active()

# get mac address
import ubinascii
ubinascii.hexlify(sta_if.config('mac'),':').decode()

# connect to your router's SSID with password now 
sta_if.connect('ssidgoeshere','passwordgoeshere')
# keep checking for a minute until connected
sta_if.isconnected()
# see ip address & network info
sta_if.ifconfig()
```

## webrepl push/pull
```bash
# update submodule
git submodule update --init --recursive
cd webrepl

# for getting help
python webrepl_cli.py --help 

# example pull (just pulls the boot.py from remote and saves to local file named "local_boot.py")
python .\webrepl_cli.py -p YOURPASSWORDHERE REMOTEIPHERE:boot.py local_boot.py

# example push (just pushes your local file main.py file located one directory above the cloned webrepl folder to your board and names it main.py)
python .\webrepl_cli.py -p YOURPASSWORDHERE ../main.py REMOTEIPHERE:main.py

# feel free to setup batch/bash scripts for your common operations
```

## `main.py` 
micropython executes main.py (if it exists) after boot.py so I generally put my code updates here.
Let's setup an example main.py to turn on the onboard LED. It's connected to GPIO2 according to the D1 Mini Schematic in an active pull down configuration.

Here's an example main.py to turn the LED on on boot

```python
import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin.off()
```

If you want to change the syntax so "on" turns led on use [this documentation](<https://docs.micropython.org/en/latest/library/machine.Signal.html>)

Now use the example push as reference to push this `main.py` file to your board:
```bash
python .\webrepl_cli.py -p YOURPASSWORDHERE ../main.py REMOTEIPHERE:main.py
```

To reset your board to let the main.py changes take effect:
- open the webrepl/webrepl.html file in your browser, connect to your W1 Mini's ip address
- type
    ```python
    import machine
    machine.reset()
    ```







Feel free to modify this main.py to your heart's content and push updates/pull current files.
Happy Hacking

