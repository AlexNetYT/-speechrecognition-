from kivy.app import App
from kivy.uix.button import Button
import os
import speech_recognition as sr
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label
import random as rnd
import pyttsx3
import datetime
from time import sleep
# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=2)

with m as source:
    r.adjust_for_ambient_noise(source)



speak_engine = pyttsx3.init()
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 1000)
time = '00:00'
bc = [.99, .45, .35, 1]
timelbl = ()

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
class KeshaApp(App):
    global time
    def build(self):
        global timelbl
        time = datetime.time()

        timelbl = (Label(
            text = str(time),
            color = (1, 1, 1, 1),
            size_hint = (.5, .5),
            font_size = (200),
            pos = (250, 150)
        ))
        bl = FloatLayout( size_hint=(None, None), size=(1024, 1024)) #BoxLayout(colmsize=(None, None), size=(500, 500))

        bl.add_widget(Button(                   #Voice
            text = 'Start !',
            background_color = bc,
            size_hint = (1, 1),
            pos = (0, 0),
            background_normal = ''))

        bl.add_widget(Button(                   #Voice
            text = '',
            background_color = [1, 1, 1, 1],
            size_hint = (.25, .25),
            pos = (0, 20),
            background_normal = 'podcast.png',
            on_press = self.btn_press))

        bl.add_widget(Button(                      #Energy
            text = '',
            pos = (250, 20),
            size_hint = (.25, .25),
            background_color = [1, 1, 1, 1],
            background_normal = 'radio.png',
            on_press = self.radio))



        bl.add_widget(Button(                       #Время
            text = '',
            size_hint = (.25, .25),
            pos = (500, 20),
            background_color = [1, 1, 1, 1],
            background_normal = 'time.png',
            on_press = self.get_time))

        bl.add_widget(Button(                   #Орел и решка
            text = '',
            size_hint = (.25, .25),
            pos = (750, 20),
            background_color = [1, 1, 1, 1],
            background_normal = 'random.png',
            on_press = self.money))

        bl.add_widget(timelbl)
        bl.add_widget(Button(                   #Voice
            text = '',
            background_color = [1, 1, 1, 1],
            size_hint = (1, 1),
            pos = (0, 0),
            background_normal = '',
            on_press = self.start))
        return bl

    def btn_press(self, instance):
        #print('Ok')
        os.system('botstart')
    def energy(self, instance):
        os.system("e.m3u")
        speak('Включаю радио энерджи!')
    def radio(self, instance):
        result = rnd.randint(0, 1)
        if result == 0:
            os.system("e.m3u")
        elif result == 1:
            os.system("ep.m3u")
    def money(self, instance):
        result = rnd.randint(0, 1)
        if result == 0:
            speak("Орёл")
        elif result == 1:
            speak("Решка")
    def wt():
        global timelbl
        pass



    def get_time(self, instance):
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
        global timelbl

        time = (str(now.hour) + ":" + str(now.minute))
        timelbl.text = str(time)
    def start(self, instance):

        instance.size_hint = (.0, .0)
        instance.background_color = bc
        instance.text = ''



if __name__ == '__main__':
    KeshaApp().run()
    speak('Всё готово!')
    #while True:
    #    time_lbl = datetime.time()

    speak('Все выключено!')
    os.system('taskkill /f /im cmd.exe /T')
