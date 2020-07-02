# Deteccion del croma
from src.Deteccion_del_Croma import Deteccion_del_Croma
# Lineas y Dientes
import src.Metodos as Metod
# Colores del croma
from src.Nombres_Colores import Clasificacion_Colores
from src.DominantColors import main

# from multiprocessing.pool import ThreadPool
# from time import time, sleep

class Croma():

    def obtener_Caracteristicas(self, nombre):
        caracteristicas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        croma = Deteccion_del_Croma()
        img = croma.Definir_Area(nombre)
        
        vLineas  = 0
        vDientes = 0

        colores , porcentaje = main(nombre)
        
        valores_color = Clasificacion_Colores()
        caracteristicas = valores_color.clasificacion(caracteristicas, colores)
        
        vLineas = Metod.detectar_lineas(img)
        caracteristicas[5] = vLineas
        
        vDientes = Metod.buscar_dientes(img)
        caracteristicas[13] = vDientes

        return caracteristicas
       