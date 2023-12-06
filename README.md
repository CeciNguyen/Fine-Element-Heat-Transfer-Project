# Fine-Element-Heat-Transfer-Project
## What is in the Repository?
In this repository, you will find three different files.
## Weak Form
### Project Prompt Part 1) Derive the weak form of this equation by-hand on paper and submit with your code.
## Forward Euler Method
### Project Prompt Part 2) Solve first by using a forward Euler time derivative discretization with a time-step of Δ𝑡 = 1/551. Plot the results at the final time. Increase the time-step until you find the instability. What dt does this occur at? How does the solution change as N decreases?
### Results
## Backward Euler Method
### Project Prompt Part 3) Part Solve the same problem with the same time-steps using an implicit backward Euler. What happens as the time-step is equal to or greater than the spatial step size? Explain why.
When the time-step is equal to or greater than the spatial step size, the backward Euler method remains stable, and the numerical solution does not exhibit the instability issues observed with the forward Euler method.

The backward Euler method is an implicit time-stepping method, which means it involves solving a linear system of equations at each time step. In the case of this heat transfer problem, the linear system involves the mass matrix (M) and the stiffness matrix (K). The implicit nature of backward Euler allows it to handle larger time-step sizes compared to explicit methods like forward Euler.

When the time-step is equal to or greater than the spatial step size, the backward Euler method remains unconditionally stable. This stability is a desirable property because it allows for larger time-step sizes, potentially reducing the computational cost of the simulation.

In summary, backward Euler is more robust in handling larger time-step sizes, and it remains stable even when the time-step is equal to or greater than the spatial step size.
### Results
## What are the differences between the two methods?
## What did I learn from this?
