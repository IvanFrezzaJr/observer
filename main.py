from tkinter import *
from observable import InputObservable
from observer import EntryObserver, TextBoxObserver
from command import Main


class UI:
    def __init__(self):
        # create UI objects
        self.setup()

        # add listeners on UI fields
        self.listeners()

        self.keybinds()

    def setup(self):
        self.window = Tk()
        self.window.title("Welcome to LikeGeeks app")
        self.window.geometry("340x260")

        ##########################################
        # row 1
        ##########################################
        self.lbl = Label(self.window, text="Type here:")
        self.lbl.grid(column=0, row=0)
        self.txt = Entry(self.window, width=20)
        self.txt.grid(column=1, row=0)

        ##########################################
        # row 2
        ##########################################
        self.lbl2 = Label(self.window, text="It will appear here:")
        self.lbl2.grid(column=0, row=1)
        self.txt2 = Entry(self.window, width=20)
        self.txt2.grid(column=1, row=1)

        ##########################################
        # row 3
        ##########################################
        self.btn = Button(
            self.window, text="Click Me", command=self.processIt, width=40
        )
        self.btn.grid(columnspan=2, row=2)

        ##########################################
        # row 4
        ##########################################
        self.inputtxt = Text(self.window, height=10, width=40)
        self.inputtxt.grid(
            columnspan=2,
            row=3,
        )

    def processIt(self):
        """run command main function"""
        self.main.run()

    def listeners(self):
        # subscribe command to tedtBox
        self.main = Main()
        tbo = TextBoxObserver(self.inputtxt)
        self.main.subscribe([tbo])

        # subscribe txt field to txt2 field
        self.input_ = InputObservable(self.txt)
        p1 = EntryObserver(self.txt2)
        self.input_.subscribe([p1])

    def keybinds(self):
        """binds key when your are typing on the txt field"""
        self.window.bind("<KeyRelease>", self.up)

    def up(self, e):
        """notify on keyup"""
        self.input_.notify()

    def run(self):
        """run window"""
        self.window.mainloop()


ui = UI()
ui.run()
