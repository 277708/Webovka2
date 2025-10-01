##  nestihol som to úplne dorobiť, zatiaľ mám tento kód kt. som robil v streamlit playgrounde

import streamlit as st
import pandas as pd
import altair as alt
import math
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
import io



st.title("Vytvor si svoju kružnicu!")
st.write("*elipsu - ak si na mobile")

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


def create_pdf(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Výstup z aplikácie", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("stred kružnice je [" + str(stredx) +";"+ str(stredy) +"]"))
    story.append(Paragraph("polomer kružnice =" + str(polomer) ))
    story.append(Paragraph("počet bodov kružnice je" + str(body) ))

    fig, ax = plt.subplots()
    ax.scatter(data["xová"], data["yová"], color=farba)  
    ax.set_title("kružnica:")
    ax.set_xlabel("[cm]")
    ax.set_ylabel("[cm]")
    ax.grid(True)  

    ax.set_xlim(-25, 25)   
    ax.set_ylim(-25, 25)

    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format="PNG")
    plt.close(fig)
    img_buffer.seek(0)

    story.append(Image(img_buffer, width=500, height=500))

    doc.build(story)
    buffer.seek(0)
    return buffer

pdf_file = create_pdf(tabulka)

st.download_button(
    label="Stiahnuť PDF",
    data=pdf_file,
    file_name="Výstup z aplikácie.pdf",
    mime="application/pdf"
)


if st.button("Send balloons!"):
    st.balloons()

st.write("Táto stránka bola vytvorená študentom FILIP BUKOVÁC, použitím stránok *https://streamlit.io/playground*, *https://chatgpt.com/*, *https://github.com/*.")
