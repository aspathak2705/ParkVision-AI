import cv2
import numpy as np
from detector import veicledetector
from tracker import vehicleTracker
from slot_mapper import SlotMapper

def main():

    cap = cv2.VideoCapture("input\input.mp4")

    detector = veicledetector()
    tracker = vehicleTracker()

    while True:
        ret , frame = cap.read()
        if not ret:
            break

        slot_mapper = SlotMapper()

        detections = detector.detect(frame)

        tracks = tracker.updates(detections)
        slot_status = slot_mapper.map_slots(tracks,tracker)
        overlay = frame.copy()

        for slot in slot_status:
            polygon = np.array(slot["polygon"], np.int32)

            color = (0,255,0) if not slot["occupied"] else (0,0,255)

            
            cv2.fillPoly(overlay, [polygon], color)

            
            cv2.polylines(frame, [polygon], True, color, 2)

        alpha = 0.3
        frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

        total_slots = len(slot_status)
        occupied = sum(1 for s in slot_status if s["occupied"])
        free = total_slots - occupied

        cv2.putText(frame, f"Free: {free}", (20,40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.putText(frame, f"Occupied: {occupied}", (20,80),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        

        for track in tracks:
            x1,y1,x2,y2,track_id = map(int,track)
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame,f"{track_id:.2f}",(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
            
        cv2.imshow("vehical Detection",frame)
        if cv2.waitKey(1)&0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__  == "__main__":
    main()
