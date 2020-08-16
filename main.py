# Taller 1
# Procesamiento de imagenes y visión
# Manuela Bravo Soto

# IMPORTACIONES
import numpy as np # Del módulo numpy
import cv2 # Del módulo opencv-python
from colorImage_class import colorImage # De la clase colorImage

# DATOS INGRESADOS POR EL USUARIO
path = input('Ingrese la ruta de la imagen: ') # Solicitud al usuario de la dirección de la imagen ej: '/Users/mbrav/OneDrive/Desktop'

image_name = input('Ingrese el nombre de la imagen: ') # Solicitud al usuario del nombre de la imagen ej: 'lena.png'

# OBJETO
# Se crea el objeto imagen pasando como parámetro los datos ingresados por el usuario
# Los atributos de este objeto son los de la clase colorImage
Image = colorImage(path,image_name)

# PROPIEDADES
Image.displayProperties() # Se llama el método displayProperties para imprimir en consola las dimensiones de la imagen

# IMAGEN EN GRISES
Image_gray = Image.makeGray() # Se llama el método makeGray para convertir la imagen a grises
cv2.imshow('Image Gray', Image_gray) # Se muestra la imagen convertida a grises en pantalla

# IMAGEN ROJIZA
color = 'red' # Canal del color del cual se desea ver la imagen
Image_colorize = Image.colorizeRGB(color) # Se llama el método colorizeRGB para generar una imagen que solo tenga el canal definido
cv2.imshow('Image '+ color, Image_colorize) # Se muestra la imagen rojiza en pantalla

# IMAGEN CON TONOS RESALTADOS (HUE)
Image_hue = Image.makeHue() # Se llama el método makeHue para generar una imagen con los tonos resaltados
cv2.imshow('Image Hue', Image_hue) # Se muestra la imagen con los tonos resaltados en pantalla

cv2.waitKey(0) # Mostrar en pantalla las imagenes hasta que se oprima una tecla
