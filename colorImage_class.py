# Taller 1
# Procesamiento de imágenes y visión
# Manuela Bravo Soto

# IMPORTACIONES
import numpy as np # Del módulo numpy
import cv2 # Del módulo opencv-python
import os # Del módulo os

#CLASE colorImage
class colorImage:

    # CONSTRUCTOR
    # Recibe como parámetros la dirección de la imagen y su nombre
    def __init__(self,path,image_name):
        self.path = path # Se guarda la dirección de la imagen en self
        self.image_name = image_name # Se guarda el nombre de la imagen en self
        self.path_file = os.path.join(self.path, self.image_name) # Se unen los componentes para tener una dirección completa a la imagen
        self.imageRGB = cv2.imread(self.path_file) # Se lee la imagen de la dirección dada y se guarda en self

    # MÉTODO PARA IMPRIMIR PROPIEDADES DE LA IMAGEN
    def displayProperties(self):
        print('PROPIEDADES DE LA IMAGEN') # Imprime el título en consola
        print('- Ancho:', self.imageRGB.shape[0]) # Imprime el ancho de la imagen en consola
        print('- Alto:', self.imageRGB.shape[1]) # Imprime el alto de la imagen en consola

    # MÉTODO PARA CONVERTIR IMAGEN A GRISES
    def makeGray(self):
        self.gray = cv2.cvtColor(self.imageRGB, cv2.COLOR_BGR2GRAY) # Se convierte del espacio de color BGR a GRAY y se guarda en self
        return self.gray # Se retorna la imagen en grises

    # MÉTODO PARA TENER IMAGEN DE UN SOLO CANAL DE COLOR
    # Recibe como parámetro el canal de color de la imagen que se desea
    def colorizeRGB(self,color):
        # Si se quiere rojiza
        if color=='red':
            self.red = np.copy(self.imageRGB) # Copiar la imagen original en el canal del color rojo
            self.red[:, :, 0] = 0 # Se establece el color azul en cero
            self.red[:, :, 1] = 0 # Se establece el color verde en cero
            return self.red # Se retorna la imagen rojiza

        #Si se quiere azuloza
        elif color=='blue':
            self.blue = np.copy(self.imageRGB) # Copiar la imagen original en self en el canal del color azul
            self.blue[:, :, 1] = 0 # Se establece el color verde en cero
            self.blue[:, :, 2] = 0 # Se establece el color rojo en cero
            return self.blue # Se retorna la imagen azuloza

        # Si se quiere verdoza
        elif color == 'green':
            self.green = np.copy(self.imageRGB) # Copiar la imagen original en self en el canal del color verde
            self.green[:, :, 0] = 0 # Se establece el color azul en cero
            self.green[:, :, 2] = 0 # Se establece el color rojo en cero
            return self.green # Se retorna la imagen verdoza

    # MÉTODO PARA TENER IMAGEN CON TONOS RESALTADOS
    def makeHue(self):
        self.hsv = cv2.cvtColor(self.imageRGB, cv2.COLOR_BGR2HSV) # Se convierte del espacio de color BGR a HSV y se guarda en self
        self.hsv[:, :, 1] = 255 # Se lleva la componente S a un valor constante
        self.hsv[:, :, 2] = 255 # Se lleva la componente V a un valor constante
        self.rgb = cv2.cvtColor(self.hsv, cv2.COLOR_HSV2BGR) # Se convierte del espacio de color HSV a BGR y se guarda en self
        return self.rgb # Se retorna la imagen con los tonos resaltados
