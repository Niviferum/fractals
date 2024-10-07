from dataclasses import dataclass
from itertools import product
from PIL import Image
from math import log

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm

@dataclass

class MandelbrotSet:
    max_iterations: int
    escape_radius: float = 2.0

    def __contains__(self, c: complex) -> bool:
        return self.stability(c) == 1

    def stability(self, c: complex, smooth=False, clamp=True) -> float:
        value = self.escape_count(c, smooth) / self.max_iterations
        return max(0.0, min(value, 1.0)) if clamp else value

    def escape_count(self, c: complex, smooth=False) -> int:
        z = 0
        for iteration in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > self.escape_radius:
                if smooth:
                    return iteration + 1 - log(log(abs(z))) / log(2)
                return iteration
        return self.max_iterations


@dataclass
class Viewport:
    image: Image.Image
    center: complex
    width: float

    @property
    def height(self):
        return self.scale * self.image.height
    
    @property
    def offset(self):
        return self.center + complex(-self.width, self.height) / 2
    
    @property
    def scale(self):
        return self.width / self.image.width
    
    def __iter__(self):
        for y in range(self.image.height):
            for x in range(self.image.width):
                yield Pixel(self, x, y)

@dataclass
class Pixel:
    viewport: Viewport
    x: int
    y: int

    @property
    def color(self):
        return self.viewport.image.getpixel((self.x, self.y))
    
    @color.setter
    def color(self, value):
        self.viewport.image.putpixel((self.x, self.y), value)

    def __complex__(self):
        return (
            complex(self.x, -self.y)
            * self.viewport.scale
            + self.viewport.offset
        )
    
def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        pixel.color = palette[index % len(palette)]

def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in palette

    ] 
width, height = 1024, 1024
BLACK_AND_WHITE = '1'
GRAYSCALE = 'L'
RGB = 'RGB'

image = Image.new(RGB, (width, height))    

mandelbrot_set = MandelbrotSet(max_iterations=256, escape_radius=1000)
viewport = Viewport(image, center=-0.7435 + 0.1314j, width=0.002)

colormap = matplotlib.cm.get_cmap('cividis').colors
palette = denormalize(colormap)

paint(mandelbrot_set, viewport, palette, smooth=True)
image.show()

