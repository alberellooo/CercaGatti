"""
Questo codice serve a mostrare graficamente nella finestra della videocamera dove sono posizionati gli oggetti.
Usufruisco di cv2 per disegnare i rettangoli che delimitano gli oggetti.
"""

import cv2, yolo, camera

def draw_rectangles_names(frame, everything):
    for el in everything:
        x1, y1, x2, y2 = map(int, el["box"])
        name_obj = el["name"]
        conf = el["conf"]
        if conf > 0.2:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
            cv2.putText(frame, name_obj, (x1, y1+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    return frame

if __name__ == "__main__":
    canale = camera.initialize_camera()
    model = yolo.initialize_YOLO()
    while True:
        check, frame = camera.read_frame(canale)
        results = yolo.get_results(model, frame)
        everything = yolo.sort_results(model, results)
        new_frame = draw_rectangles_names(frame, everything)
        camera.output_camera(new_frame)

        if camera.quit(key_to_stop="q"):
            break