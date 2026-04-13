import cv2
from detector import veicledetector
from tracker import vehicleTracker

def main():

    cap = cv2.VideoCapture("input\input.mp4")

    detector = veicledetector()
    tracker = vehicleTracker()

    while True:
        ret , frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)

        tracks = tracker.updates(detections)

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
