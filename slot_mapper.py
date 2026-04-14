import json
import cv2
import numpy as np

class SlotMapper:
    def __init__(self,config_path="config\slots.json"):
        
        with open(config_path,"r")as f:
            self.slots = json.load(f)

    def get_centroid(self,box):
        x1,y1,x2,y2 = box
        cx = int((x1+y1)/2)
        cy = int((x2+y2)/2)
        return cx,cy
    
    def is_inside(self,point,polygon):
         
        polygon = np.array(polygon,dtype=np.int32)
        return cv2.pointPolygonTest(polygon,point,False) >= 0
    
    def compute_iou(self, box, polygon):
        
        x1, y1, x2, y2 = box
        box_area = (x2 - x1) * (y2 - y1)

        poly = np.array(polygon, dtype=np.int32)
        x, y, w, h = cv2.boundingRect(poly)

        inter_x1 = max(x1, x)
        inter_y1 = max(y1, y)
        inter_x2 = min(x2, x + w)
        inter_y2 = min(y2, y + h)

        if inter_x2 <= inter_x1 or inter_y2 <= inter_y1:
            return 0

        inter_area = (inter_x2 - inter_x1) * (inter_y2 - inter_y1)

        return inter_area / box_area

    def shrink_polygon(self, polygon, factor=0.7):
        poly = np.array(polygon, dtype=np.float32)
        center = np.mean(poly, axis=0)
        shrunk = center + factor * (poly - center)
        return shrunk.astype(int)


    def map_slots(self, tracks):
        slot_status = []

        for slot in self.slots:
            polygon = slot["points"]
            occupied = False

            shrunk_poly = self.shrink_polygon(polygon, factor=0.7)

            for track in tracks:
                x1, y1, x2, y2, track_id = map(int, track)

                centroid = self.get_centroid((x1, y1, x2, y2))

                inside = cv2.pointPolygonTest(
                    np.array(shrunk_poly, dtype=np.int32),
                    centroid,
                    False
                ) >= 0

                if inside:
                    occupied = True
                    break

            slot_status.append({
                "id": slot["id"],
                "occupied": occupied,
                "polygon": polygon
            })

        return slot_status
    
