import tkinter as tk
from tkinter import messagebox
import threading
import time

def show_countdown_timer(seconds):
    # 创建主窗口
    window = tk.Tk()
    window.title("倒计时提醒")

    # 设置窗口大小和位置
    window.geometry("300x100+500+300")

    # 创建Label用于显示倒计时
    label = tk.Label(window, text=str(seconds), font=("Helvetica", 24))
    label.pack(pady=20)

    def update_label():
        nonlocal seconds
        if seconds > 0:
            seconds -= 1
            label.config(text=str(seconds))
            window.after(1000, update_label)
        else:
            window.destroy()

    # 启动倒计时线程
    countdown_thread = threading.Thread(target=update_label)
    countdown_thread.start()

    # 运行主循环
    window.mainloop()

def trigger_countdown(sec):
    # 设定倒计时时间（秒）
    countdown_seconds = sec

    # 显示倒计时提醒界面
    show_countdown_timer(countdown_seconds)

    # 在倒计时结束后，可以执行其他操作
    print("倒计时结束，执行其他操作")

