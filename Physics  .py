 physics.py
# COS 101 Assignment: 5 Physics Formulas

def calculate_force(mass, acceleration):
    """Formula 1: Force (F = m * a)"""
    return mass * acceleration

def calculate_kinetic_energy(mass, velocity):
    """Formula 2: Kinetic Energy (KE = 0.5 * m * v^2)"""
    return 0.5 * mass * (velocity ** 2)

def calculate_potential_energy(mass, height, gravity=9.8):
    """Formula 3: Potential Energy (PE = m * g * h)"""
    return mass * gravity * height

def calculate_velocity(distance, time):
    """Formula 4: Velocity (v = d / t)"""
    if time == 0:
        return "Time cannot be zero"
    return distance / time

def calculate_ohms_law(current, resistance):
    """Formula 5: Voltage (V = I * R)"""
    return current * resistance

# Example test prints to show it works
if __name__ == "__main__":
    print("--- Physics Formula Calculator Test ---")
    print(f"Force (Mass=10kg, Acc=2m/s²): {calculate_force(10, 2)} N")
    print(f"Kinetic Energy (Mass=5kg, Vel=4m/s): {calculate_kinetic_energy(5, 4)} J")
    print(f"Potential Energy (Mass=2kg, Height=5m): {calculate_potential_energy(2, 5)} J")
    print(f"Velocity (Distance=100m, Time=20s): {calculate_velocity(100, 20)} m/s")
    print(f"Voltage (Current=2A, Resistance=5Ω): {calculate_ohms_law(2, 5)} V")
