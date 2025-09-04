from fastapi import FastAPI
from pydantic import BaseModel

# Inicializa a aplicação FastAPI
app = FastAPI()

# Define um modelo de dados para a requisição POST
# Isso garante que o corpo da requisição terá o campo 'user'
class UserRequest(BaseModel):
    user: str

# Define o endpoint POST para a rota /auth/me
@app.post("/auth/me")
def auth_me(request: UserRequest):
    """
    Retorna um JSON com o usuário que enviou a requisição e a string "pong".
    Aguardando um JSON no formato: {"user": "nomeDoUsuario"}
    """
    return {"user": request.user, "ping": "pong"}
