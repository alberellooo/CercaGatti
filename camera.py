"""
Questo codice prende i frame dalla scheda di acquisizione video e li elabora.
Il risultato finale sarà che ogni frame è diviso in 3 parti.
I segmenti sono grandi (rispetto alla larghezza):
- ai lati 40%
- al centro 20%
Lo scopo è di dire il robot di girare im base a dove si trova l'oggetto.
Per esempio se l'oggetto si trova nella parte di sinistra, il robot girerà verso sinistra.
"""

import cv2

def initialize(settings):
    canale = cv2.VideoCapture(0)
    canale.set(cv2.CAP_PROP_FRAME_WIDTH, settings["width"])
    canale.set(cv2.CAP_PROP_FRAME_HEIGHT, settings["height"])
    canale.set(cv2.CAP_PROP_FPS, settings["fps"])
    return canale

def read_frame(canale):
    check, frame = canale.read()
    return check, frame

def dimension(frame):
    height, width, channel = frame.shape # channel ritorna i canali RGB
    return height, width, channel

if __name__ == "__main__":

    # regola la qualità di registrazione
    settings = {
    "width": 1280,
    "height": 1024,
    "fps": 60
    }

    canale = initialize(settings)
    
    while True:
        check, frame = read_frame(canale)

        if check:
            print("Frame catturato. Dimensioni:", dimension(frame))
        else:
            print("Frame perso")
        
        width_first_line = int(40/100*settings["width"]) # linea sinistra (40%)
        width_second_line = int(60/100*settings["width"]) # linea destra (60%)
        frame1 = cv2.line(frame, (width_first_line, settings["height"]), (width_first_line, 0), (0, 0, 0), 5)
        frame2 = cv2.line(frame, (width_second_line, settings["height"]), (width_second_line, 0), (0, 0, 0), 5)

        output = cv2.imshow("output", frame)
        cv2.waitKey(1)

        # se clicco la X dell'output video, il codice termina
        if cv2.getWindowProperty("output", cv2.WND_PROP_VISIBLE) == 0: 
            cv2.destroyAllWindows() # chiude tutte le finestre (per sicurezza)
            break