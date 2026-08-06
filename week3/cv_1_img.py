import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:/medicalAI/Pycham/week3/ex_opencv/video/p.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(f'Data Type: {type(img_rgb)}')
print(f'shape:(height, width, channels): {img_rgb.shape}')
print(f'size(pixels): {img_rgb.size})')
print(f'pixel Type: {img_rgb.dtype}')

#down sapling
down2 = img_rgb[::2, ::2]
down4 = img_rgb[::4, ::4]
down8 = img_rgb[::8, ::8]
plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1)
plt.imshow(img_rgb); plt.title('orginal'); plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(down2); plt.title('1/2'); plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(down4); plt.title('1/4'); plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(down8); plt.title('1/8'); plt.axis('off')
# plt.show()

img_gray = cv2.imread('C:/medicalAI/Pycham/week3/ex_opencv/video/p.png', cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('thresholding', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
#openCV
import os
img_face = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('C:/medicalAI/Pycham/week3/ex_opencv/haarcascade_frontalface_default.xml')

# face recognization face detaction 1.01 scan more detailed
faces = face_cascade.detectMultiScale(img_face, scaleFactor=1.01, minNeighbors=6, minSize=(20, 20))
print(f'face count: {len(faces)}')
# draw result
for (x, y, w, h) in faces:
    cv2.rectangle(img_face, (x, y), (x + w, y + h), (0, 255, 0), 2)
face = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(face)
plt.show()