# EasyLab

Offers simple solutions with GUI. From a folder, it can resize images, change their extensions, applies spatial frequencies, and remove backgrounds...

# Purpose of the project
+ The purpose of the project is to offer a simple solution to solve some of the problems that arise when working with big image datasets. 
+ The project is a work in progress, and it is not finished yet. Since it offers GUI, it is very practical to use it.

# Features
+ Resize images
+ Change extension
+ Apply spatial frequencies (low pass, high pass with Butterworth filter)
+ Apply Gaussian blur
+ Apply grayscale filter (RGB to Gray)
+ Rename images (with a prefix)
+ Remove background from images (Utilizes deep learning, so it is slow depending on the size of the images)
+ Apply histogram equalization 
+ Convert images to CFA (color filter array)

# installation
+ Install easylab with pip:
```pip install easylab  ```

# Usage
it is very simple to use the project.
For the open GUI, use the following command:
```from EasyLab import EasyLab```
then open the gui with:
```EasyLab.easylab()```
    

It's easy, just select the folder where your images are stored and select extension and size. "Rename" button will change all images' names like this: "0image", "1image","2image"... and so on...  
I use this command to standardize the picture names while doing deep learning.

### **Read before the usage!**
For unforeseen consequences be sure to copy the original images elsewhere.

## Javascript
I will also add some javascript to online version.
# E-prime scripts
get the trail list (Image names for the E-Prime) or create a jitter:
https://altunenes.github.io/EasyLab/filenames

## Contributing
Contributions are welcome!

##Author
+   Enes Altun [Main Author](https://altunenes.github.io)