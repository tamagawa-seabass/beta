import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from datetime import timedelta


import datetime
import pytz
#!pip install suntime
#from suntime import Sun

st.title("TAMAGAWA RIVER aka TAMAZON")

st.write("SEABASS RADER ｼｰﾊﾞｽﾚｰﾀﾞｰ")


option=st.selectbox(
    "季節を選択してください",
    ["early spring","spring","late spring","early summer",
    "summer","late summer","early autum","autum","late winter"]
)

"season you have chosen",option





if st.checkbox('bag of fish'):
    img=Image.open("sample.jpg")
    st.image(img,caption="stream",use_column_width=True)

# version 1

# reflecting time and season


tz = pytz.timezone('Asia/Tokyo')
dt_now = datetime.datetime.now(tz)

print(dt_now)
print(type(dt_now))

df=pd.read_csv("experiment.csv")



#latitude = 35.534230
#longitude = 139.779020
#sun = Sun(latitude, longitude)

# 日の出・日の入り時刻
#sunrise = sun.get_local_sunrise_time()
sunrise=5
#sunset = sun.get_local_sunset_time()
sunset=19

# タイムゾーンを考慮して時刻を修正
#timezone_offset = timedelta(hours=9)
#sunrise += timezone_offset
#sunset += timezone_offset

# sun system effect

# before morning
if dt_now.hour<sunrise-2:
    t=int(np.random.randint(0,10,1))

# morning     sunrise +-2
elif sunrise-2<= dt_now.hour<sunrise+2:
    t=int(np.random.randint(10,20,1))
# daytime
elif sunrise+2<=dt_now.hour<sunset-2:
    t=int(np.random.randint(20,30,1))
# sunset time  sunset+-2
elif sunset-2<=dt_now.hour<sunset+2:
    t=int(np.random.randint(30,40,1))
#night til midnight
else:
    t=int(np.random.randint(40,50,1))


# sun indivial effect
if dt_now.hour<sunrise-2:
    df["night"]=df["night"]*4

# morning     sunrise +-2
elif sunrise-2<= dt_now.hour<sunrise+2:
    df["night"]=df["night"]*4
# daytime
elif sunrise+2<=dt_now.hour<sunset-2:
    df["day"]=df["day"]*4
# sunset time  sunset+-2
elif sunset-2<=dt_now.hour<sunset+2:
    df["night"]=df["night"]*4
#night til midnight
else:
    df["night"]=df["night"]*4



# seasonal factor reflection
if dt_now.month<4:
    df["winter"]=df["winter"]*4
elif 4<=dt_now.month<7:
    df["spring"]=df["spring"]*4
elif 7<=dt_now.month<10:
    df["summer"]=df["summer"]*4
elif 10<=dt_now.month<12:
    df["autum"]=df["autum"]*4
else:
    df["winter"]=df["winter"]


#要素の集計作業
df["total"]=df[["night","day","spring","summer","autum","winter","rain","water level","tide","wind"]].sum(axis=1)

selection=df.nlargest(t,"total")

cordination=selection[["lat","lon"]]


st.map(cordination)
st.write(sunrise)

#a=[[35.524381, 139.795240],
#[35.524020, 139.792363],
#[35.523334, 139.791623],
#[35.525010, 139.795766],
#[35.534106, 139.778623],
#[35.534268, 139.778972],
#[35.534230, 139.779020],
#[35.534077, 139.779368],
#[35.534145, 139.779019],
#[35.530636, 139.787002],
#[35.530894, 139.785900],
#[35.538708, 139.765624],
#[35.539049, 139.764717],
#[35.541406, 139.767163],
#[35.539754, 139.770390]]


"""
### OBJECTIVE
## Fishing is about to spot proper place. 
## This is a map my personal knowledge is reflected. 
# This is my personal use only. 
# I owe no responsibility for any touble caused by this data. 
# Nothing has determined, risk is all yours. 



"""