import webbrowser, pyautogui as at, time

def send_message(contact, message):
    webbrowser.open(f"https://web.whatsapp.com/send?phone=+{contact}&text={message}")
    time.sleep(12)
    at.press('enter')