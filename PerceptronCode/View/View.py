from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
import os



def get_dict(adict):
    return '\n'.join('%s %s' % t for t in adict.items())



switch_case = dict ([
    (13, u'anne_hathaway'),
    (12, u'arnold_schwarzenegger'),
    (11, u'ben_afflek'),
    (10, u'dwayne_johnson'),
    (9, u'elton_john'),
    (8, u'jerry_seinfeld'),
    (7, u'kate_beckinsale'),
    (6, u'keanu_reeves'),
    (5, u'lauren_cohan'),
    (4, u'madonna'),
    (3, u'mindy_kaling'),
    (2, u'simon_pegg'),
    (1, u'sofia_vergara'),
    (0, u'will_smith')
])




class View:


    def __init__(self, yh, path):
        self.Yh = yh
        self.path = path
        self._window = self._set_window()
        self._textboxresults = self._set_results()
        self._textbox_mainresult = self._set_mainresult()
        self.button = self.set_button()
        self.lst_click = os.listdir("./Base/training/")
        self.clicks = -1
        self.num_ph = 1
        self.click_button()
        self._window.mainloop()


    def set_yh(self, yh):
        self.yh = yh

    def click_button(self):
        if self.clicks == len(self.path) - 1:
            self.clicks = 0
        else:
            self.clicks += 1
        self.show_results(dict([
            (u'anne_hathaway', '{:.2f}'.format(self.Yh[13][self.clicks]) + "%"),
            (u'arnold_schwarzenegger', '{:.2f}'.format(self.Yh[12][self.clicks]) + "%"),
            (u'ben_afflek', '{:.2f}'.format(self.Yh[11][self.clicks]) + "%"),
            (u'dwayne_johnson', '{:.2f}'.format(self.Yh[10][self.clicks]) + "%"),
            (u'elton_john', '{:.2f}'.format(self.Yh[9][self.clicks]) + "%"),
            (u'jerry_seinfeld', '{:.2f}'.format(self.Yh[8][self.clicks]) + "%"),
            (u'kate_beckinsale', '{:.2f}'.format(self.Yh[7][self.clicks]) + "%"),
            (u'keanu_reeves', '{:.2f}'.format(self.Yh[6][self.clicks]) + "%"),
            (u'lauren_cohan', '{:.2f}'.format(self.Yh[5][self.clicks]) + "%"),
            (u'madonna', '{:.2f}'.format(self.Yh[4][self.clicks]) + "%"),
            (u'mindy_kaling', '{:.2f}'.format(self.Yh[3][self.clicks]) + "%"),
            (u'simon_pegg', '{:.2f}'.format(self.Yh[2][self.clicks]) + "%"),
            (u'sofia_vergara', '{:.2f}'.format(self.Yh[1][self.clicks]) + "%"),
            (u'will_smith', '{:.2f}'.format(self.Yh[0][self.clicks]) + "%")
        ]))
        temp = self.Yh[0][self.clicks]
        pers = 0
        for j in range(1, 13):
            if temp < self.Yh[j + 1][self.clicks]:
                temp = self.Yh[j + 1][self.clicks]
                pers = j + 1

        self.show_main_result(str(switch_case.get(pers)))
        self.show_picture(self.path[self.clicks])
        self._window.mainloop()

    def _set_window(self):
        window = Tk()
        window.title("Results")
        window.geometry("745x450")
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

    def set_button(self):
        btn1 = Button(text="Next Picture", background="#000000", foreground="#fff",
                      padx="15", font="Arial 17", width=17, height=1, command=self.click_button)
        btn1.place(x=410, y=405)
        return btn1

    def show_picture(self, path):
        img = Image.open(path)
        img = img.resize((400, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self._window, image=img)
        panel.image = img
        panel.place(x=0, y=0)

    def show_results(self, adict):
        self._textboxresults.config(text=str(get_dict(adict)))

    def show_main_result(self, mainresult):
        self._textbox_mainresult.config(text=mainresult)

