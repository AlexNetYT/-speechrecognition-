# Голосовой ассистент КЕША 1.0 BETA
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import random as rnd
import sys
# настройки
opts = {
    "alias": ('кеша','кеш','инокентий','иннокентий','кишун','киш',
              'кишаня','кяш','кяша','кэш','кэша'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси', 'подкинь', 'кинь', 'брось'),
    "cmds": {
        "money": ('монетка', 'орёл или пешка', 'орёл или решка', 'монитку', 'манитку', 'манетку', 'манетка', 'орел или пешка', 'орел или решка'),
        "ctime": ('текущее время','сейчас времени','который час'),
        "radioe": ('включи энерджи','воспроизведи радио энерджи','включи радио энерджи'),
        "radioen": ('включи energy','воспроизведи радио energy','включи радио energy'),
        "radioep": ('включи европу','воспроизведи радио европа','включи радио европа плюс'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты')
    }
}

# функции

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

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
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radioe' or cmd == 'radioen':
        # воспроизвести радио

        os.system("e.m3u")
        speak('Включаю радио энерджи!')
        os._exit()
        os.system("C:\\Users\\sasch\\Desktop\\kesha.bat")

    elif cmd == 'radioep':
            # воспроизвести радио
        os.system("ep.m3u")
        speak('Включаю радио европа плюс!')

    elif cmd == 'money':
        result = rnd.randint(0, 1)
        if result == 0:
            speak("Орёл")

        elif result == 1:
            speak("Решка")

    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

    else:
        print('Команда не распознана, повторите!')

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
#voices = speak_engine.getProperty('voices')
#speak_engine.setProperty('voice', voices[2].id)

# forced cmd test

speak("Кеша слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop
