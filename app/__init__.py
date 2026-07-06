# app/__init__.py
from flask import Flask, request, jsonify
from app.core.database import db, ensure_db
import asyncio

app = Flask(__name__)

# Nova forma de executar tarefas na inicialização do Flask
@app.before_request
def startup():
    # Apenas conecta se ainda não estiver conectado
    if not db.is_connected():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(ensure_db())

# ... (resto do seu código permanece igual)