import mediapipe as mp
import cv2
import HandTrackingModule as htm
import FaceDetectionModule as fdm
import math
class faceClassifier():
    def __init__(self):
        self.handDetector = htm.handDetector(detectionCon=0.7)
        self.faceDetector = fdm.FaceDetector(minDetectionConfidance=0.7)
    def camera(self):
        cam = cv2.VideoCapture(0)
        while True:
            temp, img = cam.read()
            if temp:
                imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                img = self.handDetector.findHands(imgRGB,draw=0)
                handLm = self.handDetector.findPosition(img,draw=0)
                img,faceLm = self.faceDetector.findFaces(img,draw=0)
                if handLm and faceLm:
                    fx,fy = handLm[8][1],handLm[8][-1]
                    for id,i in enumerate(faceLm[-1][-1]):
                        h,w,c = img.shape
                        cx,cy = int(w*i.x), int(h*i.y)
                        if math.hypot(fx-cx,fy-cy) <15:
                            if id == 3:
                                img[0:100,0:100] = cv2.imread("TestImages/lips.png")
                                cv2.rectangle(img, (400-5,285-30), (400+70,285+10), (255, 0, 0),cv2.FILLED)
                                cv2.putText(img, "Lips", (400, 285), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                             (0, 0, 255),  2)
                            elif id == 2:
                                img[0:100,0:100] = cv2.imread("TestImages/nose.png")
                                cv2.rectangle(img, (400-5,285-30), (400+70,285+10), (255, 0, 0),cv2.FILLED)
                                cv2.putText(img, "Nose", (400, 285), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                             (0, 0, 255),  2)
                            elif id == 4 or id==5:
                                img[0:100,0:100] = cv2.imread("TestImages/ear.png")
                                cv2.rectangle(img, (400-5,285-30), (400+70,285+10), (255, 0, 0),cv2.FILLED)
                                cv2.putText(img, "Ear", (400, 285), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                             (0, 0, 255),  2)
                            elif id == 1 or id==0:
                                img[0:100,0:100] = cv2.imread("TestImages/eye.png")
                                cv2.rectangle(img, (400-5,285-30), (400+70,285+10), (255, 0, 0),cv2.FILLED)
                                cv2.putText(img, "Eye", (400, 285), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                             (0, 0, 255),  2)
                img =  cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                cv2.imshow("Face Classifier",img)
                if cv2.waitKey(1)==13:
                    break
        cam.release()
        cv2.destroyAllWindows()
        