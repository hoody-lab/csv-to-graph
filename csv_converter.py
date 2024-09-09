import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 데이터 로드
data = pd.read_csv('./detection_time.csv')

# 데이터 로그 변환
data['threaded'] = np.log(data['time1'] + 1)  # 0 값을 방지하기 위해 1을 더함
data['preforked'] = np.log(data['time2'] + 1)  # 0 값을 방지하기 위해 1을 더함

# 이동 평균 계산
window_size = 1000  # 윈도우 크기 설정
moving_average1 = data['threaded'].rolling(window=window_size).mean()
moving_average2 = data['preforked'].rolling(window=window_size).mean()

# 이동 평균 그래프 그리기
plt.figure(figsize=(10, 5))
plt.plot(moving_average1, color='orange', label='Threaded Moving Average')
plt.plot(moving_average2, color='blue', label='Preforked Moving Average')
plt.title('Antivirus Scan Time with Moving Average')
plt.xlabel('Scan Index')
plt.ylabel('Log of Scan Time')
plt.legend()
plt.show()
