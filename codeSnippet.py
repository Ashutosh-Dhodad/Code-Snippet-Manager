from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkcode import CodeEditor
from tkinter import font
import subprocess

root = Tk()
root.title("Code Snippet Manager")
root.geometry("1420x820")
file_path = ""

def set_file_path(path):
    global file_path
    file_path = path

    
def submit():
    folderName =searchEntry.get()
    print(folderName)
def openFile():
    try:
        filePath=filedialog.askopenfilename(title="Open File?",
                                        initialdir="D:\\",
                                        filetypes=(("text files","*.txt"),("all files","*.*"))
                                        )
        file = open(filePath,"r")
        print(file.read())
        file.close()
    except:
        print("Exception handled")

def run():
    path = f'python{file_path}'
    process = subprocess.Popen(COMMAND,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output,error = process.communicate()
    code_output.insert("1.0",output)
    code_output.insert("1.0",error)

def save_as():
    if(file_path==""):
        path = filedialog.asksaveasfilename( filetypes=(("text files","*.txt"),("all files","*.*")))
    else:
        path = file_path
    with open(path,"w") as file:
        code = editor.get("1.0",END)
        file.write(code)
        set_file_path(path)
        
def open_file():
    path = filedialog.asksaveasfilename(filetypes=(("text files","*.txt"),("all files","*.*")))
    with open(path,"r+") as file:
        code = file.read()
        editor.delete("1.0",END)
        editor.insert("1.0",code)
        set_file_path(path)

#Side frame Widget
sideFrame = Frame(root,bg="grey",
                  bd=2,
                  relief=SUNKEN,
                  height=900,
                  width=300)
sideFrame.place(x=0,y=0),

#MiddleFrame Widget
middleFrame = Frame(root,bg="grey",
                  bd=2,
                  relief=SUNKEN,
                  height=900,
                  width=500)
middleFrame.place(x=300,y=0),
editor = Text(middleFrame)
editor.pack(pady=5,padx=5)

runButton = Button(middleFrame,text="Run",
                   command=run)
runButton.pack(side=TOP,)
saveButton = Button(middleFrame,text="Save",
                    command=save_as
                   )
saveButton.pack(side=TOP)

openButton = Button(middleFrame,text="Open",
                    command=open_file
                   )
openButton.pack(side=TOP)


#LastUpperFrame Widget
lastUpperFrame = Frame(root,bg="grey",
                  bd=2,
                  relief=SUNKEN,
                  height=400,
                  width=600)
lastUpperFrame.place(x=800,y=0),
code_output = Text(lastUpperFrame,)
code_output.pack(pady=5,padx=5)



#lastDownFrame widget
lastDownFrame = Frame(root,bg="grey",
                  bd=2,
                  relief=SUNKEN,
                  height=400,
                  width=600)
lastDownFrame.place(x=800,y=400),

searchLabel = Label(root,
                    text = "Search Code Snippet",
                    activebackground="grey",
                    background="#649e98").pack(anchor=W,padx=10,pady=10)
searchEntry = Entry(root,name="seach",
                    font=("Arial",10),
                    )
searchEntry.pack(side=LEFT,anchor=N,padx=5)
submitButton = Button(root,text="Search",command= submit)
submitButton.pack(side=LEFT,anchor=N,padx=5)
openFileButton = Button(text="Open File",command=openFile)
openFileButton.pack(side=LEFT,anchor=N,padx=5)
iconPhoto = PhotoImage(file="D:\\PythonProject\\Code-Snippet-Manager\\logo.png",
                       height=100,width=100)
root.iconphoto(True,iconPhoto)
root.config(background="#649e98")
root.mainloop()
