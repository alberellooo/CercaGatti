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

def initialize_camera():
    canale = cv2.VideoCapture(1)
    return canale

def read_frame(canale):
    check, frame = canale.read()
    return check, frame

def dimension(frame):
    height, width= frame.shape[:2] # il terzo è channel che ritorna i canali BGR ma a me non serve
    return width, height

def draw_lines(frame, width, height):
        width_first_line = int(40/100*width)
        width_second_line = int(60/100*width) 
        cv2.line(frame, (width_first_line, width), (width_first_line, 0), (0, 0, 0), 5) # linea sinistra
        cv2.line(frame, (width_second_line, height), (width_second_line, 0), (0, 0, 0), 5) # linea destra 
        return width_first_line, width_second_line

def test_circle(frame, width, height, width_first_line, width_second_line):
    settings = {
        "center": (int(width/2), int(height/2)),
        "radius": 10,
        "color": (0, 0, 0),
        "thickness": -1 
    }
    cv2.circle(frame, settings["center"], settings["radius"], settings["color"], settings["thickness"])
    if settings["center"][0] <= width_first_line:
        cv2.putText(frame, "LEFT", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    elif settings["center"][0] >= width_first_line and settings["center"][0] <= width_second_line:
        cv2.putText(frame, "CENTER", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    else:
        cv2.putText(frame, "RIGHT", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

def test_rectangle(frame, width_first_line, width_second_line):
    settings = {
        "point1": (100, 400),
        "point2": (300, 300),
        "color": (0, 0, 0),
        "thickness": 2
    }
    cv2.rectangle(frame, settings["point1"], settings["point2"], settings["color"], settings["thickness"])
    center = (int((settings["point1"][0] + settings["point2"][1]) / 2), int((settings["point1"][1] + settings["point2"][1]) / 2))
    if center[0] < width_first_line:
        cv2.putText(frame, "LEFT", (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    elif center[0] > width_first_line and center[0] < width_second_line:
        cv2.putText(frame, "CENTER", (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    else:
        cv2.putText(frame, "RIGHT", (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

def output_camera(frame):
    cv2.imshow("output", frame)
    
def quit(key_to_stop):
        key = cv2.waitKey(1) # ritorna un codice ASCII se premo qualcosa, altrimenti -1

        # il secondo comando dice di stoppare quando clicco la X della finestra
        if key == ord(key_to_stop) or cv2.getWindowProperty("output", cv2.WND_PROP_VISIBLE) == 0: 
            cv2.destroyAllWindows() # chiude tutte le finestre (per sicurezza)
            return True
    
if __name__ == "__main__":

    key_to_stop = "q"
    
    canale = initialize_camera()
    
    while True:
        check, frame = read_frame(canale)

        if check:
            width, height = dimension(frame)
            print("Frame catturato. Dimensioni:", str(width), "x", str(height))
        else:
            print("Frame perso")
        
        width_first_line, width_second_line = draw_lines(frame, width, height)

        # prova per controllare un cerchio
        test_circle(frame, width, height, width_first_line, width_second_line)

        # prova per controllare un rettangolo
        test_rectangle(frame, width_first_line, width_second_line)

        output_camera(frame)

        if quit(key_to_stop):
             break