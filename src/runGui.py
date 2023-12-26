import tkinter as tk
from tkinter import messagebox
from UW import UWPropsLauncher
import multiprocessing

def run_task(battleVal,battleCity):
    UWPropsLauncher.run({"battleOn": battleVal,"battleCity": battleCity})

def onBattleCheckbox():
    # 根据复选框1的状态显示或隐藏下拉菜单
    if battleVar.get():
        cityLabel.pack()
        cityDropdown.pack()
    else:
        cityDropdown.pack_forget()
        cityLabel.pack_forget()

def on_confirm():   
    global process
    process  = multiprocessing.Process(target=run_task, args=(battleVar.get(),cityVar.get()))
    process.start()
    appRunningLabel.config(text="状态：active")

def on_cancel():
    # 结束应用程序
    if process.is_alive():
        process.terminate()
        process.join()
        root.destroy()
    else:
        messagebox.showinfo("Notifications","还没启动呢")

if __name__ == '__main__':
    # 创建主窗口
    root = tk.Tk()
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 计算窗口的x和y坐标，使窗口靠右侧显示
    window_width = 300
    window_height = 200
    # root.geometry(f"{window_width}x{window_height}")
    x = screen_width - window_width - 100
    y = (screen_height - window_height) // 2 - 200

    # 更新窗口的几何属性
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.title("UW-HELPER")

    # thread=threading.Thread(target=lambda: UWPropsLauncher.run({"battleOn": battle_var.get()}))

    battleVar = tk.BooleanVar()
    battleCheckbox = tk.Checkbutton(root, text="开启战斗", variable=battleVar, command=onBattleCheckbox)
    battleCheckbox.pack()

    cityLabel = tk.Label(root, text="战斗城市")
    # cityLabel.pack()

    # 创建下拉菜单
    cityOptions = ["narvik", "hag"]
    cityVar = tk.StringVar()
    cityVar.set(cityOptions[0])  # 设置默认值
    cityDropdown = tk.OptionMenu(root, cityVar, *cityOptions)

    # 创建一个标签来显示变量的值
    appRunningLabel = tk.Label(root, text="状态：not active")
    appRunningLabel.pack()

    # 创建确认按钮
    confirm_button = tk.Button(root, text="启动", command=on_confirm)
    confirm_button.pack()

    # 创建取消按钮
    cancel_button = tk.Button(root, text="关闭", command=on_cancel)
    cancel_button.pack()


    # 运行主循环
    root.mainloop()