import telebot
from pprint import pprint
import datetime
import requests
from config import open_weather_token

#botkey = telebot.TeleBot('5331601500:AAE1gK-lhMGsOmcVEoeumilLXcqq4__aX9s')

def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        #now_date = datetime.datetime.now().strftime('%Y-%m-%d')
        city = data["name"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно сам!"

        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        speed = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        l_day_light = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d')} {wd} ***\n"
              f"Погода в городе: {city}\nТемпература {cur_weather}C°\n"
              f"Важность: {humidity}%\nДавление: {pressure} мм.рт.ст\n"
              f"Скорость ветра: {speed} м/c\nВремя рассвета: {sunrise_timestamp}\n"
              f"Время заката: {sunset_timestamp}\nПродолжительность дня: {l_day_light}"
              )

    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
