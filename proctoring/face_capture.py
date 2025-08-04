import cv2
import os
import time
from datetime import datetime

SNAP_DIR = os.path.join(os.path.dirname(__file__), "snaps")

def ensure_snap_dir():
    if not os.path.exists(SNAP_DIR):
        os.makedirs(SNAP_DIR)

def capture_snapshots(interval=10):
    ensure_snap_dir()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Webcam not accessible!")
        return

    while True:
        ret, frame = cap.read()
        if ret:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(SNAP_DIR, f"{timestamp}.jpg")
            cv2.imwrite(filename, frame)
            print(f"[+] Snapshot saved: {filename}")
        time.sleep(interval)

    cap.release()

if __name__ == "__main__":
    capture_snapshots()
