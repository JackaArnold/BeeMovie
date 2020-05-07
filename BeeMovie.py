from pynput.keyboard import Key,Controller
import time
time.sleep(5)
a = 0
f = open("BEE.txt","r")
text = f.read()
words = text.split()
Keyboard = Controller()
while a != -1:
    Keyboard.type(words[a])
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(0.2)
    a = a + 1
