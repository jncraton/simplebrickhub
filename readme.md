# SimpleHub

Firmware for LEGO smart hubs to convert them into simple battery boxes.

## Overview

There are [a number of hubs](https://rebrickable.com/parts/?get_drill_downs=&tag=&min_year=2015&max_year=2025&min_part_cost=0&max_part_cost=20&q=Powered%20up%20hub&part_cat=45&exists_in_color=) available for powering LEGO models using [Powered Up motors](https://rebrickable.com/parts/?get_drill_downs=&tag=&min_year=2015&max_year=2025&min_part_cost=0&max_part_cost=20&q=Powered%20up%20motor&part_cat=45&exists_in_color=). Most of these are smart hubs that require a connection to a smart device either for direct control or for programming. There is [one non-Bluetooth hub](https://rebrickable.com/parts/85825/hub-powered-up-2-port-non-bluetooth-screw-opening/), but it may not make sense to purchase this separately if you already have a smart hub from something like a train set.

This project provides [firmware](main.py) that can be written to a [City Hub](https://rebrickable.com/parts/28738/hub-battery-box-powered-up/) using [PyBricks](https://pybricks.com) to convert it to something like the non-Bluetooth hub until it is reflashed with a new PyBricks program or the original firmware from LEGO.

## Modes

Different interface modes are used depending on what device is plugged into port A of the hub when it is turned on.

- Lights - Any connected lights are powered to 100% brightness on hub start. The hub button toggles between the lights in port A and port B. This is useful for traffic lights or singular lights that can be toggled on and off.
- Train Motor - The linear motor in port A is toggled between 0% and 40% power. If lights are present in port B, they are at 100% constant brightness.
- Technic Motor - A motor with rotation sensor is controlled via the button. The motor is initially off. A press of the button will turn it on with a longer press providing faster speeds. Pressing the button when the motor is running will immediately stop it. A subsequent press will work as the first, but the motor direction will alternate. If lights are present in port B, they are at 100% constant brightness.

| Mode          | Port A           | Port B               | ⏹️ Button Press Function
| ------------- | ---------------- | -------------------- | ----------------------------
| 🚦 Lights     | 💡 Lights        | 💡 Lights (optional) | Toggle between A and B
| 🚂 Train      | 🚂 Linear Motor  | 💡 Lights (optional) | Toggle motor (0%/40%)
| 🏗  Motor      | 🏗  Technic Motor | 💡 Lights (optional) | Toggle motor speed/direction

## Auto Shut-off

The hub will shut itself off after 30 minutes of inactivity to preserve battery life and prevent wear and tear.