from fastapi import FastAPI
import funcao

#Roda fastapi =  

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
    filmes = funcao.listar_movies()
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

@app.post("/")
def adicionar_filme(titulo:str, genero:str, ano:str, nota: float):
    funcao.criar_filme(titulo, genero, ano, avaliacao)
    return {"Mensagem": "Filme adicionado com sucesso"}






