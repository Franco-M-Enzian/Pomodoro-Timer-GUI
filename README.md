# Pomodoro-Timer-GUI
ポモドーロテクニックを使ったGUIタイマーアプリ。
コードは全てChatGPT製。アイコンはいらすとやから画像1点を利用。

## How to Use
下記コマンドを実行するとアプリが起動し、"Start"をクリックすることで最初のサイクルが開始する（25分作業5分休憩）。
```
python pomodoro_gui.py
```
作業、休憩のサイクルを4回繰り返し、4回目が終了すると自動で1回目のサイクルに戻る。

## BAT file
start_pomodoro_timer.bat
```
@echo off
python C:\---\---\Timer-GUI\pomodoro_gui.py
```
このファイルをコピーしてクリックすると、コマンドを自分で打たなくても起動できる。
