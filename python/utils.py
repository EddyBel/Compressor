import os
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.attributes('-topmost', True)
root.withdraw()  # Evita que la ventana de tkinter aparesca


class Utils:

    def concat_path(path, param):
        return os.path.join(path, param)
    
    def get_path_of_file(file):
        return os.path.abspath(file)

    def get_directory():
        return filedialog.askdirectory()

    def get_file():
        return filedialog.askopenfilename(initialdir='/', title='Selecciona tu archivo', filetypes=(
            ("jpeg files", ".jpg", ".jpeg"), ("png files", ".png"), ("all files", ".")))

    def get_files_to_directory(path):
        newPath = os.path.join(path)
        return os.listdir(newPath)

    def iteration_files(files, cb):
        status = []
        for file in files:
            try:
                cb(file)
                status.append(True)
            except:
                status.append(False)

        return status

    def reading_file(file, type):
        f = open(file, 'r')
        if type == 'one':
            content = f.readline()
        else:
            content = f.readlines()
        f.close()
        return content

    def writing_file(file, text):
        f = open(file, 'w')
        f.write(text)
        f.close()


if __name__ == '__main__':
    # print(Tools.path_base())
    # print(Tools.get_directory())
    # print(Tools.get_files_to_directory(
    #     'C:/Users/ben_9/OneDrive/Imágenes/prueba'))
    # Tools.writing_file('context.txt','Hello World1232132')
    # print(Tools.reading_file('context.txt','one'))
    print(Tools.get_path_of_file('context.txt'))