#Importamos las librerías 

from dataclasses import InitVar
import tkinter as tk 
from tkinter import Entry, StringVar, Toplevel, messagebox

 
    
#PARA CREAR LA INTERFAZ GRÁFICA 
#Creamos la ventana principal 
ventana = tk.Tk()
#Tamaño de la ventana:
Height = 918
Width = 520
ventana.geometry("918x520+230+100")
#Título de la ventana principal 
ventana.title("Pc Explorer")

#Fondos
imagen = tk.PhotoImage(file="pp.png")
fondo= tk.Label(ventana,image = imagen).place(x=0,y=0)
credits = tk.PhotoImage(file = "credits.png")
computadores = tk.PhotoImage(file = "comp.png")

#PARA CREAR LAS DEMÁS VENTANAS 
def MainMenu():    
    label2 = tk.Label(ventana, image=imagen)
    label2.pack()
    #boton creditos
    boton = tk.Button(ventana, text="Credits", width=7, height=1, command=Menu2,font=100)
    boton.place(x=618, y=65)
     #Para crear el textfile
    codigo = StringVar()
    codigoEntry = Entry(ventana, textvariable=codigo, bg= "#ECE7E6", width=35)
    codigoEntry.place(x=480, y=385, width=100, height=30)
    #LOGIN
    def login():
        #Validar que el campo no este vacío
        Validar_codigo = codigoEntry.get()
        if(Validar_codigo == ""):
            Error = tk.Label(ventana, text = "Error, Campos vacíos", font = 20)
            Error.place(x = 627, y = 385) 
        else: 
            for ele in ventana.winfo_children():
                ele.destroy()
            interfaz_Computadores = tk.Canvas(ventana) 
            interfaz_Computadores.pack()
            label2 = tk.Label(interfaz_Computadores, image=computadores)
            label2.pack()
    #boton login
    Button_login = tk.Button(ventana, text="Acceder", width=7, height=1, command=login,font=100)
    Button_login.place(x=500, y=430)

def Menu2():
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=credits)
    label1.pack()

MainMenu() 
#El mainloop lleva el registro de todo lo que está sucediendo en la ventana:
ventana.mainloop()

