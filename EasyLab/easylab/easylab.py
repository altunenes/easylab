import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import cv2
import numpy as np
from psychopy.visual import filters
from matplotlib import pyplot as plt

root = Tk()
root.title("Easy Lab")
root.geometry("600x750")
root.configure(background="white")

#show the author name before the program starts
messagebox.showinfo("Easylab", "Please contact github/altunenes or enesaltun2@gmail.com for any questions or suggestions")


# function to browse files
def browseFiles():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)


# browse file to save files

def outputfile():
    global output_path
    filename = filedialog.askdirectory()
    output_path.set(filename)


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


# function to rename
def rename():
    global folder_path
    folder = folder_path.get()
    files = os.listdir(folder)
    extension = extension_entry.get()

    for index, file in enumerate(files):
        os.rename(os.path.join(folder, file), os.path.join(folder, 'image'.join([str(index), '.' + f'{extension}'])))
        # os.rename(os.path.join(folder, file), os.path.join(folder, 'image'.join([str(index), '.' + f'{extension}'])))

    messagebox.showinfo("Success", "Successfully Renamed")


# function to delete
def delete():
    global folder_path
    folder = folder_path.get()
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(
                    ".BMP") or file.endswith(".tif"):
                path = os.path.join(root, file)
                os.remove(path)
    messagebox.showinfo("Success", "Successfully Deleted")


# function to clear
def clear():
    folder_path.set("")
    width_entry.delete(0, END)
    height_entry.delete(0, END)


def blur():
    global folder_path
    folder = folder_path.get()
    kernelsize = int(kernelsize_entry.get())
    sigma = int(sigmasize_entry.get())

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(
                    ".bmp") or file.endswith(".tif"):
                path = os.path.join(root, file)
                img12 = cv2.imread(path)
                img12 = cv2.GaussianBlur(img12, (kernelsize, kernelsize), sigma)

                cv2.imwrite(path, img12)
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
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(
                    ".bmp") or file.endswith(".tif"):
                path = os.path.join(root, file)
                img = cv2.imread(path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(path, img)
    messagebox.showinfo("Success", "Successfully Converted to Gray")


# low spatial frequency
def lowfrequencydomain():
    global folder_path
    folder = folder_path.get()
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
                plt.figure(figsize=(width_SF, height_SF), dpi=100)

                img_new = np.clip(img_new, a_min=-1.0, a_max=1.0)

                plt.imshow(img_new, cmap='gray')
                plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

                plt.axis("off")
                plt.rcParams['figure.facecolor'] = 'gray'
                plt.axis('tight')
                # save figures with different names
                plt.savefig(path, bbox_inches='tight', pad_inches=0, dpi=1000)  # , bbox_inches='tight', pad_inches=0
                plt.close()

    messagebox.showinfo("Success", "Successfully Converted to Frequency Domain")


# High Frequency Band Filter
def highfrequencybandfilter():
    global folder_path
    folder = folder_path.get()
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
                plt.figure(figsize=(width_SF, height_SF), dpi=100)

                img_new = np.clip(img_new, a_min=-1.0, a_max=1.0)
                plt.imshow(img_new, cmap='gray')
                plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
                plt.axis("off")
                plt.rcParams['figure.facecolor'] = 'gray'
                plt.axis('tight')
                # save figures with different names
                plt.savefig(path, bbox_inches='tight', pad_inches=0, dpi=1000)  # , bbox_inches='tight', pad_inches=0
                plt.close()

    messagebox.showinfo("Success", "Successfully High Frequency Band Filter")


# function to exit
def exit():
    root.destroy()


# title
title = Label(root, text="Select the folder", bg="white", font=("Times", 12, "bold"))
title.place(x=110, y=1)

# browse button
browse_button = Button(root, text="Browse", command=browseFiles, bg="white", font=("Times", 12, "bold"))
browse_button.place(x=130, y=20)

# output button
output_button = Button(root, text="Output", command=outputfile, bg="white", font=("Times", 12, "bold"))
output_button.place(x=130, y=60)
# folder path
folder_path = StringVar()
folder_path.set("")
# output path
output_path = StringVar()
output_path.set("")

# folder path label
folder_path_label = Label(root, textvariable=folder_path, bg="white", font=("Times", 12, "bold"))
folder_path_label.place(x=10, y=50)

# width label
width_label = Label(root, text="Width", bg="white", font=("Times", 12, "bold"))
width_label.place(x=10, y=100)

# width entry
width_entry = Entry(root, width=30, bg="white", font=("Times", 12, "bold"))
width_entry.place(x=100, y=100)

# sigma entry
sigmasize_entry = Entry(root, width=10, bg="white", font=("Times", 12, "bold"))
sigmasize_entry.place(x=360, y=260)

# sigma label
sigmasize_label = Label(root, text="Sigma", bg="white", font=("Times", 12, "bold"))
sigmasize_label.place(x=300, y=260)

# kernelsize entry
kernelsize_entry = Entry(root, text="kernel", width=10, bg="white", font=("Times", 12, "bold"))
kernelsize_entry.place(x=360, y=300)

# kernelsize label
kernelsize_label = Label(root, text="Kernel Size", bg="white", font=("Times", 12, "bold"))
kernelsize_label.place(x=270, y=300)

# rms entry
rms_entry = Entry(root, width=10, bg="white", font=("Times", 12, "bold"))
rms_entry.place(x=360, y=340)

# rms label
rms_label = Label(root, text="RMS", bg="white", font=("Times", 12, "bold"))
rms_label.place(x=300, y=340)
# cutoff entry
cutoff_entry = Entry(root, width=10, bg="white", font=("Times", 12, "bold"))
cutoff_entry.place(x=360, y=380)
# cutoff label
cutoff_label = Label(root, text="Cutoff", bg="white", font=("Times", 12, "bold"))
cutoff_label.place(x=300, y=380)
# n entry
n_entry = Entry(root, width=10, bg="white", font=("Times", 12, "bold"))
n_entry.place(x=360, y=420)
# n label
n_label = Label(root, text="N", bg="white", font=("Times", 12, "bold"))
n_label.place(x=300, y=420)

# width_SF entry
width_SF_entry = Entry(root, width=6, bg="white", font=("Times", 8, "italic"))
width_SF_entry.place(x=500, y=420)
# width_SF label
width_SF_label = Label(root, text="Width SF", bg="white", font=("Times", 8, "italic"))
width_SF_label.place(x=450, y=420)
# height_SF entry
height_SF_entry = Entry(root, width=6, bg="white", font=("Times", 8, "italic"))
height_SF_entry.place(x=505, y=440)
# height_SF label
height_SF_label = Label(root, text="Height SF", bg="white", font=("Times", 8, "italic"))
height_SF_label.place(x=450, y=440)

# extension entry
extension_label = Label(root, text="extension", bg="white", font=("Times", 12, "bold"))
extension_label.place(x=300, y=50)

# extension entry
extension_entry = Entry(root, width=5, bg="white", font=("Times", 12, "bold"))
extension_entry.place(x=400, y=50)

# height label
height_label = Label(root, text="Height", bg="white", font=("Times", 12, "bold"))
height_label.place(x=10, y=150)

# height entry
height_entry = Entry(root, width=30, bg="white", font=("Times", 12, "bold"))
height_entry.place(x=100, y=150)

width_label = Label(root, text="Width", bg="white", font=("Times", 12, "bold"))
width_label.place(x=10, y=100)

# resize button
resize_button = Button(root, text="Resize", command=resize, bg="white", font=("Times", 12, "bold"))
resize_button.place(x=130, y=200)

# rename button
rename_button = Button(root, text="Rename", command=rename, bg="white", font=("Times", 12, "bold"))
rename_button.place(x=130, y=250)

# rename button
extention = Button(root, text="exstention", command=rename, bg="white", font=("Times", 12, "bold"))
rename_button.place(x=130, y=260)

# delete button
delete_button = Button(root, text="Delete", command=delete, bg="white", font=("Times", 12, "bold"))
delete_button.place(x=130, y=300)

# clear button
clear_button = Button(root, text="Clear", command=clear, bg="white", font=("Times", 12, "bold"))
clear_button.place(x=130, y=350)

# blur button
blur_button = Button(root, text="Blur", command=blur, bg="white", font=("Times", 12, "bold"))
blur_button.place(x=370, y=200)

# gray button
gray_button = Button(root, text="Gray", command=gray, bg="white", font=("Times", 12, "bold"))
gray_button.place(x=280, y=200)

# lowfrequencydomain button
lowfrequencydomain_button = Button(root, text="Low Frequency Domain", command=lowfrequencydomain, bg="white",
                                   font=("Times", 12, "bold"))
lowfrequencydomain_button.place(x=240, y=445)

# change_extension button
change_extension_button = Button(root, text="Change Extension", command=change_extension, bg="white",
                                 font=("Times", 8, "bold"))
change_extension_button.place(x=130, y=230)

# highfrequencybandfilter button
highfrequencybandfilter_button = Button(root, text="high Frequency Band Filter", command=highfrequencybandfilter,
                                        bg="white", font=("Times", 12, "bold"))
highfrequencybandfilter_button.place(x=240, y=470)

# exit button
exit_button = Button(root, text="Exit", command=exit, bg="white", font=("Times", 12, "bold"))
exit_button.place(x=130, y=400)


def easylabgui():
    """
    function to open easylab
    """
    root.mainloop()