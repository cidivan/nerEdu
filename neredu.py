import streamlit as st
import pandas as pd
import spacy

spacy_model =spacy.load("pt_core_news_sm")

# ======================= Função ========================#
def render_ner():
    dicio = {"Palavra": [item.text for item in input_usr], "Entidade": [item.ent_type_ for item in input_usr]}
    return dicio

# ======================= body ========================#
col3,col1, col2 = st.columns((20, 60,20), vertical_alignment="center")

with col3:
    st.image("image/icon.png", width=100,use_column_width="auto")
with col1:
    st.header("Reconhecimento de Entidade", divider=True)

with col2:
    st.image("image/logoneredu.png", width=100,use_column_width="auto")
st.subheader("Ferramenta de reconhecimento de entidade nomeada para o ensino")

st.divider()

# ================================# area de input #==========================#
text = st.text_area("", height=200, placeholder="Escreva o seu texto aqui.")
input_usr = spacy_model(text)

# ================================# output #================================#
col3, col4 = st.columns(2)

with col3:
    btn1 = st.button("Documentação")
with col4:
    st.button("Entidade", on_click=render_ner)


renderizar = render_ner()
st.table(pd.DataFrame(renderizar))

st.divider()
