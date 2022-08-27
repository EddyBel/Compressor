from pickletools import optimize
from PIL import Image
import os
from python.tools import Tools

class IMG:

    # Comprimir todas las imagenes de una carpeta
    def compress_Folder(path, prefig, quality):
        files = os.listdir(path)  # Obtener todos los archivos de la carpeta

        try:
            # Crea la carpeta donde se almacenaran las imagenes comprimidas
            folder_output = Tools.concat_path(path, 'compress')
            os.mkdir(folder_output)

            # Recorrer la lista de archivos
            for file in files:
                # Obtener la extencion y la ruta completa del archivo
                name, extension = os.path.splitext(path + file)

                # Rutas de archivo a utilizar
                path_img = Tools.concat_path(path, file)
                output_path_img = Tools.concat_path(
                    folder_output, prefig + file)

                if extension in ['.jpg', '.png', '.jpeg']:
                    picture = Image.open(path_img)
                    picture.save(output_path_img,
                                 optimize=True, quality=quality)
                    print('imagen {name_file} comprimida'.format(
                        name_file=file))

            return True

        except:
            return False
