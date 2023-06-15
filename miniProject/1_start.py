from tkinter import*
from miniProject.age import age
from miniProject.weather import weather
from miniProject.miniGame import minigame

win = Tk()

win.title("miniProject")

win_x = 250
win_y = 150
total_x = win.winfo_screenwidth()
total_y = win.winfo_screenheight()
x_position = int((total_x/2) - (win_x/2))
y_position = int((total_y/2) - (win_y/2))

win.geometry("{0}x{1}+{2}+{3}".format(win_x, win_y,x_position, y_position))
win.resizable(True, True)

button1 = Button(win, font=("고딕", 10), text="만나이 계산기", overrelief="solid", width=12, height=2, command=age)
button1.pack(padx=5, pady= 10, side="top")

button2 = Button(win, font=("고딕", 10), text="오늘 날씨", overrelief="solid", width=12, height=2, command=weather)
button2.pack(padx=5, pady= 5)

button3 = Button(win, font=("고딕", 10), text="EXIT", width=12, height=2, command=win.quit)
button3.pack(padx=5, pady= 5, side="bottom")


win.mainloop()
