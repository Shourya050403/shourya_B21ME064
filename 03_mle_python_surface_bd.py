# -*- coding: utf-8 -*-
"""03-mle-python-surface-bd.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xc7DXg2a7-G0c6sY29PCZsGkydyK82jt
"""

import numpy as np
import matplotlib.pyplot as plt

def create_S_values(N):
    # Create an array S ranging from 1 to N
    S = np.arange(1, N + 1)
    return S

def create_theta_values(theta_range, num_points):
    # Create an array theta with the specified range and number of points
    theta = np.linspace(theta_range[0], theta_range[1], num_points)
    return theta

def create_likelihood_grid(S, theta):
    # Create a 2D grid of S and theta values
    S_grid, theta_grid = np.meshgrid(S, theta)
    return S_grid, theta_grid

def calculate_likelihood(S_grid, theta_grid, N):
    # Calculate the likelihood function L(theta|S)
    L = S_grid * np.log(theta_grid) + (N - S_grid) * np.log(1 - theta_grid)
    return L

# Define the variables with new values
N = 200
theta_range = [0.2, 0.8]
num_points = 150

# Create the S values
S = create_S_values(N)

# Create the theta values
theta = create_theta_values(theta_range, num_points)

# Create the likelihood grid
S_grid, theta_grid = create_likelihood_grid(S, theta)

# Calculate the likelihood function
L = calculate_likelihood(S_grid, theta_grid, N)

# Creating a 3D plot to visualize the likelihood function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
s = ax.plot_surface(S_grid, theta_grid, L, cmap='jet')

# Labeling the axes
ax.set_xlabel('S')
ax.set_ylabel('theta')
ax.set_zlabel('L')
ax.set_title('Likelihood Function L(theta|S)')
ax.view_init(65, 15)

# Saving the plot to a file
plt.savefig('s-theta-L.png')

# Display the plot
plt.show()