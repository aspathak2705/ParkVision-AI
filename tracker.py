import numpy as np
from sort.sort import Sort

class vehicleTracker:
    def __init__(self):
        self.tracker = Sort(
            max_age=20,
            min_hits=3,
            iou_threshold=0.3
        )

    def updates(self,detections):

        if len(detections)==0:
            return[]
        
        dets= np.array(detections)
        tracks = self.tracker.update(dets)

        return tracks
    
