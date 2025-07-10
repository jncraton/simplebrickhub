from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, Motor, Light
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from umath import sin, pi

hub = CityHub()

# Disable the stop button.
hub.system.set_stop_button(None)

# Animate hub light
hub.light.animate([Color.WHITE * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)

def try_train_mode():
    # Initialize the motor.
    try:
        train_motor = DCMotor(Port.A)
    except OSError:
        return # Not train mode

    # Turn on light if present
    try:
        light = Light(Port.B)
        light.on(100)
    except OSError:
        pass # Light no present

    toggle = False

    while True:
        if hub.buttons.pressed():
            toggle = not toggle
            if toggle:
                train_motor.dc(40)
            else:
                train_motor.stop()
            while hub.buttons.pressed(): pass

def try_motor_mode():
    # Initialize the motor
    try:
        motor = Motor(Port.A)
    except OSError:
        return # Not motor mode

    # Turn on light if present
    try:
        light = Light(Port.B)
        light.on(100)
    except OSError:
        pass # Light not present

    speed = 0

    while True:
        if hub.buttons.pressed():
            if speed != 0:
                speed = 0
                motor.stop()
                while hub.buttons.pressed(): pass
            else:
                speed = 50
                while hub.buttons.pressed():
                    motor.run(speed)
                    speed += 13
                    wait(50)

def try_lights_mode():
    try:
        lightA = Light(Port.A)
        lightA.on(100)
    except OSError:
        lightA = None

    try:
        lightB = Light(Port.B)
        lightB.on(100)
    except OSError:
        lightB = None

    a_on = True
    if not lightA:
        a_on = False

    while True:
        if hub.buttons.pressed():
            if a_on:
                if lightA: lightA.off()
                if lightB: lightB.on(100)
            else:
                if lightA: lightA.on(100)
                if lightB: lightB.off()
            a_on = not a_on
            while hub.buttons.pressed(): pass

try_train_mode()
try_motor_mode()
try_lights_mode()
