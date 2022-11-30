import os
from tkinter import filedialog
from tkinter import Tk

# Create a tkinter room and overlay it on all windows.
root = Tk()
root.attributes("-topmost", True)
root.withdraw()  # Prevent the window from popping up.


class Utils:

    """Class that contains all the most used methods."""

    def concat_path(path, param):
        """Concatenate two strings to form the path.

        Args:
            path (str): Base path.
            param (str): parameter to concatenate.

        Returns:
            str: new path.
        """
        return os.path.join(path, param)

    def get_path_of_file(file):
        """Returns the absolute path of a file.

        Args:
            file (str): File to search.

        Returns:
            str: Absolute path of file
        """
        return os.path.abspath(file)

    def get_directory():
        """Create a folder selection window.

        Returns:
            str: Folder path.
        """
        return filedialog.askdirectory()

    def get_file():

        """Opens a file selection window, filtered for images only.

        Returns:
            str: Image path.
        """

        return filedialog.askopenfilename(
            initialdir="/",
            title="Selecciona tu archivo",
            filetypes=(
                ("jpeg files", ".jpg", ".jpeg"),
                ("png files", ".png"),
                ("all files", "."),
            ),
        )

    def get_files_to_directory(path):
        """Get all files from a path.

        Args:
            path (str): Path to search.

        Returns:
            list[str]: file list.
        """
        newPath = os.path.join(path)
        return os.listdir(newPath)

    def iteration_files(files, cb):

        """Go through the list of files and execute a callback in each iteration and if there is an error add it to the status array.

        Returns:
            list[]: List of the status of each file.
        """

        status = []
        for file in files:
            try:
                cb(file)
                status.append(True)
            except:
                status.append(False)

        return status

    def reading_file(file, type):

        """Open a file and read its contents.

        Returns:
            str: Returns the content of the file.
        """

        f = open(file, "r")
        if type == "one":
            content = f.readline()
        else:
            content = f.readlines()
        f.close()
        return content

    def writing_file(file, text):
        """Open a file and write to it.

        Args:
            file (str): File.
            text (str): Text to write.
        """
        f = open(file, "w")
        f.write(text)
        f.close()


if __name__ == "__main__":
    pass
