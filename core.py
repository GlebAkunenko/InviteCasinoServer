from random import random
from enum import Enum

class Color(Enum):
    black = 'black',
    gray = 'gray'
    green = 'green'
    blue = 'blue'
    purple = 'purple'
    red = 'red'
    yellow = 'yellow'

arr = [
    (0.2, 0, Color.black),
    (0.249, 0.2, Color.gray),
    (0.19, 1, Color.green),
    (0.057, 2, Color.blue),
    (0.25, 0.5, Color.gray),
    (0.023, 4, Color.purple),
    (0.02, 10, Color.red),
    (0.011, 20, Color.yellow),
]
S = sum([x[0] for x in arr])
if S != 1:
    raise Exception(f"Sum must be 1! But it is {S}")

def get_value(dep: int) -> tuple[int, Color]:
    value = random()
    acc = 0
    for a in arr:
        acc += a[0]
        if value <= acc:
            return int(a[1] * dep), a[2]