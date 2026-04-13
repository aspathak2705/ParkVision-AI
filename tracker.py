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
    
    def is_stationary(self, track_id, box):
        self.previous_positions = {}
        x1, y1, x2, y2 = box
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        if track_id not in self.previous_positions:
            self.previous_positions[track_id] = (cx, cy)
            return False

        prev_cx, prev_cy = self.previous_positions[track_id]

        dist = ((cx - prev_cx)**2 + (cy - prev_cy)**2)**0.5

        self.previous_positions[track_id] = (cx, cy)

        return dist < 10  
    
