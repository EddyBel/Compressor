from PIL import Image
import io
import base64
import os


def save_img_from_base64(
    img_base64: str, name: str, output: str, quality: int = 100, format: str = "JPEG"
):
    """This function will take the information from a base 64 decoded image and convert it to a readable buffer to create an image.

    Args:
        img_base64 (str): _description_
        output (str): _description_
        quality (int, optional): _description_. Defaults to 100.
        format (str, optional): _description_. Defaults to "JPEG".
    """

    split = img_base64.split(",")
    body_base64 = split[1]

    img_bytes = base64.b64decode(body_base64)
    img_buffer = io.BytesIO(img_bytes)
    img = Image.open(img_buffer)

    new_img = io.BytesIO()
    img.save(new_img, format=format, quality=quality)
    new_img.seek(0)

    os.path.dirname(output)
    os.makedirs(output, exist_ok=True)

    with open(os.path.join(output, name), "wb") as f:
        f.write(new_img.read())

    img_buffer.close()
    new_img.close()
