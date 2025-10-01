##  nestihol som to úplne dorobiť, zatiaľ mám tento kód kt. som robil v streamlit playgrounde

import streamlit as st
import pandas as pd
import altair as alt
import math

st.title("Vytvor si svoju kružnicu!")
st.write("*elipsu ak si na mobile")

polomer = st.number_input("Vyber si polomer:", min_value=1, max_value=20, value=3, step=1,)
stredx = st.number_input("X-ová súradnica stredu:", min_value=-20, max_value=20, value=0,)

stredy = st.number_input("Y-ová súradnica stredu:", min_value=-20, max_value=20, value=0,)
body = st.number_input("Vyber si počet bodov:", min_value=3, max_value=500, value="min", step=1,)
farba = st.color_picker("Zvoľ si farbu", "#00f900")

uhol = math.radians(360/body)
xx = []
yy =[]

for i in range(body):
    xx.append(stredx+math.cos(uhol*i)*polomer)
    yy.append(stredy+math.sin(uhol*i)*polomer)
    

tabulka = pd.DataFrame(
    { "xová":xx, "yová": yy, })

chart = (
    alt.Chart(tabulka)
    .mark_circle(size=100, color=farba)
    .encode(x=alt.X("xová", title="[cm]", scale=alt.Scale(domain=[-25, 25])),
            y=alt.Y("yová", title="[cm]", scale=alt.Scale(domain=[-25, 25])))
    .properties(width=750, height=750)
    .configure_axis(grid=True)
)

st.altair_chart(chart, use_container_width=True)


if st.button("Send balloons!"):
    st.balloons()

st.write("Táto stránka bola vytvorená študentom FILIP BUKOVÁC, použitím stránok *https://streamlit.io/playground*, *https://chatgpt.com/*, *https://github.com/*")
