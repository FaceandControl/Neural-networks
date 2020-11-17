from PIL import Image
from Model.EnumPerson import EnumPerson
import numpy as np
import os

def Parse():

    X = []
    Y = []

    dir_name = EnumPerson


    def rec_path(path):
        if os.path.basename(path) != "origin" and \
                os.path.basename(path) != "check":
            global dir_name
            if os.path.isdir(path):
                lst_dir = os.listdir(path)
                if os.path.basename(path) == "anne_hathaway":
                    dir_name = EnumPerson.ANNE_HATHAWAY
                elif os.path.basename(path) == "arnold_schwarzenegger":
                    dir_name = EnumPerson.ARNOLD
                elif os.path.basename(path) == "ben_afflek":
                    dir_name = EnumPerson.BEN_AFFLIEK
                elif os.path.basename(path) == "elton_john":
                    dir_name = EnumPerson.ELTON_JOHN
                elif os.path.basename(path) == "jerry_seinfeld":
                    dir_name = EnumPerson.JERRY_SEINFELD
                elif os.path.basename(path) == "kate_beckinsale":
                    dir_name = EnumPerson.KATE_BECKINSALE
                elif os.path.basename(path) == "keanu_reeves":
                    dir_name = EnumPerson.KEANU_REEVES
                elif os.path.basename(path) == "lauren_cohan":
                    dir_name = EnumPerson.LAUREN_COHAN
                elif os.path.basename(path) == "madonna":
                    dir_name = EnumPerson.MADONNA
                elif os.path.basename(path) == "mindy_kaling":
                    dir_name = EnumPerson.MINDY_KALING
                elif os.path.basename(path) == "simon_pegg":
                    dir_name = EnumPerson.SIMON_PEGG
                elif os.path.basename(path) == "sofia_vergara":
                    dir_name = EnumPerson.SOFIA_VERGARA
                elif os.path.basename(path) == "will_smith":
                    dir_name = EnumPerson.WILL_SMITH
                for elem in lst_dir:
                    rec_path(path + "/" + elem)
            else:
                im = Image.open(path)
                imageSizeW, imageSizeH = im.size
                pixel = []
                for i in range(0, imageSizeW):
                    for j in range(0, imageSizeH):
                        pixel.append(im.getpixel((i, j)))
                x_row = []
                y_row = []
                for i in range(0, len(pixel)):
                    x_row.append(pixel[i][0] / 255)
                X.append(x_row)
                Y.append(dir_name.value)


    rec_path('./Base')
    return X, Y