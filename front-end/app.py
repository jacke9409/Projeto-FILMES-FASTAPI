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
#Menu lateral sidebar
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar filme"])

if menu == "Catalogo":
    st.subheader("Todos os filmes 🎥")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(f" **{filme['titulo']}** ({filme['ano']}) - {filme['genero']} - ⭐")
        else:
            st.info("Nenhum filme cadastrado")
    else:
        st.error("Erro ao conectar com a API")

elif menu == "Adicionar filme":
    st.subheader("➕ Adicionar Filme")
    titulo = st.text_input("Título do Filme")
    genero = st.text_input("Gênero")
    ano = st.number_input("Ano de lançamento", min_value=1900, max_value=2100, step=1)
    avaliacao = st.number_input("Avaliação de 0 a 10", min_value=0, max_value=10, step=1)

    if st.button("Salvar filme"):
        params = {"titulo": titulo, "genero": genero, "ano": ano, "avaliacao": avaliacao}
        response = requests.post(f"{API_URL}/filmes", params=params)
        if response.status_code == 200:
            st.success("Filme adicionado com sucesso")
        else:
            st.error("Erro ao adicionar filme")

elif menu == "Atualizar Filme":
    st.subheader("Atualizar filme")
    id_filme = st.number_input("ID do Filme a atualizar", min_value=1, step=1)
    nova_avaliacao = st.number_input("Nova avaliação", min_value=0, max_value=10)
    
    if st.button("Atualizar"):
        dados = {"nova_avaliacao": nova_avaliacao}
        response = requests.put(f"{API_URL}/filmes/{id_filme}", params=dados)
        
        if response.status_code == 200:
            data = response.json()
            if "erro" in data:
                st.warning(data["erro"])
            else:
                st.success("Filme atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar filme")