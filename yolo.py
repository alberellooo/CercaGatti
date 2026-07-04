"""
Questo codice serve per inizializzare YOLO e avere le funzioni per fargli riconoscere gli oggetti e dare l'output delle loro posizioni
"""

from ultralytics import YOLO
import camera

def initialize_YOLO():
    model = YOLO("yolov8n.pt")
    return model

def get_results(model, frame):
    results = model(frame, verbose=False)
    return results

def sort_results(model, results):
    everything = []
    for box in results[0].boxes:
        pos = box.xyxy[0].tolist() # [x1, y1, x2, y2]
        name_obj = model.names[int(box.cls[0])] # str ("cat")
        conf = float(box.conf[0]) # float (0.41029383)
        everything.append({
            "box": pos,
            "name": name_obj,
            "conf": conf
            })
    return everything

if __name__ == "__main__":

    # stampa una volta tutto quello che vede (test)
    canale = camera.initialize_camera()
    check, frame = camera.read_frame(canale)
    model = initialize_YOLO()
    results = get_results(model, frame)
    everything = sort_results(model, results)

    print(everything)