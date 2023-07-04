import pyautogui as gui
import time

message = input("Coloca tu mensaje: ")
number = input("Coloca la cantidad de mensajes: ")

time.sleep(2)

for i in range(int(number)):
    gui.typewrite(message)
    gui.press('Enter')