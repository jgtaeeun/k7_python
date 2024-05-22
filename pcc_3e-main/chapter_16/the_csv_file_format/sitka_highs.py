from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt
import os


os.chdir('pcc_3e-main/chapter_16/the_csv_file_format')

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()      #lines :리스트

reader = csv.reader(lines)#reader:리스트를 가지고 있다. 객체이다. 커서 개념을 가지고 있다. 
header_row = next(reader)           

# # Extract dates and high temperatures.
dates, highs = [], []
for row in reader:    #2번째 행부터의 리스트를 reader가 한개씩 넘긴다.
    current_date = datetime.strptime(row[2], '%Y-%m-%d')  #2024-05-22에 해당하는 객체를 만든다.
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

plt.style.use('seaborn-v0_8')     #격자
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()         #날짜가 겹치지 않게 대각선으로 그린다.
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
