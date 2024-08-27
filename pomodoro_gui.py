import tkinter as tk
from tkinter import PhotoImage

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        # ウィンドウを常にトップに表示
        self.root.attributes("-topmost", True)

        # アプリのアイコンを設定
        icon = PhotoImage(file='tokei.png')
        root.iconphoto(False, icon)

        self.work_time = 25 * 60  # 作業時間（秒）
        self.short_break = 5 * 60  # 短い休憩時間（秒）
        self.long_break = 15 * 60  # 長い休憩時間（秒）
        self.cycles = 4  # サイクル数

        self.current_cycle = 0
        self.remaining_time = 0
        self.running = False

        self.label = tk.Label(root, text="Welcome to Pomodoro Timer", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.time_label = tk.Label(root, text="", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Helvetica", 14))
        self.start_button.pack(pady=20)

    def update_timer(self):
        mins, secs = divmod(self.remaining_time, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        self.time_label.config(text=timeformat)

        if self.running and self.remaining_time > 0:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        elif self.remaining_time == 0 and self.running:
            self.label.config(text="Time is up!")
            self.root.after(1000, self.start_next_session)

    def start_timer(self):
        self.running = True
        self.current_cycle = 1
        self.label.config(text=f"Cycle {self.current_cycle} - Work Time")
        self.remaining_time = self.work_time
        self.update_timer()

    def start_next_session(self):
        if self.current_cycle < self.cycles:
            if self.current_cycle % 2 == 1:
                self.label.config(text="Short Break")
                self.remaining_time = self.short_break
            else:
                self.label.config(text=f"Cycle {self.current_cycle // 2 + 1} - Work Time")
                self.remaining_time = self.work_time
            self.current_cycle += 1
        else:
            self.label.config(text="Long Break")
            self.remaining_time = self.long_break
        self.update_timer()

    def stop_timer(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
