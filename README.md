[![PyPI version](https://badge.fury.io/py/easylab.svg)](https://badge.fury.io/py/easylab)
[![pages-build-deployment](https://github.com/altunenes/easylab/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/altunenes/easylab/actions/workflows/pages/pages-build-deployment)
[![Downloads](https://pepy.tech/badge/easylab)](https://pepy.tech/project/easylab)

#### EasyLab

Offers simple solutions with GUI. From a folder, it can resize images, change their extensions, applies spatial frequencies, and remove backgrounds...

#### Purpose of the project

+ The purpose of the project is to offer a simple solution to solve some of the problems that arise when working with big image datasets.
+ The project is a work in progress, and it is not finished yet. Since it offers GUI, it is very practical to use it.

#### Features

+ Resize images
+ Change extension
+ Apply spatial frequencies
+ Apply Gaussian blur
+ Apply gray scale filter
+ Rename images
+ Remove background from images

#### installation

+ Install easylab with pip:
  ```pip install easylab  ```

#### Usage

it is very simple to use the project.
For the open GUI, use the following command:
```from EasyLab import EasyLab```
then open the gui with:
```EasyLab.easylab()```

It's easy, just select the folder where your images are stored and select extension and size. "Rename" button will change all images' names like this: "0image", "1image","2image"... and so on...
I use this command to standardize the picture names while doing deep learning.

#### **Read before the usage!**

For unforeseen consequences be sure to copy the original images elsewhere.

#### Javascript

I will also add some javascript to online version.

#### E-prime scripts

get the trail list (Image names for the E-Prime) or create a jitter:
https://altunenes.github.io/EasyLab/filenames

#### Contributing

Contributions are welcome!

+ Enes Altun [Main Author](https://altunenes.github.io)

### Current look of the GUI

![easylab.png](./docs/images/easylab.PNG)
