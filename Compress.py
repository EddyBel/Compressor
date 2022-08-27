from python.functions import IMG
import eel

eel.init('web')


@eel.expose
def compress_img(img_path, prefig, quality):
    return IMG.compress_Folder(path=img_path, prefig=prefig, quality=quality)


eel.start('index.html', size=(700, 600))
