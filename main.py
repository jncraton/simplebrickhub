from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, Light
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from umath import sin, pi

hub = CityHub()

# Animate hub light
hub.light.animate([Color.WHITE * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)

wait(10000)