"""
Questo codice serve a mostrare graficamente nella finestra della videocamera dove sono posizionati gli oggetti.
Usufruisco di cv2 per disegnare i rettangoli che delimitano gli oggetti.
"""

import cv2, yolo, camera

def draw_rectangles_names(frame, everything):
    for el in everything:
        x1, y1, x2, y2 = el["box"]
        name_obj = el["name"]
        conf = el["conf"]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
        cv2.putText(frame, name_obj, (x1, y1+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

if __name__ == "__main__":
    while True:
        everything, frame = yolo.do_everything_yolo()
        
        draw_rectangles_names(frame, everything)

        camera.output_camera()