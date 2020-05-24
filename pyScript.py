'''
Created on 15 May 2020
by amine
@author: rooot
'''
from tkinter import *
from tkinter import ttk
from random import randrange
x=1
def pr_info(event):
    '''simple fun for adding user to a file named employer.txt'''
    global x
    if len(entr1.get())!=0 and len(entr2.get())!=0 and len(entr3.get())!=0 and len(entr4.get())!=0:
        print(entr1.get())
        file=open('employer.txt','a')
        
        file.write("first name:\t")
        file.write(entr1.get())
        file.write("\nfamilly name:\t")
        file.write(entr2.get())
        file.write("\nemail: \t")
        file.write(entr3.get())
        file.write("\ndate of birth:\t")
        file.write(entr4.get())
        file.write("\nnomber:\t")
        file.write(str(x))
        file.write("\n\n----------------------------------------\n\n")
        
        x=x+1
        entr1.delete(0,END)
        entr2.delete(0,END)
        entr3.delete(0,END)
        entr4.delete(0,END)
        file.close()
        lbl3.configure(text="success",font=('',7),fg="green")
    else:
        lbl3.configure(text="error empty field",font=('',7),fg="red")
#inused list        
coList=["green","pink","black","white","red","blue","cyan","yellow","purple","maroon","orange"]
mywindow=Tk()
mywindow.geometry("300x190")
mywindow.title("registred")

#gui

lbl1=Label(mywindow,text="welcom")
lbl1.grid(row=0,column=0,sticky=E)
lbl2=Label(mywindow,text="put your info here:")
lbl2.grid(row=0,column=1,sticky=W)

lbl3=Label(mywindow,text=" ")
lbl3.grid(row=1,column=0,sticky=W)


txt1=Label(mywindow,text="  first name:")
txt1.grid(row=2,column=0,sticky=W)

entr1=Entry(mywindow,width=22)
entr1.grid(row=2,column=1)

txt2=Label(mywindow,text="  familly name: ")
txt2.grid(row=3,column=0,sticky=W)

entr2=Entry(mywindow,width=22)
entr2.grid(row=3,column=1)

txt3=Label(mywindow,text="  email:")
txt3.grid(row=4,column=0,sticky=W)

entr3=Entry(mywindow,width=22)
entr3.grid(row=4,column=1)

txt4=Label(mywindow,text="  date of birth: ")
txt4.grid(row=5,column=0,sticky=W)

entr4=Entry(mywindow,width=22)
entr4.grid(row=5,column=1)
entr4.bind("<Return>",pr_info)

lbl3=Label(mywindow,text=" ")
lbl3.grid(row=6,column=0,sticky=E)

btn1=Button(mywindow,text="done",width=5)
btn1.grid(row=7,column=0)
btn1.bind("<Button-1>",pr_info)

btn1=Button(mywindow,text="quit",width=5,command=mywindow.quit)
btn1.grid(row=7,column=1,sticky=E)


#end of gui
mywindow.mainloop()
print("end of program")
