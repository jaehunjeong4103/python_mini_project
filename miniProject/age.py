from tkinter import*
import time

def age():
    age = Tk()
    age.title("만 나이 계산기")
    age_x = 280
    age_y = 250
    total_x = age.winfo_screenwidth()
    total_y = age.winfo_screenheight()
    x_position = int((total_x / 2) - (age_x / 2))
    y_position = int((total_y / 2) - (age_y / 2))

    # 윈도우 크기 가로*세로
    age.geometry("{0}x{1}+{2}+{3}".format(age_x, age_y, x_position, y_position))
    age.resizable(True, True)

    global tyear
    global tmonth
    global tday
    global inyear
    global inmonth
    global inday

    today = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    tyear = int(time.strftime('%Y', time.localtime(time.time())))
    tmonth = int(time.strftime('%m', time.localtime(time.time())))
    tday = int(time.strftime('%d', time.localtime(time.time())))

    def dates():
        inyear = int(ent1.get())
        inmonth = int(ent2.get())
        inday = int(ent3.get())
        age = tyear - inyear
        if tmonth < inmonth:
            age -= 1
        elif tmonth == inmonth:
            if day < inday:
                age -= 1

        ansDate.config(text=ent1.get() + "." + ent2.get() + "." + ent3.get())
        ansRealAge.config(text=f"만 {age}세")

    label0 = Label(age, font=("고딕", 10), text ="만 나이계산을 해봅시다")
    year = Label(age, font=("고딕", 10), text="년")
    month = Label(age, font=("고딕", 10), text="월")
    day = Label(age, font=("고딕", 10), text="일")
    stand = Label(age, font=("고딕", 10), text="기준일")
    ansStand = Label(age, font=("고딕", 10), text=today)
    date = Label(age, font=("고딕", 10), text="출생일")
    ansDate = Label(age, font=("고딕", 10))
    realAge = Label(age, font=("고딕", 10), text="만나이")
    ansRealAge = Label(age, font=("고딕", 10))

    input_text = IntVar

    ent1 = Entry(age,  font=("고딕", 10), bg='white', width=27)
    ent2 = Entry(age,  font=("고딕", 10), bg='white', width=27)
    ent3 = Entry(age,  font=("고딕", 10), bg='white', width=27)

    bt1 = Button(age, font=("고딕", 10), text="계산하기", overrelief="solid", width=15, height=2, command=dates)


    label0.grid(row=0, column=1, padx=5, pady=5)
    year.grid(row=1, column=0, padx=5, pady=5)
    month.grid(row=2, column=0, padx=5, pady=5)
    day.grid(row=3, column=0, padx=5, pady=5)
    stand.grid(row=5, column=0, padx=5, pady=5)
    ansStand.grid(row=5, column=1)
    date.grid(row=6, column=0, padx=5, pady=5)
    ansDate.grid(row=6, column=1)
    realAge.grid(row=7, column=0, padx=5, pady=5)
    ansRealAge.grid(row=7, column=1)

    ent1.grid(row=1, column=1)
    ent2.grid(row=2, column=1)
    ent3.grid(row=3,column=1)

    bt1.grid(row=4,column=1)
