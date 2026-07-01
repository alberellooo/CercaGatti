"""
Questo codice serve per inizializzare YOLO e avere le funzioni per fargli riconoscere gli oggetti e dare l'output delle loro posizioni
"""

from ultralytics import YOLO
import camera

def initialize_YOLO():
    model = YOLO("yolov8n.pt")
    return model

def get_frame():
    canale = camera.initialize_camera()
    check, frame = camera.read_frame(canale)
    return frame

def get_results(model, frame):
    results = model(frame)
    return results

def sort_results(model, results):
    everything = []
    for box in results[0].boxes:
        pos = box.xyxy[0].tolist()
        name_obj = model.names[int(box.cls[0])]
        conf = float(box.conf[0])
        everything.append({
            "box": pos,
            "name": name_obj,
            "conf": conf
            })
    return everything

def do_everything_yolo():
    model = initialize_YOLO()
    frame = get_frame()
    results = get_results(model, frame)
    everything = sort_results(model, results)
    return results, frame

if __name__ == "__main__":
    everything = do_everything_yolo()
    print(everything)