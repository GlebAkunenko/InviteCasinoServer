from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import core
from models import *

app = FastAPI()

# Разрешаем CORS для всех доменов (можно ограничить только нужными доменами)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены, или замените на список ваших доменов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все HTTP методы (GET, POST, PUT, DELETE, и т.д.)
    allow_headers=["*"],  # Разрешаем все заголовки
)

@app.get("/play")
async def say_hello(user: str, bet: int):
    if user not in users:
        raise Exception(f"User {user} not found")
    if users[user] < bet:
        raise Exception(f"Balance is too low")
    cards = []
    for i in range(40):
        value, color = core.get_value(bet)
        # value, color = i, core.Color.gray
        cards.append(Card(style=color.name, value=value))
    win = cards[19].value
    users[user] = users[user] - bet + win
    return Result(slots=cards, win=win)

users: dict[str, int] = {}

@app.post("/user")
async def add_user(user: str):
    if user not in users:
        users[user] = 0
    return "OK"


@app.delete("/user")
async def remove_user(user: str):
    del users[user]
    return "OK"


@app.post("/balance")
async def change_balance(user: str, value: int):
    users[user] = value
    return "OK"


@app.get('/balance')
async def get_balance(user: str) -> int:
    if not user in users:
        users[user] = 0
    return users[user]


@app.get('/users')
async def get_users() -> list[tuple[str, int]]:
    return [
        (u, users[u])
        for u in users
    ]