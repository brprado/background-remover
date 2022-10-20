# user graphic interface to remove the image background
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sys
from rembg import remove

# create a window
window = Tk()
window.title("Background Remover")
window.geometry("500x500")
window.configure(background="white")

# create a label
Label(window, text="Background Remover", bg="white", fg="black", font="none 12 bold").pack()

# create a function to open the image
def open_img():
    global img
    img = Image.open(filedialog.askopenfilename(initialdir="/", title="Select an image", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"))))
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.pack()

# create a button to open the image
Button(window, text="Open Image", width=10, command=open_img).pack()

# create a function to remove the background save the image on the desktop

def remove_background(img_path, output_path):
    input_path = img_path
    output_path = output_path
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

def remove_bg():
    img_path = filedialog.askopenfilename(initialdir="/", title="Select an image", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    output_path = os.path.join(os.path.expanduser("~"), "Downloads", "output.png")
    remove_background(img_path, output_path)
    messagebox.showinfo("Success", "Background removed successfully!")


# create a button to remove the background
Button(window, text="Remove Background", width=15, command=remove_bg).pack()

# create a function to exit the window
def exit_window():
    window.destroy()

# create a button to exit the window
Button(window, text="Exit", width=5, command=exit_window).pack()

# run the window
window.mainloop()

# Path: code\bgremove.py