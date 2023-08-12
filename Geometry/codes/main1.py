import numpy as np
import matplotlib.pyplot as plt

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

# intersection point of BE and CA
BE_p = B
BE_m = m_BE
AC_p = np.array([1, -1])
AC_m = np.array([4, 4])

sp_p1 = AC_p - BE_p
det1 = np.cross(BE_m, AC_m)
t1 = np.cross(sp_p1, AC_m)/ det1
E = BE_p + t1*BE_m
print("E = ",E)

# intersection point of CF and AB
CF_p = C
CF_m = m_CF
AB_p = np.array([1, -1])
AB_m = np.array([5, -7])

sp_p2 = AB_p - CF_p
det2 = np.cross(CF_m, AB_m)
t2 = np.cross(sp_p2, AB_m)/ det2
F = CF_p + t2*CF_m
print("F = ",F)

# Create a figure and axis
fig, ax = plt.subplots()

# Set aspect ratio to 1:1
plt.gca().set_aspect('equal')

# Plot the triangle ABC
triangle_vertices = np.array([A, B, C, A])
plt.plot(triangle_vertices[:, 0], triangle_vertices[:, 1], marker='o', linestyle='-', color='b', label='Triangle ABC')

# Plot the extended lines AC and AB
plt.plot([A[0], E[0]],[A[1], E[1]], linestyle=':', color='b', label='Extended AC')
plt.plot([A[0], F[0]],[A[1], F[1]], linestyle=':', color='b', label='Extended AB')

# Plot the shortened altitudes BE and CF
plt.plot([B[0], E[0]], [B[1], E[1]], linestyle='--', color='r', label='Altitude BE')
plt.plot([C[0], F[0]], [C[1], F[1]], linestyle='--', color='g', label='Altitude CF')

# Plot the points E and F
plt.text(E[0], E[1], 'E', fontsize=15, ha='right', va='bottom')
plt.text(F[0], F[1], 'F', fontsize=15, ha='right', va='bottom')
plt.plot(E[0], E[1], marker='o', color='b', label='E')
plt.plot(F[0], F[1], marker='o', color='b', label='E')


# Label the vertices A, B, and C
plt.text(A[0], A[1], 'A', fontsize=15, ha='right', va='bottom')
plt.text(B[0], B[1], 'B', fontsize=15, ha='right', va='bottom')
plt.text(C[0], C[1], 'C', fontsize=15, ha='right', va='bottom')

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

