import numpy as np
import matplotlib.pyplot as plt

# Define the vertices of the triangle ABC
A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])

# Calculate vectors representing sides AB, BC, and CA
AB = B - A
BC = C - B
CA = A - C

# Calculate direction vectors of altitudes of AB and AC
slope_BE = np.array([-CA[1], CA[0]])  # Perpendicular to AC
slope_CF = np.array([AB[1], -AB[0]])  # Perpendicular to AB

# Calculate the intersection points of altitudes BE and CF
BE_intersection = B + np.dot(CA, slope_BE) / np.dot(AB, slope_BE) * AB
CF_intersection = C + np.dot(AB, slope_CF) / np.dot(BC, slope_CF) * BC

# Generate points on the altitudes
t_values_BE = np.linspace(-5, 5, 50)  # range for BE
t_values_CF = np.linspace(-3, 3, 50)  # range for CF
BE_points = np.array([BE_intersection + t * slope_BE for t in t_values_BE])
CF_points = np.array([CF_intersection + t * slope_CF for t in t_values_CF])

# Create a figure and axis
fig, ax = plt.subplots()

# Set aspect ratio to 1:1
plt.gca().set_aspect('equal')

# Plot the triangle ABC
triangle_vertices = np.array([A, B, C, A])
plt.plot(triangle_vertices[:, 0], triangle_vertices[:, 1], marker='o', linestyle='-', color='b', label='Triangle ABC')

# Plot the shortened altitudes BE and CF
plt.plot(BE_points[:, 0], BE_points[:, 1], linestyle='--', color='r', label='Altitude BE')
plt.plot(CF_points[:, 0], CF_points[:, 1], linestyle='--', color='g', label='Altitude CF')

# Label the vertices A, B, and C
plt.text(A[0], A[1], 'A', fontsize=12, ha='right', va='bottom')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right', va='bottom')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right', va='bottom')

# Set labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangle ABC and Altitudes')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Show the plot
plt.show()

