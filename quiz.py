from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import random

sample={"東" , "西" , "南" , "北" , "入ります" , "出ます" , "口","入口","出口","東口","西口","南口","北口"}
reference={"東":"ひがし" , "西": "にし", "南" : "みなみ", "北": "きた" , "入ります" : "はいります", "出ます" :"でます", "口":"くち","入口":"いりぐち","出口":"でぐち","東口":"ひがしぐち","西口":"にしぐち" , "南口":"みなみぐち" , "北口": "きたぐち"}
def main():
    q=quiz()
class quiz:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("800x800")
        self.window.title("quiz one")
        self.window.config(background="black")
        self.mg=Image.open("j.png").resize((800, 800), Image.ANTIALIAS)
        self.im=ImageTk.PhotoImage(self.mg)
        self.l1=Label(self.window , image=self.im , bg="black").place(x=0 , y=0)
        self.l=Label(self.window,text="",font=("Arial", 25),fg="red",bg="black")
        self.l.place(x=200 , y=200)            
        self.item= random.choice(tuple(sample))
        self.l.config(text=f"write the hiragana of kanji {self.item}: ")
        self.e=Entry(self.window ,font=("Arial", 23) ,fg="black" , bg="#EF1700")
        self.e.place(x=250 , y=500)
        self.answer=self.e.get()
        self.mg2=Image.open("l.png").resize((100, 100), Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.mg2)
        self.b=Button(self.window , text="sumbit" , font=("Arial", 25),image=self.im2,fg="black",bg="black",border=0,command=self.click)
        self.b.place(x=350 ,y=550)
        self.window.mainloop()
    def click(self):
        if(self.answer==reference[self.item]):
            messagebox.showinfo("quiz one","correct")
            self.reset()
        else:
            self.l.config(text=f"enter again hiragana of kanji{self.item}")
            self.answer=self.e.get()
            if(self.answer==reference[self.item]):
                messagebox.showinfo("quiz one","correct")
                self.reset()
                
    def reset(self):
        self.window.destroy()
        main()
if __name__ == '__main__':
    main()

    

    
