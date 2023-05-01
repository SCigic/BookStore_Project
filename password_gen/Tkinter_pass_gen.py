"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Tkinter GUI modulom
                    Password Generator

1. Korak - Organizirajmo Widgete tako da napisemo njihve nazive u komentarima
    te ovisno o hijerarhiji uvucemo te komentare ili koristimo minuse
    Na ovaj nacin ce nam biti lakse pisati kôd.
    VAZNO: Sam kôd, NE smijemo uvlaciti jer cemo tako dobiti blokove, a to nije ispravno
2. Korak - Napisati kôd za Widgete i dodati svaku funkciju tako da koriti pass kljucnu rijec
3. Korak - Napisati stvarni kôd za svaku funkciju

Nazivi variajbli Widgeta
Widget  Variable    Example
Label   lbl         lbl_name
Button	btn         btn_submit
Entry	ent         ent_age
Text	txt         txt_note
Frame	frm         frm_address
"""


import random as rd
import tkinter as tk



# SQLAlchemy klasa
#   engine
#   session



root = tk.Tk()
root.title('Algebra - Python Developer | Password Generator')
#root.geometry('600x400')


'''
id
password_text
username
'''


# Globalne varijable
prikazi_lozinku = tk.StringVar()
prikazi_lozinku.set('prikazi')
lozinka_var = tk.StringVar()
slova_var = tk.BooleanVar()
brojevi_var = tk.BooleanVar()
znakovi_var = tk.BooleanVar()


# DIO ZA FUNKCIJE
def set_duzina_lozinke(value):
    duzina_lozinke.set(int(value))

def generiraj_lozinku():
    # od 33 do 47 i 58 do 64 i 91 do 96     posebni znakovi
    # od 65 do 90 i 97 do 122               slova
    # od 48 do 57                           brojevi
    broj_znakova = duzina_lozinke.get()
    lozinka = '' 

    for znak in range(broj_znakova):
        if slova_var.get():
            kompleksnost = rd.choice([(65,90), (97,122)])
        elif brojevi_var.get():
            kompleksnost = rd.choice([(48,57)])
        elif znakovi_var.get():
            kompleksnost = rd.choice([(33,47), (58,64), (91,96)])
        else:
            kompleksnost = rd.choice([(33,122)])

        random_broj = rd.randint(*kompleksnost)
        znak = chr(random_broj)
        lozinka += znak
    
    lozinka_var.set(str(lozinka))


def resetiraj_postavke():
    lozinka_var.set('')


def set_prikaz_lozinke():
    if prikazi_lozinku.get() == 'prikazi':
        ent_lozinka.config(show="")
    else:
        ent_lozinka.config(show='*')

def kopiraj_lozinku():
    root.clipboard_clear()
    root.clipboard_append(
        f'{lozinka_var.get()}\n{ent_unser_name_var.get()}'
    )
    # pohrani u bazu




# DIO ZA DODAVANJE DRUGIH ELEMENATA GUI-a
# Frame Postavke
frm_postavke = tk.Frame(root).grid(column=0, columnspan=3, row=0, rowspan=3)

# --LabelFrame - Postavke
lbl_frm_postavke = tk.LabelFrame(frm_postavke, text="Postavke")
lbl_frm_postavke.columnconfigure((0, 1, 2), weight=1, minsize=90)
lbl_frm_postavke.grid(column=0, columnspan=3, row=0, padx=10, pady=10, ipadx=20, ipady=10)

# -- -- Checkbox
ch_box_slova = tk.Checkbutton(lbl_frm_postavke, 
                                text='Samo slova',
                                variable=slova_var).grid(column=0, row=0)
ch_box_brojevi = tk.Checkbutton(lbl_frm_postavke, 
                                text='Samo brojevi',
                                variable=brojevi_var).grid(column=1, row=0)
ch_box_znakovi = tk.Checkbutton(lbl_frm_postavke, 
                                text='Samo posebni znakovi',
                                variable=znakovi_var).grid(column=2, row=0)

# -- -- Radiobuttons
rb_prikazi_lozinku = tk.Radiobutton(lbl_frm_postavke, 
                                    text='Prikazi generiranu loziku', 
                                    variable=prikazi_lozinku, 
                                    command=set_prikaz_lozinke,
                                    value='prikazi').grid(column=0, row=1)
rb_sakrij_lozinku = tk.Radiobutton(lbl_frm_postavke, 
                                    text='Sakrij generiranu loziku', 
                                    variable=prikazi_lozinku, 
                                    command=set_prikaz_lozinke,
                                    value='sakrij').grid(column=2, row=1)
# -- -- Klizac za duzinu lozinke
duzina_lozinke = tk.IntVar()
duzina_lozinke.set(10)
scl_duzina = tk.Scale(lbl_frm_postavke, 
                        orient = 'horizontal', 
                        variable = duzina_lozinke, 
                        length = 300, 
                        from_ = 8, 
                        to = 40,
                        command=set_duzina_lozinke)
scl_duzina.grid(column=0, columnspan=3, row=2)


# UserName
lbl_user_name = tk.Label(lbl_frm_postavke,
                         text='Korisnicko ime')
lbl_user_name.grid(column=0, row=3, pady=20, sticky=tk.E)
ent_unser_name_var = tk.StringVar()
ent_unser_name = tk.Entry(lbl_frm_postavke,
                          textvariable=ent_unser_name_var)
ent_unser_name.grid(column=1, row=3, pady=20, sticky=tk.E)



# Gumbi
frm_action_buttons = tk.Frame(root).grid(column=0, columnspan=3, row=4, ipadx=20, ipady=20, padx=10, pady=10)
    # Generiraj Button
btn_generiraj = tk.Button(frm_action_buttons, text='Generiraj Lozinku', command=generiraj_lozinku)
btn_generiraj.grid(column=0, row=4)
    # Copy Button
btn_kopiraj = tk.Button(frm_action_buttons, text='Kopiraj Lozinku', command=kopiraj_lozinku)
btn_kopiraj.grid(column=1, row=4)
    # Reset
btn_resetiraj = tk.Button(frm_action_buttons, text='Resetiraj', command=resetiraj_postavke)
btn_resetiraj.grid(column=2, row=4)

# Frame Display Generated Password
frm_display_gen_password = tk.Frame(root).grid(column=0, columnspan=3, row=5, rowspan=2, ipadx=20, ipady=20, padx=10, pady=10)
    # Label Dusplay
lbl_password = tk.Label(frm_display_gen_password, text='Generirana Lozinka', font=('Segoe UI', 14))
lbl_password.grid(column=0, columnspan=3, row=5, ipadx=15)
    # Entry Dsplay
ent_lozinka = tk.Entry(frm_display_gen_password, 
                        textvariable=lozinka_var, 
                        justify='center', 
                        font=('Segoe UI', 16),
                        width=30, 
                        bd=0)
ent_lozinka.grid(column=0, columnspan=3, row=5, ipadx=15, ipady=10, padx=15, pady=10)




root.mainloop()
