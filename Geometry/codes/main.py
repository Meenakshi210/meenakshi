import numpy as np

# Define the vertices of the triangle ABC
A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])

# Calculate direction vectors of sides AB, BC and CA
AB = B - A
BC = C - B
CA = A - C

# Calculate direction vectors of altitudes of AB and AC 
m_BE = np.array([-CA[1], CA[0]])  # Normal to AC
m_CF = np.array([-AB[1], AB[0]])  # Normal to AB

# Equations of the altitudes BE and CF in vector form
equation_BE = np.array([B, m_BE])
equation_CF = np.array([C, m_CF])


print("\nEquation of altitude BE in vector form:")
print("x =", equation_BE[0, 0], "+ t *", equation_BE[1, 0])
print("y =", equation_BE[0, 1], "+ t *", equation_BE[1, 1])

print("\nEquation of altitude CF in vector form:")
print("x =", equation_CF[0, 0], "+ t *", equation_CF[1, 0])
print("y =", equation_CF[0, 1], "+ t *", equation_CF[1, 1])



