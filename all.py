from tkinter import*

def ready(x,mm):
    if x == 1:
        mm = 1
    else:
        mm = 2

    return mm          
    

class tictacmoe(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,background = "pink")
        self.jendela = parent
        self.initUI()
        self.tombol()
    def initUI(self):
        self.jendela.title("TicTacMOE")
        self.pack(fill = BOTH, expand = 1,)
        self.jendela.geometry("600x650+0+0")
        self.turn = BooleanVar()
        self.aq = IntVar()
        self.bq = IntVar()
        self.cq = IntVar()
        self.dq = IntVar()
        self.eq = IntVar()
        self.fq = IntVar()
        self.gq = IntVar()
        self.hq = IntVar()
        self.iq = IntVar()
    def tombol(self):
        btnreset = Button(self, text = "RESET")
        btnreset.place(x = 0,y = 0, width = 600, height = 50)
        variable = self.turn
        variable = False
        v = self.aq
        va = self.bq
        var = self.cq
        v = self.dq
        va = self.eq
        var = self.fq
        v = self.gq
        va = self.hq
        var = self.iq
        self.aq = 10
        self.bq = 20
        self.cq = 30
        self.dq = 40
        self.eq = 50
        self.fq = 60
        self.gq = 70
        self.hq = 80
        self.iq = 90

        a = Button(self, text = "MOE", command = self.ai).place(x = 0, y = 51, width = 200, height = 200)
        b = Button(self, text = "MOE", command = self.bi).place(x = 201, y = 51, width = 200, height = 200)
        c = Button(self, text = "MOE", command = self.ci).place(x = 401, y = 51, width = 200, height = 200)
        d = Button(self, text = "MOE", command = self.di).place(x = 0, y = 251, width = 200, height = 200)
        e = Button(self, text = "MOE", command = self.ei).place(x = 201, y = 251, width = 200, height = 200)
        f = Button(self, text = "MOE", command = self.fi).place(x = 401, y = 251, width = 200, height = 200)
        g = Button(self, text = "MOE", command = self.gi).place(x = 0, y = 451, width = 200, height = 200)
        h = Button(self, text = "MOE", command = self.hi).place(x = 201, y = 451, width = 200, height = 200)
        i = Button(self, text = "MOE", command = self.ii).place(x = 401, y = 451, width = 200, height = 200)
        
    def ai(self):
        if self.turn == True:
            tictacmoe.a(root)
            self.turn = False
            self.aq = ready(1,self.aq)
            tictacmoe.last(self)
            return self.turn
        else:
            tictacmoe.a1(root)    
            self.turn = True
            self.aq = ready(2,self.aq)
            tictacmoe.last(self)
            return self.turn   
    def bi(self):
        if self.turn == True:
            tictacmoe.b(root)
            self.turn = False
            self.bq = ready(1,self.bq)
            tictacmoe.last(self)
            return self.turn
        else:
            tictacmoe.b1(root)  
            self.turn = True
            self.bq = ready(2,self.bq)
            tictacmoe.last(self)
            return self.turn      
    def ci(self):
        if self.turn == True:
            tictacmoe.c(root)
            self.turn = False
            self.cq = ready(1,self.cq)
            tictacmoe.last(self)
            return self.turn
        else:
            tictacmoe.c1(root)  
            self.turn = True
            self.cq = ready(2,self.cq)
            tictacmoe.last(self)
            return self.turn
    def di(self):
        if self.turn == True:
            tictacmoe.d(root)
            self.turn = False
            self.dq = ready(1,self.dq)
            tictacmoe.last(self)
            return self.turn
        else:
            tictacmoe.d1(root)    
            self.turn = True
            self.dq = ready(2,self.dq)
            tictacmoe.last(self)
            return self.turn
    def ei(self):
        if self.turn == True:
            tictacmoe.e(root)
            self.turn = False
            self.eq = ready(1,self.eq)
            tictacmoe.last(self)
            return self.turn
        else:
            tictacmoe.e1(root)    
            self.turn = True
            self.eq = ready(2,self.eq)
            tictacmoe.last(self)
            return self.turn
    def fi(self):
        if self.turn == True:
            tictacmoe.f(root)
            self.turn = False
            self.fq = ready(1,self.fq)
            tictacmoe.last(self)
            return self.turn
        else:
            tictacmoe.f1(root)    
            self.turn = True
            self.fq = ready(2,self.fq)
            tictacmoe.last(self)
            return self.turn
    def gi(self):
        if self.turn == True:
            tictacmoe.g(root)
            self.turn = False
            self.gq = ready(1,self.gq)
            tictacmoe.last(self)
            return self.turn
        else:
            tictacmoe.g1(root)    
            self.turn = True
            self.gq = ready(2,self.gq)
            tictacmoe.last(self)
            return self.turn
    def hi(self):
        if self.turn == True:
            tictacmoe.h(root)
            self.turn = False
            self.hq = ready(1,self.hq)
            tictacmoe.last(self)
            return self.turn
        else:
            tictacmoe.h1(root)    
            self.turn = True
            self.hq = ready(2,self.hq)
            tictacmoe.last(self)
            return self.turn
    def ii(self):
        if self.turn == True:
            tictacmoe.i(root)
            self.turn = False
            self.iq = ready(1,self.iq)
            tictacmoe.last(self)
            return self.turn
        else:
            tictacmoe.i1(root)    
            self.turn = True
            self.iq = ready(2,self.iq)
            tictacmoe.last(self)
            return self.turn

    def last(self):
        if self.aq == self.bq == self.cq:
            if self.aq == 2:
                print("Rikka menang,Fake Mori Summer emang NOOB!")
                a = Label(root, image = o).place(x = 800, y = 150, width = 400, height = 400)
            else:
                print("Sepertinya waifu kita kali ini lagi ngePURE")
                a = Label(root, image = x).place(x = 800, y = 150, width = 400, height = 400)
        if self.gq == self.hq == self.iq:
            if self.gq == 2:
                print("Rikka menang,Fake Mori Summer emang NOOB!")
                a = Label(root, image = o).place(x = 800, y = 150, width = 400, height = 400)
            else:
                print("Sepertinya waifu kita kali ini lagi ngePURE")
                a = Label(root, image = x).place(x = 800, y = 150, width = 400, height = 400)
        if self.aq == self.dq == self.gq:
            if self.aq == 2:
                print("Rikka menang,Fake Mori Summer emang NOOB!")
                a = Label(root, image = o).place(x = 800, y = 150, width = 400, height = 400)
            else:
                print("Sepertinya waifu kita kali ini lagi ngePURE")
                a = Label(root, image = x).place(x = 800, y = 150, width = 400, height = 400)   
        if self.cq == self.fq == self.iq:
            if self.cq == 2:
                print("Rikka menang,Fake Mori Summer emang NOOB!")
                a = Label(root, image = o).place(x = 800, y = 150, width = 400, height = 400)
            else:
                print("Sepertinya waifu kita kali ini lagi ngePURE")
                a = Label(root, image = x).place(x = 800, y = 150, width = 400, height = 400)
        if self.aq == self.eq == self.iq:
            if self.aq == 2:
                print("Rikka menang,Fake Mori Summer emang NOOB!")
                a = Label(root, image = o).place(x = 800, y = 150, width = 400, height = 400)
            else:
                print("Sepertinya waifu kita kali ini lagi ngePURE")
                a = Label(root, image = x).place(x = 800, y = 150, width = 400, height = 400)
        if self.cq == self.eq == self.gq:
            if self.cq == 2:
                print("Rikka menang,Fake Mori Summer emang NOOB!")
                a = Label(root, image = o).place(x = 800, y = 150, width = 400, height = 400)
            else:
                print("Sepertinya waifu kita kali ini lagi ngePURE")
                a = Label(root, image = x).place(x = 800, y = 150, width = 400, height = 400)
        if self.bq == self.eq == self.hq:
            if self.bq == 2:
                print("Rikka menang,Fake Mori Summer emang NOOB!")
                a = Label(root, image = o).place(x = 800, y = 150, width = 400, height = 400)
            else:
                print("Sepertinya waifu kita kali ini lagi ngePURE")
                a = Label(root, image = x).place(x = 800, y = 150, width = 400, height = 400)
        if self.dq == self.eq == self.fq:
            if self.cq == 2:
                print("Rikka menang,Fake Mori Summer emang NOOB!")
                a = Label(root, image = o).place(x = 800, y = 150, width = 400, height = 400)
            else:
                print("Sepertinya waifu kita kali ini lagi ngePURE")
                a = Label(root, image = x).place(x = 800, y = 150, width = 400, height = 400)



    def a(self):
        a = Label(root, image = x).place(x = 0, y = 51, width = 200, height = 200)
    def a1(self):    
        a = Label(root, image = o).place(x = 0, y = 51, width = 200, height = 200)
    def b(self):    
        b = Label(root, image = x).place(x = 201, y = 51, width = 200, height = 200)
    def b1(self):
        b = Label(root, image = o).place(x = 201, y = 51, width = 200, height = 200)  
    def c(self):
        c = Label(root, image = x).place(x = 401, y = 51, width = 200, height = 200)
    def c1(self):    
        c = Label(root, image = o).place(x = 401, y = 51, width = 200, height = 200)
    def d(self):    
        d = Label(root, image = x).place(x = 0, y = 251, width = 200, height = 200)
    def d1(self):
        d = Label(root, image = o).place(x = 0, y = 251, width = 200, height = 200)
    def e(self):
        e = Label(root, image = x).place(x = 201, y = 251, width = 200, height = 200)
    def e1(self):    
        e = Label(root, image = o).place(x = 201, y = 251, width = 200, height = 200)
    def f(self):    
        f = Label(root, image = x).place(x = 401, y = 251, width = 200, height = 200)
    def f1(self):
        f = Label(root, image = o).place(x = 401, y = 251, width = 200, height = 200) 
    def g(self):
        g = Label(root, image = x).place(x = 0, y = 451, width = 200, height = 200)
    def g1(self):    
        g = Label(root, image = o).place(x = 0, y = 451, width = 200, height = 200)
    def h(self):    
        h = Label(root, image = x).place(x = 201, y = 451, width = 200, height = 200)
    def h1(self):
        h = Label(root, image = o).place(x = 201, y = 451, width = 200, height = 200)
    def i(self):    
        i = Label(root, image = x).place(x = 401, y = 451, width = 200, height = 200)
    def i1(self):
        i = Label(root, image = o).place(x = 401, y = 451, width = 200, height = 200)    

   
          

    
if __name__=='__main__':
    root = Tk()
    o = PhotoImage(file = "D:/Amal/rikka.png")
    x = PhotoImage(file = "D:/Amal/nibutani.png")
    tictacmoe(root)
    mainloop()
