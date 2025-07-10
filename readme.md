# SimpleHub

Firmware for LEGO smart hubs to convert them into simple battery boxes.

## Modes

- Lights - Both light are powered to 100% brightness on hub start. The hub button toggles between the lights in port A and port B. This is useful for traffic lights or singular lights that can be toggled on and off.
- Train - The linear motor in port A is toggled between 0% and 40% power. If lights are present in port B, they are at 100% constant brightness.
- Motor - A motor with rotation sensor is controlled via the button. The motor is initially off. A press of the button will turn it on with a longer press providing faster speeds. Pressing the button when the motor is running will immediately stop it. A subsequent press will work as the first, but the motor direction will have changed. If lights are present in port B, they are at 100% constant brightness.

| Mode          | Port A           | Port B               | ⏹️ Button Press Function
| ------------- | ---------------- | -------------------- | ----------------------------
| 🚦 Lights     | 💡 Lights        | 💡 Lights (optional) | Toggle between A and B
| 🚂 Train      | 🚂 Linear Motor  | 💡 Lights (optional) | Toggle motor (0%/40%)
| 🏗  Motor      | 🏗  Technic Motor | 💡 Lights (optional) | Toggle motor speed/direction
