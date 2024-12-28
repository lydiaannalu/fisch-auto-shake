import pyautogui


while True:
    try:
        center = pyautogui.locateCenterOnScreen("images/shakeButton.png", confidence=0.75)
        print(center)
        pyautogui.click(center[0], center[1])
    except pyautogui.ImageNotFoundException:
        print("Shake button not found")
