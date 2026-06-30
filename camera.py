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

def initialize():
    canale = cv2.VideoCapture(0)
    return canale

def read_frame(canale):
    check, frame = canale.read()
    return check, frame

def dimension(frame):
    height, width, channel = frame.shape # channel ritorna i canali BGR
    return width, height, channel

def lines(frame):
        width_first_line = int(40/100*width)
        width_second_line = int(60/100*width) 
        cv2.line(frame, (width_first_line, width), (width_first_line, 0), (0, 0, 0), 5) # linea sinistra
        cv2.line(frame, (width_second_line, height), (width_second_line, 0), (0, 0, 0), 5) # linea destra 
        return width_first_line, width_second_line
        

def quit(key_to_stop):
        key = cv2.waitKey(1) # ritorna un codice ASCII se premo qualcosa, altrimenti -1

        # il secondo comando dice di stoppare quando clicco la X della finestra
        if key == ord(key_to_stop) or cv2.getWindowProperty("output", cv2.WND_PROP_VISIBLE) == 0: 
            cv2.destroyAllWindows() # chiude tutte le finestre (per sicurezza)
            return True

def test(frame, width, height):
    settings = {
         "center": (int(width/2), int(height/2)),
         "radius": 10,
         "color": (0, 0, 0),
         "thickness": -1 
        }
    cv2.circle(frame, settings["center"], settings["radius"], settings["color"], settings["thickness"])
    return settings

def find_circle(width_first_line, width_second_line):
    circle_pos = test(frame, width, height)
    if circle_pos["center"][0] <= width_first_line:
        cv2.putText(frame, "LEFT", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    elif circle_pos["center"][0] >= width_first_line and circle_pos["center"][0] <= width_second_line:
        cv2.putText(frame, "CENTER", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    else:
        cv2.putText(frame, "RIGHT", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

    

if __name__ == "__main__":

    key_to_stop = "q"
    
    canale = initialize()
    
    while True:
        check, frame = read_frame(canale)

        if check:
            width, height, channel = dimension(frame)
            print("Frame catturato. Dimensioni:", str(width), "x", str(height))
        else:
            print("Frame perso")
        
        width_first_line, width_second_line = lines(frame)

        find_circle(width_first_line, width_second_line)

        cv2.imshow("output", frame)

        if quit(key_to_stop):
             break