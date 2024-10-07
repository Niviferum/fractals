# Mendelbrot's Fractals : 

Welcome to this small python project, based on "Hacker Alpha's" video on YouTube. 

So, what are Mendelbrot's set's Fractals ? It's a two dimensional set defined on the complex plane as the complex numbers "c" for which the function fc(z) = z² + c doesn't diverge to infinity when iterated starting at z = 0.
The goal of this project is to offer a visualization of the set, at any iteration you want, with whichever color theme you want, with only a few code changes in the main.py.

## How does it works ? 

The code needs you to install numpy and matplotlib for it to work. 
Whenever you're setup, you only need to run the program to get an image to be generated. 
The default image will be a z=256 iteration, with a 1000 escape radius. If you want to modify the pattern of the fractal, you can play with these two numbers at line 97. 
Caution : the bigger the number, the longer it will take to generate it, as the formula is quite complex and depending on how powerful your computer is, it might take several seconds, to a few minutes. 

# How to change the color theme ?

By default, you have the "cividis" color theme. You might want something different, so here is how you can change it :

On matplotlib's documentation, you have the full list of every palette you can use (https://matplotlib.org/stable/users/explain/colors/colormaps.html)
To modify it in our code, here is how you can do it : 
At line 100, you will notice there is :
```colormap = matplotlib.cm.get_cmap('cividis').colors```

You can replace 'cividis' by any color palette you want, from matplotlib's doc. Make sure not to forget the apostrophes, or it won't compile.

------


This is an open source project, feel free to use it partially or fully in your own projects.
