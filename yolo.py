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

def get_results(frame):
    results = model(frame)
    return results

def sort_results(results):
    everything = []
    for box in results[0].boxes:
        pos = box.xyxy[0].tolist()
        name_ogg = model.names[int(box.cls[0])]
        conf = float(box.conf[0])
        everything.append([pos, name_ogg, conf])
    return everything

if __name__ == "__main__":
    model = initialize_YOLO()

    frame = get_frame()
    
    results = get_results(frame)

    everything = sort_results(results)

    print(list)