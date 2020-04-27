import math

def mandel(real, imag):
    x = 0 
    y = 0
    for i in range(1, 257):
        if x*x +y*y > 4.0:
            break
        xt = real + x*x - y*y
        y = imag + 2.0 * x * y
        x = xt
    return int(math.log(i) * 256 / math.log(256)) - 1

def mandelbrot(size_x, size_y):
    return [[mandel((3.5 * x / size_x) -  2.5,
                    (2.0 * y / size_y) - 1.0)
            for x in range(size_x)]
            for y in range(size_y)]




#this was tested by running in the CLI
#import fractal
#pixels = fractal.mandelbrot(448,256) #crea la base para un archivo de 448 * 225 pixeles
#import reprlib 
#reprlib.repr(pixels) # to look into the file 
#import bmp
#bmp.write_grayscale("mandel.bmp", pixels) #generates the bmp file