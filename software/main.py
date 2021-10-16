# main.py
import machine
import time
import math

servoState = False
servoPulseIdx = 0
threeCountWait = 0

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

def heartbeat(pinpwm, pulseCount):
    heartbeat_delay_ms = 250
    for c in range(pulseCount):
        pulse(pinpwm, 80)
        time.sleep_ms(heartbeat_delay_ms)

def togglepin(p):
    if p.value() == 0:
        p.on()
    elif p.value() == 1:
        p.off()

def debounce(p):
    '''debounce a button pin'''
    window_length_ms = 100
    s = 0
    for i in range(window_length_ms):
        s += p.value()
        time.sleep_ms(1)
    return round(s/window_length_ms)

# def toggleServo():
#     global servoState
#     servoState = not servoState
#     if servoState:
#         servoLEDpin.on()
#     else:
#         servoLEDpin.off()

# def servoButtonCallback(p):
#     val = debounce(p)
#     if val == 0:
#         toggleServo()

def runServoHeartbeat():
    global servoPulseIdx
    global threeCountWait
    if servoPulseIdx >= 20:
        threeCountWait += 1
        # servopwm.duty(0)
        if threeCountWait >= 3:
            threeCountWait = 0
            servoPulseIdx = 0
    else:
        servopwm.duty(int(math.sin(servoPulseIdx / 10 * math.pi) * 500 + 500))
        servoPulseIdx += 1

def blockingHeartbeat():
    pulse(servopwm, 80)

def timerCallback(t):
    blockingHeartbeat()

# onboard LED setup
boardLEDpin = machine.Pin(2, machine.Pin.OUT)
boardLEDpin.off() # this turns on board LED since active low

# servo button, led, and pwm setup
# servobutton = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
# servobutton.irq(trigger=machine.Pin.IRQ_FALLING, handler=servoButtonCallback)
# servoLEDpin = machine.Pin(13, machine.Pin.OUT)
# servoLEDpin.off() # active high. start off though.
servopwm = machine.PWM(machine.Pin(5), freq=50) # GPIO5 is D1 on the mini

# servo timer loop setup
servoLoopPeriod_ms = 1850
servoTimer = machine.Timer(-1)
servoTimer.init(period=servoLoopPeriod_ms, mode=machine.Timer.PERIODIC, callback=timerCallback)

### heartbeat tests ###
# pulseCount = 25
## led heartbeat test
# ledpwm = machine.PWM(ledpin, freq=50)
# heartbeat(ledpwm, pulseCount)
## servo heartbeat
# block_webrepl = True
# while True and block_webrepl:
#     heartbeat(servopwm, 25)

## socket server backdoor testing
# import socket 
# import sys 
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind('10.160.0.105', 6969)
# while True:
#     data, addr = s.recvfrom(1024)
#     if data == b'hello there':
#         jamSignal = True
#         togglepin(boardLEDpin)
#         time.sleep(2)
#     data = ''
