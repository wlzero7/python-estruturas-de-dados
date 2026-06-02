# filas/fila.py

from collections import deque

fila = deque()

fila.append("Cliente 1")
fila.append("Cliente 2")
fila.append("Cliente 3")

print(fila)

atendido = fila.popleft()

print(f"Atendido: {atendido}")
print(fila)
