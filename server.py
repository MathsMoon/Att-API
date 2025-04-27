# pip install flask flask-sqlalchemy flask-cors werkzeug.security 

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Inicialize o Flask e o SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
db = SQLAlchemy(app)

# Configure o CORS
CORS(app, origins=['http://127.0.0.1:5500'])

### ESTRUTURA DAS CLASSES PARA CRIAR AS TABELAS NO BANCO

# Classe que representa a entidade Carro
class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    modelo = db.Column(db.String(80), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'modelo': self.modelo,
            'ano': self.ano,
            'preco': self.preco,
        }

# Classe que representa a entidade Usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

### CRUD PARA O Carro

# Rota para Listar Todos os Carros
@app.route('/carros', methods=['GET'])
def get_carros():
    carros = Carro.query.all()
    return jsonify([carro.serialize() for carro in carros])

# Rota para Listar um Carro Específico
@app.route('/carros/<int:carro_id>', methods=['GET'])
def get_carro(carro_id):
    carro = Carro.query.get(carro_id)
    if carro is None:
        return jsonify({'mensagem': 'Carro não encontrado'}), 404
    return jsonify(carro.serialize())

# Rota para Criar um Novo Carro
@app.route('/carros', methods=['POST'])
def create_carro():
    dados = request.get_json()
    nome = dados.get('nome')
    modelo = dados.get('modelo')
    ano = dados.get('ano')
    preco = dados.get('preco')

    if not nome or not modelo or ano is None or preco is None:
        return jsonify({'mensagem': 'Nome, modelo, ano e preço são obrigatórios'}), 400

    novo_carro = Carro(nome=nome, modelo=modelo, ano=ano, preco=preco)
    db.session.add(novo_carro)
    db.session.commit()
    return jsonify(novo_carro.serialize()), 201

# Rota para Atualizar um Carro
@app.route('/carros/<int:carro_id>', methods=['PUT'])
def update_carro(carro_id):
    dados = request.get_json()
    carro = Carro.query.get(carro_id)
    if carro is None:
        return jsonify({'mensagem': 'Carro não encontrado'}), 404

    carro.nome = dados.get('nome', carro.nome)
    carro.modelo = dados.get('modelo', carro.modelo)
    carro.ano = dados.get('ano', carro.ano)
    carro.preco = dados.get('preco', carro.preco)

    db.session.commit()
    return jsonify(carro.serialize())

# Rota para Deletar um Carro
@app.route('/carros/<int:carro_id>', methods=['DELETE'])
def delete_carro(carro_id):
    carro = Carro.query.get(carro_id)
    if carro is None:
        return jsonify({'mensagem': 'Carro não encontrado'}), 404
    db.session.delete(carro)
    db.session.commit()
    return jsonify({'mensagem': 'Carro excluído com sucesso'}), 200

### CRUD PARA O Usuário

# Rota para Listar Todos os Usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.serialize() for usuario in usuarios])

# Rota para Buscar um Usuário pelo ID
@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404
    return jsonify(usuario.serialize())

# Rota para Criar um Novo Usuário
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')

    if not nome or not email or not senha:
        return jsonify({'mensagem': 'Nome, email e senha são obrigatórios'}), 400

    # Verificar se o e-mail já está cadastrado
    if Usuario.query.filter_by(email=email).first():
        return jsonify({'mensagem': 'Email já cadastrado'}), 400

    senha_hash = generate_password_hash(senha)

    novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash)
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify(novo_usuario.serialize()), 201

# Rota para Atualizar um Usuário
@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    dados = request.get_json()
    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404

    usuario.nome = dados.get('nome', usuario.nome)
    usuario.email = dados.get('email', usuario.email)

    if 'senha' in dados:
        usuario.senha = generate_password_hash(dados['senha'])

    db.session.commit()
    return jsonify(usuario.serialize())

# Rota para Deletar um Usuário
@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário excluído com sucesso'}), 200


### RODANDO A APLICAÇÃO

if __name__ == '__main__':
    app.run(debug=True)
