import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일을 불러옴
df = pd.read_csv('./scan_result.csv', header=None, names=['filepath', 'threatname', 'result'])

# 감염 여부 통계 계산
status_counts = df['result'].value_counts()

# 빈도가 낮은 항목 제외
# filtered_counts = status_counts[status_counts >= 10]

# 감염 여부를 막대 그래프로 시각화
status_counts.plot(kind='bar', color=['green', 'red'])
plt.title('Antivirus Scan Results')
plt.xlabel('Scan Status')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()
