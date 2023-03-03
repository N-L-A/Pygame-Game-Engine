import tkinter

import pygame.display

from PE_tools import maths
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

# init - making hidden tkinter root for the messages
root = tkinter.Tk()
root.title("Dialogs root")
root.withdraw()
# init end


def ask_open_file(title: str, file_types=[('all files', '*')], initial_dir=None):
    """open file explorer and get the path as string of the selected file"""
    return filedialog.askopenfilename(title=title, initialdir=initial_dir, filetypes=file_types)


def ask_open_files(title: str, file_types=[('all files', '*')], initial_dir=None):
    """open file explorer and get the paths as strings of the selected files inside a tuple"""
    return filedialog.askopenfilenames(title=title, initialdir=initial_dir, filetypes=file_types)


def ask_open_folder(title: str, initial_dir=None):
    """open file explorer and get the path as string of the selected folder"""
    return filedialog.askdirectory(title=title, initialdir=initial_dir)


def show_error(title: str, message: str):
    """show system error message"""
    return messagebox.showerror(title, message)


def show_info(title: str, message: str):
    """show system information message"""
    return messagebox.showinfo(title, message)


def show_warning(title: str, message: str):
    """show system warning message"""
    return messagebox.showwarning(title, message)


def ask_yes_no(title: str, message: str, icon='question'):
    """show system message with 2 buttons: yes, no. and get the bool value for his choice"""
    return messagebox.askyesno(title, message, icon=icon)


def ask_ok_cancel(title: str, message: str, icon='question'):
    """show system message with 2 buttons: ok, cancel. and get the bool value for his choice"""
    return messagebox.askokcancel(title, message, icon=icon)


def ask_retry_cancel(title: str, message: str, icon='error'):
    """show system message with 2 buttons: retry, cancel. and get the bool value for his choice"""
    return messagebox.askretrycancel(title, message, icon=icon)


def ask_yes_no_cancel(title: str, message: str, icon='question'):
    """show system message with 3 buttons: yes, no, cancel. and get the bool value for his choice, or None value for
    cancel"""
    return messagebox.askyesnocancel(title, message, icon=icon)


def ask_int(title: str, message: str, num_range=None):
    """show system message with input label that you can put in only integer in specific range"""
    ans = simpledialog.askinteger(title, message)
    if num_range:
        while (ans not in num_range) and ans:
            show_warning("range error", f"your integer must be in range: {num_range}")
            ans = simpledialog.askinteger(title, message)
            if not ans: break
    return ans


def ask_float(title: str, message: str, num_range=None):
    """show system message with input label that you can put in only float in specific range"""
    ans = simpledialog.askfloat(title, message)
    if num_range:
        while (not maths.float_in_range(ans, num_range)) and ans:
            show_warning("range error", f"your float must be in range: {num_range}")
            ans = simpledialog.askfloat(title, message)
            if not ans: break
    return ans


def ask_str(title: str, message: str):
    """show system message with input label"""
    return simpledialog.askstring(title, message)


def ask_bool_console(question: str, options_true=["yes", "y"], options_false=["no", "n"]):
    """ask the user for bool value in the console"""
    inp = input(question)
    while inp not in options_true and inp not in options_false:
        inp = input(f"'{inp}' isn't correct value, please use: '{options_true[0]}' or '{options_false[0]}': ")
    return inp in options_true


def ask_float_console(question: str, num_range: range):
    """ask the user for float value in the console"""
    inp = input(question)
    while not maths.string_in_range(inp, num_range):
        inp = input(f"'{inp}' isn't correct value, please use enter a float in range: {num_range} : ")
    return float(inp)


def ask_int_console(question: str, num_range: range):
    """ask the user for int value in the console"""
    inp = input(question)
    while not maths.string_in_range(inp, num_range) or inp.find(".") > 0:
        inp = input(f"'{inp}' isn't correct value, please use enter an integer in range: {num_range} : ")
    return int(inp)


def set_cursor_icon(icon: pygame.cursors.Cursor):
    """change cursor system icon"""
    pygame.mouse.set_cursor(icon)
