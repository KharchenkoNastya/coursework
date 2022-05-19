import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import img_send


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")

@dp.message_handler()
async def get_weather(message: types.Message):
    chat_id = message.chat.id
    #photo1 = open("img\icon_bot.jpg", "rb")
    #photo2 = open("img\Frame.jpg", "rb")
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
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        # now_date = datetime.datetime.now().strftime('%Y-%m-%d')
        city = data["name"]
#!!!!!
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        #else:
        #wd = "Посмотри в окно сам!"

        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        speed = data["wind"]["speed"]
        feels_like = data["main"]["feels_like"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        l_day_light = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d')} {wd} ***\n"
              f"Погода в городе: {city}\nТемпература {cur_weather}C°\n"
              f"Ощущается как: {feels_like} C°\n"
              f"Важность: {humidity}%\nДавление: {pressure} мм.рт.ст\n"
              f"Скорость ветра: {speed} м/c\nВремя рассвета: {sunrise_timestamp}\n"
              f"Время заката: {sunset_timestamp}\nПродолжительность дня: {l_day_light}"

              )

        if ((feels_like >= -30) and (feels_like <= -25)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo1)
        if ((feels_like >= -24) and (feels_like <= -20)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo2)
        if ((feels_like >= -19) and (feels_like <= -15)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo3)
        if ((feels_like >= -14) and (feels_like <= -10)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo4)
        if ((feels_like >= -9) and (feels_like <= -5)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo5)
        if ((feels_like >= -4) and (feels_like <= 0)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo6)
        if ((feels_like >= 1) and (feels_like <= 5)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo7)
        if ((feels_like >= 6) and (feels_like <= 10)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo8)
        if ((feels_like >= 11) and (feels_like <= 15)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo9)
        if ((feels_like >= 16) and (feels_like <= 20)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo10)
        if ((feels_like >= 21) and (feels_like <= 25)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo11)
        if ((feels_like >= 26) and (feels_like <= 30)):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo12)
        if (feels_like < -30):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo13)
        if (feels_like > 30):
            await bot.send_photo(caption="", chat_id=chat_id, photo=img_send.photo14)
        else:
            await message.reply("")

    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")

if __name__ == '__main__':
    executor.start_polling(dp)