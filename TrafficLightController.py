# -*- coding: utf-8 -*-
"""
A Python script for controlling a traffic light sequence on a Raspberry Pi.

This program demonstrates:
- Controlling multiple GPIO outputs.
- Creating a specific, timed sequence of events.
- Using loops and functions for clean, readable code.

Hardware Required:
- 1x Red LED
- 1x Yellow LED
- 1x Green LED
- 3x 330 Ohm resistors
- Jumper wires
- A breadboard

Wiring:
- Connect GPIO 9 to the resistor for the Green LED.
- Connect GPIO 10 to the resistor for the Yellow LED.
- Connect GPIO 11 to the resistor for the Red LED.
- Connect the short leg (cathode) of all LEDs to a common Ground (GND) pin on the Pi.
"""

import RPi.GPIO as GPIO
import time

# --- Configuration ---
# Use BCM pin numbering (the numbers after "GPIO")
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the LEDs
PIN_RED = 11
PIN_YELLOW = 10
PIN_GREEN = 9

# Create a list of all LED pins for easier setup/cleanup
ALL_PINS = [PIN_RED, PIN_YELLOW, PIN_GREEN]

# --- Core Functions ---

def setup_pins():
    """Set up all our LED pins as outputs."""
    # GPIO.setup can take a list of pins, which is very convenient.
    GPIO.setup(ALL_PINS, GPIO.OUT)
    print("GPIO pins set up as outputs.")
    # Start with all lights off
    GPIO.output(ALL_PINS, GPIO.LOW)

def all_lights_off():
    """Turn all the LEDs off."""
    GPIO.output(ALL_PINS, GPIO.LOW)

def traffic_light_sequence():
    """Runs the main traffic light sequence loop."""
    print("Starting traffic light sequence... (Press Ctrl+C to stop)")
    while True:
        # --- GREEN ---
        print("Light: GREEN")
        GPIO.output(PIN_GREEN, GPIO.HIGH)
        time.sleep(5) # Green light on for 5 seconds

        # --- YELLOW ---
        print("Light: YELLOW")
        GPIO.output(PIN_GREEN, GPIO.LOW)
        GPIO.output(PIN_YELLOW, GPIO.HIGH)
        time.sleep(2) # Yellow light on for 2 seconds

        # --- RED ---
        print("Light: RED")
        GPIO.output(PIN_YELLOW, GPIO.LOW)
        GPIO.output(PIN_RED, GPIO.HIGH)
        time.sleep(5) # Red light on for 5 seconds

        # --- RED & YELLOW (Amber) before GREEN ---
        print("Light: RED + YELLOW")
        GPIO.output(PIN_YELLOW, GPIO.HIGH)
        time.sleep(2) # Red and Yellow on for 2 seconds

        # --- Back to GREEN ---
        all_lights_off() # Reset for the next loop

# --- Main Program Execution ---
if __name__ == "__main__":
    try:
        setup_pins()
        traffic_light_sequence()
    except KeyboardInterrupt:
        # This block runs when the user presses Ctrl+C
        print("\nProgram stopped by user.")
    finally:
        # This block runs no matter how the program ends
        print("Cleaning up GPIO pins.")
        GPIO.cleanup()
