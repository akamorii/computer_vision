import cv2
import numpy as np

### отображение видео

kernel = np.array([[1,1,1],[1,1,1],[1,1,1]], dtype=np.uint8)
# kernel = np.ones((15,15), np.uint8)

# cap = cv2.VideoCapture('/Users/akamori/proga/python/computer_vision/videos/videc.mov')
cap = cv2.VideoCapture(0)
cap.set(3, 100)
cap.set(4, 100)


while True:
    success, img = cap.read()
    nm = cv2.resize(img, (250, 200))
    # nm = cv2.GaussianBlur(nm, (15, 15), 5)
    nm = cv2.cvtColor(nm, cv2.COLOR_BGR2GRAY)
    
    nm = cv2.Canny(nm, 120, 120)
    nm = cv2.dilate(nm, kernel, iterations=1)
    
    nm = cv2.erode(nm, kernel, 1)
    
    # nm[0:50, 0:50]
    cv2.imshow(f'{nm.shape[0]}', nm)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break