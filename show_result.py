"""
Questo codice serve a mostrare graficamente nella finestra della videocamera dove sono posizionati gli oggetti.
Usufruisco di cv2 per disegnare i rettangoli che delimitano gli oggetti.
"""

import cv2, yolo, camera
from colors import COLORS

def draw_rectangles_and_names(frame, everything):
    for el in everything:
        x1, y1, x2, y2 = map(int, el["box"])
        name_obj = el["name"]
        conf = el["conf"]
        if conf > 0.3 or name_obj == "cat":
            testo = name_obj + " " + str(int(conf*100)) + "%"
            cv2.rectangle(frame, (x1, y1), (x2, y2), COLORS[name_obj], 2)
            (text_w, text_h), baseline = cv2.getTextSize(testo, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 3)
            cv2.rectangle(frame, (x1, y1 + 20 - text_h - 6), (x1 + text_w + 10, y1 + 20), COLORS[name_obj], -1)                                
            cv2.putText(frame, testo, (x1 + 5, y1 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    return frame

if __name__ == "__main__":
    canale = camera.initialize_camera()
    model = yolo.initialize_YOLO()
    while True:
        check, frame = camera.read_frame(canale)
        results = yolo.get_results(model, frame)
        everything = yolo.sort_results(model, results)
        new_frame = draw_rectangles_and_names(frame, everything)
        camera.output_camera(new_frame)

        if camera.quit(key_to_stop="q"):
            break