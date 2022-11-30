from python.imagen import IMG
from python.utils import Utils
import eel

eel.init("web")


@eel.expose
def compress_img_to_folder(path, prefig, quality, output):
    try:
        Folder = IMG(
            path=path,
            prefig=prefig,
            quality=quality,
            output_path=output,
            extension="",
            count="",
        )
        Folder.get_files_of_path()
        Folder.for_files_of_path(Folder.compress_img)
        return True
    except:
        return False


@eel.expose
def convert_img_to_folder(path, prefig, quality, output, extension, count):
    try:
        Folder = IMG(
            path=path,
            prefig=prefig,
            quality=quality,
            output_path=output,
            extension=extension,
            count=count,
        )
        Folder.get_files_of_path()
        Folder.for_files_of_path(Folder.convert_img)
        return True
    except:
        return False


@eel.expose
def open_select_folder():
    return Utils.get_directory()


eel.start("index.html", size=(1000, 600))
