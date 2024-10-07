# Mendelbrot's Fractals : 

Welcome to this small python project, based on "Hacker Alpha's" video on YouTube. 

So, what are Mendelbrot's set's Fractals ? It's a two dimensional set defined on the complex plane as the complex numbers "c" for which the function ``fc(z) = z² + c`` doesn't diverge to infinity when iterated starting at z = 0.
The goal of this project is to offer a visualization of the set, at any iteration you want, with whichever color theme you want, with only a few code changes in the main.py.

## How does it works ? 

The code needs you to install numpy and matplotlib for it to work. 
Whenever you're setup, you only need to run the program to get an image to be generated. 
The default image will be a z=256 iteration, with a 1000 escape radius. If you want to modify the pattern of the fractal, you can play with these two numbers at line 97. 
Caution : the bigger the number, the longer it will take to generate it, as the formula is quite complex and depending on how powerful your computer is, it might take several seconds, to a few minutes. 

## How to change the color theme ?

By default, you have the "cividis" color theme. You might want something different, so here is how you can change it :

On matplotlib's documentation, you have the full list of every palette you can use (https://matplotlib.org/stable/users/explain/colors/colormaps.html)
To modify it in our code, here is how you can do it : 
At line 100, you will notice there is :
```colormap = matplotlib.cm.get_cmap('cividis').colors```

You can replace 'cividis' by any color palette you want, from matplotlib's doc. Make sure not to forget the apostrophes, or it won't compile.

------


This is an open source project, feel free to use it partially or fully in your own projects.


# Fractales de Mendelbrot :
Bienvenue dans ce petit projet Python, basé sur la vidéo de "Hacker Alpha" sur YouTube.

Alors, que sont les fractales de l'ensemble de Mandelbrot ? Il s'agit d'un ensemble sur deux dimensions défini sur le plan complexe comme étant les nombres complexes "c" pour lesquels la fonction ``fc(z) = z² + c``  ne diverge pas vers l'infini lorsqu'elle est itérée en commençant par z = 0.
L'objectif de ce projet est de proposer une visualisation de cet ensemble, avec le nombre d'itérations de votre choix et le thème de couleur de votre choix, avec seulement quelques modifications dans le fichier main.py.

## Comment ça fonctionne ?
Le code nécessite l'installation de numpy et matplotlib pour fonctionner.
Une fois que vous êtes configuré, il vous suffit d'exécuter le programme pour générer une image.
L'image par défaut sera générée avec une itération z=256, avec un rayon d'échappement de 1000. Si vous souhaitez modifier le motif de la fractale, vous pouvez jouer avec ces deux nombres à la ligne 97.
Attention : plus les nombres sont élevés, plus le temps de génération sera long, car la formule est assez complexe, et en fonction de la puissance de votre ordinateur, cela peut prendre plusieurs secondes voire quelques minutes.

## Comment changer le thème de couleur ?
Par défaut, vous avez le thème de couleurs "cividis". Vous pourriez vouloir quelque chose de différent, alors voici comment vous pouvez le changer :

Sur la documentation de matplotlib, vous avez la liste complète de toutes les palettes que vous pouvez utiliser (https://matplotlib.org/stable/users/explain/colors/colormaps.html)
Pour le modifier dans notre code, voici comment vous pouvez le faire :
À la ligne 100, vous remarquerez qu'il y a : ```colormap = matplotlib.cm.get_cmap('cividis').colors```

Vous pouvez remplacer 'cividis' par n'importe quelle palette de couleurs de la documentation matplotlib. Assurez-vous de ne pas oublier les apostrophes, sinon cela ne compilera pas.

----- 

Ceci est un projet open source, n'hésitez pas à l'utiliser partiellement ou totalement dans vos propres projets.
