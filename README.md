# EasyLab
basic lab tools with GUI
# Usage
It's easy, just select your folder where your images are stored and select extension and size. "Rename" button will change all images' names like this: "0image", "1image","2image"... and so on...  

# Read before the usage!
 this program replaces the original images with the desired images. Be sure to copy the original ones elsewhere.
 
# E-prime scripts
get the trail list or create a jitter:
https://altunenes.github.io/EasyLab/filenames

 ---------------

The extension button transforms images' extensions to the desired extension.

Gray button converts all images to GRAY

Blur button applies gaussian blur to all images (you need to define sigma and kernel size)

Low and High Spatial filter buttons applies Butterworth class of filter with given cutoff frequency. For details see the Psychopy: [Psychopy](https://psychopy.org/api/filters.html)

Matplotlib doesn't work with pixels directly, but rather physical sizes and DPI. If you want to display a figure with certain pixel size, you need to know the DPI of your monitor. I added two labels; just enter your desired dimensions (it will be multiplied with 1000; for example, if you want 800x800 pixels enter the 0.8 for both labels).
 
 
 
![image](https://user-images.githubusercontent.com/54986652/147148597-c1e1eb89-b11b-4ab6-be6c-0ff466487b88.png)
