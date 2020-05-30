import tkinter as tk
import pages.home


class PageTwo(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent.title("page two")
        PageTwo.make_widgets(self, parent)

    def make_widgets(self, parent):
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(
            side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: parent.switch_frame(pages.home.MainPage)).pack()
