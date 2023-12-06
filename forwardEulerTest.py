import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# User Input
N = 11  # Number of nodes
xl = 0.0  # Left boundary
xr = 1.0  # Right boundary
T0 = 0.0  # Initial time
Tf = 1.551  # Final time
dt = 1/551  # Time step around 1/551
ud_left = 0.0  # Dirichlet boundary condition at left
ud_right = 0.0  # Dirichlet boundary condition at right

# Create a Uniform Grid and Connectivity Map
Ne = N - 1
h = (xr - xl) / (N - 1)
x = np.linspace(xl, xr, N)
iee = np.array([np.arange(i, i + 2) for i in range(Ne)])

# Define Lagrange basis functions and derivatives
def lagrange_basis(xi, x, i):
    result = 1.0
    for j in range(len(x)):
        if j != i:
            result *= (xi - x[j]) / (x[i] - x[j])
    return result

def lagrange_derivative(xi, x, i):
    result = 0.0
    for j in range(len(x)):
        if j != i:
            result += 1 / (x[i] - x[j])
    return result

# Initialize matrices
K = np.zeros((N, N))
M = np.zeros((N, N))
F = np.zeros(N)

# Assemble mass and stiffness matrices using 2nd order Gaussian quadrature
for k in range(Ne):
    x_elem = x[iee[k]]
    J = h / 2  # Jacobian for 1D linear mapping

    for l in range(2):
        xi_l, w_l = np.polynomial.legendre.leggauss(2)
        xi_local = 0.5 * (x_elem[0] + x_elem[1]) + 0.5 * (x_elem[1] - x_elem[0]) * xi_l[l]
        w_local = 0.5 * (x_elem[1] - x_elem[0]) * w_l[l]

        for m in range(2):
            phi_l = lagrange_basis(xi_local, x_elem, m)
            phi_m = lagrange_basis(xi_local, x_elem, l)
            dphi_dxi_l = lagrange_derivative(xi_local, x_elem, m)
            dphi_dxi_m = lagrange_derivative(xi_local, x_elem, l)

            M[iee[k, l], iee[k, m]] += phi_l * phi_m * J * w_local
            K[iee[k, l], iee[k, m]] += dphi_dxi_l * dphi_dxi_m * J * w_local

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

        # Build the time-dependent R.H.S. vector using 2nd order Gaussian quadrature
        F[:] = 0

        for k in range(Ne):
            x_elem = x[iee[k]]
            J = h / 2  # Jacobian for 1D linear mapping

            for l in range(2):
                xi_l, w_l = np.polynomial.legendre.leggauss(2)
                xi_local = 0.5 * (x_elem[0] + x_elem[1]) + 0.5 * (x_elem[1] - x_elem[0]) * xi_l[l]
                w_local = 0.5 * (x_elem[1] - x_elem[0]) * w_l[l]

                f_local = (np.pi**2 - 1) * np.exp(-ctime) * np.sin(np.pi * xi_local)
                phi_l = lagrange_basis(xi_local, x_elem, l)
                F[iee[k, l]] += f_local * phi_l * J * w_local

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