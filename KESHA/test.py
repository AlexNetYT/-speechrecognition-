# pip install keyboard
import keyboard

def foo():
    print('World')

keyboard.add_hotkey('Ctrl + 1', lambda: print('Hello'))
keyboard.add_hotkey('Ctrl + 2', lambda: foo())

keyboard.wait('Ctrl + Q')
