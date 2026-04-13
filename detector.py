from ultralytics import YOLO

class veicledetector:
    def __init__(self,model_path="yolov8m.pt"):
        
        self.model = YOLO(model_path)

        self.vehicle_classes=[2,3,5,7]

    def detect(self,frame):
        results = self.model(frame, imgsz=1280, conf=0.25,iou=0.5)[0]

        detections = []
        
        for box in results.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
             
            if cls in self.vehicle_classes:
                x1,y1,x2,y2 =map(int, box.xyxy[0])
                detections.append([x1,y1,x2,y2,conf])
        
        return detections
    
