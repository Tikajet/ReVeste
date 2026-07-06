# app/core/database.py
from prisma import Prisma
import os

# Inicializa o cliente do Prisma
db = Prisma()

# Função para garantir que a conexão esteja ativa
async def ensure_db():
    if not db.is_connected():
        await db.connect()