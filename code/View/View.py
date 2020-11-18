from tkinter import *
from PIL import ImageTk, Image

myDict = dict([
    (u'anne_hathaway', 45),
    (u'arnold_schwarzenegger', 25),
    (u'ben_afflek', 30),
    (u'dwayne_johnson', 45),
    (u'elton_john', 25),
    (u'jerry_seinfeld', 30),
    (u'kate_beckinsale', 45),
    (u'keanu_reeves', 25),
    (u'lauren_cohan', 30),
    (u'madonna', 45),
    (u'mindy_kaling', 25),
    (u'simon_pegg', 30),
    (u'sofia_vergara', 45),
    (u'will_smith', 25)
])
path = "D:\\Visual Studio Projects\\Neural-networks\\Neural-networks\\code\\Base\\training\\anne_hathaway\\bmp\\1.bmp"


def get_dict(adict):
    return '\n'.join('%s %s' % t for t in adict.items())


class View:

    def __init__(self):
        self._window = self._set_window()
        self._textboxresults = self._set_results()
        self._textbox_mainresult = self._set_mainresult()
        self.button = self._set_button()

        #
        self.show_main_result("arnold_schwarzenegger")
        self.show_results(myDict)
        self.show_picture(path)
        #

        self._window.mainloop()

    def _set_window(self):
        window = Tk()
        window.title("Results")
        window.geometry("720x450")
        window.resizable(width=False, height=False)
        return window

    def _set_results(self):
        textbox = Label(font="Arial 16", pady="20", justify=LEFT)
        textbox.place(x=410, y=0)
        return textbox

    def _set_mainresult(self):
        textbox = Label(font="Arial 22", pady="5", width="20")
        textbox.place(x=0, y=400)
        return textbox

    def _set_button(self):
        btn1 = Button(text="Next Picture", background="#000000", foreground="#fff",
                      padx="15", font="Arial 17", width=17, height=1)
        btn1.place(x=410, y=405)

    def show_picture(self, path):
        img = Image.open(path)
        img = img.resize((400, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self._window, image=img)
        panel.image = img
        panel.place(x=0, y=0)

    def show_results(self, adict):
        self._textboxresults.config(text=get_dict(adict))

    def show_main_result(self, mainresult):
        self._textbox_mainresult.config(text=mainresult)
