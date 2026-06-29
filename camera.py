"""
Questo codice prende i frame dalla scheda di acquisizione video e li elabora.
Il risultato finale sarà che ogni frame è diviso in 3 parti.
I segmenti sono grandi (rispetto alla larghezza):
- ai lati 40%
- al centro 20%
Lo scopo è di dire il robot di girare in base a dove si trova l'oggetto.
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
    return width, height, channel

if __name__ == "__main__":

    # regola la qualità di registrazione
    settings = {
    "width": 1280,
    "height": 720,
    "fps": 30,
    "key_to_stop": "q"
    }

    canale = initialize(settings)
    
    while True:
        check, frame = read_frame(canale)

        width, height, channel = dimension(frame)

        if check:
            print("Frame catturato. Dimensioni:", str(width), "x", str(height))
        else:
            print("Frame perso")
        
        width_first_line = int(40/100*width)
        width_second_line = int(60/100*width) 
        cv2.line(frame, (width_first_line, settings["height"]), (width_first_line, 0), (0, 0, 0), 5) # linea sinistra
        cv2.line(frame, (width_second_line, settings["height"]), (width_second_line, 0), (0, 0, 0), 5) # linea destra 

        cv2.imshow("output", frame)

        key = cv2.waitKey(1) # ritorna un codice ASCII se premo qualcosa, altrimenti -1

        # il secondo comando dice di stoppare quando clicco la X della finestra
        if key == ord(settings["key_to_stop"]) or cv2.getWindowProperty("output", cv2.WND_PROP_VISIBLE) == 0: 
            cv2.destroyAllWindows() # chiude tutte le finestre (per sicurezza)
            break