from enum import Enum #importamos Enum para poder crear un lista que contenga 
#los nombres de los lugares donde se pueden prestar computadores
from datetime import date, time, datetime #importamos date debido a que algunas
#de nuestras clases trabajan con dicho tipo de dato
from inspect import _void #importamod void debido a que algunas de nuestras 
#clases trabajaran con el

class lugares (Enum): #creamos la clase lugares que sera un enum
    CASA_ESTUDIO = "Casa Estudio" #le asignamos su nombre
    BIBLIOTECA = "Biblioteca" #le asignamos su nombre
    BLOQUEB = "Bloque B" #le asignamos su nombre
    BLOQUEC = "Bloque C" #le asignamos su nombre
    BLOQUED = "Bloque D"  #le asignamos su nombre
    BLOQUEG = "Bloque G" #le asignamos su nombre
    BLOQUEK = "Bloque K" #le asignamos su nombre

class PCExplorer: #cremaos la clase 
  def __init__(self): #definimos el constructor
   nombre: str #le damos un atributo
  def disponibilidad(self, lugares):bool #creamos una funcion
  def disponibilidad (self, lugares):int  #creamos una funcion
  def disponibilidad (self):int  #creamos una funcion
  def disponibilidad (self):bool #creamos una funcion
  pass

class Computador:  #creamos la clase computador
  def __init__(self): #definimos el constructor
   ID:int #le damos un atributo
  def cantidadPC(): int #creamos una funcion
  pass

class Persona: #creamos la clase persona
 def __init__(self): #definimos el constructor
  nombre:str #le damos un atributo
  apellido:str #le damos un atributo
  edad:int #le damos un atributo
  pass

class Estudiante (Persona): #creamos la clase estudiante la cual hereda de persona
  def __init__(self): #definimos el constructor
   user:str #le damos un atributo
   password:str #le damos un atributo
   codEst:int #le damos un atributo
  def verificarLogin():bool #creamos una funcion
  pass

class Prestamo (Estudiante, Computador): #creamos la clase prestamo, que hereda de estudiante y computador
  def __init__(self): #definimos el constructor
   fechaPrestamo:date #le damos un atributo
   horaPrestamo:date #le damos un atributo
   horaDevolucion:date #le damos un atributo
   ubicacion:Lugar #le damos un atributo
   codEst:int #le damos un atributo
   pcID:int #le damos un atributo
  def prestar(self, CodEst, ID): _void #creamos una funcion
  pass

class Lugar(Prestamo): #creamos la clase lugar
  def __init__(self): #definimos el constructor
   ubicacion:lugares #le damos un atributo
   piso:int #le damos un atributo
   disponibles:int #le damos un atributo
  def hayDispo():bool #creamos una funcion
  pass 



