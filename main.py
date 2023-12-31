from tkinter import *

win = Tk()
win.geometry("500x500")
win.title("My First GUI")
win.resizable(0,0)

#Pantallas
def home():
    #home_label = Label(win, text="Home")
    home_label.config(
        fg="white",
        bg="black",
        font=("Open Sans", 30),
        padx=200,
        pady=20
    )
    home_label.grid(row=0, column=0, columnspan=2)
    add_label.grid_remove()
    add_frame.grid_remove()
   

def add():
    #Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Open Sans", 30),
        padx=110,
        pady=20,
        
        
    )
    add_label.grid(row=0, column=0, columnspan=3, sticky=W)

    #Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    add_separator.grid(row=4, column=1)

    button.grid(row=5, column=1, sticky=NW)
    button.config(
        padx=15,
        pady=5,
        bg="black",
        fg="white"
    )
    home_label.grid_remove()

#variables importantes
name_data = StringVar()
price_data = StringVar()
description_data = StringVar()


#Definir campos de pantalla HOME
home_label = Label(win, text="Home")

#Definir campos de pantalla ADD
add_label = Label(win, text="Añadir producto")

#Campos de formulario
add_frame = Frame(win)

add_name_label = Label(add_frame, text="Nombre del producto:")
add_name_entry = Entry(add_frame, textvariable="name_data")
add_name_entry.focus()
add_name_entry.config(justify="left", state="normal")

add_price_label = Label(add_frame, text="Precio del producto:")
add_price_entry = Entry(add_frame, textvariable="price_data")

add_description_label = Label(add_frame, text="Descripción del producto:")
add_description_entry = Text(add_frame)
add_description_entry.config(
    width=30,
    height=5,
    font=("Arial", 12),
    padx=5,
    pady=5
)

add_separator = Label(add_frame)

button = Button(add_frame, text="Guardar")

#Cargar la pantalla de inicio
home()

# Menu Superior
menu_superior = Menu(win)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Salir", command=win.quit)
#cargar menu
win.config(menu=menu_superior)


win.mainloop()


