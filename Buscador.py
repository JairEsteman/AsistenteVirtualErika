import webbrowser, pyautogui as at, time


#función que permite buscar interrogantes en google
def buscar(something):
    webbrowser.open(f"https://www.google.com/search?q={something}&hl=es&sxsrf=ALiCzsaOm4WbLmejYVNso5IR9dSI-GGH7Q%3A1666502132436&source=hp&ei=9M1UY9btF-GykvQPgPCTkAY&iflsig=AJiK0e8AAAAAY1TcBCpeW5EC90drHR-z3KqYoARSZUXi&ved=0ahUKEwjWt_mczPX6AhVhmYQIHQD4BGIQ4dUDCAg&uact=5&oq=Youtube&gs_lp=Egdnd3Mtd2l6uAED-AEBMgoQLhjHARjRAxgnMgQQABhDMgQQABhDMgQQABhDMgQQABhDMgQQABhDMgQQABhDMgQQABhDMgQQABhDMgsQABiABBixAxiDAcICBxAjGOoCGCfCAgcQLhjqAhgnwgIREC4YgAQYsQMYgwEYxwEY0QPCAggQABiABBixA8ICCBAuGIAEGLEDwgIOEC4YgAQYsQMYxwEY0QPCAhEQLhiABBixAxiDARjHARivAagCCkj6L1CPEFi0KXABeADIAQCQAQCYAYcBoAGwBqoBAzAuNw&sclient=gws-wiz")
    time.sleep(12)
    at.press('enter')