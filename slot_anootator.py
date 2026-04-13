import cv2
import json

points = []
slots = []
slot_id = 1

def mouse_callback(event, x, y, flags, param):
    global points, slots, slot_id

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Point: {(x, y)}")

        if len(points) == 4:
            slots.append({
                "id": slot_id,
                "points": points.copy()
            })
            print(f"Slot {slot_id} saved!")

            slot_id += 1
            points = []

def main():
    cap = cv2.VideoCapture("input\input.mp4")

    ret, frame = cap.read()
    if not ret:
        print("Error loading video")
        return

    cv2.namedWindow("Annotate Slots")
    cv2.setMouseCallback("Annotate Slots", mouse_callback)

    while True:
        display = frame.copy()

        
        for p in points:
            cv2.circle(display, p, 5, (0, 255, 0), -1)

    
        for slot in slots:
            pts = slot["points"]
            for i in range(len(pts)):
                cv2.line(display, pts[i], pts[(i+1)%4], (255, 0, 0), 2)

        cv2.imshow("Annotate Slots", display)

        key = cv2.waitKey(1)

        if key == 27:  
            break

        elif key == ord('s'):
            with open("config/slots.json", "w") as f:
                json.dump(slots, f, indent=4)
            print("Slots saved to slots.json")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()