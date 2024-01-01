from terms import terms
from tkinter import*
import random
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk

Mainwindow = Tk()
Mainwindow.geometry('2000x2000')
Mainwindow.title('Typing Accuracy Game')
#Mainwindow.config(bg='black')
bg = ImageTk.PhotoImage(file='bg.png')
canvas=Canvas(Mainwindow,width =400,height=200)
canvas.pack(expand=True,fill=BOTH)
canvas.create_image(0,0,image=bg,anchor='nw')
Font_tuple=('Public Sans Thin',40)

score = 0
miss = 0
result=0
time = 60
count = 0
movingword = ''



start = Label(Mainwindow, text = 'Start Typing!', font=(Font_tuple),bg = 'black', fg = 'white')
start.place(x = 650, y = 100)

random.shuffle(terms)
labelforward = Label(Mainwindow, text = terms[0], font=('Public San Thin', 45),bg = 'black', fg = 'yellow',justify = 'center')
labelforward.place(x = 630, y = 300)

score1 = Label(Mainwindow, text = 'Your Score: ', font=('Helvetica',40),bg = 'black', fg = 'white')
score1.place(x = 100, y = 100)

scorecount = Label(Mainwindow, text = score, font=('Helvetica',40),bg = 'dark blue', fg = 'yellow')
scorecount.place(x = 230, y = 180)

timer = Label(Mainwindow, text = 'Time Left: ', font=('Helvetica', 40),bg = 'black', fg = 'white', )
timer.place(x = 1175, y = 100)

timercount = Label(Mainwindow, text = time, font=('Helvetica', 40), bg = 'dark blue', fg = 'red')
timercount.place(x = 1230, y = 180)

gameinstruction = Label(Mainwindow, text = 'Hit enter to start the game \n' 'and after typing every term.\n'' Game is case sensitive' , font=('Helvetica', 25),bg ='black', fg = 'pink',bd = 10)
gameinstruction.place(x = 580, y = 600)

termentry = Entry(Mainwindow, font = ('Helvetica', 30), bd = 10, justify = 'center')
termentry.place(x = 550, y = 450)
termentry.focus_set()

font = Label(Mainwindow, text = '', font=(Font_tuple), bg = 'black', fg = 'yellow', width = 47)
font.place(x = 32, y = 10)


def movingtext():
    global count, movingword
    floatingtext = 'TYPING ACCURACY GAME'
    if count>=len(floatingtext):
        count = 0
        movingword = ''
    movingword+=floatingtext[count]
    count+=1
    font.configure(text = movingword)
    font.after(200, movingtext)

movingtext()

def giventime():
    global time, score, miss, result
    result=score-miss
    if time>11:
        pass
    else:
        timercount.configure(fg = 'red')
    if time>0:
        time-=1
        timercount.configure(text = time)
        timercount.after(1000, giventime)
    else:
        result=score-miss
        gameinstruction.configure(text='HITS: {} | MISSES: {} | TOTAL SCORE: {}'.format(score, miss, result))
        r = messagebox.askretrycancel('Notification','Do you want to play again?')
        print(result)
        if r==True:
            time=60
            score=0
            miss=0
            gameinstruction.configure(text = '')
            start.configure(text= '')
            labelforward.configure(text = terms[0])
            scorecount.configure(text=score)
            termentry.delete(0, END)    
        else:
            Mainwindow.destroy()
            
def game(event):
    global score, miss
    if time==60:
        giventime()
    #gameinstruction.configure(text = '')
    #start.configure(text= '')
    if termentry.get()==labelforward['text']:
        score+=1
        scorecount.configure(text = score)
    else:
        miss+=1
        print(termentry.get())
    #print(score)
    random.shuffle(terms)
    labelforward.configure(text = terms[0])
    termentry.delete(0, END)
                
Mainwindow.bind('<Return>', game)
mainloop()
