import tkinter as tk
import pages.detail
import pages.pagetwo


class MainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent.title("Todo Tasks")
        MainPage.make_widgets(self, parent)

    def make_widgets(self, parent):
        
        tk.Label(self, text="Current Tasks", font=(
            'Helvetica', 18, "bold")).grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        tk.Button(self, text="Go to page one",
                  command=lambda: parent.switch_frame(pages.detail.DetailPage)).grid(row=2, column=0)
        tk.Button(self, text="Go to page two",
                  command=lambda: parent.switch_frame(pages.pagetwo.PageTwo)).grid(row=3, column=1)
