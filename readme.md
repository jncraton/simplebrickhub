# SimpleHub

Firmware for LEGO smart hubs to convert them into simple battery boxes.

## Modes

- Lights - The hub button toggles between the lights in port A and port B. Lights are always at 100% brightness. This is useful for traffic lights or singular lights that can be toggled on and off.
- Train - The linear motor in port A is toggled between 0% and 40% power. If lights are present in port B, they are at 100% constant brightness.

Mode         Port A         Port B
------------ -------------- -----------------
Lights       Lights         Lights (optional)
Train        Linear Motor   Lights (optional)
