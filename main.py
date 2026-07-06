"""
Questo è il file principale da eseguire per fare funzionare il programma.
Chiama le funzioni dagli altri file e le esegue
"""
import camera, yolo, show_result, direction

if __name__ == "__main__":
    canale = camera.initialize_camera()
    model = yolo.initialize_YOLO()
    count = 0
    while True:
        check, frame = camera.read_frame(canale)
        if count % 10 == 0:
            results = yolo.get_results(model, frame)
            everything = yolo.sort_results(model, results)
            frame, is_cat = direction.check_cat(frame, everything)
            print(is_cat)
            count = 0
        frame = show_result.draw_rectangles_and_names(frame, everything)
        count += 1
        camera.output_camera(frame)

        if camera.quit(key_to_stop="q"):
            break