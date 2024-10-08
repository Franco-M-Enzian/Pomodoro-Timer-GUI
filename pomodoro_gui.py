import tkinter as tk
from tkinter import PhotoImage, messagebox

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

        # タイトルラベル
        self.label = tk.Label(root, text="Welcome to Pomodoro Timer", font=("Helvetica", 24))
        self.label.pack(pady=20)

        # タイマー表示ラベル
        self.time_label = tk.Label(root, text="", font=("Helvetica", 48))
        self.time_label.pack()

        # Startボタン
        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Helvetica", 14))
        self.start_button.pack(pady=20)

        # Closeボタン
        self.close_button = tk.Button(root, text="Close", command=self.close_app, font=("Helvetica", 14))
        self.close_button.pack(pady=20)
        self.close_button.pack_forget()  # 初期状態では非表示

    def update_timer(self):
        mins, secs = divmod(self.remaining_time, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        self.time_label.config(text=timeformat)

        if self.running and self.remaining_time > 0:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        elif self.remaining_time == 0 and self.running:
            self.handle_session_end()

    def handle_session_end(self):
        if self.current_cycle % 2 == 1:
            # 作業時間終了時
            messagebox.showinfo("タイマー終了", "時間になりました。休憩しましょう！")
            self.label.config(text="Short Break")
            self.remaining_time = self.short_break
        else:
            # 休憩時間終了時
            if self.current_cycle == self.cycles * 2 - 1:
                messagebox.showinfo("タイマー終了", "時間になりました。長い休憩を取りましょう！")
                self.label.config(text="Long Break")
                self.remaining_time = self.long_break
            else:
                messagebox.showinfo("タイマー終了", "休憩が終わりました。次の作業を始めましょう！")
                self.label.config(text=f"Cycle {self.current_cycle // 2 + 1} - Work Time")
                self.remaining_time = self.work_time

        self.current_cycle += 1

        # 4回目のサイクル終了後に1回目のサイクルに戻る
        if self.current_cycle >= self.cycles * 2:
            self.current_cycle = 0

        self.update_timer()

    def start_timer(self):
        print("Start button clicked")  # デバッグ用
        self.running = True
        self.current_cycle = 1
        self.label.config(text=f"Cycle {self.current_cycle} - Work Time")
        self.remaining_time = self.work_time
        self.start_button.pack_forget()  # Startボタンを非表示
        self.close_button.pack(pady=20)  # Closeボタンを表示
        self.update_timer()

    def close_app(self):
        self.root.quit()  # アプリケーションを終了

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    print("Starting main loop")
    try:
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")