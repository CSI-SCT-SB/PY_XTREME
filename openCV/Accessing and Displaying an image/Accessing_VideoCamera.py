import cv2

video = cv2.VideoCapture(0)

while (True):

    success, image = video.read()
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
