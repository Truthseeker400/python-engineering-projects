# -*- coding: utf-8 -*-
"""
A simple command-line tool to solve for Voltage, Current, or Resistance
using Ohm's Law (V = I * R).

This program demonstrates basic user input, functions, and error handling.
"""


def get_float_input(prompt: str) -> float:
    """
    Prompts the user for a number and ensures the input is a valid float.
    It will keep asking until valid input is received.

    Args:
        prompt: The message to display to the user.

    Returns:
        The user's input as a float.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_voltage():
    """Calculates voltage when current and resistance are known."""
    print("\n--- Calculate Voltage (V = I * R) ---")
    current = get_float_input("Enter current (in Amps): ")
    resistance = get_float_input("Enter resistance (in Ohms): ")
    voltage = current * resistance
    print(f"\n✅ Result: The voltage is {voltage:.2f} Volts.")


def calculate_current():
    """Calculates current when voltage and resistance are known."""
    print("\n--- Calculate Current (I = V / R) ---")
    voltage = get_float_input("Enter voltage (in Volts): ")
    resistance = get_float_input("Enter resistance (in Ohms): ")

    if resistance == 0:
        print("\n❌ Error: Resistance cannot be zero for this calculation (division by zero).")
        return

    current = voltage / resistance
    print(f"\n✅ Result: The current is {current:.2f} Amps.")


def calculate_resistance():
    """Calculates resistance when voltage and current are known."""
    print("\n--- Calculate Resistance (R = V / I) ---")
    voltage = get_float_input("Enter voltage (in Volts): ")
    current = get_float_input("Enter current (in Amps): ")

    if current == 0:
        print("\n❌ Error: Current cannot be zero for this calculation (division by zero).")
        return

    resistance = voltage / current
    print(f"\n✅ Result: The resistance is {resistance:.2f} Ohms.")


def main():
    """Main function to run the calculator."""
    print("===================================")
    print("   Ohm's Law Circuit Calculator    ")
    print("===================================")

    while True:
        print("\nWhat would you like to calculate?")
        print("  1. Voltage (V)")
        print("  2. Current (I)")
        print("  3. Resistance (R)")
        print("  4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            calculate_voltage()
        elif choice == '2':
            calculate_current()
        elif choice == '3':
            calculate_resistance()
        elif choice == '4':
            print("\nExiting calculator. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

        print("\n-----------------------------------")


if __name__ == "__main__":
    main()
