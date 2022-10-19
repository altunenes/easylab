# installation
+ Install easylab with pip:
```pip install easylab  ```

# Usage
easylab provides a GUI, so you don't need to write any code. Just open the gui with:

first import the easylab module:
```from easylab import easylab```
then open the gui with following command:
```easyLab.easylabgui()```

I also provide a online demo for the getting image names from the folder with Javascript. You can find it here:

https://altunenes.github.io/easylab/filenames

It also contains a jitter list generator for further processing. It is useful for some experiments to avoid problems with the constant durations.

# Other Scripts 

Easylab will be updated as solutions come to the problems encountered in the laboratory. These problems are mostly related to stimulant preparation and E-Prime. So some solutions probably only basic scripts and they will not add to the GUI.

List of other Scripts:

- **Filelistfromfolder.py** : Generates a list of filenames from a folder. You can find the information on the script. By the way, online demo that written in javascript do same thing.

- **e_prime_bullshit.py** : A strange problem with E-Prime. Sometimes, e-prime doesn't read the images ( We still don't know why). This basic script will fix the whole process.



# requirements
+ Python 3.6 or higher
+ Tkinter (for GUI)
+ psychopy (for the butterworth filter) 
+ opencv (for the filters, image processing)
+ numpy (for the mathematical operations)
+ matplotlib (for the image visualization)
+ rembg (for the background removal)
    