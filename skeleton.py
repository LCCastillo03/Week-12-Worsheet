from enum import Enum
from datetime import date, time, datetime
from inspect import _void
class lugares (Enum):
    CASA_ESTUDIO = "Casa Estudio"
    BIBLIOTECA = "Biblioteca"
    BLOQUEB = "Bloque B"
    BLOQUEC = "Bloque C" 
    BLOQUED = "Bloque D"  
    BLOQUEG = "Bloque G"
    BLOQUEK = "Bloque K"
class PCExplorer:
  def __init__(self):
   nombre: str
  def disponibilidad(self, lugares):bool 
  def disponibilidad (self, lugares):int
  def disponibilidad (self):int 
  def disponibilidad (self):bool

class Prestamo:
  def __init__(self):
   fechaPrestamo:date
   horaPrestamo:date
   horaDevolucion:date
   ubicacion:Lugar
   codEst:int
   pcID:int
  def prestar(self, est, pc): _void

class Computador:
  def __init__(self):
   ID:int
  def cantidadPC(): int

class Lugar:
  def __init__(self):
   ubicacion:lugares
   piso:int
   disponibles:int
  def hayDispo():bool

class Estudiante (Persona):
  def __init__(self):
   user:str
   password:str
   codEst:int
  def verificarLogin():bool

class Persona:
 def __init__(self):
  nombre:str
  apellido:str
  edad:int


