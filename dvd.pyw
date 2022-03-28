from tkinter import *
from random import randint
from keyboard import add_hotkey


class App:
    def __init__(self, master):
        self.master = master
        self.user_scr_width = self.master.winfo_screenwidth()
        self.user_scr_height = self.master.winfo_screenheight()
        self.make_it()
        self.master.withdraw()

    def make_it(self, x_add=4, y_add=3):
        root = Toplevel(self.master)
        root.attributes('-topmost', True)
        root_width = 250
        root_height = 100
        x_pos = randint(1, root.winfo_screenwidth() - root_width)
        y_pos = randint(1, root.winfo_screenheight() - root_height)
        root.geometry(f'{root_width}x{root_height}+{x_pos}+{y_pos}')
        root.overrideredirect(True)
        root.config(bg="black")
        Label(root, text="DVD", font=('Copperplate Gothic Bold', 72, 'bold'), fg="yellow", bg="black").pack()
        root.resizable(False, False)

        def close():
            self.master.unbind_all('<Button-1>')

            bob = Toplevel(self.master)
            bob.attributes('-topmost', True)
            bob.title('Close?')
            bob.geometry('250x50')
            bob.resizable(False, False)
            frame1 = Frame(bob)
            frame2 = Frame(bob)
            frame2.pack(side='right')
            frame1.pack(side='right')
            Button(frame1, text="Close", command=self.master.destroy).pack(side='right', padx=5)
            Button(frame2, text="Cancel", command=lambda: [bob.destroy(), self.master.bind_all('<Button-1>', lambda e: self.multiply())]).pack(side='right', padx=5)

        self.master.bind_all('<Button-1>', lambda e: self.multiply())
        self.master.bind_all('<Button-3>', lambda e: close())

        def move(x_p, y_p, x_a, y_a):
            x_p += x_a
            y_p += y_a
            if x_p >= self.user_scr_width - root_width:
                x_p = self.user_scr_width - root_width
                x_a = 0 - x_a
            elif x_p < 0:
                x_p = 0
                x_a = abs(x_a)
            if y_p >= self.user_scr_height - root_height:
                y_p = self.user_scr_height - root_height
                y_a = 0 - y_a
            elif y_p < 0:
                y_p = 0
                y_a = abs(y_a)
            try:
                root.geometry(f'+{x_p}+{y_p}')
            except:
                pass
            self.master.after(20, lambda: move(x_p, y_p, x_a, y_a))

        move(x_pos, y_pos, x_add, y_add)

    def multiply(self):
        self.make_it(x_add=randint(2, 7), y_add=randint(1, 6))


if __name__ == '__main__':
    mainapp = Tk()
    a = App(mainapp)
    add_hotkey("ctrl+*", lambda: mainapp.destroy())
    mainapp.mainloop()
