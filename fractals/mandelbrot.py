import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

"""
    This script creates an animated plot of the Mandelbrot set.
    You can import the function mandelbrot() to create a static plot.
"""

MAX_DENSITY = 100
n = 1000
m = 1000

xmin, xmax = -2.5, 0.75
ymin, ymax = -1.5, 1.5

def matrix(n, m, xmin, xmax, ymin, ymax, density=20):
    """Create a grid of complex numbers (matrix)"""
    # Real component
    real_comp = np.linspace(xmin, xmax, int((xmax - xmin) * density))
    # Imaginary component
    imag_comp = np.linspace(ymin, ymax, int((ymax - ymin) * density))

    # Create a matrix of complex numbers
    c_matrix = real_comp[np.newaxis, :] + imag_comp[:, np.newaxis] * 1j

    return c_matrix


def within_threshold(c, iterations=100):
    """Check if a complex number is within the threshold
    Iterations required to diverge returned"""
    z = 0

    for i in range(iterations):
        z = z**2 + c
        diverge = np.abs(z) > 2
        if diverge.any():
            return i
        
    return iterations


def mandelbrot(n, m, xmin, xmax, ymin, ymax, density=20):
    """Create a matrix of iterations required to diverge"""
    c_matrix = matrix(n, m, xmin, xmax, ymin, ymax, density=density)
    # Create a matrix of iterations required to diverge
    mandelbrot_matrix = np.zeros(c_matrix.shape, dtype=int)

    # For each row in the matrix
    for i in range(c_matrix.shape[0]):
        # For each column in the matrix
        for j in range(c_matrix.shape[1]):
            # For each complex number in the matrix,
            # check if it is within the threshold
            # Set the value to the number of iterations required to diverge in the mandelbrot matrix
            mandelbrot_matrix[i, j] = within_threshold(c_matrix[i, j])

    return mandelbrot_matrix

if __name__ == '__main__':
    # Animated plot
    # Density increases 1 every frame
    # Change title to show density
    fig = plt.figure()
    ax = plt.axes()
    density = 1
    im = ax.imshow(mandelbrot(n, m, xmin, xmax, ymin, ymax, density=density), cmap='hot', interpolation='nearest', animated=True)
    ax.set_title(f'Density: {density}')

    def updatefig(*args):
        global density
        if density < MAX_DENSITY:
            print(f'Density: {density}')
            density += 1
            im.set_array(mandelbrot(n, m, xmin, xmax, ymin, ymax, density=density))
            ax.set_title(f'Density: {density}')
            return im,
    
    ani = animation.FuncAnimation(fig, updatefig, interval=10, blit=True)
    # Save animation
    ani.save(f'mandelbrot_to_{MAX_DENSITY}.gif', writer='imagemagick', fps=10)
    # plt.show()
