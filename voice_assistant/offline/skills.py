import os
import webbrowser
import sys
import requests
import subprocess
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 180)  # скорость речи


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def weather():
    # нужна регистрация на сайте
    try:
        params = {'q': 'London', 'units': 'metric', 'lang': 'ru', 'appid': 'ключ к API'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def browser():
    webbrowser.open('https://www.google.ru/')


def game():
    # .exe file (!)
    subprocess.Popen('C:\windows_upgrade\Rainmeter___Ageo\Rainmeter + Ageo\Rainmeter.exe')


def off_pc():
    # выключает пк с ос windows
    os.system('shutdown/s')


def offBot():
    sys.exit()


def passive():
    pass
