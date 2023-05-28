# FILE: eg_streamlit.py
# pip install streamlit pyecharts streamlit-echarts
# streamlit run eg_streamlit.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
import pandas as pd

st.markdown(
   '''
   # Streamlit with Markdown

   ##  Header Level 2

   Put some write up here.  $e^{i\pi}+1=0$.

   - bullet *point 1*
   - bullet **point 2**
   ''' 
   )

x = np.linspace(0, 4*np.pi, 500)
y = np.sin(x)
fig,ax = plt.subplots(1,1,figsize=(2,1))
ax.plot(x,y)
st.pyplot(fig)

bar = Bar()
bar.add_xaxis(["Mon","Tue","Wed", "Thu", "Fri"])
bar.add_yaxis('Income', [500,400, 350, 600, 200])
bar.add_yaxis('Expenses', [320, 120, 400, 350, 200])
st_pyecharts(bar)

data = np.array([[5.2945, 100.2593]])
data = np.random.randn(10,2)/100 + [5.2945, 100.2593]
data = pd.DataFrame(data, columns=['lat','lon'])
st.map(data)

