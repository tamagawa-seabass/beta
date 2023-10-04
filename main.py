import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import datetime
from datetime import timedelta
#import suntime
#from suntime import Sun
"""
### 多摩川シーバス予報（ベータ版） 
### Tama River Labrax forecast. beta 2.0
一般に知られてる生態を元にその日のシーバスの場所を予想します。
季節（春夏秋冬）、時刻（夜、朝、昼、夜）を変数にし
場所を選定します。
シーバスの生態について学習中の方の助けになれば幸いです。


"""


# code for transfer

dt_now=datetime.datetime.now()





#sun=Sun(35.534230,139.779020)
#sunrise=sun.get_local_sunrise_time()
#sunset=sun.get_local_sunset_time()

sunrise=5
sunset=18

# タイムゾーンを考慮して時刻を修正
#sunrise += datetime.timedelta(hours=9)
#sunset += datetime.timedelta(hours=9)

df=pd.read_csv("experiment.csv")

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



#core code !!!!!

output=df.sample(weights=df[s],frac=float(t/100))
print(t)
print(output.count())


coordination=output[["lon","lat"]]

r=output[s].mean()

#st.write(f'多摩川シーバス\nポイント予想要素\n\n〇日付  {dt_now.month}月{dt_now.day}日\n〇時刻  {dt_now.strftime("%H:%M")}\n〇季節   {s}\n〇日の出: 5:30\n〇日没: 18:30\n\n\n〇遡上係数　：　{r}\n*数値が高いほど上流に期待\n\n\n対応準備中項目\n〇潮汐　：　準備中\n〇天気　：　雨履歴　\n〇水位　：　')

st.write("マップの算出結果は計算毎に異なります。計算要素が同じでも異なる結果になります。")

#option=st.selectbox(
#    "季節を選択してください",
#    ["early spring","spring","late spring","early summer",
#    "summer","late summer","early autum","autum","late winter"]
#)

#"season you have chosen",option





#if st.checkbox('bag of fish'):
#    img=Image.open("sample.jpg")
#    st.image(img,caption="stream",use_column_width=True)


st.map(coordination)

"""
### Tama River Labrax forecast. beta 2.0
一般に知られてる生態を元にその日のシーバスの場所を予想します。
情報精度、選出される場所が危険な場合も想定されます。
情報により生じる如何なる問題においても一切の責任を負いません。
釣り禁止の箇所、夜釣り禁止時刻においても表示が出でますがルールを確認の上
ルールに従う必要があります。


"""


