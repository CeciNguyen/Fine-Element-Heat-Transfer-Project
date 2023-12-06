import numpy as np
import matplotlib.pyplot as plt

# User Input
N = 11  # Number of nodes
xl = 0.0  # Left boundary
xr = 1.0  # Right boundary
T0 = 0.0  # Initial time
Tf = 1.551  # Final time
dt = 1  # Time step around 1/551
ud_left = 0.0  # Dirichlet boundary condition at left
ud_right = 0.0  # Dirichlet boundary condition at right

# Create a Uniform Grid and Connectivity Map
Ne = N - 1
h = (xr - xl) / (N - 1)
x = np.linspace(xl, xr, N)
iee = np.array([np.arange(i, i + 2) for i in range(Ne)])

# Define parent grid [-1, 1] basis functions and derivatives
xi = np.array([-1 / np.sqrt(3), 1 / np.sqrt(3)])

def phi(xi):
    return 0.5 * np.array([1 - xi, 1 + xi])

def dphi_dxi(xi):
    return 0.5 * np.array([-1, 1])

# Initialize matrices
K = np.zeros((N, N))
M = np.zeros((N, N))
F = np.zeros(N)

# Assemble mass and stiffness matrices
for k in range(Ne):
    J = h / 2  # Jacobian for 1D linear mapping
    x_elem = x[iee[k]]

    for l in range(2):
        for m in range(2):
            phi_l = phi(xi[l])
            phi_m = phi(xi[m])
            M[iee[k, l], iee[k, m]] += np.dot(phi_l, phi_m) * J
            K[iee[k, l], iee[k, m]] += np.dot(dphi_dxi(xi[l]), dphi_dxi(xi[m])) * J

# Apply Dirichlet boundary conditions to stiffness matrix and mass matrix
K[0, :] = 0
K[:, 0] = 0
K[0, 0] = 1
K[-1, :] = 0
K[:, -1] = 0
K[-1, -1] = 1

M[0, :] = 0
M[:, 0] = 0
M[0, 0] = 1
M[-1, :] = 0
M[:, -1] = 0
M[-1, -1] = 1

# Initialize solution vector
u = np.sin(np.pi * x)  # Initial condition

# Time-stepping loop using Backward Euler
nt = int((Tf - T0) / dt)

# Plot initial condition
plt.plot(x, u, label=f'Numerical Solution (t={T0})')

for n in range(1, nt + 1):
    ctime = T0 + n * dt

    # Build the time-dependent R.H.S. vector
    F[:] = 0

    for k in range(Ne):
        J = h / 2  # Jacobian for 1D linear mapping
        x_elem = x[iee[k]]

        for l in range(2):
            xi_local = xi[l]
            f_local = (np.pi**2 - 1) * np.exp(-ctime) * np.sin(np.pi * (x_elem[0] + xi_local * h / 2))
            phi_l = phi(xi_local)
            F[iee[k, l]] += f_local * phi_l[l] * J

    # Backward Euler update
    u = np.linalg.solve(M + dt * K, u + dt * F)

    # Plot the results at every 100th time step for visibility
    if n % 100 == 0:
        plt.plot(x, u, label=f'Numerical Solution (t={ctime})')

# Analytical solution at final time
u_analytical = np.exp(-Tf) * np.sin(np.pi * x)
plt.plot(x, u_analytical, label='Analytical Solution', linestyle='--')

# Finalize and show the plot
plt.xlabel('x')
plt.ylabel(f'u(x, {Tf})')
plt.title(f'Heat Transfer Problem - Numerical Solution (Backward Euler) with dt={dt}')
plt.legend()
plt.show()