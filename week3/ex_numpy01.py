import numpy as np


# 1dimension
arr1d = np.array([1,2,3,4,5,6])
print(f'1d{arr1d}')
print(f'ndim:{arr1d.ndim}')
print(f'shape:{arr1d.shape}')
print(f'dtype:{arr1d.dtype}')

#reshape
print("="*100)
arr2d = arr1d.reshape(2,3)
print(arr1d)
print(arr2d)
print(f'1d{arr2d}')
print(f'ndim:{arr2d.ndim}')
print(f'shape:{arr2d.shape}')
print(f'dtype:{arr2d.dtype}')
arr_auto = arr1d.reshape(3, -1) #3행 -1은 알아서처리
print(arr_auto)
# 브로드캐스팅 = 반복없이 한번에 처리
a = np.array([1,2,3,4])
b = np.array([10, 20, 30, 40])
print(f'a+b={a+b}')
print(f'a x b = {a*b}')
print(f'a+100 = {a+100}')
print(f'a > 2 = {a>2}')
loop = [x**2 for x in a]
print(loop, '벡터화:', list(a*2))

#열병합, 행 병합
print(f'axis=0:{arr2d.sum(axis=0)}')
print(f'axis=1:{arr2d.sum(axis=1)}')
v= np.arange(12)
print(v)
x=v.reshape(3,4)
print('3x4reshape',x)
print(x.T)
w= np.array([10, 20, 30])
print('array_multiply', w@x)

import matplotlib.pyplot as plt
img = plt.imread('C:/medicalAI/Pycham/week3/Data_processing/imageNet/cat1.jpg')
print(f'(height, width, channel): {img.shape}')
plt.imshow(img)
plt.show()
crop = img[40:250, 130:400] #[세로, 가로]
# #좌우반전
crop = img[40:250, 130:400]
flip = img[:,::-1] #시작부터 끝까지 거꾸로(-1) /상하반전[::-1,:]
gray = img.mean(axis=2)
fig, ax = plt.subplots(1, 3, figsize=(13, 3.6))
ax[0].imshow(crop)
ax[1].imshow(flip)
ax[2].imshow(gray, cmap='gray') #흑백으로 출력
plt.imshow(crop)
plt.show()
v_img = np.vstack((img, img)) #수직결합
h_img = np.hstack((img, img)) #수평결합
plt.imshow(v_img)
plt.imshow(h_img)
plt.show()

#cat face hide
print('pixel[0,0]', img[0,0])
sample =img.copy()
sample[40:250, 130:400] = [180, 180, 180]
plt.imshow(sample)
plt.show()

small = img[::5, ::5] #1/5다운샘플 흐릿하게 보인다
print(img.shape, small.shape)
plt.imshow(small)
plt.show()