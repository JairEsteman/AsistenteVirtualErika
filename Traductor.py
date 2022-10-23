import webbrowser, pyautogui as at, time


#función que permite buscar interrogantes en google
def traducir(any):
    webbrowser.open(f"https://translate.google.com/?sl=es&tl=en&text={any}&op=translate")
    time.sleep(12)
    at.press('enter')