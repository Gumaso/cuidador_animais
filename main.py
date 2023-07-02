import time
from random import choice
estados = ["sono", "sede", "fome", 'dores', 'mal estar', 'alegria', 'um bom semblante', 'certeza bem']
animais = ["Tamanduá", "Capivara", "Arara-Azul", "Onça-Pintada", "Boto Cor de Rosa", "Tatu"]
print(f"""
Vamos checar os animais""")
for animal in animais:
    print(f"O(a) {animal} está com {choice(estados)}")
