from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Criar uma API flask
app = Flask(__name__) # recebe o nome da app ('estrutura_banco)
# Criar uma instancia de SQLAlchemy
app.config['SECRET_KEY'] = 'Hermes82wars!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///token.db' # connection string

db = SQLAlchemy(app)
db:SQLAlchemy



# Definir a estrutura da tabela autores
# id, nome, email, senha, admin, postagens
class Token(db.Model):
    __tablename__ = 'token'
    id_token = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String)
    data = db.Column(db.DateTime, default=datetime.utcnow)


def inicializar_banco():
    # Executar o comando para criar o banco de dados
    db.drop_all()
    db.create_all()
    
    token = Token(token='d37da25a05833312d59fe931fc69d394')
    db.session.add(token)
    db.session.commit()


if __name__ == "__main__":
    inicializar_banco()
