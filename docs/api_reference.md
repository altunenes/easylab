### API REFERENCE
This page gives an overview of the functions.

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