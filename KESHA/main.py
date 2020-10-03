# Голосовой ассистент КЕША 1.0 BETA
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import random as rnd
import sys
import webbrowser as web
from gtts import gTTS
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")


# настройки
opts = {
    "alias": ('кеша','кеш','инокентий','иннокентий','кишун','киш',
              'кишаня','кяш','кяша','кэш','кэша', 'яша'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси', 'подкинь', 'кинь', 'брось', 'открой', 'аткрой', 'покажи', 'запусти'),
    "cmds": {
        "money": ('монетка', 'орёл или пешка', 'орёл или решка', 'монитку', 'манитку', 'манетку', 'манетка', 'орел или пешка', 'орел или решка'),
        "ctime": ('текущее время','сейчас времени','который час'),
        "radioe": ('включи энерджи','воспроизведи радио энерджи','включи радио энерджи'),
        "radioen": ('включи energy','воспроизведи радио energy','включи радио energy'),
        "radioep": ('включи европу','воспроизведи радио европа','включи радио европа плюс'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты'),
        "youtube": ('ютуб', 'йутуб' , 'youtube', 'видио', 'видео', 'ютаб', 'йутаб'),
        "google": ('гугл', 'гуугл' , 'google', 'поиск', 'гугал', 'гугол', 'googl'),
        "bad": ('лох','тупой','идиод','придурок','дибил','ужасный'),
        "restart": ('перезагрузка', 'перезапуск'),
        "weather": ('погода', 'пагода' , 'погодка', 'какая погода', 'сколько градусов', 'Тепло на улице?', 'температура')
    }
}

# функции
def speack(what):
    print(what)
    speak.Speak(what)
    time.sleep(0.4)
def youtub():
    web.open("https://www.youtube.com/alexnet")
    time.sleep(0.4)

def googl():
    web.open("https://www.google.com")
    time.sleep(0.4)

def weath():
    web.open("https://yandex.ru/pogoda/")
    time.sleep(0.4)
# def speak(what):
#     print( what )
#     speak_engine.say( what )
#     speak_engine.runAndWait()
#     speak_engine.stop()
#

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Кеше
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC

def execute_cmd(cmd):
    print(cmd)
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speack("Сейчас " + str(now.hour) + 'часов' + ":" + str(now.minute) + 'Минут')
    elif cmd == 'bad':
        speack('Такой... умный?')
        time.sleep(0.5)
        speack("А ты сам кто,,,,,,,,,, , скажи?")
    elif cmd == 'radioe' or cmd == 'radioen':
        # воспроизвести радио

        os.system("e.m3u")
        speack('Включаю радио энерджи!')


    elif cmd == 'radioep':
            # воспроизвести радио
        os.system("ep.m3u")
        speack('Включаю радио европа плюс!')

    elif cmd == 'money':
        result = rnd.randint(0, 1)
        if result == 0:
            speack("Орёл")

        elif result == 1:
            speack("Решка")

    elif cmd == 'stupid1':
        # рассказать анекдот
        speack("Мой разработчик не научил меня анекдотам ... Ха ха ха")
    elif cmd == 'youtube':
        speack("Открываю ютуб")
        youtub()
    elif cmd == 'google':
        speack("Открываю google")
        googl()
    elif cmd == 'weather':
        speack("Открываю Яндекс погоду")
        weath()
    elif cmd == 'restart':
        os.system("python main.py")
        os.exit()
    else:
        speack('Команда не распознана, повторите!')
        print('Команда не распознана, повторите!')

# запуск


# Только если у вас установлены голоса для синтеза речи!
#voices = speak_engine.getProperty('voices')
#speak_engine.setProperty('voice', voices[2].id)

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
speack("Запуск голосового помощника Кеша Версии 2.0")
with m as source:
    r.adjust_for_ambient_noise(source)
    time.sleep(1)
    speack('Кеша слушает')

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)

# forced cmd test
#speack("Мой разработчик не научил меня анекдотам ... Ха ха ха")

#speack("Добрый день, повелитель")

stop_listening = r.listen_in_background(m, callback)

while True:

    time.sleep(0.1) # infinity loop
