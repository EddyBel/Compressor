from python.imagen import IMG
from python.utils import Utils
from functions.img import save_img_from_base64
import os
import eel

eel.init("web")


@eel.expose
def get_output_path():
    system = os.name
    outputFolder = "CompressIMG"

    if system == "posix":  # Linux or macOS
        return os.path.join(os.path.expanduser("~/Documents"), outputFolder)
    elif system == "nt":  # Windows
        return os.path.join(os.path.expanduser("~"), "Documents", outputFolder)


@eel.expose
def compress_img(data_img: str, name_img: str, output: str, quality: int):
    save_img_from_base64(
        img_base64=data_img, name=name_img, output=output, quality=quality
    )
    return {"name": name_img, "status": True}


eel.start("index.html", size=(1000, 600))
