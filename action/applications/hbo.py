import webbrowser
import pyautogui
import time

class HboPath:
    def __init__(self, url):
        self.url = url
        
    def run(self):
        webbrowser.open(self.url)
        time.sleep(3)
        pyautogui.scroll(-3)