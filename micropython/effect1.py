
from machine import Pin, PWM
from time import sleep

# PWM configuration
FREQ = 1000

# Star configuration: (Red GPIO, Green GPIO)
center = (
    PWM(Pin(4), freq=FREQ),
    PWM(Pin(5), freq=FREQ)
)

middle = (
    PWM(Pin(2), freq=FREQ),
    PWM(Pin(3), freq=FREQ)
)

outer = (
    PWM(Pin(0), freq=FREQ),
    PWM(Pin(1), freq=FREQ)
)

stars = [center, middle, outer]

# Set brightness of one star (0-100%)
def set_star(star, red, green):
    star[0].duty_u16(int(red * 65535 / 100))
    star[1].duty_u16(int(green * 65535 / 100))

def all_off():
    for star in stars:
        set_star(star, 0, 0)

def fade(star, red, green, duration=0.4):
    steps = 40
    for i in range(steps + 1):
        level = i / steps
        set_star(star, red * level, green * level)
        sleep(duration / steps)

def wave():
    all_off()

    # Center -> Middle -> Outer
    for star in stars:
        fade(star, 100, 0)
        sleep(0.1)

    # Outer -> Middle -> Center
    for star in reversed(stars):
        fade(star, 0, 100)
        sleep(0.1)

    # All stars glow yellow
    for star in stars:
        set_star(star, 100, 100)

    sleep(0.5)

    all_off()
    sleep(0.3)

while True:
    wave()
