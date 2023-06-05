import pyautogui as py
while True:
    x,y = py.position()
    print(x,y)
    py.sleep(1.0)