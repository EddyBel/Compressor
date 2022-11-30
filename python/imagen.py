from distutils import extension
from pickletools import optimize
from PIL import Image
import os


class IMG:

    """This class contains all the image manipulation methods."""

    def __init__(self, path, prefig, quality, output_path, extension, count):

        """
        Constructor which has all the variables to use.

        Args:
            path: Path where the images will be searched.
            prefig: Extra name that the file will carry
            quality: Quality to which it will be compressed
            output_path: Destination or departure route
            extencion: Destination or departure route
            count: Total converted files counter
        """

        self.path = path
        self.output_path = output_path
        self.files = []
        self.prefig = prefig
        self.quality = quality
        self.extension = extension
        self.extensions_img = [".jpg", ".png", ".jpeg"]
        self.count = count

    def get_files_of_path(self):

        """Get all files by path.

        Returns:
            list[str] : List of files obtained
        """

        self.files = os.listdir(self.path)
        return self.files

    def for_files_of_path(self, cb):
        """Method that traverses the entire list of files and executes a callback for each file.

        Args:
            cb (function): Callback that receives (file, path, prefix and quality) parameters.

        Returns:
            Literal(True): Validate that everything was executed correctly.
        """

        for file in self.files:
            if self.count == "":
                pass
            else:
                self.count = self.count + 1
            cb(file=file, path=self.path, prefig=self.prefig, quality=self.quality)

        print("Completado")

        return True

    def compress_img(self, file, path, prefig, quality):
        """Compress the images.

        Args:
            file (str): file name.
            path (str): Path where the files are located.
            prefig (str): String or name that will be added to the output file.
            quality (int): Compression level.

        Returns:
            str: Name file


        Steps
        ------
        - Separate the file with its extension and name.
        - Define the routes to use and if the route does not exist, create it.
        - Define the routes to use and if the route does not exist, create it.
        - first validate that the file is an image, then access its image properties and validate that the image is rgb and not rgba if it is not so you convert it.
        - At the end it saves the image with the parameters of the class previously marked.
        - Print the conversion status

        """

        name, extension = os.path.splitext(path + file)  # Separate name

        input_path_img = os.path.join(path, file)  # Input path
        # Define the routes to use and if the route does not exist, create it.
        if os.path.exists(self.output_path) == False:
            os.mkdir(self.output_path)
        output_path_img = os.path.join(self.output_path, prefig + file)  # output path

        # Validate image
        if extension in self.extensions_img:
            picture = Image.open(input_path_img)  # open image

            # If the image is rgba type, convert it to rgb.
            if picture.mode in ("RGBA", "P"):
                picture = picture.convert("RGB")

            picture.save(
                output_path_img, optimize=True, quality=quality
            )  # Save to image
            print(
                "imagen {name_file} comprimida".format(name_file=file)
            )  # Print the conversion status

        return name

    def convert_img(self, file, path, prefig, quality):
        """Print the conversion status.

        Args:
            file (str): file name.
            path (str): Path where the files are located.
            prefig (str): String or name that will be added to the output file.
            quality (int): Compression level.

        Returns:
            str: Name file
        """

        name, extension = os.path.splitext(file)  # Separate name

        input_path_img = os.path.join(path, file)  # Input path
        # Define the routes to use and if the route does not exist, create it.
        if os.path.exists(self.output_path) == False:
            os.mkdir(self.output_path)
        count = self.count

        output_path_img = os.path.join(
            self.output_path, prefig + str(count) + name + self.extension
        )  # output path

        # Validate image
        if extension in self.extensions_img:
            picture = Image.open(input_path_img)  # Open image

            # If the image is rgba type, convert it to rgb.
            if picture.mode in ("RGBA", "P"):
                picture = picture.convert("RGB")

            picture.save(output_path_img, quality=95)  # Save to image

            print(
                "imagen {name_file} convertida a {name_output}".format(
                    name_file=file, name_output=name + self.extension
                )
            )  # Print the convert status

        return name
