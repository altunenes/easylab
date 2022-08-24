[![PyPI version](https://badge.fury.io/py/easylab.svg)](https://badge.fury.io/py/easylab)
[![pages-build-deployment](https://github.com/altunenes/easylab/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/altunenes/easylab/actions/workflows/pages/pages-build-deployment)
[![Downloads](https://pepy.tech/badge/easylab)](https://pepy.tech/project/easylab)
# EasyLab

Offers simple solutions with GUI. From a folder, it can resize images, change their extensions, applies spatial frequencies, and more.

check the following link for more details:

https://altunenes.github.io/easylab/

# Purpose of the project
+ The purpose of the project is to offer a simple solution to solve some of the problems that arise when working with big image datasets. 
+ The project is a work in progress, and it is not finished yet. Since it offers GUI, it is very practical to use it.

# Features
+ Resize images
+ Change extension
+ Apply spatial frequencies
+ Apply Gaussian blur
+ Apply gray scale
+ Rename images

# installation
+ Install easylab with pip:
```pip install easylab  ```

# Usage
it is very simple to use the project.
For the open GUI, use the following command:
```from easylab import easylab```
then open the gui with:
```easylab.easylabgui()```
    

It's easy, just select your folder where your images are stored and select extension and size. "Rename" button will change all images' names like this: "0image", "1image","2image"... and so on...  
I use this command to standardize the picture names while doing deep learning.

# Read before the usage!
 this program replaces the original images with the desired images. Be sure to copy the original ones elsewhere.

# Javascript
I will also add some javascript to online version.
# E-prime scripts
get the trail list (Image names for the E-Prime) or create a jitter:
https://altunenes.github.io/EasyLab/filenames

 ---------------


The extension button transforms images' extensions to the desired extension.

Gray button converts all images to GRAY

Blur button applies gaussian blur to all images (you need to define sigma and kernel size)

Low and High Spatial filter buttons applies Butterworth class of filter with given cutoff frequency. For details see the Psychopy: [Psychopy](https://psychopy.org/api/filters.html)

Matplotlib doesn't work with pixels directly, but rather physical sizes and DPI. If you want to display a figure with certain pixel size, you need to know the DPI of your monitor. I added two labels; just enter your desired dimensions (it will be multiplied with 1000; for example, if you want 800x800 pixels enter the 0.8 for both labels).
 
 
