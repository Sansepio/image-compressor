from PIL import Image

import os

imgFolder = input("Introduce el directorio de las imagenes a comprimir: ")

compressed = input("Introduce el directorio donde desea guardar las imagenes: ")

if __name__ == "__main__":
    for filename in os.listdir(imgFolder):
        name, extension = os.path.splitext(imgFolder + filename)
        

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(imgFolder + filename)
            picture.save(compressed + filename, optimize=True , quality=60)
        else:
            print("directorio no valido")

print("imagenes guardadas en " + compressed)