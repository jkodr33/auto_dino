from PIL import ImageGrab
import pyautogui


def IsCollision(data):
    for x in range(780, 840):
        for j in range(290, 330):
            if data[x, j] > 0:
                print("pulando")
                pyautogui.keyDown('up')
                return
    return

while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    IsCollision(data)

    for i in range(780, 840):
        for j in range(290, 330):
            data[i, j] = 0

    image.show()
    break