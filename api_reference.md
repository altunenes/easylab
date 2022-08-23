### API REFERENCE
This page gives an overview of the functions.

+[browseFiles](#browseFiles)
+[outputfile](#outputfile)
+[resize](#resize)
+[rename](#rename)
+[delete](#delete)
+[clear](#clear)
+[blur](#blur)
+[change_extension](#change_extension)
+[gray](#gray)
+[lowfrequencydomain](#lowfrequencydomain)
+[highfrequencybandfilter](#highfrequencybandfilter)
+[exit](#exit)
+[easylabgui](#easylabgui)

***browseFiles***<a name="browseFiles"></a>
browseFiles is a function that opens a file browser and lets you select a folder.

***outputfile***<a name="outputfile"></a>
outputfile is a function that opens a file browser and lets you select a folder for the exportin after processing.

***resize***<a name="resize"></a>
resize is a function that resizes all images in the folder to the desired size.

***rename***<a name="rename"></a>
rename is a function that renames all images in the folder following a pattern: 01image, 02image, 03image, ...

***delete***<a name="delete"></a>
delete is a function that deletes all images in the folder.

***clear***<a name="clear"></a>
clear the selected folder and all its contents.

***blur***<a name="blur"></a>
blur is a function that applies gaussian blur to all images in the folder with the given sigma and kernel size.

***change_extension***<a name="change_extension"></a>
change_extension is a function that changes all images' extensions to the desired extension.

***gray***<a name="gray"></a>
gray is a function that converts all images to GRAY.

***lowfrequencydomain***<a name="lowfrequencydomain"></a>
lowfrequencydomain is a function that applies low frequency filter to all images in the folder with the given cutoff frequency.
the function is based on the PsychoPy: [Psychopy](https://psychopy.org/api/filters.html). You can adjust RMS, cutoff frequency, and order of the filter.

**Warning**: Matplotlib doesn't work with pixels directly, but rather physical sizes and DPI. If you want to display a figure with certain pixel size, you need to know the DPI of your monitor. I added two labels; just enter your desired dimensions (it will be multiplied with 1000; for example, if you want 800x800 pixels enter the 0.8 for both labels).


***highfrequencybandfilter***<a name="highfrequencybandfilter"></a>
highfrequencybandfilter is a function that applies high frequency filter to all images in the folder with the given cutoff frequency.
the function is based on the PsychoPy: [Psychopy](https://psychopy.org/api/filters.html). You can adjust RMS, cutoff frequency, and order of the filter.

***exit***<a name="exit"></a>
exit is a function that exits the program.

***easylabgui***<a name="easylabgui"></a>
easylabgui is a function that starts the easylab.