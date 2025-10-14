from fastapi import FastAPI
import funcoes

#Roda fastapi =  python -m uvicorn api:app --reload

#Testar as rotas no fastapi
# /docs > documentação Swagger
# /redoc > Documentação Redoc

app = FastAPI(title="Gerenciador de Filmes")

#GET > Pegar/Listar
#POST > Enviar/Cadastrar
#PUT > Atualizar
#DELETE > Deletar

#API sempre retorna dados em JSON (Chave: Valor)

@app.get("/")
def home():
    return {"Mensagem": "Bem-vindo ao gerenciador de filmes"}


@app.get("/filmes")
def catalogo():
    filmes = funcoes.listar_movies()
    lista = []
    for filme in filmes:
        lista.append({
            "id": filme[0],
            "titulo": filme[1],
            "genero": filme[2],
            "ano": filme[3],
            "avaliacao": filme[4]
        })
    return {"filmes": lista}

@app.post("/filmes")
def adicionar_filme(titulo:str, genero:str, ano:str, avaliacao: float):
    funcoes.criar_filme(titulo, genero, ano, avaliacao)
    return {"Mensagem": "Filme adicionado com sucesso"}

@app.put("/filmes/{id_filmes}")
def atualizar_filme(id_filme: int, nova_avaliacao: float):
    filme = funcoes.buscar_filme(id_filme)
    if filme:
        funcoes.atualizar_movies(id_filme)
    






