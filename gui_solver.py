import time
import tkinter as tk
import copy
import puzzles
from solver import SudokuGame

Font_tuple1 = ("Comic Sans MS", 20, "bold")
Font_tuple2 = ("Comic Sans MS", 13)

class Grid:

    def isvalid(self, inputString, widgetName):

        curWidget = self.canvas1.nametowidget(widgetName)
        
        r=None
        c=None

        for key, widget in self.entries.items():

            if widget == curWidget:

                r = int(key[5])
                c =int(key[7])
                #print(key)
        
        
        if inputString=='':            
            self.validLabel.config(text='')            
            return True
        elif inputString.isdigit() and self.game.possible(self.queryPuzzle, r, c,int(inputString)):
                     
            labelText = inputString+' is Valid'
            
            if int(inputString) != self.solved_puzzle[r][c]:
                labelText += '\n but not correct'
                self.validLabel.config(text=labelText)
                return False
            
            self.queryPuzzle[r][c]=int(inputString)
            self.validLabel.config(text=labelText)            
            return True
        else:
            curWidget.delete(0, tk.END)
            self.validLabel.config(text='Not valid')
            return False
        

    def display_Grid(self):
        
        self.show_time()
        for i in range(9):
            for j in range(9):

                if self.puzzle[i][j]!=0:
                    req_widget = self.entries['label_'+str(i)+'_'+str(j)]
                else:
                    req_widget = self.entries['text_'+str(i)+'_'+str(j)]                    

                      
                self.canvas1.create_window(j*56+29,i*56+29, height = 56, width=56, window=req_widget)
        self.canvas1.pack()
        self.canvas2.pack()
        
    def __init__(self, mode, win=None):
        self.paused = False
        self.mode = mode
        self.initialTime = time.time()        
        self.puzzle = puzzles.puzzles.get(self.mode)
        self.queryPuzzle = copy.deepcopy(self.puzzle)
        self.game = SudokuGame(self.puzzle)
        self.solved_puzzle = self.game.solve(self.puzzle)
        
        if win is None:
            self.window = tk.Toplevel()
        else:
            self.window = win

        self.window.title('Sudoku Game')
        self.window.geometry('504x600')
        self.window.resizable(False, False)
        self.bg_image = tk.PhotoImage(file='screen.png')
        self.canvas1 = tk.Canvas(self.window, width=504,
                            height=504,
                            bg='white')
        self.canvas2 = tk.Canvas(self.window, width=504,
                            height=96,
                            bg='white')
        self.canvas2.create_image( 0, 0, image = self.bg_image, 
                        anchor = "nw")
        self.validLabel = tk.Label(text='', font = Font_tuple2,
                                            relief='solid',
                                            borderwidth=1)
        self.clockLabel = tk.Label(text='00:00', font = Font_tuple2,
                                                relief='solid',
                                                borderwidth=1)
        # self.Button1 = tk.Button(text='Print Puzzle', 
        #                 command=self.print_query_puzzle,
        #                  font = Font_tuple2)
        self.Button2 = tk.Button(text='Solve Puzzle',
                         command=self.solve,
                          font = Font_tuple2)
        self.canvas2.create_window(60,30, window=self.validLabel)
        self.canvas2.create_window(200,30, window=self.clockLabel)
        #self.canvas2.create_window(450,30, window=self.Button1)        
        self.canvas2.create_window(300,30, window=self.Button2)        
        self.validatefunction = self.canvas1.register(self.isvalid)
        

        self.entries = {}
        for i in range(9):
            for j in range(9):

                if self.puzzle[i][j]!=0:
                    
                    self.entries['label_'+str(i)+'_'+str(j)]=tk.Label(text = self.puzzle[i][j], 
                                                                bg ='white', relief='solid',
                                                                borderwidth=1, font = Font_tuple1)    
                else:
                    self.entries['text_'+str(i)+'_'+str(j)] = tk.Entry(validate='key' ,
                            validatecommand=(self.validatefunction, '%P', '%W'), 
                            highlightthickness=1,highlightbackground="black",
                            justify=tk.CENTER, font = Font_tuple1)
        
        self.display_Grid()
        
    def print_query_puzzle(self):

        for row in self.queryPuzzle:
            print('\t\t', end='')
            for val in row:
                print(val, end=' ')                
            print()
    
    def show_time(self):
        if not self.paused:
            delta = int(time.time()-self.initialTime)
            timestr = '{:02}:{:02}'.format(*divmod(delta, 60))
            self.clockLabel.config(text=timestr)
            self.clockLabel.after(1000, self.show_time)
    

    def set_text(self, widget, text):
        #if widget.get() is not '':
        widget.insert(0, str(text))
        widget.delete(1)
        
        return   

    def solve(self):
        #print(self.puzzle is self.queryPuzzle)
        #print(self.puzzle)
        # solved_puzzle = self.game.solve(self.puzzle)
        #print(self.solved_puzzle)
        self.paused=True

        for key, widget in self.entries.items():
            if key[:5]=='label':
                continue
            r = int(key[5])
            c = int(key[7])
            #print(r, c)
            self.set_text(widget, self.solved_puzzle[r][c])
            widget.config(state='readonly')

if __name__ == "__main__":
    
    mode = input('Enter the mode{easy, medium, hard}:').lower()
    #mode = 'easy'
    if mode not in ['easy', 'medium', 'hard']:
        print('Enter correct mode')
    else:
        win = tk.Tk()
        grid = Grid(mode, win)
        grid.window.mainloop() 