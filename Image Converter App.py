import tkinter as imageConverter
from tkinter import filedialog
from PIL import Image

root = imageConverter.Tk()
root.title('Basic Image converter App')



def getJPEG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browse = imageConverter.Button(root, text="      Browse    ", command=getJPEG)
browse.place(relx=0.05, relwidth=0.4, relheight=0.4)


def JPEGToPNG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)


b2 = imageConverter.Button(root, text='JPEG to PNG', command=JPEGToPNG)
b2.place(relx=0.5, relwidth=0.5, relheight=0.4)

root.geometry("400x100")
root.mainloop()
