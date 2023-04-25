import cv2

# OpenCV Python Tutorial 1

# img = cv2.imread("/Users/juanmonteverde/juanm0nt.dev/myProjects/uFace/cyberpunk.jpg", 1)
# img = cv2.resize(img, (1920,1080))
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# OpenCV Python Tutorial 2

# import random

# img = cv2.imread("/Users/juanmonteverde/juanm0nt.dev/myProjects/uFace/cyberpunk.jpg", -1)

# for x in range(800):
#     for i in range(img.shape[1]):
#         img[x][i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        
# cv2.imshow("Imagen Random Pixels", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# OpenCV Python Tutorial 3

# import numpy as np

# capture = cv2.VideoCapture(0)

# while True:
#    ret, frame = capture.read()
    
#    cv2.imshow("Frame", frame)
    
#    if cv2.waitKey(1) == ord("q"):
#        break
    
# capture.release()
# cv2.destroyAllWindows()
