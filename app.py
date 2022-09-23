from flask import Flask, jsonify, request, make_response
from estrutura_banco import Token, app, db
import json
from datetime import datetime, timedelta
from functools import wraps
# Rota padrão - GET http://localhost:5000


@app.route('/token')
def obter_tokens():
    tokens = Token.query.all()
    lista_tokens = []
    for token in tokens:
        token_atual = {}
        token_atual['id_token'] = token.id_token
        token_atual['token'] = token.token
        token_atual['data'] = token.data
        lista_tokens.append(token_atual)

    return jsonify({'token': lista_tokens})


@app.route('/token/<int:id_token>', methods=['GET'])
def obter_token_por_id(id_token):
    token = Token.query.filter_by(id_token=id_token).first()
    if not token:
        return jsonify(f'token não encontrado!')
    token_atual = {}
    token_atual['id_token'] = token.id_token
    token_atual['token'] = token.token
    token_atual['data'] = token.data

    return jsonify({'token': token_atual})


# Criar novo token
@app.route('/token', methods=['POST'])
def novo_token(token):
    novo_token = request.get_json()
    token = token(
        token=novo_token['token'])

    db.session.add(token)
    db.session.commit()

    return jsonify({'mensagem': 'Token criado com sucesso'}, 200)


@ app.route('/token/<int:id_token>', methods=['PUT'])
def alterar_token(token, id_token):
    token_a_alterar = request.get_json()
    token = token.query.filter_by(id_token=id_token).first()
    if not token:
        return jsonify({'Mensagem': 'Este token não foi encontrado'})
    try:
        token.token = token_a_alterar['token']
    except:
        pass
   
    db.session.commit()
    return jsonify({'mensagem': 'Token alterado com sucesso!'})


@ app.route('/tokenes/<int:id_token>', methods=['DELETE'])
def excluir_token(token, id_token):
    token_existente = token.query.filter_by(id_token=id_token).first()
    if not token_existente:
        return jsonify({'mensagem': 'Este token não foi encontrado'})
    db.session.delete(token_existente)
    db.session.commit()

    return jsonify({'mensagem': 'Token excluído com sucesso!'})


if __name__== '__main__':
    app.run(port=5000, host='localhost', debug=True)
