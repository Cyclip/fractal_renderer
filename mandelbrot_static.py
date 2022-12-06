import matplotlib.pyplot as plt
import fractals.mandelbrot as mandelbrot

"""
    This script creates a static plot of the Mandelbrot set.
"""

def view(n, m, xmin, xmax, ymin, ymax, density):
    # Create a static plot of the Mandelbrot set
    start = time.time()
    mandelbrot_matrix = mandelbrot.mandelbrot(n, m, xmin, xmax, ymin, ymax, density=density)
    plt.imshow(mandelbrot_matrix, cmap='hot', interpolation='nearest')
    # Hide the axes
    plt.title(f"Mandelbrot set [Density: {density}]")
    plt.axis('off')

    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")
    plt.show()

if __name__ == '__main__':
    import time
    # Static plot
    # Density is constant
    n = 1000
    m = 1000
    xmin, xmax = -2.5, 0.75
    ymin, ymax = -1.5, 1.5
    density = 500

    print("Creating static plot...")
    view(n, m, xmin, xmax, ymin, ymax, density)