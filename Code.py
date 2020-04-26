import tkinter
from tkinter import *
from tkinter import ttk
window=Tk()
window.configure(bg="purple")
window.title("GSG Project")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.overrideredirect(1)
window.geometry("%dx%d+0+0" % (w, h))
a=" "
Q=[]
A=[]
count=0
class SU():
    def __init__(self,c,r,q,a):
        self.c=c
        self.r=r
        self.q=q
        self.a=a
    def call(self):
        if self.q == " ":
            def get():
                V=tkinter.IntVar()
                User_Entry=Entry(window,width=1,bg=self.a,textvariable=V)
                User_Entry.grid(column=self.c,row=self.r)
                def assign():
                    Q[self.c][self.r]=V.get()
                    bt=Button(window,text=str(V.get()),bg=self.a,command=get, height = 4, width = 6, font=('Helvetica', '10'))
                    bt.grid(column=self.c,row=self.r)
                    print(Q)
                    bt_a.destroy()
                bt_a=ttk.Button(window,text="ASSIGN",command=assign)
                bt_a.grid(column=14,row=15)
            bt=Button(window,text="_",bg=self.a,command=get, height = 4, width = 6)
            bt.grid(column=self.c,row=self.r,sticky=W+N+E+S)
        else:
            bt=Button(window,text=str(self.q),bg=self.a, height = 4, width = 6,fg="red", font=('Helvetica', '10'))
            bt.grid(column=self.c,row=self.r)
def play():
    Button_1.destroy()
    Button_7.destroy()
    Button_5.destroy()
    Label_1.destroy()
    for i in range(0,9):
        for j in range(0,9):
            global a
            if i in [0,1,2,6,7,8] and j in [0,1,2,6,7,8]:
                a="yellow"
            elif i in [3,4,5] and j in [3,4,5]:
                a="yellow"
            else:
                a="white"
            M=SU(i,j,Q[i][j],a)
            SU.call(M)
    def action_submit():
        global count
        count=0
        for m in Q:
            if " "  in m:
                count=count+1
        if Q==A:
            windo=Tk()
            windo.configure(bg="pink")
            windo.title("GSG Project")
            windo.geometry("400x400")
            Label_1=ttk.Label(windo,text="WELL DONE!!!",background="purple",foreground="white")
            Label_1.grid(column=1,row=0)
            window.destroy()
            windo.mainloop()
        elif count>1:
                windo=Tk()
                windo.configure(bg="pink")
                windo.title("GSG Project")
                windo.geometry("400x400")
                Label_1=ttk.Label(windo,text="complete the tabel first ",background="purple",foreground="white")
                Label_1.grid(column=1,row=0)
            
        else:
            windo=Tk()
            windo.configure(bg="pink")
            windo.title("GSG Project")
            windo.geometry("400x400")
            Label_1=ttk.Label(windo,text="Better luck next ",background="purple",foreground="white")
            Label_1.grid(column=1,row=0)
            window.destroy()
            windo.mainloop()
    
    Button_0=ttk.Button(window,text="SUBMIT",command=action_submit)
    Button_0.grid(column=14,row=16)
def play_hard():
    global Q
    global A
    Q=[[5," "," "," ",4,8," "," ",1],[" ",8," ",9," "," "," ",4," "],[9," ",3," "," ",2," "," ",7],[" "," "," ",7," ",1,3," "," "],[" ",1,8," ",5," "," "," ",9],[" "," ",4," "," "," ",2," "," "],[" ",5," "," ",3," "," ",7," "],[" ",2," "," ",9," "," "," ",8],[7," ",1,2," ",4,5," "," "]]
    A=[[5,6,7,3,4,8,9,2,1],[1,8,2,9,7,5,6,4,3],[9,4,3,6,1,2,8,5,7],[6,9,5,7,2,1,3,8,4],[2,1,8,4,5,3,7,6,9],[3,7,4,8,6,9,2,1,5],[8,5,9,1,3,6,4,7,2],[4,2,6,5,9,7,1,3,8],[7,3,1,2,8,4,5,9,6]]
    play()
def play_easy():
    global Q
    global A
    Q=[[1," "," ",4,8,9," "," ",6],[7,3," "," ",5," "," ",4," "],[4,6," "," "," ",1,2,9,5],[3,8,7,1,2," ",6," "," "],[5," ",1,7," ",3," "," ",8],[" ",4,6," ",9,5,7,1," "],[9,1,4,6," "," "," ",8," "],[" ",5," "," ",4," "," ",3,7],[8," ",3,5,1,2," "," ",4]]
    A=[[1,5,2,4,8,9,3,7,6],[7,3,9,2,5,6,8,4,1],[4,6,8,3,7,1,2,9,5],[3,8,7,1,2,4,6,5,9],[5,9,1,7,6,3,4,2,8],[2,4,6,6,9,5,7,1,3],[9,1,4,6,2,7,5,8,2],[6,2,5,9,4,8,1,3,7],[8,7,3,5,1,2,9,6,4]]
    play()
def play_med():
    global Q
    global A
    Q=[[" ",8,4," "," ",7,9," ",1],[" "," "," "," "," ",3," "," "," "],[" ",9,3," ",2," "," ",8," "],[" "," ",5,1," "," "," ",2," "],[8,7," "," ",3," "," "," ",4],[" ",1," "," ",4,9," ",5," "],[" "," "," "," "," "," ",7," ",3],[" ",2," "," ",8," "," ",9," "],[" "," ",1,7," ",4,2," "," "]]
    A=[[2,8,4,5,6,7,9,3,1],[1,5,6,8,9,3,4,7,2],[7,9,3,4,2,1,5,8,6],[6,4,5,1,7,8,3,2,9],[8,7,9,2,3,5,6,1,4],[3,1,2,6,4,9,8,5,7],[5,6,8,9,1,2,7,4,3],[4,2,7,3,8,6,1,9,5],[9,3,1,7,5,4,2,6,8]]
    play()
Label_1=ttk.Label(window,text="Want to play SUDOKO",background="purple",foreground="white")
Label_1.grid(column=1,row=0)
def action_exit():
    window.destroy()
Button_0=ttk.Button(window,text="EXIT",command=action_exit)
Button_0.grid(column=14,row=17)
Button_1=ttk.Button(window,text="EASY",command=play_easy)
Button_1.grid(column=0,row=1)
Button_7=ttk.Button(window,text="MEDIUM",command=play_med)
Button_7.grid(column=1,row=1)
Button_5=ttk.Button(window,text="HARD",command=play_hard)
Button_5.grid(column=2,row=1)

window.mainloop()

