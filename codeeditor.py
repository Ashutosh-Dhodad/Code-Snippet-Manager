code_editor = CodeEditor(
    middleFrame,
    width=99,
    height =30,
    language="python",
    highlighter="dracula",
    background = "black",
    font = "Consolas",
    autofocus=True,
    blockcursor = True,
    insertofftime=0,
    padx =10,
    pady=10,   
)
code_editor.pack()