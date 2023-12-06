# Fine-Element-Heat-Transfer-Project
## What is in the Repository?
In this repository, you will find two programs and three different files.
#### BEM plots.pdf
This is where you can find all the plots for the Backward Euler Method ranging from time steps 0.000181 to 1.814.
#### FEM plots.pdf
This is where you can find all the plots for the Forward Euler Method ranging from 2 Nodes to 11 Nodes. Each Node plot is broken down with time steps ranging from 0.00181 to 0.116.
#### WeakForm.pdf
This is where you can find how I solved the weak form of the heat equation given in the project prompt.
#### backwardEulerTest.py
This is where you can find the Backward Euler Method code used to answer the third prompt of the project.
#### forwardEulerTest.py
This is where you can find the Forward Euler Method code used to answer the second prompt of the project.

## Weak Form

### Project Prompt Part 1) Derive the weak form of this equation by-hand on paper and submit with your code.
Before we dive into what the file entails, let's discuss what the weak form is.

#### What is the Weak Form?
The weak form is a mathematical reformulation of a partial differential equation (PDE) that is more amenable to numerical approximation, particularly in the context of finite element methods. It is derived by multiplying the PDE by a test function and integrating it over the problem domain.
Once the weak form is derived, numerical methods like finite element methods can be applied to approximate the solution by discretizing the domain and replacing the continuous functions with finite-dimensional approximations. The weak form provides a more flexible and general framework for numerical simulations, allowing for easy adaptation to different geometries, boundary conditions, and types of problems.

#### What is in the file?
The pdf file contains the weak form of the heat transfer equation given by the project prompt. In this process, I define the elemental matrices for mass and stiffness (and possibly other) terms and integrate over each element using numerical quadrature to obtain the elemental contributions to the global matrices. 


## Forward Euler Method

### Project Prompt Part 2) Solve first by using a forward Euler time derivative discretization with a time-step of Δ𝑡 = 1/551. Plot the results at the final time. Increase the time-step until you find the instability. What dt does this occur at? How does the solution change as N decreases?
Before we get into the questions, let's discuss the code!
This Python script solves a one-dimensional heat transfer problem using the Finite Element Method (FEM) with the Forward Euler time integration scheme. The problem is defined on a domain with Dirichlet boundary conditions.

#### Key Features:
1. Finite Element Method:
- Discretizes the domain into elements and solves the heat transfer problem numerically.
2. Gaussian Quadrature:
- Utilizes Gaussian quadrature for numerical integration when assembling mass and stiffness matrices.
3. Time Integration:
- Employs the Forward Euler method for time discretization. Updates the solution at each time step.
4. Dirichlet Boundary Conditions:
- Applies Dirichlet boundary conditions by modifying the stiffness matrix.
5. Adaptive Time Stepping:
- Implements an adaptive time-stepping approach to handle stability. Starts with a small time step and increases it iteratively.
6. Instability Check:
- Monitors for instability by checking for NaN or Inf values in the solution.
7. Plotting:
- Generates plots of the numerical solution at each iteration with different time steps.
8. Analytical Solution:
- Computes an analytical solution at the final time for comparison.

#### Usage:
<p> Adjust parameters such as the number of nodes, boundaries, initial and final time, and boundary conditions in the user input section. </p>
<p> Run the script to obtain numerical solutions for different time steps. Plots will be generated to visualize the results. </p>
<p> The script includes an adaptive time-stepping mechanism to avoid instability. The maximum allowable time step is also displayed. </p>

#### Dependencies:
NumPy
Matplotlib
SciPy

### Results
<p> So, what happens when the time step increases? As seen in the given plots, the peaks of each parabolic graph increase but, why? The increasing peak in the plots might be related to numerical instability. The explicit Forward Euler method I used for time integration is conditionally stable, meaning there is a maximum time step beyond which the solution becomes unstable. With my code, I found that the maximum allowable dt before instability occurs is 0.1161524500907441. </p>

<p>How does the solution change as N decreases? The graph becomes less defined and the peak becomes lower. Why? As the number of nodes decreases and the spatial grid becomes coarser, the numerical solution may lose accuracy, exhibit a smoother profile, and potentially result in a lower peak value. It's essential to strike a balance between computational efficiency (which benefits from coarser grids) and the need for accurate representation of the solution features (which benefits from finer grids). Experimenting with different spatial resolutions and assessing the impact on the solution can help in understanding the trade-offs involved. </p>

## Backward Euler Method

### Project Prompt Part 3) Part Solve the same problem with the same time-steps using an implicit backward Euler. What happens as the time-step is equal to or greater than the spatial step size? Explain why.
Before we get into the questions, let's discuss the code!
This Python script provides a numerical solution to a 1D heat transfer problem using the Backward Euler method. The code utilizes the finite element method to discretize the domain, and Dirichlet boundary conditions are applied to simulate heat transfer within the specified boundaries.

#### Key Components:
1. Grid and Connectivity Map:
- Generates a uniform grid and connectivity map for the finite element method.
2. Basis Functions and Derivatives:
- Defines linear basis functions and their derivatives on the parent element.
3. Matrix Assembly:
- Initializes and assembles the mass (M) and stiffness (K) matrices based on the finite element method.
4. Dirichlet Boundary Conditions:
- Applies Dirichlet boundary conditions to the stiffness and mass matrices.
5. Initialization:
- Sets the initial condition u to a sine function.
6. Time-Stepping Loop (Backward Euler):
- Performs a time-stepping loop using the Backward Euler method to numerically solve the heat equation.
7. Building Right-Hand Side (RHS) Vector:
- Constructs the time-dependent right-hand side (RHS) vector using the given source term.
8. Backward Euler Update:
- Applies the Backward Euler update to solve the system of equations at each time step.
9. Plotting:
- Plots the initial condition and the numerical solution at selected time steps.
- Compares the numerical solution with the analytical solution at the final time.

#### Usage:
Adjust parameters such as the number of nodes, boundaries, time steps, and boundary conditions as needed.
Run the script to obtain visualizations of the numerical solution's evolution over time.

#### Dependencies:
NumPy: For numerical operations.
Matplotlib: For plotting.

#### Notes:
The script is designed to be a starting point for solving 1D heat transfer problems using the Backward Euler method. Users can modify parameters and extend the code for specific applications.
### Results
What happens as the time-step is equal to or greater than the spatial step size? When the time-step is equal to or greater than the spatial step size, the backward Euler method remains stable, and the numerical solution does not exhibit the instability issues observed with the forward Euler method. The backward Euler method is an implicit time-stepping method, which means it involves solving a linear system of equations at each time step. In the case of this heat transfer problem, the linear system involves the mass matrix (M) and the stiffness matrix (K). The implicit nature of backward Euler allows it to handle larger time-step sizes compared to explicit methods like forward Euler. When the time-step is equal to or greater than the spatial step size, the backward Euler method remains unconditionally stable. This stability is a desirable property because it allows for larger time-step sizes, potentially reducing the computational cost of the simulation. In summary, backward Euler is more robust in handling larger time-step sizes, and it remains stable even when the time-step is equal to or greater than the spatial step size.


## What are the differences between the two methods?

### Viewing the different conditions
With the given project prompt, the Forward Euler Method becomes unstable as the time steps increase. The stability of the Forward Euler Method is subject to the Courant-Friedrichs-Lewy (CFL) condition, which is a necessary condition for stability in numerical methods, especially for solving partial differential equations like the heat equation. The time step must be small enough compared to the spatial grid size and the diffusivity to ensure stability. If the time step exceeds this limit, the forward Euler method becomes numerically unstable, leading to unphysical oscillations and growing solution amplitudes. As you increase the time step (Δt), you might be violating the CFL condition, making the numerical solution unstable. The instability becomes more pronounced as the time step increases, and you observe unphysical behavior in the solution.

With the plots provided by the Backward Euler Method, the plots become more stable as the time steps increase! While the Backward Euler Method is unconditionally stable, its accuracy may depend on the time step size. Smaller time steps usually result in more accurate numerical solutions. However, if the time step becomes extremely small, numerical precision issues may arise, causing instability.

### Stable Conditions
If you look into the different plots from both methods, you will find that the Forward Euler Method and the Backward Euler Method have very similar parabolic shapes when given the same stable conditions. However, if you look at the y-axis for both plots you can find that the peak is drastically different. Why is that?

The difference in peak values between the forward Euler and backward Euler methods is likely due to the stability characteristics and numerical dissipation introduced by each method.

#### Numerical Dissipation: 
The forward Euler method is known for introducing numerical dissipation, which tends to smooth out high-frequency components in the solution. This numerical dissipation can be beneficial for stabilizing the solution, especially when the time step is relatively large. However, it can also lead to a damping effect, reducing the amplitude of oscillations in the solution.

#### Stability Characteristics: 
The forward Euler method is conditionally stable, meaning there are restrictions on the time step for stability. If the time step exceeds certain limits (related to the CFL condition), the solution becomes unstable. On the other hand, the backward Euler method is unconditionally stable for linear problems, allowing for larger time steps without stability concerns.

#### Accuracy and Truncation Errors: 
The backward Euler method generally provides more accurate results than the forward Euler method for the same time step. The backward Euler method is an implicit scheme, which means it involves solving a linear system at each time step. This implicit treatment can lead to better accuracy, especially for stiff problems.

#### Analytical Solution Discrepancy: 
It's important to note that the analytical solution serves as a reference, and discrepancies between numerical and analytical solutions may arise due to various factors, including numerical approximations, time step size, and the nature of the problem.

In summary, while the backward Euler method may yield a closer match to the analytical solution in terms of peak values, the forward Euler method introduces more numerical dissipation, potentially leading to a smoother and less oscillatory solution. The choice between these methods often involves a trade-off between stability, accuracy, and computational efficiency. Experimenting with different time step sizes and numerical methods can help find a balance that meets the requirements of your specific problem.


## What did I learn from this?
It is safe to say that I learned a lot from coding this project (about myself and the subject). 

### Learnings from Forward Euler Implementation:
Numerical Solution Using Forward Euler:
#### Finite Element Method:
The code applies the finite element method to solve a 1D heat transfer problem with Dirichlet boundary conditions.
#### Lagrange Basis Functions:
Lagrange basis functions and their derivatives are employed to interpolate and differentiate within the elements.
#### Matrix Assembly with Gaussian Quadrature:
Mass (M) and stiffness (K) matrices are assembled using second-order Gaussian quadrature to integrate over the elements.
#### Dirichlet Boundary Conditions:
Dirichlet boundary conditions are enforced by modifying the stiffness matrix.
#### Time Integration with Forward Euler:
Forward Euler method is used for time integration, updating the solution at each time step.
#### Adaptive Time Stepping:
The code employs adaptive time stepping, iteratively doubling the time step until instability is reached, with a maximum allowable time step.
#### Plotting and Visualization:
The numerical solution is visualized at different time steps, and the analytical solution at the final time is compared.
#### Stability Check:
The code checks for numerical instability by examining if the solution contains NaN or Inf values.


Forward Euler Limitations:
#### Instability: 
Forward Euler may become unstable for large time steps, leading to inaccurate results or divergence.
#### Courant-Friedrichs-Lewy (CFL) Condition: 
Care must be taken to ensure the time step adheres to the CFL stability condition for explicit methods.

### Learnings from Backward Euler Implementation:
Numerical Solution Using Backward Euler:
#### Finite Element Method:
The code applies the finite element method to solve the same 1D heat transfer problem with Dirichlet boundary conditions.
#### Parent Grid Basis Functions:
Parent grid basis functions and their derivatives are utilized for element-wise calculations.
#### Matrix Assembly:
Mass (M) and stiffness (K) matrices are assembled for the finite element problem.
#### Dirichlet Boundary Conditions:
Dirichlet boundary conditions are applied by modifying both the stiffness and mass matrices.
#### Backward Euler Time Integration:
Backward Euler method is employed for time integration, providing unconditional stability for linear problems.
#### Plotting and Visualization:
The numerical solution is visualized at different time steps, and the analytical solution at the final time is compared.
Backward Euler Advantages:
#### Stability:
Backward Euler is unconditionally stable for linear problems, allowing for larger time steps without compromising stability.
##### Implicit Time Stepping:
The implicit nature of Backward Euler can be advantageous for stiff problems.

### General Observations:
#### Comparison of Methods: 
Both methods are implemented to solve the same problem, allowing for a comparison of their stability, accuracy, and computational efficiency.

#### Adaptive Time Stepping vs. Fixed Time Stepping: 
The Forward Euler implementation employs adaptive time stepping, while the Backward Euler method uses a fixed time step. This difference affects the stability and accuracy of the solutions.

#### Numerical vs. Analytical Solutions: 
The numerical solutions are compared with the analytical solution at the final time to assess accuracy.

#### Code Structure:
Both implementations share similarities in terms of matrix assembly, boundary condition application, and visualization, providing insights into the general structure of finite element heat transfer solvers.


I think that this project really tested my limits and my overall understanding of the course. Although this was a very difficult project to finish and to navigate, I am proud that I was able to get to the finish line and showcase my learnings with you. I am sure as you navigate through my repository you will find things I can improve on and I would love to hear the feedback! Thank you for a great semester and I hope you enjoy my project!
