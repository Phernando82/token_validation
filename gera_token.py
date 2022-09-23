import secrets
from datetime import datetime
from flask import Flask, jsonify, request, make_response
from estrutura_banco import Token, app, db
import json
from datetime import datetime, timedelta
from functools import wraps
import time


def cria_token():
    while True:
        tokens = Token.query.filter_by(id_token=1).first()
        data_token = tokens.data
        data_atual = datetime.now()
        periodo_seconds = abs((data_atual - data_token).total_seconds()) # .total_seconds()
        periodo_hours = divmod(periodo_seconds, 3600)[0]

        if periodo_hours > 1:
            chave = secrets.token_hex(16)
            db.drop_all()
            db.create_all()
            
            token = Token(token=chave)
            db.session.add(token)
            db.session.commit()
            print(f'Novo token: {chave}')
        else:
            print('Token válido')
        print('executando')
        time.sleep(3600)


if __name__== '__main__':
    cria_token()