# gui.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(__file__ + "\\..\\..\\utils"))

from CDKManager import CDKeyManager
from UWLauncher import UWLauncher


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("功能管理器")
        self.geometry("800x600")

        self.CDKeyManager = CDKeyManager()
        self.UWLauncher = UWLauncher

        self.frames = {}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (CDKeyPage, MainPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        if self.CDKeyManager.is_verified():
            self.show_frame(MainPage)
        else:
            self.show_frame(CDKeyPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class CDKeyPage(tk.Frame):
    def __init__(self, parent, controller: Application):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="请输入CDKey", font=("Helvetica", 14))
        label.pack(pady=10, padx=10)

        self.cdkey_entry = tk.Entry(self)
        self.cdkey_entry.pack(pady=10)

        verify_button = tk.Button(self, text="验证", command=self.verify_cdkey)
        verify_button.pack()

    def verify_cdkey(self):
        cdkey = self.cdkey_entry.get()
        if self.controller.CDKeyManager.verify_key(cdkey):
            self.controller.CDKeyManager.save_verification()
            self.controller.CDKeyManager(MainPage)
        else:
            messagebox.showerror("错误", "无效的CDKey")


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both")

        self.tabs = []
        for i in range(3):
            tab = FunctionTab(self.notebook, f"功能组{i+1}")
            self.tabs.append(tab)
            self.notebook.add(tab, text=f"功能组{i+1}")

        start_button = tk.Button(self, text="启动", command=self.start)
        start_button.pack(pady=10)

    def start(self):
        current_tab = self.notebook.select()
        tab_id = self.notebook.index(current_tab)
        options = self.tabs[tab_id].get_options()

        self.controller.UWLauncher.run(tab_id + 1, options)


class FunctionTab(tk.Frame):
    def __init__(self, parent, name):
        tk.Frame.__init__(self, parent)
        self.name = name

        self.checkboxes = []
        self.vars = []

        options = ["选项1", "选项2", "选项3", "选项4"]
        for option in options:
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self, text=option, variable=var)
            checkbox.pack(pady=5, anchor="w")
            self.checkboxes.append(checkbox)
            self.vars.append(var)

    def get_options(self):
        return {f"选项{i+1}": var.get() for i, var in enumerate(self.vars)}
