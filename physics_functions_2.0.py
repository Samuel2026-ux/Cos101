def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def kinetic_energy():
    mass = get_number("Enter mass (in Kg): ")
    velocity = get_number("Enter velocity (in m/s): ")
    print("Kinetic Energy =", 0.5 * mass * velocity ** 2, "J")


def momentum():
    mass = get_number("Enter mass (in Kg): ")
    velocity = get_number("Enter velocity (in m/s): ")
    print("Momentum =", mass * velocity, "Kg·m/s")


def density():
    mass = get_number("Enter mass (in Kg): ")
    volume = get_number("Enter volume (in m³): ")
    if volume == 0:
        print("Volume cannot be zero.")
    else:
        print("Density =", mass / volume, "Kg/m³")


def power():
    work = get_number("Enter work (in J): ")
    time = get_number("Enter time (in seconds): ")
    if time == 0:
        print("Time cannot be zero.")
    else:
        print("Power =", work / time, "W")


def acceleration():
    initial = get_number("Enter initial velocity (in m/s): ")
    final = get_number("Enter final velocity (in m/s): ")
    time = get_number("Enter time (in seconds): ")
    if time == 0:
        print("Time cannot be zero.")
    else:
        print("Acceleration =", (final - initial) / time, "m/s²")


operations = {
    "A": kinetic_energy,
    "B": momentum,
    "C": density,
    "D": power,
    "E": acceleration,
}


def show_menu():
    print("\nSelect a Physics formula")
    print("A. Kinetic Energy (KE = 0.5 * m * v²)")
    print("B. Momentum (p = m * v)")
    print("C. Density (ρ = m / V)")
    print("D. Power (P = W / t)")
    print("E. Acceleration (a = (v - u) / t)")


while True:
    show_menu()
    user_choice = input("Enter a letter A-E: ").strip().upper()

    if user_choice in operations:
        operations[user_choice]()
    else:
        print("Invalid choice. Please choose from A to E.")
        continue

    again = input("\nDo you want to run another operation? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break
