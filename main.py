from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title("My Compiler")
file_path = ""


def open_file():
    path = askopenfilename(
        filetypes=[("Python Files", "*.py")],
    )
    with open(path, "r") as file:
        code = file.read()
        editor.delete("1.0", END)
        editor.insert("1.0", code)
        set_file_path(path)


def set_file_path(path):
    global file_path
    file_path = path


def save_as():
    if file_path == "":
        path = asksaveasfilename(
            filetypes=[("Python Files", "*.py")],
        )
    else:
        path = file_path
    with open(path, "w") as file:
        code = editor.get("1.0", END)
        file.write(code)


def run():
    if file_path == "":
        save_prompt = Toplevel()
        text = Label(save_prompt, text="Please save your code")
        text.pack()
        return
    command = f"python {file_path}"
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    compiler_output.insert("1.0", output)
    compiler_output.insert("1.0", error)


menu_bar = Menu(compiler)

file_bar = Menu(menu_bar, tearoff=0)
file_bar.add_command(label="Open", command=open_file)
file_bar.add_command(label="Save", command=save_as)
file_bar.add_command(label="Save As", command=save_as)
file_bar.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="File", menu=file_bar)
compiler.config(menu=menu_bar)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)
compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

compiler_output = Text(height=7)
compiler_output.pack()

compiler.mainloop()
