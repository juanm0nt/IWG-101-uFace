import cv2

# ---OpenCV Python Tutorial 1---

# img = cv2.imread("/Users/juanmonteverde/juanm0nt.dev/myProjects/uFace/cyberpunk.jpg", 1)
# img = cv2.resize(img, (1920,1080))
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ---OpenCV Python Tutorial 2---

# import random

# img = cv2.imread("/Users/juanmonteverde/juanm0nt.dev/myProjects/uFace/cyberpunk.jpg", -1)

# for x in range(800):
#     for i in range(img.shape[1]):
#         img[x][i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        
# cv2.imshow("Imagen Random Pixels", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ---OpenCV Python Tutorial 3---

# import numpy as np

# capture = cv2.VideoCapture(0)

# while True:
#     ret, frame = capture.read()
    
#     cv2.imshow("Frame", frame)
    
#     if cv2.waitKey(1) == ord("q"):
#         break
    
# capture.release()
# cv2.destroyAllWindows()

# ---OpenCV Python Tutorial 4---

# import numpy as np

# capture = cv2.VideoCapture(0)

# while True:
#     ret, frame = capture.read()
#     width = int(capture.get(3))
#     height = int(capture.get(4))
    
#     image = cv2.line(frame, (0, 0), (width, height), (255, 153 ,255), 10)
#     image = cv2.line(image, (0, height), (width, 0), (255, 153 ,255), 10)
#     image = cv2.rectangle(image, (800, 500), (300, 300), (128, 128, 128), 5)
#     image = cv2.circle(image, (400, 400), 50, (0, 0, 255), -1)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     image = cv2.putText(image, "Juan es el mejor", (200 , height - 10), font, 4, (0, 0 ,0), 5, cv2.LINE_AA)
    
#     cv2.imshow("Frame", image)

#     if cv2.waitKey(1) == ord("q"):
