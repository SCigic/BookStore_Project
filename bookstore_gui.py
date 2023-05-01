import tkinter


def button_save_handler():
    
    publisher_name = entry_publisher_name_var.get()
    author_first_name = entry_author_first_name_var.get()
    author_last_name = entry_author_last_name_var.get()
    book_title = entry_book_title_var.get()
    message = f"{publisher_name} {author_first_name} {author_last_name} {book_title}"

    label_display_message_var.set(message)

    button_cancel_handler() #nakon sto se snimi, zelimo da se sve resetira
   

def button_cancel_handler():
    entry_publisher_name_var.set("")
    entry_author_first_name_var.set("")
    entry_author_last_name_var.set("")
    entry_book_title_var.set("")


#inicijaliziramo glavni okvir
main_window = tkinter.Tk()
main_window.title("Algebra - Book Store")
main_window.geometry("600x400")


label_publisher_name = tkinter.Label(main_window, 
                                     text="Naziv izdavaca:",
                                     font=("Seqoe UI", 14))
label_publisher_name.grid(row=0, column=0, padx=10, pady=15, sticky=tkinter.E)

entry_publisher_name_var = tkinter.StringVar()
entry_publisher_name = tkinter.Entry(main_window,
                                     font=("Seqoe UI", 14),
                                     textvariable=entry_publisher_name_var)
entry_publisher_name.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky=tkinter.W)

label_author_first_name = tkinter.Label(main_window, 
                                        text="Ime autora:",
                                        font=("Seqoe UI", 14))
label_author_first_name.grid(row=1, column=0, padx=10, pady=5, sticky=tkinter.E)

entry_author_first_name_var = tkinter.StringVar()
entry_author_first_name = tkinter.Entry(main_window,
                                        font=("Seqoe UI", 14), 
                                        textvariable=entry_author_first_name_var)
entry_author_first_name.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky=tkinter.W)

label_author_last_name = tkinter.Label(main_window, 
                                       text="Prezime autora:",
                                       font=("Seqoe UI", 14))
label_author_last_name.grid(row=2, column=0, padx=10, pady=5, sticky=tkinter.E)

entry_author_last_name_var = tkinter.StringVar()
entry_author_last_name = tkinter.Entry(main_window,
                                       font=("Seqoe UI", 14),
                                       textvariable=entry_author_last_name_var)
entry_author_last_name.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky=tkinter.W)

label_book_title = tkinter.Label(main_window,
                                 text="Naziv knjige:",
                                 font=("Seqoe UI", 14))
label_book_title.grid(row=3, column=0, padx=10, pady=15, sticky=tkinter.E)

entry_book_title_var = tkinter.StringVar()
entry_book_title = tkinter.Entry(main_window,
                                 font=("Seqoe UI", 14),
                                 textvariable=entry_book_title_var)
entry_book_title.grid(row=3, column=1, columnspan=2, padx=10, pady=15, sticky=tkinter.W)





button_save = tkinter.Button(main_window,
                             text="Snimi",
                             font=("Seqoe UI", 12),
                             command=button_save_handler) #samo se navede f-ja (ne poziva se () jer bi se odmah izvrsila)
button_save.grid(row=4, column=1, padx=10, pady=15, sticky=tkinter.W)

button_cancel = tkinter.Button(main_window,
                               text="Odustani",
                               font=("Seqoe UI", 12),
                               command=button_cancel_handler)
button_cancel.grid(row=4, column=2, padx=10, pady=15, sticky=tkinter.E) 


label_display_message_var = tkinter.StringVar()
label_display_message_var.set("Labela za prikaz poruka")

label_display_message = tkinter.Label(main_window,
                                      textvariable=label_display_message_var,
                                      font=("Segoe UI", 18))
label_display_message.grid(row=5, column=0, columnspan=3,
                           padx=10, pady=15, sticky=tkinter.W)



#pokrecemo glavni prozor
main_window.mainloop()