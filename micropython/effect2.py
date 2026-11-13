
from machine import Pin, PWM
from time import sleep
import math

center = [PWM(Pin(4), freq=1000),
          PWM(Pin(5), freq=1000)]

middle = [PWM(Pin(2), freq=1000),
          PWM(Pin(3), freq=1000)]

outer = [PWM(Pin(0), freq=1000),
         PWM(Pin(1), freq=1000)]

stars = [center, middle, outer]

def brightness(star, red, green):
    star[0].duty_u16(int(red * 65535 / 100))
    star[1].duty_u16(int(green * 65535 / 100))

t = 0

while True:
    # Smooth breathing using sine wave
    b1 = (math.sin(t * 0.06) + 1) / 2
    b2 = (math.sin(t * 0.04 + 2) + 1) / 2
    b3 = (math.sin(t * 0.03 + 4) + 1) / 2

    # Center: red
    brightness(center, 100 * b1, 0)

    # Middle: green
    brightness(middle, 0, 100 * b2)

    # Outer: yellow
    brightness(outer, 100 * b3, 100 * b3)

    t += 1
    sleep(0.03)
