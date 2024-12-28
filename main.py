import pyautogui


# The retina screens have a scale of 2 to 1 with this library
SCALE = 2

width, height = pyautogui.size()

width *= SCALE
height *= SCALE

region = (width // 5, height // 5, width - width // 5, height - height // 5)

while True:
    try:
        center = pyautogui.locateCenterOnScreen("images/shakeButton.png", confidence=0.5, grayscale=True, region=region)
        print(center)
        pyautogui.click(center[0] / 2, center[1] / 2)
    except pyautogui.ImageNotFoundException:
        print("Shake button not found")
