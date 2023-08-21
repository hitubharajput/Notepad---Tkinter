from tkinter import *
import os
import tkinter.messagebox as box
from tkinter.filedialog import askopenfilename, asksaveasfilename


x = 0
#screen settings----------------------------------------------------------------------
window  = Tk()
window.title("Notepad")
window.geometry("600x600")
window.minsize(300,300)
window.maxsize(1600,1600)
window.configure(background="white")

#scrolbar setting---------------------------------------------------------------------
scrolbarh = Scrollbar(window,orient='horizontal')
scrolbarh.pack(side=BOTTOM,fill=X)

scrolbarv = Scrollbar(window)
scrolbarv.pack(side=RIGHT,fill=Y)

textbox = Text(window,width = 60000000,undo=True,height= 60000,yscrollcommand=scrolbarv.set,xscrollcommand=scrolbarh.set)
file = None
textbox.pack(fill=BOTH,expand=True)

scrolbarh.config(command=textbox.xview)
scrolbarv.config(command=textbox.yview)

#create a menu-------------------------------------------------------------------------------
mainmenu = Menu(window)
# commands-----------------------------------------------------------------------------------

def newfile(event=None) :
    global file
    window.title("Untitled - Notepad")
    file = None
    textbox.delete(1.0, END)

def openfile(event = None) :
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + " - Notepad")
        textbox.delete(1.0, END)
        f = open(file, "r")
        textbox.insert(1.0, f.read())
        f.close()

def deleteall(event = None) :
      textbox.delete(1.0, END)

def saveas(event = None) :
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(textbox.get(1.0, END))
            f.close()

            window.title(os.path.basename(file) + " - Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textbox.get(1.0, END))
        f.close()

def fontsize() :
    pass
def fonttype() :
    pass
def fontcolour() :
    pass
def bold(event = None) :
    pass
def italic(event = None) :
    pass
def lineunder(event = None) :
    pass
def copy(event = None) :
    textbox.event_generate(("<<Copy>>"))

def paste(event = None) :
    textbox.event_generate(("<<Paste>>"))

def cut(event = None) :
     textbox.event_generate(("<<Cut>>"))

def aboutas() :
    box.showinfo("About us","This Notepad is Created by Hitesh Mori\nNirma University , Ahmedabad\nCompleted : Tuesday,23:46 PM,7 March 2023")
def feedback() :
    a =  box.askquestion("Feedback","This Notepad Good or Not ?")
    if a=='yes' :
        box.showinfo("Feedback","Thanks for positive reply")
    
        if(not os.path.exists("FEEDBACK.txt")) :
            with open("FEEDBACK.txt","a") as f :
                f.write("")


        with open("FEEDBACK.txt","a") as f :
                        f.write(str("yes\n"))
    elif a=='no' :
        box.showinfo("Feedback","We will try to improve this software")
        if(not os.path.exists("FEEDBACK.txt")) :
            with open("FEEDBACK.txt","a") as f :
                f.write("")


        with open("FEEDBACK.txt","a") as f :
                        f.write(str("no\n"))
       

            
def help1() :
    pass

#sub menu of file------------------------------------------------------------------------
menu1 = Menu(mainmenu,tearoff=0)

menu1.add_command(label="New File",command=newfile,accelerator="Ctrl+N")
menu1.bind_all("<Control-n>",newfile)

menu1.add_command(label="Open File",command=openfile,accelerator="Ctrl+O")
menu1.bind_all("<Control-o>",openfile)

menu1.add_separator()

menu1.add_command(label="Delete all",command=deleteall,accelerator="Ctrl+D")
menu1.bind_all("<Control-d>",deleteall)

menu1.add_command(label="Save us",command=saveas,accelerator="Ctrl+S")
menu1.bind_all("<Control-s>",saveas)

menu1.add_command(label="Exit",command=quit,accelerator="Ctrl+e")
menu1.bind_all("<Control-e>",exit)


#sub menu of edit-------------------------------------------------------------------------
menu3 = Menu(mainmenu,tearoff=0)

menu3.add_command(label="Copy",command=copy,accelerator="Ctrl+C")
menu3.bind_all("<Control-c>",copy)

menu3.add_command(label="Paste",command=paste,accelerator="Ctrl+P")
menu3.bind_all("<Control-p>",paste)

menu3.add_command(label="Cut",command=cut,accelerator="Ctrl+K")
menu3.bind_all("<Control-k>",cut)

menu3.add_command(label="undo",command=textbox.edit_undo,accelerator="Ctrl+Z")

menu3.add_command(label="redo",command=textbox.edit_redo,accelerator="Ctrl+Y")


#sub menu of Format-----------------------------------------------------------------------
menu2 = Menu(mainmenu,tearoff=0)
menu2.add_command(label="Font Size",command=fontsize)

menu2.add_command(label="Font Colour",command=fontcolour)

menu2.add_command(label="Font Type",command=fonttype)

menu2.add_separator()

menu2.add_command(label="Bold",command=bold,accelerator="Ctrl+B")
menu2.bind_all("<Control-b>",bold)

menu2.add_command(label="Italic",command=italic,accelerator="Ctrl+I")
menu2.bind_all("<Control-i>",italic)

menu2.add_command(label="Underline",command=lineunder,accelerator="Ctrl+U")
menu2.bind_all("<Control-u>",lineunder)

# main menu------------------------------------------------------------------------------ 
mainmenu.add_cascade(label="File",menu=menu1)

mainmenu.add_cascade(label="Edit",menu=menu3)

mainmenu.add_cascade(label="Format",menu=menu2)

mainmenu.add_command(label="About as",command=aboutas)

mainmenu.add_command(label="Feedback",command=feedback)

mainmenu.add_command(label="Help",command=help1)

window.config(menu=mainmenu)
#----------------------------------------------------------------------------------------
window.mainloop()