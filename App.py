#Importamos las librerías 
import tkinter as tk 
from tkinter import ttk
from tkinter import Entry, StringVar, Toplevel, messagebox
import tkinter.font as tkFont

#PARA CREAR LA INTERFAZ GRÁFICA 
#Creamos la ventana principal 
ventana = tk.Tk()
#Tamaño de la ventana:
Height = 918
Width = 520
ventana.geometry("918x520+230+100")
#Título de la ventana principal 
ventana.title("Pc Explorer")
#Tipo de letra 
Fuente_principal = tkFont.Font(family="Lucida Grande", size=11)
#Fondos
imagen = tk.PhotoImage(file="pp.png")
fondo= tk.Label(ventana,image = imagen).place(x=0,y=0)
credits = tk.PhotoImage(file = "credits.png")
opciones = tk.PhotoImage(file = "opciones.png")
Imagen_Regresar = tk.PhotoImage(file = "boton regresar.png")
Imagen_Regresar_Creditos = tk.PhotoImage( file = "regresar Creditos.png")
#Esta función valida que el usuario no ingrese letras, solo números 
def validate_code(text: str):
    return text.isdecimal()

#PARA CREAR LAS DEMÁS VENTANAS 
#Cada función es un menú 
def MainMenu():    
    #Para resetear la pantalla cuando uno se devuelva al menu principal
    for ele in ventana.winfo_children():
        ele.destroy()
    #Label que muestra la imagen de la pantalla principal
    label2 = tk.Label(ventana, image=imagen)
    label2.pack()
    #Botón creditos que hace que se cambie a la ventana de créditos 
    Boton_Creditos = tk.Button(ventana, text="Credits", width=8, height=1,font=Fuente_principal,command=Ventana_creditos, bg = "#FFFFFF",  bd=1, disabledforeground=None,  relief="flat", overrelief="raised")
    Boton_Creditos.place(x=618, y=65)
    #Para crear el textfile en el que el usuario ingresará su código
    codigo = StringVar() 
    #Aquí se valida lo que el usuario ingresa 
    codigoEntry = Entry(ventana, textvariable=codigo,bg= "#ECE7E6", width=35, validate="key", 
    validatecommand=(ventana.register(validate_code), "%S"))
    codigoEntry.place(x=480, y=385, width=100, height=30)
    #LOGIN
    def login():
        #Validar que el campo no este vacío
        Validar_codigo = codigoEntry.get()
        if(Validar_codigo == ""):
            Error = tk.Label(ventana, text = "Error, campos vacíos, intente de nuevo.", font = 20, disabledforeground="#F50743")
            Error.place(x = 627, y = 385) 
        else:  #si no esta vacío entonces se muestra la otra interfaz 
            Ventana_Opciones()

    #boton para ingresar o acceder 
    Button_login = tk.Button(ventana, text="Acceder", width=7, height=1, command=login,font=100)
    Button_login.place(x=500, y=430)

#Ventana de creditos
def Ventana_creditos():
    #Destruye o resetea todo lo que se encuentra en la ventana anterior 
    for ele in ventana.winfo_children():
        ele.destroy()
    #Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    #En el label se carga la imagen
    label1 = tk.Label(interfaz, image=credits)
    label1.pack()
    #Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command= MainMenu, width=7, height=1, font=100, image = Imagen_Regresar_Creditos, bg = "#FFFFFF", bd=1, disabledforeground=None,  relief="flat", overrelief="raised")
    Boton_Regreso.place(x = 847, y =449, width=63, height=64)

def Ventana_Opciones():
    #Destruye o resetea todo lo que se encuentra en la ventana anterior 
    for ele in ventana.winfo_children():
        ele.destroy()
    #Se crea la nueva Interfaz
    interfaz_opciones = tk.Canvas(ventana) 
    interfaz_opciones.pack()
    #En el label se carga la imagen
    label2 = tk.Label(interfaz_opciones, image=opciones)
    label2.pack()
    #Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command= MainMenu, width=7, height=1, font=100, image = Imagen_Regresar, bg = "#FFFFFF", bd=1, disabledforeground=None,  relief="flat", overrelief="raised")
    Boton_Regreso.place(x = 4, y =467, width=60, height=60)
    

MainMenu() 
#El mainloop lleva el registro de todo lo que está sucediendo en la ventana:
ventana.mainloop()

