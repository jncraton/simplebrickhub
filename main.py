from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, Light
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from umath import sin, pi

hub = CityHub()

# Disable the stop button.
hub.system.set_stop_button(None)

# Animate hub light
hub.light.animate([Color.WHITE * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)

lightA = Light(Port.A)
lightB = Light(Port.B)

lightA.on(100)
lightB.on(100)

a_on = True

while True:
    if hub.buttons.pressed():
        if a_on:
            lightA.off()
            lightB.on(100)
        else:
            lightA.on(100)
            lightB.off()
        a_on = not a_on
        wait(200)
