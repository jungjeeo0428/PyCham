import matplotlib.pyplot as plt
import pandas as pd, numpy as np
# Series: 이름표(index) 달린 1차원
s = pd.Series([90, 85, 77], index=['국어', '영어', '수학'])
print('■ Series:'); print(s)
# DataFrame: 표 (딕셔너리로 생성)
df = pd.DataFrame({
    '이름': ['철수', '영희', '민수', '지훈', '수아'],
    '반':   ['A', 'B', 'A', 'B', 'A'],
    '국어': [90, 85, 70, 60, 95],
    '수학': [80, 95, 60, 75, 88],
})
# print(df.head)
# # print('shape', df.shape)
# # print('columns', df.columns)
# # print(df.describe())
# # print(df.info())
# #data + x
# print(df['국어'] + 10)
# df['국어_수학'] = df['국어']+df['수학']
print(df)
# print('='*50)
# print(df['국어'].values)
# print(df[['이름', '수학']])
# print(df[df['수학'] >= 80][['이름', '수학']])
# #iloc위치 df.iloc[0, 2] 0행 2열
# print(df.iloc[0,2])

#groupby
# print('='*50)
# print(df.groupby('반')[['국어','수학']].mean())
# print(df.groupby('반').size(), '반별 인원수')
# print(df.groupby('반')['수학'].agg(['mean', 'max', 'min']))
# 결측치
df2 = df.copy()
# df2.loc[2, '수학'] = np.nan #결측치를 일부러 만든거 민수 수학 nan
# print(df2['수학'].isna().values) #민수거 True 나온다
# print(df2['수학'].isna().sum())


# 결측치 채우기
# filled = df2['수학'].fillna(df2['수학'].mean()) #평균으로 null값 채우기
# print(filled)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']
ax = df.set_index('이름')[['국어', '수학']].plot(kind='bar', figsize=(8, 3.5))
ax.set_title('학생별 국어&수학점수')
ax.set_ylabel('점수')
plt.tight_layout()
plt.show()