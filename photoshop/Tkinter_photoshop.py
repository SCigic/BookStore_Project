"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Tkinter GUI modulom
                    Photoshop
"""


### TODO Blur event


from PIL import ImageTk, Image, ImageFilter
from tkinter import filedialog
import tkinter as tk


# DIO ZA GLOBALNE VARIJABLE
photo_filename = "algebra_ucionica.jpeg"
width = 800
height = 550
img = Image.open(photo_filename) 
img = img.resize((width, height)) # Var img treba podesiti da se ne otvara nego da je konstanta
slika_props = f"Format slike:\t{img.format}\nMod slike:\t{img.mode}\nDimenzije slike:\t{img.size}"


# DIO ZA FUNKCIJE
def openfilename():
    global label_slika, img, slika_props, photo_filename
    photo_filename = filedialog.askopenfilename(title ='Open image')
    img = Image.open(str(photo_filename))
    img = img.resize((width, height))
    slika_props = f"Format slike:\t{img.format}\nMod slike:\t{img.mode}\nDimenzije slike:\t{img.size}"
    slika_props_var.set(slika_props)
    label_slika = ImageTk.PhotoImage(img)
    lbl_slika['image'] = label_slika


def save_image():
    img.save(f'{photo_filename}_01.jpg','JPEG')


def reset():
    global label_slika, img
    img = Image.open(photo_filename)
    img = img.resize((width, height))
    label_slika = ImageTk.PhotoImage(img)
    lbl_slika['image'] = label_slika


def flip_left():
    global label_slika, img
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    label_slika = ImageTk.PhotoImage(img)
    lbl_slika['image'] = label_slika


def flip_top():
    global label_slika, img
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    label_slika = ImageTk.PhotoImage(img)
    lbl_slika['image'] = label_slika


def blur():
    global label_slika, img
    img = Image.open(photo_filename)
    img = img.resize((width, height))
    img = img.filter(ImageFilter.GaussianBlur(radius=int(blur_radius.get())))
    label_slika = ImageTk.PhotoImage(img)
    lbl_slika['image'] = label_slika
def set_blur_radius(value):
    blur_radius.set(int(value))
    blur()


def contour():
    global label_slika, img
    img = img.filter(ImageFilter.CONTOUR)
    label_slika = ImageTk.PhotoImage(img)
    lbl_slika['image'] = label_slika


def reljef():
    global label_slika, img
    img = img.filter(ImageFilter.EMBOSS)
    label_slika = ImageTk.PhotoImage(img)
    lbl_slika['image'] = label_slika


def edges():
    global label_slika, img
    img = img.filter(ImageFilter.FIND_EDGES)
    label_slika = ImageTk.PhotoImage(img)
    lbl_slika['image'] = label_slika


root = tk.Tk()
root.title('Algebra - Python Developer | Photoshop')


# DIO ZA DODAVANJE DRUGIH ELEMENATA GUI-a
# Labela za prikaz slike
label_slika = ImageTk.PhotoImage(img)
lbl_slika = tk.Label(root, image=label_slika)
lbl_slika.grid(row = 0, column=0, rowspan=9)


#Gumbi
btn_flip_left = tk.Button(root, text ='Flip left-right', command=flip_left)
btn_flip_left.grid(column=1, row = 0, sticky='W', padx=20)

btn_flip_top = tk.Button(root, text ='Flip top-botom', command=flip_top)
btn_flip_top.grid(column=1, row = 1, sticky='W', padx=20)

btn_blur = tk.Button(root, text ='Zamuti', command=blur)
btn_blur.grid(column=1, row = 2, sticky='SW', padx=20)
# -- -- Klizac za podesavanje zamicivanja
blur_radius = tk.IntVar()
blur_radius.set(1)
scl_blur = tk.Scale(root, 
                        orient = 'horizontal', 
                        variable = blur_radius, 
                        length = 150, 
                        from_ = 1, 
                        to = 20,
                        command=set_blur_radius)
scl_blur.grid(column=1, row=3, sticky='NW', padx=20, ipady=5)


btn_contour = tk.Button(root, text ='Contour', command=contour)
btn_contour.grid(column=1, row = 4, sticky='W', padx=20)

btn_reljef = tk.Button(root, text ='Reljef', command=reljef)
btn_reljef.grid(column=1, row = 5, sticky='W', padx=20)

btn_edges = tk.Button(root, text ='Edges', command=edges)
btn_edges.grid(column=1, row = 6, sticky='W', padx=20)


btn_save = tk.Button(root, text ='Save', command=save_image)
btn_save.grid(column=1, row = 7, sticky='W', padx=20)

btn_open = tk.Button(root, text ='Open', command=openfilename)
btn_open.grid(column=1, row = 7)

btn_reset = tk.Button(root, text ='Reset', command=reset)
btn_reset.grid(column=1, row = 7, sticky='E', padx=20)
   

slika_props_var = tk.StringVar()
slika_props_var.set(slika_props)
lbl_slika_props = tk.Label(root, 
                            textvariable=slika_props_var,
                            justify='left')
lbl_slika_props.grid(column=1, row=8, ipadx=5, padx=10)




root.mainloop()