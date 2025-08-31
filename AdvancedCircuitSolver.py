# -*- coding: utf-8 -*-
"""
To run the code, save it and execute it from the terminal with:
python circuit_solver_v2.py

This version effectively gamifies revision. He can check his own
homework answers or quickly experiment with different combinations
of resistors to see how they affect the total resistance, building
a stronger intuition for the concepts. A great next step from here
would be to create a function that can solve a combination circuit (e.g., two resistors in parallel that are in series with a third).
An advanced command-line tool to solve for basic circuit properties.

Features:
- Calculates Voltage, Current, or Resistance using Ohm's Law (V = I * R).
- Calculates the total resistance of multiple resistors in series.
- Calculates the total resistance of multiple resistors in parallel.

This program builds on the previous version by introducing list handling,
more complex calculations, and sub-menus.
"""


# --- Input Helper Functions ---

def get_float_input(prompt: str) -> float:
    """
    Prompts the user for a single number and ensures the input is a valid float.
    It will keep asking until valid input is received.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  Invalid input. Please enter a valid number.")


def get_multiple_float_inputs(prompt: str) -> list[float]:
    """
    Prompts the user for multiple numbers separated by spaces and returns them as a list of floats.
    """
    while True:
        try:
            user_input = input(prompt)
            # Split the input string by spaces and convert each part to a float
            values = [float(val) for val in user_input.split()]
            if not values:
                print("  Please enter at least one value.")
                continue
            # Ensure no negative resistance values, which are not physically possible here.
            if any(v < 0 for v in values):
                print("  Invalid input. Resistance values cannot be negative.")
                continue
            return values
        except ValueError:
            print("  Invalid input. Please ensure you enter only numbers separated by spaces.")


# --- Calculation Functions ---

def calculate_voltage():
    """Calculates voltage from current and resistance."""
    print("\n--- Calculate Voltage (V = I * R) ---")
    current = get_float_input("Enter current (in Amps): ")
    resistance = get_float_input("Enter resistance (in Ohms): ")
    voltage = current * resistance
    print(f"\n✅ Result: The voltage is {voltage:.2f} Volts.")


def calculate_current():
    """Calculates current from voltage and resistance."""
    print("\n--- Calculate Current (I = V / R) ---")
    voltage = get_float_input("Enter voltage (in Volts): ")
    resistance = get_float_input("Enter resistance (in Ohms): ")
    if resistance == 0:
        print("\n❌ Error: Resistance cannot be zero for this calculation (division by zero).")
        return
    current = voltage / resistance
    print(f"\n✅ Result: The current is {current:.2f} Amps.")


def calculate_resistance():
    """Calculates resistance from voltage and current."""
    print("\n--- Calculate Resistance (R = V / I) ---")
    voltage = get_float_input("Enter voltage (in Volts): ")
    current = get_float_input("Enter current (in Amps): ")
    if current == 0:
        print("\n❌ Error: Current cannot be zero for this calculation (division by zero).")
        return
    resistance = voltage / current
    print(f"\n✅ Result: The resistance is {resistance:.2f} Ohms.")


def calculate_series_resistance():
    """Calculates total resistance for resistors in series."""
    print("\n--- Calculate Total Resistance in Series (R_total = R1 + R2 + ...) ---")
    resistors = get_multiple_float_inputs("Enter resistor values in Ohms, separated by spaces: ")
    # The total resistance in series is the sum of all individual resistances.
    total_resistance = sum(resistors)
    print(f"\n✅ Result: The total series resistance is {total_resistance:.2f} Ohms.")


def calculate_parallel_resistance():
    """Calculates total resistance for resistors in parallel."""
    print("\n--- Calculate Total Resistance in Parallel (1/R_total = 1/R1 + 1/R2 + ...) ---")
    resistors = get_multiple_float_inputs("Enter resistor values in Ohms, separated by spaces: ")
    # Check for a zero-ohm resistor, which would short the circuit.
    if 0 in resistors:
        # The total resistance in parallel with a short circuit (0 Ohms) is 0 Ohms.
        total_resistance = 0
    else:
        # Calculate the sum of the reciprocals (1/R) for each resistor.
        sum_of_reciprocals = sum(1 / r for r in resistors)
        # The total resistance is the reciprocal of that sum.
        total_resistance = 1 / sum_of_reciprocals
    print(f"\n✅ Result: The total parallel resistance is {total_resistance:.2f} Ohms.")


# --- Main Application Logic ---

def resistance_submenu():
    """Displays the menu for resistance calculations."""
    while True:
        print("\n  Calculate Total Resistance:")
        print("    1. Resistors in Series")
        print("    2. Resistors in Parallel")
        print("    3. Back to Main Menu")
        choice = input("  Enter your choice (1-3): ")

        if choice == '1':
            calculate_series_resistance()
            break
        elif choice == '2':
            calculate_parallel_resistance()
            break
        elif choice == '3':
            return
        else:
            print("\n  Invalid choice. Please select an option from the menu.")


def main():
    """Main function to run the calculator."""
    print("===================================")
    print("    Advanced Circuit Calculator    ")
    print("===================================")

    while True:
        print("\nWhat would you like to calculate?")
        print("  1. Voltage (from I and R)")
        print("  2. Current (from V and R)")
        print("  3. Resistance (from V and I)")
        print("  4. Total Resistance (Series/Parallel)")
        print("  5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            calculate_voltage()
        elif choice == '2':
            calculate_current()
        elif choice == '3':
            calculate_resistance()
        elif choice == '4':
            resistance_submenu()
        elif choice == '5':
            print("\nExiting calculator. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

        print("\n-----------------------------------")


if __name__ == "__main__":
    main()
