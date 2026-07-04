"""
Questo codice dice al robot la direzione da seguire in base a dove si trova il gatto nella scena.
La funzione ritorna -1 (LEFT), 0 (FORWARD) o 1 (RIGHT) e il file del robot penserà a tradurlo in movimenti.
"""

import camera, yolo, show_result

def check_cat(frame, everything):
    for name in everything:
        if name["name"] == "cat":
            width, height = camera.dimension(frame)
            frame, lline, rline = camera.draw_lines(frame, width, height, draw=False)
            x1, y1, x2, y2 = name["box"]
            center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
            if center[0] < lline:
                return frame, -1
            elif center[0] > lline and center[0] < rline:
                return frame, 0
            else:
                return frame, 1
        else:
            return frame, None
    return frame, None

if __name__ == "__main__":
    canale = camera.initialize_camera()
    model = yolo.initialize_YOLO()
    while True:
        check, frame = camera.read_frame(canale)
        results = yolo.get_results(model, frame)
        everything = yolo.sort_results(model, results)
        new_frame = show_result.draw_rectangles_and_names(frame, everything)
        new_frame, is_cat = check_cat(frame, everything)
        if is_cat == -1:
            print("LEFT")
        elif is_cat == 0:
            print("FORWARD")
        elif is_cat == 1:
            print("RIGHT")
        else:
            print("No cat")
        camera.output_camera(new_frame)

        if camera.quit(key_to_stop="q"):
            break