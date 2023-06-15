from tkinter import*
from requests import *
from bs4 import BeautifulSoup

def weather():
    weather = Tk()
    weather.title("오늘 날씨")
    weather_x = 230
    weather_y = 200
    total_x = weather.winfo_screenwidth()
    total_y = weather.winfo_screenheight()
    x_position = int((total_x / 2) - (weather_x / 2))
    y_position = int((total_y / 2) - (weather_y / 2))

    # 윈도우 크기 가로*세로
    weather.geometry("{0}x{1}+{2}+{3}".format(weather_x, weather_y, x_position, y_position))
    weather.resizable(True, True)

    global temp
    global tempText
    global wind
    global humidity
    global dust

    def wsearch():
        keyword = went1.get()
        baseUrl = "https://search.daum.net/search?w=tot&q="
        response = get(f"{baseUrl}{keyword}날씨")
        html = BeautifulSoup(response.text, "html.parser")
        weathers = html.select("div.wrap_region")
        for weat in weathers:
            tempText = weat.select_one("span.txt_weather").text.strip()
            temp = weat.select_one("strong.txt_temp").text.strip()
            datas = weat.select("dl.dl_weather")
            wdata = []
            for da in datas:
                data = da.select_one("dd").text
                wdata.append(data)
        wind = wdata[0]
        humidity = wdata[1]
        dust = wdata[2]

        la2.config(text=f"현재온도: {temp}")
        la3.config(text=f"현재풍속: {wind}m/s")
        la4.config(text = f"현재습도: {humidity}%")
        la5.config(text=f"미세먼지: {dust}")

    la0 = Label(weather, font=("고딕", 10), text=" 지역", height=2)

    la2 = Label(weather, font=("고딕", 10), height=2)
    la3 = Label(weather, font=("고딕", 10), height=2)
    la4 = Label(weather, font=("고딕", 10), height=2)
    la5 = Label(weather, font=("고딕", 10), height=2)

    went1 = Entry(weather, font=("고딕", 10), bg='white', width=22)

    but1 = Button(weather, font=("고딕", 10), text="검색", overrelief="solid", width=6, height=1, command=wsearch)


    la0.grid(row=0, column=0, sticky="w")

    la2.grid(row=3, column=0, sticky="w", padx=5)
    la3.grid(row=4, column=0, sticky="w", padx=5)
    la4.grid(row=5, column=0, sticky="w", padx=5)
    la5.grid(row=6, column=0, sticky="w", padx=5)

    went1.grid(row=1, column=0, padx=5)

    but1.grid(row=1, column=1)

