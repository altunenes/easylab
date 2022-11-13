####################################### Easylab GUI #############################################
###################################### Author: Enes Altun #######################################
###################################### Verrsion 2.3 #############################################


import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import cv2
import numpy as np
from psychopy.visual import filters
from matplotlib import pyplot as plt
from rembg import remove
from ttkthemes import ThemedTk

root = Tk()
root.title("Easy Lab")
root.geometry("600x750")
root.configure(background='white')
messagebox.showinfo("Easylab", "Please contact github/altunenes or enesaltun2@gmail.com for any questions or suggestions")



# function to browse files
def browseFiles():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    messagebox.showinfo("Easylab", "Input folder is set to " + folder_path.get())
# browse file to save files
def outputfile():
    global output_path
    filename = filedialog.askdirectory()
    output_path.set(filename)
    messagebox.showinfo("Easylab", "Output path is set to " + output_path.get())
# function to resize
def resize():
    global folder_path
    folder = folder_path.get()
    output = output_path.get()
    width = width_entry.get()
    height = height_entry.get()
    width = int(width)
    height = int(height)
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            resized_image = cv2.resize(img, (width, height))
            cv2.imwrite(os.path.join(output, filename), resized_image)
            messagebox.showinfo("Success", "Resized images saved in output folder")
        else:
            messagebox.showerror("Error", "No such file or directory")
#function to remove background
def remove_background():
    global folder_path
    global output_path
    folder = folder_path.get()
    output = output_path.get()
    messagebox.showwarning("Warning", "Make sure that all images are in png format for best results, the process will take a long time if there are many images")
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            result = remove(img)
            cv2.imwrite(os.path.join(output, filename), result)
        else:
            messagebox.showerror("Error", "No such file or directory")
    messagebox.showinfo("Success", "Background removed images saved in output folder")

def blur():
    global folder_path
    folder = folder_path.get()
    output = output_path.get()
    kernelsize = int(kernelsize_entry.get())
    sigma = int(sigmasize_entry.get())

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(
                    ".bmp") or file.endswith(".tif"):
                path = os.path.join(root, file)
                img12 = cv2.imread(path)
                img12 = cv2.GaussianBlur(img12, (kernelsize, kernelsize), sigma)
                cv2.imwrite(os.path.join(output, file), img12)
    messagebox.showinfo("Success", "Successfully Blurred")

def change_extension():
    global folder_path
    folder = folder_path.get()
    output = output_path.get()
    extension = extension_entry.get()
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            name = filename.split(".")
            new_name = name[0] + "." + extension
            cv2.imwrite(os.path.join(output, new_name), img)
            messagebox.showinfo("Success", "Extensions changed, images saved in output folder")
        else:
            messagebox.showerror("Error", "No such file or directory")


def gray():
    global folder_path
    folder = folder_path.get()
    output = output_path.get()
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(
                    ".bmp") or file.endswith(".tif"):
                path = os.path.join(root, file)
                img = cv2.imread(path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(os.path.join(output, file), img)
    messagebox.showinfo("Success", "Successfully Converted to Gray")


# low spatial frequency
def lowfrequencydomain():
    global folder_path
    folder = folder_path.get()
    output = output_path.get()

    rms = float(rms_entry.get())
    cutoff = float(cutoff_entry.get())
    n = int(n_entry.get())
    width_SF = float(width_SF_entry.get())
    height_SF = float(height_SF_entry.get())

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(
                    ".bmp") or file.endswith(".tif"):
                path = os.path.join(root, file)
                img = cv2.imread(path, 0)
                raw_img = (img / 255.0) * 2.0 - 1.0
                rms = rms
                w, h = img.shape

                # make the mean to be zero
                raw_img = raw_img - np.mean(raw_img)
                # make the standard deviation to be 1
                raw_img = raw_img / np.std(raw_img)
                # make the standard deviation to be the desired RMS
                raw_img = raw_img * rms

                # convert to frequency domain
                img_freq = np.fft.fft2(raw_img)

                # calculate amplitude spectrum
                img_amp = np.fft.fftshift(np.abs(img_freq))

                lp_filt = filters.butter2d_lp(
                    size=raw_img.shape,
                    cutoff=cutoff,
                    n=n
                )

                img_filt = np.fft.fftshift(img_freq) * lp_filt

                # convert back to an image
                img_new = np.real(np.fft.ifft2(np.fft.ifftshift(img_filt)))

                # convert to mean zero and specified RMS contrast
                img_new = img_new - np.mean(img_new)
                img_new = img_new / np.std(img_new)
                img_new = img_new * rms

                # there may be some stray values outside of the presentable range; convert < -1
                # to -1 and > 1 to 1
                plt.figure(figsize=(width_SF, height_SF), dpi=1000)

                img_new = np.clip(img_new, a_min=-1.0, a_max=1.0)

                plt.imshow(img_new, cmap='gray')
                plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

                plt.axis("off")
                plt.rcParams['figure.facecolor'] = 'gray'
                plt.axis('tight')
                # save figures  to output folder
                plt.savefig(os.path.join(output, file), bbox_inches='tight', pad_inches=0,dpi=1000)
                plt.close()

    messagebox.showinfo("Success", "Successfully Converted to Frequency Domain")


# High Frequency Band Filter
def highfrequencybandfilter():
    global folder_path
    folder = folder_path.get()
    output = output_path.get()
    rms = float(rms_entry.get())
    cutoff = float(cutoff_entry.get())
    n = int(n_entry.get())
    width_SF = float(width_SF_entry.get())

    height_SF = float(height_SF_entry.get())

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(
                    ".bmp") or file.endswith(".tif"):
                path = os.path.join(root, file)
                img = cv2.imread(path)
                raw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                raw_img = (raw_img / 255.0) * 2.0 - 1.0
                # standart deviation of the contrast of the image
                rms = rms
                raw_img = raw_img - np.mean(raw_img)
                raw_img = raw_img / np.std(raw_img)
                raw_img = raw_img * rms

                img_freq = np.fft.fft2(raw_img)
                # size: width height
                hp_filt = filters.butter2d_hp(
                    size=raw_img.shape,
                    cutoff=cutoff,
                    n=n
                )

                img_filt = np.fft.fftshift(img_freq) * hp_filt

                # convert back to an image
                img_new = np.real(np.fft.ifft2(np.fft.ifftshift(img_filt)))

                # convert to mean zero and specified RMS contrast
                img_new = img_new - np.mean(img_new)
                img_new = img_new / np.std(img_new)
                img_new = img_new * rms
                plt.figure(figsize=(width_SF, height_SF), dpi=1000)

                img_new = np.clip(img_new, a_min=-1.0, a_max=1.0)
                plt.imshow(img_new, cmap='gray')
                plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
                plt.axis("off")
                plt.rcParams['figure.facecolor'] = 'gray'
                plt.axis('tight')
                plt.savefig(os.path.join(output, file), bbox_inches='tight', pad_inches=0,dpi=1000)
                plt.close()

    messagebox.showinfo("Success", "Successfully High Frequency Band Filter")

def rename():
    global folder_path
    folder = folder_path.get()
    files = os.listdir(folder)
    extension = extension_entry.get()
    prefix = prefix_entry.get()

    #if extension is empty raise error and tell user to enter extension
    if extension == "":
        messagebox.showerror("Error", "Please enter extension, e.g jpg or png; not .jpg or .png")
    else:
        for index, file in enumerate(files):
            os.rename(os.path.join(folder, file), os.path.join(folder, ''.join([prefix, str(index), '.' + f'{extension}'])))

        messagebox.showinfo("Success", "Successfully Renamed")

def histogram_equalization():
    global folder_path
    folder = folder_path.get()
    output = output_path.get()
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(
                    ".bmp") or file.endswith(".tif"):
                path = os.path.join(root, file)
                img = cv2.imread(path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.equalizeHist(img)
                cv2.imwrite(os.path.join(output, file), img)
    messagebox.showinfo("Success", "Successfully Histogram Equalized")

def cfa():
    global folder_path
    folder = folder_path.get()
    output = output_path.get()
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(
                    ".bmp") or file.endswith(".tif"):
                path = os.path.join(root, file)
                img = cv2.imread(path)
                (B,G,R) = cv2.split(img)
                (height, width) = img.shape[:2]
                cfa0 = np.empty((height, width), np.uint8)
                cfa1 = np.empty((height, width), np.uint8)
                cfa2 = np.empty((height, width), np.uint8)
                cfa3 = np.empty((height, width), np.uint8)

                cfa0[0::2, 0::2] = G[0::2, 0::2]
                cfa0[0::2, 1::2] = R[0::2, 1::2] 
                cfa0[1::2, 0::2] = B[1::2, 0::2] 
                cfa0[1::2, 1::2] = G[1::2, 1::2]

                cfa1[::, 0::2] = G[::, 0::2]
                cfa1[::2, 1::4] = R[::2, 1::4]  
                cfa1[1::2, 1::4] = B[1::2, 1::4]   
                cfa1[1::2, 3::4] = R[1::2, 3::4]  
                cfa1[::2, 3::4] = B[::2, 3::4] 

                cfa2[::4, 0::2] = G[::4, 0::2]
                cfa2[1::4, 0::2] = G[1::4, 0::2]
                cfa2[::4, 1::2] = R[::4, 1::2] 
                cfa2[1::4, 1::2] = B[1::4, 1::2]
                cfa2[2::4, 1::2] = G[2::4, 1::2]
                cfa2[3::4, 1::2] = G[3::4, 1::2]
                cfa2[2::4, 0::2] = R[2::4, 0::2] 
                cfa2[3::4, 0::2] = B[3::4, 0::2] 

                cfa3[::, 0::3] = G[::, 0::3] 
                cfa3[::, 1::3] = R[::, 1::3] 
                cfa3[::, 2::3] = B[::, 2::3] 
                cfa0 = cv2.cvtColor(cfa0, cv2.COLOR_GRAY2BGR)
                cfa0[0::2, 0::2, 0::2] = 0
                cfa0[0::2, 1::2, 0:2] = 0 
                cfa0[1::2, 0::2, 1:] = 0   
                cfa0[1::2, 1::2, 0::2] = 0 
                cfa1 = cv2.cvtColor(cfa1, cv2.COLOR_GRAY2BGR)
                cfa1[::, 0::2, 0::2] = 0
                cfa1[::2, 1::4,0:2] = 0
                cfa1[1::2, 1::4,1:] = 0
                cfa1[1::2, 3::4,:2] = 0  
                cfa1[::2, 3::4,1:] = 0
                cfa2 = cv2.cvtColor(cfa2, cv2.COLOR_GRAY2BGR)
                cfa2[0::4, 0::2, 0::2] = 0
                cfa2[1::4, 0::2, 0::2] = 0
                cfa2[0::4, 1::2, 0:2] = 0 
                cfa2[1::4, 1::2,1:] = 0
                cfa2[2::4, 1::2, 0::2] = 0
                cfa2[3::4, 1::2, 0::2] = 0 
                cfa2[2::4, 0::2, 0:2] = 0 
                cfa2[3::4, 0::2,1:] = 0
                cfa3 = cv2.cvtColor(cfa3, cv2.COLOR_GRAY2BGR)
                cfa3[::, 0::3, 0::2] = 0 
                cfa3[::, 1::3, :2] = 0 
                cfa3[::, 2::3, 1:] = 0  
                cv2.imwrite(os.path.join(output, 'cfa0_' + file), cfa0)
                cv2.imwrite(os.path.join(output, 'cfa1_' + file), cfa1)
                cv2.imwrite(os.path.join(output, 'cfa2_' + file), cfa2)
                cv2.imwrite(os.path.join(output, 'cfa3_' + file), cfa3)               
    messagebox.showinfo("Success", "Successfully Converted to CFA")

# function to exit
def exit():
    root.destroy()


folder_path = StringVar()
output_path = StringVar()

browsebutton = Button(root, text="Browse", command=browseFiles)
browsebutton.grid(row=0, column=2, padx=10, pady=10)

browsebutton2 = Button(root, text="Browse", command=outputfile)
browsebutton2.grid(row=1, column=2, padx=10, pady=10)

resizebutton = Button(root, text="Resize", command=resize)
resizebutton.grid(row=2, column=2, padx=10, pady=10)

removebutton = Button(root, text="Remove Background", command=remove_background)
removebutton.grid(row=3, column=2, padx=10, pady=10)

renamebutton = Button(root, text="Rename", command=rename)
renamebutton.grid(row=4, column=2, padx=10, pady=10)

histogrambutton = Button(root, text="Histogram Equalization", command=histogram_equalization)
histogrambutton.grid(row=5, column=2, padx=10, pady=10)

cfa_button = Button(root, text="CFA", command=cfa)
cfa_button.grid(row=6, column=2, padx=10, pady=10)

blurbutton = Button(root, text="Blur", command=blur)
blurbutton.grid(row=7, column=2, padx=10, pady=10)

changeextensionbutton = Button(root, text="Change Extension", command=change_extension)
changeextensionbutton.grid(row=8, column=2, padx=10, pady=10)

graybutton = Button(root, text="Gray", command=gray)
graybutton.grid(row=9, column=2, padx=10, pady=10)

lowfrequencydomainbutton = Button(root, text="Low Frequency Domain", command=lowfrequencydomain)
lowfrequencydomainbutton.grid(row=10, column=2, padx=10, pady=10)

highfrequencybandfilterbutton = Button(root, text="High Frequency Band Filter", command=highfrequencybandfilter)
highfrequencybandfilterbutton.grid(row=11, column=2, padx=10, pady=10)

exitbutton = Button(root, text="Exit", command=exit)
exitbutton.grid(row=12, column=2, padx=10, pady=10)

folder_label = Label(root, text="Input Folder")
folder_label.grid(row=0, column=0, padx=10, pady=10)

folder_entry = Entry(root, textvariable=folder_path)
folder_entry.grid(row=0, column=1, padx=10, pady=10)

output_label = Label(root, text="Output Folder")
output_label.grid(row=1, column=0, padx=10, pady=10)

output_entry = Entry(root, textvariable=output_path)
output_entry.grid(row=1, column=1, padx=10, pady=10)

width_label = Label(root, text="Width")
width_label.grid(row=2, column=0, padx=10, pady=10)

width_entry = Entry(root)
width_entry.grid(row=2, column=1, padx=10, pady=10)

height_label = Label(root, text="Height")
height_label.grid(row=3, column=0, padx=10, pady=10)

height_entry = Entry(root)
height_entry.grid(row=3, column=1, padx=10, pady=10)

extension_label = Label(root, text="Extension")
extension_label.grid(row=4, column=0, padx=10, pady=10)

extension_entry = Entry(root)
extension_entry.grid(row=4, column=1, padx=10, pady=10)

kernelsize_label = Label(root, text="Kernel Size")
kernelsize_label.grid(row=5, column=0, padx=10, pady=10)

kernelsize_entry = Entry(root)
kernelsize_entry.grid(row=5, column=1, padx=10, pady=10)

sigmasize_label = Label(root, text="Sigma Size")
sigmasize_label.grid(row=6, column=0, padx=10, pady=10)

sigmasize_entry = Entry(root)
sigmasize_entry.grid(row=6, column=1, padx=10, pady=10)

rms_label = Label(root, text="RMS")
rms_label.grid(row=7, column=0, padx=10, pady=10)

rms_entry = Entry(root)
rms_entry.grid(row=7, column=1, padx=10, pady=10)

cutoff_label = Label(root, text="Cutoff")
cutoff_label.grid(row=8, column=0, padx=10, pady=10)

cutoff_entry = Entry(root)
cutoff_entry.grid(row=8, column=1, padx=10, pady=10)

n_label = Label(root, text="N")
n_label.grid(row=9, column=0, padx=10, pady=10)

n_entry = Entry(root)
n_entry.grid(row=9, column=1, padx=10, pady=10)

width_SF_label = Label(root, text="Width SF")
width_SF_label.grid(row=10, column=0, padx=10, pady=10)

width_SF_entry = Entry(root)
width_SF_entry.grid(row=10, column=1, padx=10, pady=10)

height_SF_label = Label(root, text="Height SF")
height_SF_label.grid(row=11, column=0, padx=10, pady=10)

height_SF_entry = Entry(root)
height_SF_entry.grid(row=11, column=1, padx=10, pady=10)

prefix_label = Label(root, text="Rename Prefix")
prefix_label.grid(row=12, column=0, padx=10, pady=10)

prefix_entry = Entry(root)
prefix_entry.grid(row=12, column=1, padx=10, pady=10)



def info():
    messagebox.showinfo("Easylab", "RMS (Contrast), Cutoff and N (order of the Butterworth) for the spatial frequency. Width SF and Height SF is about the dpi of the screen. it will be multiplied with 1000; for example, if you want 800x800 pixels enter the 0.8 for both labels")

info_button = Button(root, text="Info", command=info)
info_button.grid(row=15, column=0, padx=10, pady=10)


def darkmode():
    root.configure(background="black")
    folder_label.configure(background="black", foreground="gray")
    output_label.configure(background="black", foreground="gray")
    width_label.configure(background="black", foreground="gray")
    height_label.configure(background="black", foreground="gray")
    extension_label.configure(background="black", foreground="gray")
    kernelsize_label.configure(background="black", foreground="gray")
    sigmasize_label.configure(background="black", foreground="gray")
    rms_label.configure(background="black", foreground="gray")
    cutoff_label.configure(background="black", foreground="gray")
    n_label.configure(background="black", foreground="gray")
    width_SF_label.configure(background="black", foreground="gray")
    height_SF_label.configure(background="black", foreground="gray")
    info_button.configure(background="black", foreground="gray")
    exitbutton.configure(background="black", foreground="gray")
    browsebutton.configure(background="black", foreground="gray")
    browsebutton2.configure(background="black", foreground="gray")
    resizebutton.configure(background="black", foreground="gray")
    removebutton.configure(background="black", foreground="gray")
    renamebutton.configure(background="black", foreground="gray")
    blurbutton.configure(background="black", foreground="gray")
    changeextensionbutton.configure(background="black", foreground="gray")
    graybutton.configure(background="black", foreground="gray")
    lowfrequencydomainbutton.configure(background="black", foreground="gray")
    highfrequencybandfilterbutton.configure(background="black", foreground="gray")
    prefix_label.configure(background="black", foreground="gray")
    histogrambutton.configure(background="black", foreground="gray")
    cfa_button.configure(background="black", foreground="gray")




def lightmode():
    root.configure(background="white")
    folder_label.configure(background="white", foreground="black")
    output_label.configure(background="white", foreground="black")
    width_label.configure(background="white", foreground="black")
    height_label.configure(background="white", foreground="black")
    extension_label.configure(background="white", foreground="black")
    kernelsize_label.configure(background="white", foreground="black")
    sigmasize_label.configure(background="white", foreground="black")
    rms_label.configure(background="white", foreground="black")
    cutoff_label.configure(background="white", foreground="black")
    n_label.configure(background="white", foreground="black")
    width_SF_label.configure(background="white", foreground="black")
    height_SF_label.configure(background="white", foreground="black")
    info_button.configure(background="white", foreground="black")
    exitbutton.configure(background="white", foreground="black")
    browsebutton.configure(background="white", foreground="black")
    browsebutton2.configure(background="white", foreground="black")
    resizebutton.configure(background="white", foreground="black")
    removebutton.configure(background="white", foreground="black")
    renamebutton.configure(background="white", foreground="black")
    blurbutton.configure(background="white", foreground="black")
    changeextensionbutton.configure(background="white", foreground="black")
    graybutton.configure(background="white", foreground="black")
    lowfrequencydomainbutton.configure(background="white", foreground="black")
    highfrequencybandfilterbutton.configure(background="white", foreground="black")
    prefix_label.configure(background="white", foreground="black")
    histogrambutton.configure(background="white", foreground="black")
    cfa_button.configure(background="white", foreground="black")


darkmode_button = Button(root, text="Dark Mode", command=darkmode)
darkmode_button.grid(row=1, column=7, padx=10, pady=10)

lightmode_button = Button(root, text="Light Mode", command=lightmode)
lightmode_button.grid(row=2, column=7, padx=10, pady=10)

def easylabgui():
    """
    function to open easylab
    """
    root.mainloop()