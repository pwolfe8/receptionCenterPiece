# main.py
import machine
import time
import math

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

def pulse2(p1, p2, t):
    for i in range(20):
        p1.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        p2.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

def heartbeat(pinpwm, pulseCount):
    heartbeat_delay_ms = 250
    for c in range(pulseCount):
        pulse(pinpwm, 80)
        time.sleep_ms(heartbeat_delay_ms)

def heartbeat2(p1, p2, pulseCount):
    heartbeat_delay_ms = 250
    for c in range(pulseCount):
        pulse2(p1, p2, 80)
        time.sleep_ms(heartbeat_delay_ms)

def togglepin(p):
    if p.value() == 0:
        p.on()
    elif p.value() == 1:
        p.off()

def debounce(p):
    ''' debounces a pin for a button or similar '''
    window_length_ms = 100
    s = 0
    for i in range(window_length_ms):
        s += p.value()
        time.sleep_ms(1)
    return round(s/window_length_ms)

def servoButtonCallback(p):
    val = debounce(p)
    if val == 0:
        togglepin(servoLEDpin)
    
def timerCallback(t):
    togglepin(boardLEDpin)

# onboard LED setup
boardLEDpin = machine.Pin(2, machine.Pin.OUT)
boardLEDpin.off() # this turns on board LED since active low

# servo button, led, and pwm setup
servobutton = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
servobutton.irq(trigger=machine.Pin.IRQ_FALLING, handler=servoButtonCallback)

servoLEDpin = machine.Pin(13, machine.Pin.OUT)
servoLEDpin.off() # active high. start off though.

servopwm = machine.PWM(machine.Pin(5), freq=50) # GPIO5 is D1 on the mini

# servo timer loop setup
tim = machine.Timer(-1)
time.init(period=2000, mode=machine.Timer.PERIODIC, callback=timerCallback)


### heartbeat tests
# pulseCount = 25
## led heartbeat test
# ledpwm = machine.PWM(ledpin, freq=50)
# heartbeat(ledpwm, pulseCount)
## servo heartbeat
# heartbeat(servopwm, pulseCount)

# turn on to stop blocking webrepl with infinite loop
# use_webrepl = True
# if not use_webrepl:    
#     while True:
#         time.sleep_ms(100)
# end turn off system led and servo
# servopwm.duty(0)
# boardLEDpin.on()

