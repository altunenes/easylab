### API REFERENCE
This page gives an overview of the functions.

### Modules needed to run the GUI

python 3.6 or higher
psychopy
numpy
opencv-python
matplotlib
tkinter
rembg

### Functions
+[browseFiles](#browseFiles)

+[outputfile](#outputfile)

+[resize](#resize)

+[rename](#rename)

+[blur](#blur)

+[change_extension](#change_extension)

+[Histogram equalization](#Histogram-equalization)

+[gray](#gray)

+[lowfrequencydomain](#lowfrequencydomain)

+[highfrequencybandfilter](#highfrequencybandfilter)

+[remove_background](#remove_background)

+[cfa](#cfa)

+[exit](#exit)

+[easylabgui](#easylabgui)

***browseFiles***<a name="browseFiles"></a>
browseFiles is a function that opens a file browser and lets you select a folder.

***outputfile***<a name="outputfile"></a>
outputfile is a function that opens a file browser and lets you select a folder for the exportin after processing.

***resize***<a name="resize"></a>
resize is a function that resizes all images in the folder to the desired size.

***rename***<a name="rename"></a>
rename is a function that renames all images in the folder with desired prefix. Don't forget to add extension if you use rename option. If you starts with a number, it will be added to the end of the name. For example, if you use 1 as prefix, the image name will be 1_1.jpg, 1_2.jpg, 1_3.jpg, etc. 

***blur***<a name="blur"></a>
blur is a function that applies gaussian blur to all images in the folder with the given sigma and kernel size.
Sigma is the standard deviation of the gaussian kernel. Kernel size is the size of the kernel. It should be odd. For example, 3, 5, 7, etc.

***change_extension***<a name="change_extension"></a>
change_extension is a function that changes all images' extensions to the desired extension.

***gray***<a name="gray"></a>
gray is a function that converts all images to GRAY.

***Histogram equalization***<a name="Histogram-equalization"></a>
Histogram equalization is a function that applies histogram equalization to all images in the folder. It is a method in which the image is transformed so that the intensity distribution is uniform. This method is useful to improve the contrast of images, especially when the usable data of the image is represented by close contrast values. Function uses cv2.equalizeHist().

***lowfrequencydomain***<a name="lowfrequencydomain"></a>
lowfrequencydomain is a function that applies low frequency filter to all images in the folder with the given cutoff frequency.
the function is based on the PsychoPy: [Psychopy](https://psychopy.org/api/filters.html). You can adjust RMS, cutoff frequency, and order of the filter.

Since this code is based on PsychoPy and little is known about the filter I would like to explain little bit more about what this code actually doing. Same words also same with the highfrequencybandfilter function.

This code defines a function named butter2d_lp that creates a 2D lowpass Butterworth filter. A lowpass filter is a type of filter that attenuates (or reduces) the amplitude of high frequency signals, while allowing low frequency signals to pass through. A Butterworth filter is a type of lowpass filter that has a smooth frequency response and provides a constant gain in the passband (i.e., the frequency range that is passed through the filter).

The butter2d_lp function takes three parameters: size, cutoff, and n. The size parameter specifies the size of the filter kernel, which is a 2D array of values that defines the filter. The cutoff parameter specifies the relative cutoff frequency of the filter, which is the frequency at which the filter begins to attenuate the high frequency signals. The n parameter specifies the order of the filter, which determines how sharp the transition is between the passband and the stopband (i.e., the frequency range that is attenuated by the filter).

The butter2d_lp function starts by checking if the cutoff and n parameters are valid. The cutoff parameter must be a float between 0 and 1.0, and the n parameter must be an integer greater than or equal to 1. If either of these conditions is not met, the function raises a ValueError to indicate that an invalid parameter was provided.

Next, the butter2d_lp function creates a 2D grid of values using the numpy.linspace function from the NumPy library. This grid defines the spatial coordinates of the filter kernel, and is used to calculate the distance of each pixel from the center of the kernel.

The function then calculates the radius of each pixel relative to the center of the kernel using the numpy.sqrt function, which calculates the square root of the sum of the squares of the x and y coordinates of each pixel. This radius is used to calculate the filter kernel, which is defined as the inverse of the sum of the radius squared and the cutoff parameter raised to the power of twice the n parameter.

Finally, the butter2d_lp function returns the filter kernel, which is a 2D array of values that defines the lowpass Butterworth filter. This kernel can be applied to an image using a convolution operation to filter the image and attenuate its high frequency content.

The cutoff parameter specifies the relative cutoff frequency of the filter, which is the frequency at which the filter begins to attenuate the high frequency signals. In the context of image processing, the cutoff frequency of a filter can be thought of as the number of cycles per pixel that the filter will pass through without attenuating.

For example, if the cutoff parameter is set to 0.5, the filter will pass through frequencies up to 0.5 cycles/pixel without attenuating them. This means that any frequencies above 0.5 cycles/pixel will be attenuated by the filter, while frequencies below 0.5 cycles/pixel will be passed through without being affected.

Overall, the cutoff parameter in the butter2d_lp function is related to the cycles/pixel of an image because it determines the frequencies that the filter will pass through without attenuating. By setting the cutoff parameter to a specific value, you can control the range of frequencies that the filter will pass through, and therefore control the amount of attenuation applied to the high frequency content of an image.


### Difference between Fourier Transform and Butterworth Filter

The main difference between a Butterworth filter and a Fourier filter in the context of image processing is their frequency response. A Butterworth filter has a smooth frequency response that provides a constant gain in the passband (i.e., the frequency range that is passed through the filter). This means that the amplitude of the high frequency content of an image is not attenuated by the filter, and the filter provides a smooth transition from the passband to the stopband (i.e., the frequency range that is attenuated by the filter).

In contrast, a Fourier filter has a frequency response that is determined by the Fourier transform of the filter kernel. This means that the amplitude of the high frequency content of an image can be attenuated by the filter, and the filter may not provide a smooth transition from the passband to the stopband.

Another difference between a Butterworth filter and a Fourier filter in the context of image processing is their implementation. A Butterworth filter can be implemented using a simple mathematical formula, which makes it easy to understand and modify. In contrast, a Fourier filter is implemented using the Fourier transform, which is a complex mathematical operation that requires more computation and may be harder to understand and modify.

Overall, the main difference between a Butterworth filter and a Fourier filter in the context of image processing is their frequency response and implementation. A Butterworth filter provides a smooth frequency response and is easy to implement, while a Fourier filter has a frequency response determined by the Fourier transform and may require more computation to implement.

Easylab using Butterworth filter instead of Fourier. 


**Warning**: Matplotlib doesn't work with pixels directly, but rather physical sizes and DPI. If you want to display a figure with certain pixel size, you need to know the DPI of your monitor. I added two labels; just enter your desired dimensions (it will be multiplied with 1000; for example, if you want 800x800 pixels enter the 0.8 for both labels).


***highfrequencybandfilter***<a name="highfrequencybandfilter"></a>
highfrequencybandfilter is a function that applies high frequency filter to all images in the folder with the given cutoff frequency.
the function is based on the PsychoPy: [Psychopy](https://psychopy.org/api/filters.html). You can adjust RMS, cutoff frequency, and order of the filter.

***remove_background***<a name="remove_background"></a>
remove_background is a function that removes the background from all images in the folder. It is based on the rembg package: [rembg](https://github.com/danielgatis/rembg)

***cfa***<a name="cfa"></a>
cfa is a function that converts all images to CFA which stands for Color Filter Array or color filter mosaic. It is a method of color filter array photography. There are 4 types of CFA.

***exit***<a name="exit"></a>
exit is a function that exits the program.

***easylabgui***<a name="easylabgui"></a>
easylabgui is a function that starts the easylab.