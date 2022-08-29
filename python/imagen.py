from distutils import extension
from pickletools import optimize
from PIL import Image
import os


class IMG:

    def __init__(self, path, prefig, quality, output_path, extension, count):
        self.path = path
        self.output_path = output_path
        self.files = []
        self.prefig = prefig
        self.quality = quality
        self.extension = extension
        self.extensions_img = ['.jpg', '.png', '.jpeg']
        self.count = count

    # Obtener los archivos de la ruta
    def get_files_of_path(self):
        self.files = os.listdir(self.path)
        print(len(self.files))
        return self.files

    # Recorre todos los archivos
    def for_files_of_path(self, cb):

        # Recorrer la lista de archivos
        for file in self.files:
            if self.count == '':
                print()
            else:
                self.count = self.count + 1
            cb(file=file, path=self.path,
               prefig=self.prefig, quality=self.quality)
        
        print('Completado')
        
        return True

    # Comprimir todas las imagenes de una carpeta
    def compress_img(self, file, path, prefig, quality):

        # Separa el archivo en su extencion y nombre
        name, extension = os.path.splitext(path + file)

        # Rutas de archivo a utilizar
        input_path_img = os.path.join(path, file)
        if os.path.exists(self.output_path) == False:
            os.mkdir(self.output_path)

        output_path_img = os.path.join(self.output_path, prefig + file)

        # Revisa si es una imagen
        if extension in self.extensions_img:
            # Habre la imagen
            picture = Image.open(input_path_img)
            # Si la imagen es de tipo rgba convertir a rgb
            if picture.mode in ("RGBA", "P"):
                picture = picture.convert("RGB")
            # Guarda la imagen comprimida
            picture.save(output_path_img, optimize=True, quality=quality)
            # Imprime si la imagen se a comprimido
            print('imagen {name_file} comprimida'.format(name_file=file))

        return name

    # Convertir imagen
    def convert_img(self, file, path, prefig, quality):

        name, extension = os.path.splitext(file)

        # Rutas de archivo a utilizar
        input_path_img = os.path.join(path, file)
        if os.path.exists(self.output_path) == False:
            os.mkdir(self.output_path)

        count = self.count

        output_path_img = os.path.join(
            self.output_path, prefig + str(count) + name + self.extension)

       # Revisa si es una imagen
        if extension in self.extensions_img:
            # Habre la imagen
            picture = Image.open(input_path_img)
            # Si la imagen es de tipo rgba convertir a rgb
            if picture.mode in ("RGBA", "P"):
                picture = picture.convert("RGB")
            # Guarda la imagen convertida
            picture.save(output_path_img, quality=95)
            # Imprime si la imagen se a comprimido
            print('imagen {name_file} convertida a {name_output}'.format(
                name_file=file, name_output=name+self.extension))

        return name
