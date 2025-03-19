import pyautogui
import mediapipe as mp
import cv2

webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:
    _, image = webcam.read()
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate (landmarks):
                x = int (landmark.x * frame_width)
                y = int (landmark.y * frame_height)
                if id==8: #index finger
                    cv2.circle(image, (x,y), 8, (0, 255, 255), 3)
                if id==4: # thumb
                    cv2.circle(image, (x,y), 8, (0, 0, 255), 3)
    cv2.imshow("Hand volume control using python", image)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()