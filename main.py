import streamlit as st
import numpy as np
import pandas as pd

st.title("Ferum AI")

st.write("seabass count")
count =pd.DataFrame({
    'month':[1,2,3,4,5,6,7,8,9,10,11,12],
    'seabass':[1,2,3,0,3,1,4,5,6,7,8,1]
})

#st.table(count)

df =pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)

st.line_chart(df)


"""
### OBJECTIVE
## interactive benefits
# Truth of information power is ferumic, this power should be interactive. 
# Taking is okay but interactive is better. 



"""