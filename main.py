import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import datetime
#from datetime import timedelta

dt_now=datetime.datetime.now()

srss=pd.read_csv("sr_ss.csv")
st.write("test")

srss['sr'] = pd.to_datetime(srss['sr'])
srss['ss'] = pd.to_datetime(srss['ss'])


srt=srss.loc[(srss["d"]==str(dt_now.date())),"sr"]
sst=srss.loc[(srss["d"]==str(dt_now.date())),"ss"]

#google colab test only
#timedelta to adjust to japan time
#dt_now+=datetime.timedelta(hours=9)

sunrise=srt.iloc[0].hour
sunset=sst.iloc[0].hour

# sun system effect
hour_ranges = [(0, sunrise-2), (sunrise-2, sunrise+2), (sunrise+2, sunset-2), (sunset-2, sunset+2), (sunset+2, 24)]
rand_ranges = [(40, 60), (70, 80), (10, 15), (60, 75), (40, 60)]

for i, (h_start, h_end) in enumerate(hour_ranges):
    if h_start <= dt_now.hour < h_end:
        t = int(np.random.randint(*rand_ranges[i], 1))
        break


# season definder
month = [(1, 3), (4, 5), (6, 9), (10, 12)]
season = ["winter", "spring", "summer", "autumn"]

s = None

for i, (s_start, s_end) in enumerate(month):
    if s_start <= dt_now.month <= s_end:
        s = season[i]
        break



df=pd.read_csv("experiment.csv")

#core code !!!!!

output=df.sample(weights=df[s],frac=float(t/100))
print(t)
print(output.count())

coordination=output[["lon","lat"]]

rating=output["lat"].count()

st.write(f'多摩川シーバス\nポイント予想要素\n\n〇日付  {dt_now.month}月{dt_now.day}日\n〇時刻  {dt_now.strftime("%H:%M")}\n〇季節   {s}\n〇日の出: 5:30\n〇日没: 18:30\n\n\n〇遡上係数　： {rating}ポイント　\n*数値が高いほど上流に期待\n\n\n対応準備中項目\n〇潮汐　：　準備中\n〇天気　：　雨履歴　\n〇水位　：　')

st.map(coordination)


# マニュアル版

year=st.selectbox(
    "年度選択",
    ["2023","2024","2025","2026"]
)
month=st.selectbox(
    "月",
    ["1","2","3","4","5","6","7","8","9","10","11","12"]
)

date=st.selectbox(
    "日",
    ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",
     "16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
)

hour=st.selectbox(
    "時間",
    ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",
     "16","17","18","19","20","21","22","23","24"]
)
min=st.selectbox(
    "分",
    ["00","15","30","45"]
)


s_txt=f'{year}-{month}-{date} {hour}:{min}'

st.write(s_txt)

s_dt=pd.to_datetime(s_txt)

s_sr=srss.loc[(srss["d"]==str(s_dt.date())),"sr"]
s_ss=srss.loc[(srss["d"]==str(s_dt.date())),"ss"]


s_sr.iloc[0].minute

#time zone definder
s_h_ranges = [(0, sunrise-2), (sunrise-2, sunrise+2), (sunrise+2, sunset-2), (sunset-2, sunset+2), (sunset+2, 24)]
for i, (h_start, h_end) in enumerate(s_h_ranges):
    if h_start <= s_dt.hour < h_end:
        st = int(np.random.randint(*rand_ranges[i], 1))
        break


#season definder
month = [(1, 3), (4, 5), (6, 9), (10, 12)]
season = ["winter", "spring", "summer", "autumn"]

s_s = None

for i, (s_start, s_end) in enumerate(month):
    if s_start <= s_dt.month <= s_end:
        s_s = season[i]
        break

sop=df.sample(weights=df[s_s],frac=float(st/100))
print(st)
print(sop.count())


scd=sop[["lon","lat"]]


#st.map(scd)











