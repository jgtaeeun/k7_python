from pathlib import Path
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')   #2021 7월 단기 데이터
path = Path('weather_data/sitka_weather_2021_simple.csv')    #2021 총 데이터  avg데이터는 ''이다.
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

highs,dates,lows=[],[],[]       #파이썬다중할당


for index, column_header in enumerate(header_row):
    print(index, column_header)

for row in reader:
    current_date=datetime.strptime(row[2], '%Y-%m-%d')
    

    
    try:
            high=int(row[4])
            low=int(row[5])
            # avg=int(row[3])    #    #ValueError: invalid literal for int() with base 10:''/ avg데이터는 ''이다.
    
    except ValueError:
        print(f"missing data for value={current_date}")
    
    else :
        
        # avgs.append(avg)
        lows.append(low)
        highs.append(high)
        dates.append(current_date)

# print(highs)
# print(lows)
# # print(avgs)
# print(dates)

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates,highs, color='red', alpha=0.5)
ax.plot(dates,lows, color='blue', alpha=0.5)
# ax.plot(dates,avgs, color='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.5)
ax.set_title('high/low temperature', fontsize=14)
fig.autofmt_xdate()
ax.set_xlabel('date', fontsize=10)
ax.set_ylabel('temperature', fontsize=14)
ax.tick_params(labelsize=8)
plt.show()