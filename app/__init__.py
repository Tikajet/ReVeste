# app/__init__.py
from flask import Flask, request, jsonify
from app.core.database import db
import asyncio

app = Flask(__name__)

# Conecta ao banco ao iniciar o servidor
@app.before_first_request
def startup():
    asyncio.run(db.connect())

# Rota para cadastrar um produto
@app.route('/produtos', methods=['POST'])
def create_product():
    data = request.json
    # O uso de loop permite chamar funções assíncronas do Prisma
    loop = asyncio.get_event_loop()
    product = loop.run_until_complete(db.product.create(
        data={
            "name": data['name'],
            "description": data['description'],
            "price": float(data['price']),
            "category": data['category'],
            "imageUrl": data['imageUrl'],
            "stock": int(data.get('stock', 0))
        }
    ))
    return jsonify(product), 201

# Rota para listar produtos
@app.route('/produtos', methods=['GET'])
def list_products():
    loop = asyncio.get_event_loop()
    products = loop.run_until_complete(db.product.find_many())
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)