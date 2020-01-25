from tkinter import *
from PIL import  ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Learn To Code at gowebkit.com")
root.iconbitmap("c:/gui/gowebkit.ico")
root.geometry("700x300")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/gui", title="Select a File", filetypes=(("png files", "*.png"), ("All Files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()



my_button = Button(root, text="Open File", command=open).pack()

root.mainloop()