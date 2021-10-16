# Reception Center Piece
This was the planetary gear center piece that I designed & implemented for my reception. 

This repo is a way to share design files and provide an assembly tutorial for those who want to use this for their own reception, fork off the design, or just print their own copy of this cool decoration piece. 

## Clone this repository
Open a terminal wherever you want to place this folder. Then clone this repository and the webrepl submodule with:
```bash
git clone https://github.com/pwolfe8/receptionCenterPiece
cd receptionCenterPiece
git submodule update --init --recursive
```
___
## Mechanical
I printed this on a Prusa i3 MK3S. The trays and all the settings are in the `print_trays` folder.
I printed with [standard 1.75mm black PETG filament](<https://www.amazon.com/dp/B08XGX23TP?psc=1&ref=ppx_yo2_dt_b_product_details>) on a textured prusa print tray. 

Design files can be found on Onshape: 
- [fullDesignReception](<https://cad.onshape.com/documents/7be5b9b09e066ba446a30efc/w/afbadb4d389ea6207fcba0bc/e/a346c253faa0d5286ebe5b9c?renderMode=0&uiState=616b083ecb150f63125368d4>)
- [AA_3V_Boost5V](<https://cad.onshape.com/documents/a1963687730519ec8fcaa736/w/4932db5a468bc2b8e7c12e8f/e/31f6f86f6f40c3d5acde4a41?renderMode=0&uiState=616b1a22ca3c791168b4c31e>)

## Painting & Decoration
I did not do the painting/decoration my wife and her sister did. But the premise was paint a thin copper layer leaving some black showing underneath to look like worn copper for more of a steampunk feel. 
DO NOT print the smooth interface between the ring gear and the sun/planetary gears as it will add too much friction to move easily. 

Here's a quick DO NOT paint list: 
- bottom of planetary gears
- bottom of sun gear
- part of ring gear touching the bottom of the planetary/sun gears
- the base drive gear & anything used to hold it in place as it's hidden underneath anyways
- the servo horn attachment (it's hidden as well)

## Electrical

Wanted to try out micropython so I got these [D1 Mini modules](<https://www.amazon.com/dp/B08QZ2887K?psc=1&ref=ppx_yo2_dt_b_product_details>) based on the ESP8266 and flashed them with the latest version. They averaged 3 dollars each at the time I purchased them. 

If you just care about You can use any microcontroller and make your own electronics box for it as long as
- powerable off 5V since that's what the boost converter output is. (and servo needs 5V pwr). though you could power off 3V directly from battery if you modify the circuit
- has a pwm pin to drive servo

Anyways here's the parts list to make a single center piece: 
- 1x [microcontroller](<https://www.amazon.com/dp/B08QZ2887K?psc=1&ref=ppx_yo2_dt_b_product_details>) (D1 mini)
- 1x [micro servo](<https://www.amazon.com/dp/B07L2SF3R4?psc=1&ref=ppx_yo2_dt_b_product_details>) (modified for continuous rotation. you can just buy one that's continuous to make your life easier. only slightly pricier though. In the improved version I will make it based off of a continuous one.)
- 1x [5V 1A boost converter](<https://www.adafruit.com/product/4654>)(adafruit/digikey): This might've been more current than needed, but was better to be safe for a rapid prototype)
- 1x [mechanical switch](<https://www.adafruit.com/product/3221>)(adafruit): just a cool clickly mechanical switch
- 2x [battery contact positive](<https://www.digikey.com/en/products/detail/mpd-memory-protection-devices/SN-T5-2/2439587>)(digikey)
- 2x [battery contact negative](<https://www.digikey.com/en/products/detail/mpd-memory-protection-devices/SN-T5-1/2439583>)(digikey)

and here's the schematic: 
![circuit_schematic](schematic.png)

### Servo Modification for Continuous Rotation



## Firmware/Software
I'll put flashing instructions here along with the main.py I used. Also talk about setting up over the air updates.

___
## Assembly
Once you have all the pieces printed, follow this guide on assembly.

### Platforms
### 