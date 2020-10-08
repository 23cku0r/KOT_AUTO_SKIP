import multiprocessing.dummy as multiprocessing
from termcolor import colored
import pyautogui
import winsound
import keyboard
import time
import os

cg = None
result = 0
big_gg = ["gbgg", "bbgg", "rbgg", "pbgg", "obgg"]
simple_gg = ["rgg", "bgg", "ggg", "ogg"]
big_gems = ["bbg", "gbg", "pbg", "rbg"]
all_gg = ["rgg", "bgg", "ggg", "ogg", "gbgg", "bbgg", "rbgg", "pbgg", "obgg"]
all_gems = ["bbg", "gbg", "pbg", "rbg", "rgg", "bgg", "ggg", "ogg", "gbgg", "bbgg", "rbgg", "pbgg", "obgg"]



def finder(a):
    global result
    time.sleep(1)
    ah1 = a[:len(a)//2]
    ah2 = a[len(a)//2:]
    x1 = ah1[:len(ah1)//2]
    x2 = ah1[len(ah1)//2:]
    x3 = ah2[:len(ah2)//2]
    x4 = ah2[len(ah2)//2:]
    c1 = x1[:len(x1)//2]
    c2 = x1[len(x1)//2:]
    c3 = x2[:len(x2)//2]
    c4 = x2[len(x2)//2:]
    c5 = x3[:len(x3)//2]
    c6 = x3[len(x3)//2:]
    c7 = x4[:len(x4)//2]
    c8 = x4[len(x4)//2:]
    def t1(x):
        global result
        for i in x:
            x = pyautogui.locateCenterOnScreen('images/'+i+'.png', confidence=0.8)
            if x == None:
                result += 1
    p = multiprocessing.Pool()
    results = p.map(t1, [c1, c2, c3, c4, c5, c6, c7, c8])
    p.close()
    p.join()
    
    if result == len(cg):
        result = 0
        keyboard.send("space")
        print(colored('Small Gem.', 'yellow'), colored('Skipped.', 'green'))
        finder(cg)
    else:
        result = 0
        print(colored('Find a gem. Stopping...', 'green'))
        for s in range(0, 2):
            winsound.Beep(1000, 300)
        p.close()




os.system('cls')
choice = input('1. Big Golden Gems\n2. Simple Golden Gems\n3. Big Gems\n4. All Golden Gems\n5. All Gems\n\nInput: ')
def ch():
    global cg
    if choice == '1':
        cg = big_gg
        finder(big_gg)
    elif choice == '2':
        cg = simple_gg
        finder(simple_gg)
    elif choice == '3':
        cg = big_gems
        finder(big_gems)
    elif choice == '4':
        cg = all_gg
        finder(all_gg)
    elif choice == '5':
        cg = all_gems
        finder(all_gems)
    else:
        print('Please type number of function...')
ch()
