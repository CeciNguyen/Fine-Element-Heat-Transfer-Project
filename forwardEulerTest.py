import numpy as np
import matplotlib.pyplot as plt

# User Input
N = 11  # Number of nodes
xl = 0.0  # Left boundary
xr = 1.0  # Right boundary
T0 = 0.0  # Initial time
Tf = 1.551  # Final time
dt = 0.00181488203  # Time step around 1/551
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

# Apply Dirichlet boundary conditions to stiffness matrix
K[0, :] = 0
K[:, 0] = 0
K[0, 0] = 1
K[-1, :] = 0
K[:, -1] = 0
K[-1, -1] = 1

# Initialize solution vector
u = np.sin(np.pi * x)  # Initial condition

# Iterate over increasing time steps until instability is reached
max_dt = 0.2  # Set a maximum allowable dt to avoid excessive runtime
while dt <= max_dt:
    nt = int((Tf - T0) / dt)
    
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

        # Update the solution using forward Euler
        u = u + dt * np.linalg.solve(M, F)

    # Analytical solution at final time
    u_analytical = np.exp(-Tf) * np.sin(np.pi * x)

    # Plot the results
    plt.plot(x, u, label=f'Numerical Solution (dt={dt})')
    plt.xlabel('x')
    plt.ylabel(f'u(x, {Tf})')
    plt.title(f'Heat Transfer Problem - Numerical Solution (Forward Euler) with dt={dt}')
    plt.legend()
    plt.show()

    # Check for instability
    if np.isnan(u).any() or np.isinf(u).any():
        print(f"Instability reached at dt={dt}")
        break

    # Increase dt for the next iteration
    dt *= 2

# Print the maximum allowable time step before instability
print(f"Maximum allowable dt before instability: {dt / 2}")