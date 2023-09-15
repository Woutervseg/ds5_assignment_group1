from PIL import Image
import colorsys
from math import log, log2

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - (log(log2(abs(z))) / log(2))

def draw_mandel(width):
    height = width
    x_min, x_max = -1.5, 0.5
    y_min, y_max = -1, 1
    max_iter = 256  # Adjust this for more or less detail

    image = Image.new("RGB", (width, height))
    pixels = image.load()

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
