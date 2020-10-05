import multiprocessing.dummy as multiprocessing
from termcolor import colored
import pyautogui
import winsound
import keyboard
import time
import os

result = 0
big_gg = ["gbgg", "bbgg", "rbgg", "pbgg"]
simple_gg = ["bgg", "ggg", "ogg", "rgg"]
big_gems = ["gbg", "bbg", "pbg", "rbg"]
all_gg = ["gbgg", "bbgg", "rbgg", "bgg", "ggg", "ogg", "pbgg"]
all_gems = ["gbgg", "bbgg", "rbgg", "bgg", "ggg", "ogg", "gbg", "bbg", "pbg", "rbg", "pbgg"]



def finder(a):
    global result
    time.sleep(1)
    ah1 = a[:len(a)//2]
    ah2 = a[len(a)//2:]
    x1 = ah1[:len(ah1)//2]
    x2 = ah1[len(ah1)//2:]
    x3 = ah2[:len(ah2)//2]
    x4 = ah2[len(ah2)//2:]
    def t1(x):
        global result
        for i in x:
            x = pyautogui.locateCenterOnScreen('images/'+i+'.png', confidence=0.8)
        if x == None:
            result += 1

    p = multiprocessing.Pool()
    results = p.map(t1, [x1, x2, x3, x4])
    p.close()
    p.join()


    if result == 4:
        result = 0
        keyboard.send("space")
        print(colored('Small Gem.', 'yellow'), colored('Skipped.', 'green'))
        ch()
    else:
        result = 0
        print(colored('Find a gem. Stopping...', 'green'))
        for s in range(0, 2):
            winsound.Beep(1000, 300)
        p.close()




os.system('cls')
choice = input('1. Big Golden Gems\n2. Simple Golden Gems\n3. Big Gems\n4. All Golden Gems\n5. All Gems\n\nInput: ')
def ch():
    if choice == '1':
        finder(big_gg)
    elif choice == '2':
        finder(simple_gg)
    elif choice == '3':
        finder(big_gems)
    elif choice == '4':
        finder(all_gg)
    elif choice == '5':
        finder(all_gems)
    else:
        print('Please type number of function...')
ch()