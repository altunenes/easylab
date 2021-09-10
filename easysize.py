# ==========================================================================================================================================================
                                                                     #Just run the script
# ==========================================================================================================================================================


import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Image Resizer")
root.geometry("500x500")
root.configure(background="white")

# function to browse files
def browseFiles():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

# function to resize
def resize():
    global folder_path
    folder = folder_path.get()
    width = width_entry.get()
    height = height_entry.get()
    width = int(width)
    height = int(height)
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                path = os.path.join(root, file)
                img = Image.open(path)
                img = img.resize((width, height), Image.ANTIALIAS)
                img.save(path)
    messagebox.showinfo("Success", "Successfully Resized")

# function to rename
def rename():
    global folder_path
    folder = folder_path.get()
    files = os.listdir(folder)
    extension = extension_entry.get()


    for index, file in enumerate(files):
        os.rename(os.path.join(folder, file), os.path.join(folder, 'image'.join([str(index), '.'+f'{extension}'])))
    messagebox.showinfo("Success", "Successfully Renamed")

# function to delete
def delete():
    global folder_path
    folder = folder_path.get()
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                path = os.path.join(root, file)
                os.remove(path)
    messagebox.showinfo("Success", "Successfully Deleted")

# function to clear
def clear():
    folder_path.set("")
    width_entry.delete(0, END)
    height_entry.delete(0, END)

# function to exit
def exit():
    root.destroy()

# title
title = Label(root, text="Image Resizer", bg="white", font=("Times", 20, "bold"))
title.place(x=130, y=10)

# browse button
browse_button = Button(root, text="Browse", command=browseFiles, bg="white", font=("Times", 12, "bold"))
browse_button.place(x=130, y=50)

# folder path
folder_path = StringVar()
folder_path.set("")

# folder path label
folder_path_label = Label(root, textvariable=folder_path, bg="white", font=("Times", 12, "bold"))
folder_path_label.place(x=10, y=50)

# width label
width_label = Label(root, text="Width", bg="white", font=("Times", 12, "bold"))
width_label.place(x=10, y=100)

# width entry
width_entry = Entry(root, width=30, bg="white", font=("Times", 12, "bold"))
width_entry.place(x=100, y=100)

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
rename_button.place(x=140, y=260)


# delete button
delete_button = Button(root, text="Delete", command=delete, bg="white", font=("Times", 12, "bold"))
delete_button.place(x=130, y=300)

# clear button
clear_button = Button(root, text="Clear", command=clear, bg="white", font=("Times", 12, "bold"))
clear_button.place(x=130, y=350)

# exit button
exit_button = Button(root, text="Exit", command=exit, bg="white", font=("Times", 12, "bold"))
exit_button.place(x=130, y=400)

root.mainloop()
