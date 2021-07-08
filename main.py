import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)


def isCollide(data):
    for i in range(400, 520):
        for j in range(620, 650):
            if data[i, j] < 100:
                return True
    return False        

#def draw():
    
            
#def takeScreenshot():
    #return image
    if __name__ == "__main__":
        print("T-rex dino about to start in 6 seconds")
        time.sleep(6)
        hit('up')

        while True:
            image = ImageGrab.grab().convert('L')
            data = image.load()
            if isCollide(data):
                hit("up")
    #print(asarray(image))

    # Draw the rectangle
    #for i in range(400, 520):
     #   for j in range(621, 650):
      #      data[i, j] = 0
       #     image.show()
        #    break
    