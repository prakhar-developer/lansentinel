import cv2
import os

def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(f"[+] Detected {len(faces)} face(s) in {os.path.basename(image_path)}")
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    preview_path = image_path.replace(".jpg", "_faces.jpg")
    cv2.imwrite(preview_path, img)
    print(f"[+] Output saved: {preview_path}")
