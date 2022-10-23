import webbrowser, pyautogui as at, time


#función que permite buscar interrogantes en google
def comprar(articulo):
    webbrowser.open(f"https://www.amazon.com/s?k={articulo}&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=198MATDQGNZ06&sprefix=youtube%2Caps%2C138&ref=nb_sb_noss_1")
    time.sleep(12)
    at.press('enter')