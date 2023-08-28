import cv2
import mediapipe as mp
import pafy

# 使用 mediapipe face_detection 臉部偵測物件
mp_face_detection = mp.solutions.face_detection

# 使用 mediapipe drawing_utils 繪圖物件
mp_drawing = mp.solutions.drawing_utils

url = "https://www.youtube.com/watch?v=m_dhMSvUCIc"
video = pafy.new(url)
stream = video.getbest(preftype="mp4")
cap = cv2.VideoCapture(stream.url)

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.8) as face_detection:
    while cap.isOpened():
        if 27 == 0xFF & cv2.waitKey(3):
            break

        success, image = cap.read()
        if not success:
            print("empty stream frame")
            continue

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # image.flags.writeable = False
        result = face_detection.process(image)
        # image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if result.detections:
            for dection in result.detections:
                mp_drawing.draw_detection(image, dection)
                cv2.imshow("MediaPipe face detection", image)


cap.release()
cv2.destroyAllWindows()