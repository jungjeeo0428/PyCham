import pandas as pd
import matplotlib.pyplot as plt
import FinanceDataReader as fdr
from IPython.core.pylabtools import figsize

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']

df_samsung = fdr.DataReader('005930', '2025-01-01', '2026-08-03')
print(df_samsung.tail())
df_samsung['Close'].plot()
# plt.show()
# df_samsung.to_excel('samsung_2025.xlsx', index=False, engine='openpyxl')
df_krx = fdr.StockListing('krx')
df_krx.to_excel('krx.xlsx', engine='openpyxl')

#삼성 &나 5, 20, 60일 이동 평균선
samsung = fdr.DataReader('005930', '2025-01-01')
sk = fdr.DataReader('000660', '2023-01-01')
samsung['MA5'] = samsung['Close'].rolling(window=5).mean()
samsung['MA20'] = samsung['Close'].rolling(window=20).mean()
samsung['MA60'] = samsung['Close'].rolling(window=60).mean()
plt.figure(figsize=(12,6))
plt.plot(samsung.index, samsung['Close'], label='종가', color='black', alpha=0.3)
plt.plot(samsung.index, samsung['MA5'], label='5일 평균이동', linestyle='--')
plt.plot(samsung.index, samsung['MA20'], label='20일 평균이동', linestyle='--')
plt.plot(samsung.index, samsung['MA60'], label='60일 평균이동', linestyle='--')
plt.title('삼성 주가 및 이동평균선')
plt.legend()
plt.show()