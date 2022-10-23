import subprocess as sub
import Whatsapp as wa
import pywhatkit
import speech_recognition as sr
import pyttsx3
import wikipedia
import Buscador
import Amazon
import Traductor
import face_recognizer as fr
import Reconocimiento_Camara as rc
import threading as tr


# Estructura instintiva y automatica para el relacionamiento a traves de la comunicación
name = "erika"
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 156)

# sitios que debe abrir la asistente virtual
sites = {
    'linkedin': 'www.linkedin.com/in/jairestebanmendezcifuentes/',
    'traductor': 'translate.google.com/?hl=es',
    'amazon': 'amazon.com',
    'youtube': 'www.youtube.com/watch?v=d0Nwc9jLsqA',
    'wikipedia': 'es.wikipedia.org'
}


# funciones de las palabras claves
def reproduce(rec):
    video = rec.replace('reproduce', '')
    talk("Reproduciendo en Youtube" + video)
    pywhatkit.playonyt(video)


def busca(rec):
    something = rec.replace('buscar', '')
    Buscador.buscar(something)


def qué_es(rec):
    search = rec.replace('qué es', '')
    wikipedia.set_lang("es")
    wiki = wikipedia.summary(search, 1)
    talk(wiki)


def saber_más_de(rec):
    something = rec.replace('saber más de', '')
    Buscador.buscar(something)
    articulo = rec.replace('saber más de', '')
    Amazon.comprar(articulo)
    vid = rec.replace('saber más de', '')
    pywhatkit.playonyt(vid)


def abre(rec):
    abrir = rec.replace('abre', '')

    for site in sites:
        if site in rec:
            sub.call(f'start chrome.exe {sites[site]}', shell=True)
            talk(f'Abriendo{site}')

def whatsapp(rec):
        talk("por favor dictame el número de contacto con el codigo del país sin el simbolo más")
        contact = listen()
        talk("el número" + contact + "¿es correcto?")
        rec = listen()
        if 'sí' in rec:
            talk("que mensaje quieres enviar")
            message = listen()
            talk("el mensaje" + message + "¿es correcto?")
            rec = listen()
            if  'sí' in rec:
                wa.send_message(contact, message)
                talk("enviando mensaje a traves de Whatsapp")
            elif 'no' in rec:
                talk("repite el mensaje por favor")
                message = listen()
                talk("el mensaje" + message + "¿es correcto?")
                rec = listen()
                if 'sí' in rec:
                    wa.send_message(contact, message)
                    talk("enviando mensaje a traves de Whatsapp")
        elif 'no' in rec:
            talk("repite el número de contacto")
            contact = listen()
            talk("el número" + contact + "¿es correcto?")
            rec = listen()
            if 'sí' in rec:
                talk("que mensaje quieres enviar")
            message = listen()
            talk("el mensaje" + message + "¿es correcto?")
            rec = listen()
            if  'sí' in rec:
                wa.send_message(contact, message)
                talk("enviando mensaje a traves de Whatsapp")
            elif 'no' in rec:
                talk("repite el mensaje por favor")
                message = listen()
                talk("el mensaje" + message + "¿es correcto?")
                rec = listen()
                if 'sí' in rec:
                    wa.send_message(contact, message)
                    talk("enviando mensaje a traves de Whatsapp")


def traducir(rec):
    any = rec.replace('traducir', '')
    Traductor.traducir(any)

def reconocimiento(rec):
    talk("Abriendo camara")
    rc.capture()

def facerecog(rec):
    rec = rec.replace('facerecog', '').strip()
    if rec == 'activado':
        t = tr.Thread(target=fr.face_rec, args=(0,))
        t.start()
        talk("Activando Reconocimiento")
    elif 'aguacate':
        fr.face_rec(1)

def recomendar(rec):
    contact = 525569772999
    message = "Te recomiendo que revises esta página web youtube': 'www.youtube.com/watch?v=d0Nwc9jLsqA"
    wa.send_message(contact, message)



# diccionario de palabras claves
palabrasClaves = {
    'reproduce': reproduce,
    'busca': busca,
    'qué es': qué_es,
    'saber más de': saber_más_de,
    'whatsapp': whatsapp,
    'abre': abre,
    'facerec': facerecog,
    'recomendar': recomendar,
    'reconocimiento': reconocimiento,
    'traducir': traducir
}


engine.say("Hola, Soy Erika tu asistente virtual, ¿Como te puedo ayudar?")
engine.runAndWait()

# función que permite hablar al asitente


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as micro:
        listener.adjust_for_ambient_noise(micro)
        talk("Te estoy escuchando")
        pc = listener.listen(micro)
    try:
        rec = listener.recognize_google(pc, language='es-MX')
        rec = rec.lower()
        print(rec)
        if name not in rec:
            rec = rec.replace(name, '')
    except sr.UnknownValueError:
        talk("No te entedí, puedes por favor repetir")
    except sr.RequestError as e:
        talk(
            "La información que me has solicitado no se ha logrado completar; {0}".format(e))
    return rec


def run_erika():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            continue
        if 'qué es' in rec:
            palabrasClaves['qué es'](rec)
        else:
            for word in palabrasClaves:
                if word in rec:
                    palabrasClaves[word](rec)
        if 'cómo estás' in rec:
            talk("Muy bien, ¿cómo te puedo ayudar?")
        elif 'gracias' in rec:
            talk("un gusto ayudarte")
        elif 'adiós' in rec:
            talk("Que tengas un buen día")
            break


if __name__ == '__main__':
    run_erika()
