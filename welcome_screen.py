import tkinter as tk
import gui_solver

class Welcome:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('600x400')
        self.bg = tk.PhotoImage(file='screen.png')
        self.bg_label = tk.Label(self.window, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.window.resizable(False, False)
        self.mode = tk.StringVar()
        
        self.rd1 = tk.Radiobutton(self.window,
                                    text='Easy',
                                    variable=self.mode,
                                    value='easy',
                                    indicator=0,
                                    background='light blue',
                                    command=self.call_puzzle)

        self.rd2 = tk.Radiobutton(self.window,
                                    text='Medium',
                                    variable=self.mode,
                                    value='medium',
                                    indicator=0,
                                    background='light blue',
                                    command=self.call_puzzle)

        self.rd3 = tk.Radiobutton(self.window,
                                    text='Hard',
                                    variable=self.mode,
                                    value='hard',
                                    indicator=0,
                                    background='light blue',
                                    command=self.call_puzzle)
                                    
        self.rd1.place(x=200, y=200)
        self.rd2.place(x=270, y=200)
        self.rd3.place(x=360, y=200)

    def call_puzzle(self):
        print(type(self.mode.get()))
        print(self.mode.get())
        m = self.mode.get()
        
        self.req_screen = gui_solver.Grid(m)
       
if __name__ == "__main__":
    sc= Welcome()
    sc.window.mainloop()