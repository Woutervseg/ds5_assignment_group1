from PIL import Image
import colorsys
from math import log, log2

def mandelbrot(c, max_iter):
    """
    Calculate the Mandelbrot set's diverging index for a given complex number.

    Args:
        c (complex): The complex number for which to calculate the diverging index.
        max_iter (int): The maximum number of iterations to perform.

    Returns:
        int: The diverging index of the complex number.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - (log(log2(abs(z))) / log(2))

def draw_mandel(width):
    """
    Generate and save an image of the Mandelbrot set with a blue background.

    Args:
        width (int): The width and height of the image (it is always a square).

    Returns:
        None
    """
    height = width
    x_min, x_max = -1.5, 0.5
    y_min, y_max = -1, 1
    max_iter = 256  # Adjust this for more or less detail

    image = Image.new("RGB", (width, height))
    pixels = image.load()

    # Set the background color to blue
    for x in range(width):
        for y in range(height):
            pixels[x, y] = (255, 0, 0)

    for x in range(width):
        for y in range(height):
            # Map pixel coordinate to complex number
            real = x * (x_max - x_min) / (width - 1) + x_min
            imag = y * (y_max - y_min) / (height - 1) + y_min
            c = complex(real, imag)

            # Calculate the diverging index for the Mandelbrot set
            color_index = mandelbrot(c, max_iter)

            # Map the color index to an RGB color using colorsys
            hue = color_index / max_iter
            saturation = 1.0
            value = 1.0 if color_index < max_iter else 0.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, saturation, value)]

            # Set the pixel color
            pixels[x, y] = (r, g, b)

    image.save("mandelbrot.png", "PNG")

# Example usage:
draw_mandel(200)
