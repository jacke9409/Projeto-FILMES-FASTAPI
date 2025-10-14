# pip install fastapi uvicorn streamlit requests psycopg2 dotenv
#  pip freeze > requirements.txt
import streamlit as st
import requests

#Rodar o streamlit
# python -m streamlit run app.py

#URL da API do FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes", page_icon="🎬")

st.title("🍿 Gerenciador de filmes")

#Menu lateral sidebar
menu = st.sidebar.radio("Navegação", ["Catalogo"])

if menu == "Catalogo":
    st.subheader("Todos os filmes 🎥")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(f" **{filme['titulo']}** ({filmes['ano']}) - {filme['genero']} - ⭐")
            else:
                st.info("Nenhum filme cadastrado")
        else:
            st.error("Erro ao conectar com a API") 

elif menu == "Adicionar Filme":
    st.subheader("Adicionar filme")
    titulo = st.text_input("titulo do Filme")       
    genero = st.text_input("Gênero")
    ano = st.number_input("Ano de lançamento", mi_value=1900, max_vali=2100, stp=1)
    avaliacao = st.number_input("Avalição de (0 a 10)", min_value=0, max_value=10, step=1)

    if st.button("Salvar filme"):
        params = {"titulo": titulo, "genero": genero, "ano": ano, "avaliacao": avaliacao}
        response = requests.post(f"(API_URL)/filmes",params=params)
        if response.status_code ==200:
            st.success("Filme adicionado com sucesso")
        else:
            st.error("Erro ao adicionar filme!")
