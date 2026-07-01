"""
Questo codice serve a mostrare graficamente nella finestra della videocamera dove sono posizionati gli oggetti.
Usufruisco di cv2 per disegnare i rettangoli che delimitano gli oggetti.
"""

import cv2, yolo

def draw_rectangle(frame):
    everything = yolo.sort_results()
    