from machine import UART, Pin, PWM
import time

# Setup UART (HC-08 uses 9600 by default)
uart = UART(1, baudrate=9600, tx=Pin(8,  Pin.OUT), rx=Pin(9, Pin.IN, Pin.PULL_UP), bits=8, parity=None, stop=1)

# Setup servo on GPIO15
servo = PWM(Pin(15))
servo.freq(50)

# Helper function to set servo angle (0 to 180)
def set_servo_angle(angle):
    # 0.5ms to 2.5ms pulse width, converted to duty for 16-bit PWM
    min_duty = int(1638)  # ~0.5ms
    max_duty = int(8192)  # ~2.5ms
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty_u16(duty)
    
uart.write("hello world")

# Main loop
while True:
    if uart.any():
        command = uart.read(1)  # Read one byte
        uart.write(command)
        if command == b'a':
            print("Turning 180° counter-clockwise")
            set_servo_angle(0)  # Adjust if your 0° is not CCW
            time.sleep(1)
        elif command == b'f':
            print("Turning 180° clockwise")
            set_servo_angle(180)
            time.sleep(1)
