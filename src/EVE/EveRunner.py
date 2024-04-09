import tkinter as tk
from tkinter import messagebox, scrolledtext
from enemyChecker import runTask
import multiprocessing
from utils import *
from windows import *


class Runner:
    processes = []
    allWindowsWithTitle = []
    appRunningLabel = None
    queue = None
    text = ""
    text_area = None

    def __init__(self) -> None:
        self.pauseEvent = multiprocessing.Event()
        self.queue = multiprocessing.Queue()

    def on_reset(self):
        self.on_stop()
        self.on_start()

    def on_start(self):
        for index, window in enumerate(self.allWindowsWithTitle):
            process = multiprocessing.Process(
                target=runTask,
                args=[window["hwnd"], index, [self.pauseEvent, self.queue]],
            )
            process.start()
            self.processes.append(process)
            self.appRunningLabel.config(text="状态：运行中")

    def update_gui_from_queue(self, text_area):
        while not self.queue.empty():
            message = self.queue.get()
            text_area.insert(tk.END, message + "\n")
        # Schedule this function to be called again after 100ms
        root.after(100, self.update_gui_from_queue, text_area)

    def on_pause(self):
        # 暂停应用程序
        if self.pauseEvent.is_set():
            self.pauseEvent.clear()
        else:
            self.pauseEvent.set()
        self.appRunningLabel.config(
            text="状态：已暂停" if self.pauseEvent.is_set() else "状态：运行中"
        )

    def on_stop(self):
        # 结束应用程序
        try:
            for process in self.processes:
                process.terminate()
            for process in self.processes:
                self.processes.remove(process)
            self.text_area.delete(1.0, tk.END)
            self.appRunningLabel.config(text="状态：停止")
        except NameError:
            messagebox.showinfo("Notifications", "还没启动呢")


if __name__ == "__main__":
    # 创建主窗口
    global root
    root = tk.Tk()
    runner = Runner()

    print("开工前todo list: 打开本地列表,v船到广角,驻地最后一个,改变战斗列表为名称排序")
    #
    runner.allWindowsWithTitle = getAllWindowsWithTitles(
        ["MuMu模拟器-1", "MuMu模拟器-2"], 1254, 741
    )
    runner.processes = []
    runner.text = ""

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 计算窗口的x和y坐标，使窗口靠右侧显示
    window_width = 300
    window_height = 400
    # root.geometry(f"{window_width}x{window_height}")
    x = screen_width - window_width - 100
    y = (screen_height - window_height) // 2 - 200

    # 更新窗口的几何属性
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.title("EVE-HELPER")

    # 创建一个标签来显示变量的值
    runner.appRunningLabel = tk.Label(root, text="状态：停止")
    runner.appRunningLabel.pack()

    # 创建确认按钮
    confirm_button = tk.Button(root, text="启动", command=runner.on_start)
    confirm_button.pack()

    # 创建确认按钮
    reset_button = tk.Button(root, text="重置", command=runner.on_reset)
    reset_button.pack()

    # 创建确认按钮
    pause_button = tk.Button(root, text="暂停", command=runner.on_pause)
    pause_button.pack()

    # 创建取消按钮
    stop_button = tk.Button(root, text="停止", command=runner.on_stop)
    stop_button.pack()

    runner.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    runner.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    runner.text_area.insert(tk.END, runner.text)

    runner.update_gui_from_queue(runner.text_area)

    # 运行主循环
    root.mainloop()
