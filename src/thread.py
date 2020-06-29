from openal import oalOpen, oalQuit
import keyboard
import time
import threading


def playBumbo():
    bumbo.play()

def playCaixa():
    caixa.play()
    
def playHhClose():
    hhClose.play()

def playHhOpen():
    hhOpen.play()

def playTomOne():
    tomOne.play()

def playTomTwo():
    tomTwo.play()

def playTomThree():
    tomThree.play()

def playSplash():
    splash.play()

caixa = oalOpen("caixa.wav")
bumbo = oalOpen("bumbo.wav")
hhClose = oalOpen("hhClose.wav")
hhOpen = oalOpen("hhOpen.wav")
tomOne = oalOpen("tom1.wav")
tomTwo = oalOpen("tom2.wav")
tomThree = oalOpen("tom3.wav")
splash = oalOpen("splash.wav")

while True:
    time.sleep(0.02)

    if keyboard.is_pressed('v'):
        t = threading.Thread(target=playCaixa)
        t.start()
        time.sleep(0.02)
        
    if keyboard.is_pressed('m'):
        b = threading.Thread(target=playBumbo)
        b.start()
        time.sleep(0.02)

    if keyboard.is_pressed('n'):
        hh = threading.Thread(target=playHhClose)
        hh.start()
        time.sleep(0.02)

    if keyboard.is_pressed('b'):
        hh = threading.Thread(target=playHhOpen)
        hh.start()
        time.sleep(0.02)

    if keyboard.is_pressed('f'):
        hh = threading.Thread(target=playTomOne)
        hh.start()
        time.sleep(0.02)

    if keyboard.is_pressed('g'):
        hh = threading.Thread(target=playTomTwo)
        hh.start()
        time.sleep(0.02)

    if keyboard.is_pressed('h'):
        hh = threading.Thread(target=playTomThree)
        hh.start()
        time.sleep(0.02)

    if keyboard.is_pressed('j'):
        s = threading.Thread(target=playSplash)
        s.start()
        time.sleep(0.02)

oalQuit()