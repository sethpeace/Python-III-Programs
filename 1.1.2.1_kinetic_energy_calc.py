# Seth Peace
# Sample Python/Pygame Programs Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

# Calculate Kinetic Energy
print("This program calculates the kinetic energy of a moving object.")
m_String = input("Enter the object's mass in kilograms: ")
m = float(m_String)
v_String = input("Enter the object's speed in meters per second: ")
v = float(v_String)
e = 0.5 * m * v**2
print("The object has " + str(e) + " joules of energy.")