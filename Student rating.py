import random
from tkinter import *

class Student:
    def __init__(self, name):
        self.name = name
        self.point = 0
        with open('res/questions.txt') as q:
            self.question = q.read().splitlines()
            
        random.shuffle(self.question)
        

with open('res/names.txt') as n:
    names = n.read().splitlines()
    
mass = []
objectStudent = []

for name in names:
    objectStudent.append(Student(name))
    
random.shuffle(objectStudent)


def lab_conf():
    lab.config(text=("Имя: "+objectStudent[stname].name +
                  "\nБаллы: "+str(objectStudent[stname].point) +
                  "\nВопрос: ") + objectStudent[stname].question[stques])

def byPoint_key(person):
    return person.point


def for_butNextStud(event):
    global stname
    

    stname += 1
    if stname >= len(objectStudent):
        stname = 0
    lab_conf()
    
def for_butPrevStud(event):
    global stname
    
    stname -= 1
    if stname <0:
        stname = len(objectStudent)-1
    lab_conf()
    
def for_butAddPoint(event):
    global stname
    global mass
    objectStudent[stname].point +=1

    lab_conf()
    i = 0
    objectStud = sorted(objectStudent, key = byPoint_key)
    objectStud.reverse()
    for i in range(len(names)):
        mass[i].config(objectStud[i].name + ": " + str(objectStud[i].point))
    

def for_butNextQues(event):
    global stques 
    stques += 1
    if stques >= len(objectStudent[0].question):
        stques = 0
    lab_conf()

def for_butPrevQues(event):
    global stques
    stques -= 1
    if stques <0:
        stques = 5
    lab_conf()    
#-------------------------------------------------------------------------
root = Tk()
root.title("Проверочная работа")
root.configure(background='lightyellow')
root.geometry("400x300")

win = Toplevel(root)
win.minsize(width = 300, height = 100)
win.title("Рейтинг студентов")

stname = 0
stques = 0

class New_lab():
    def __init__(self, text,x,y,w,h):
        self.lab = Label(win, text = text, font = "Times_New_Roman, 14")
        self.lab.place(x = x, rely = y, width = w, relheight = h)
    def config(self,text):
        self.lab.config(text = text)
        
       


i = 0
if len(names) <= 17:
    win.minsize(width = 300, height = 40*len(names))
else:
    win.minsize(width = 300, height = 680)
for i in range(len(names)):
    he = (1/len(names))
    y = he * i
    
    mass.append(New_lab(objectStudent[i].name + ": " + str(objectStudent[i].point),0,y, 300, he))
    
    i = i+1


        

lab = Label(text=("Имя: "+objectStudent[stname].name +
                  "\nБаллы: "+str(objectStudent[stname].point) +
                  "\nВопрос: ") + objectStudent[stname].question[stques],bg = "lightyellow", font="Times_New_Roman, 20")
lab.pack()





butPrevQues = Button(root, text="Предыдущий вопрос", font="Times_New_Roman, 14", bg = "red", fg = "white")
butPrevQues.bind('<Button-1>', for_butPrevQues)
butPrevQues.place(relx=0, rely=0.53, relheight = 0.13, relwidth = 0.5)

butNextQues = Button(root, text="Следующий вопрос", font="Times_New_Roman, 14", bg = "lightblue", fg = "darkblue")
butNextQues.bind('<Button-1>', for_butNextQues)
butNextQues.place(relx=0.5, rely=0.53, relheight = 0.13, relwidth = 0.5)

butAddPoint = Button(root, text = "Правильный ответ!", font="Times_New_Roman, 18", bg = "lightgreen", fg = "black")
butAddPoint.bind('<Button-1>', for_butAddPoint)
butAddPoint.place(relx=0, rely=0.66, relheight = 0.21, relwidth = 1)

butPrevStud = Button(root, text="Предыдущий студент", font="Times_New_Roman, 14", bg = "lightblue", fg = "darkblue")
butPrevStud.place(relx=0, rely=0.87, relheight = 0.13, relwidth = 0.5)
butPrevStud.bind('<Button-1>', for_butPrevStud)

butNextStud = Button(root, text="Следующий студент", font="Times_New_Roman, 14", bg = "red", fg = "white")
butNextStud.bind('<Button-1>', for_butNextStud)
butNextStud.place(relx=0.5, rely=0.87, relheight = 0.13, relwidth = 0.5)


root.mainloop()
