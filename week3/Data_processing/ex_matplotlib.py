import matplotlib.pyplot as plt
import pandas as pd, numpy as np
from IPython.core.pylabtools import figsize

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']

월 = [1,2,3,4,5,6]
매출 = [20, 35, 30, 50, 65, 60]
plt.plot(월, 매출)
plt.title('월별 매출 추세')
plt.xlabel('월')
plt.ylabel('매출(백만원)')
# plt.show()
작년 = [18, 30, 28, 42, 55, 50]
#색, 마커, 선모양
plt.plot(월, 매출, color='red', marker='o', label='올해')
plt.plot(월, 작년, color='blue', linestyle='--', label ='작년')
plt.title('올해 VS 작년 매출')
plt.legend()
plt.grid(alpha=.3) #격자 추가
# plt.show()
#
# 과목 = ['국어', '수학', '영어']
# 점수 = [88, 76, 95]
# #bar
# fig, ax = plt.subplot(1, 2, figsize=(11, 3.6))
# ax[0].bar(과목, 점수, color='blue')
# ax[1].barch(과목, 점수, color='orange')
# plt.show()
import pandas as pd
hw = pd.read_csv('C:/medicalAI/Pycham/week3/Data_processing/heights.csv')
print(hw.head(10))
print(hw.describe())
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].scatter(hw['height'], hw['weight'], s=15, alpha=0.5, color='green')
ax[0].set_title('키 VS 몸무게')
ax[1].hist(hw['height'], bins=25, color='blue', edgecolor='white')
ax[1].axvline(hw['weight'].mean(), color='red', ls= '--', label='mean')
ax[1].set_title('키 분포')
plt.tight_layout()
plt.show()