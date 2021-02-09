import pyautogui as pg
import win32api,win32con
import time
import keyboard

#Website : "www.https://www.agame.com/game/magic-piano-tiles"

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pg.pixel(1320,520)[0] == 0:
        click(1320,520)
    if  pg.pixel(1415,520)[0] == 0:
        click(1415,520)
    if pg.pixel(1505,520)[0]==0:
        click(1505,520)
    if pg.pixel(1600,520)[0] == 0:
        click(1600,520)
