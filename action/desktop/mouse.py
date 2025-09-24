import pyautogui

class Mouse:
    def __init__(self, data):
        self.direction = data['path'].split('-')[1]
        self.posX, self.posY = pyautogui.position()
    
    def _control_(self):
        if self.direction == 'up':
            self.mouseUp()
                
        elif self.direction == 'down':
            self.mouseDown()
                
        elif self.direction == 'left':
            self.mouseLeft()
                
        elif self.direction == 'right':
            self.mouseRight()
            
        elif self.direction == 'ok':
            self.mouseOk()
            
        elif self.direction == 'back':
            self.mouseBack()
    def mouseUp(self):
        if self.posY<=250:
            pyautogui.scroll(+3)
            pyautogui.moveTo(self.posX, self.posY+300)
        pyautogui.moveTo(self.posX, self.posY-100)
    
    def mouseDown(self):
        pyautogui.moveTo(self.posX, self.posY+100)
        if self.posY>=650:
            pyautogui.scroll(-3)
            pyautogui.moveTo(self.posX, self.posY-300)
    
    def mouseLeft(self):
        pyautogui.moveTo(self.posX-100, self.posY)
    
    def mouseRight(self):
        pyautogui.moveTo(self.posX+100, self.posY)
    
    def mouseOk(self):
        pyautogui.click(self.posX, self.posY)
    
    def mouseBack(self):
        pyautogui.press('backspace')