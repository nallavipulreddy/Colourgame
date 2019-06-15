import tkinter 
import random
#print(tkinter.__doc__)
score=0
timeleft=30
colours = ['Red','Blue','Green','Pink','Black', 
        'Yellow','Orange','White','Purple','Brown']
def start(event):
    if timeleft==30:
        count()
    nextcolor()
def count():
    global timeleft
    if timeleft>0:
        timeleft-=1
        time.config(text="Time Left:"+str(timeleft))
        time.after(1000,count)
        if timeleft==0:
            endgame.config(text="The End \n Your score:"+str(score))        

def nextcolor():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower() == colours[1].lower(): 
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scorelable.config(text = "Score: " + str(score))
#Gui Module
t=tkinter.Tk()
t.title("Color")
t.geometry("375x250")
intro=tkinter.Label(t,text="Type in the colour of the words, and not the word text!\n Press Enter to start",font=("Helvetica",12),foreground="blue")
intro.pack()
scorelable=tkinter.Label(t,text='Score:'+str(score),font=("Helvetica",12))
scorelable.pack()

time=tkinter.Label(t,text='Time Left:'+str(timeleft),font=("Helvetica",12))
time.pack()

label=tkinter.Label(t,font=("Helvetica",20))
label.pack()

endgame=tkinter.Label(t,font=("Helvetica",20))
endgame.pack()
e=tkinter.Entry(t)
t.bind('<Return>',start)
e.pack()
e.focus_set()
