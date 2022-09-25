import secrets
from datetime import datetime
from estrutura_banco import Token, db
from datetime import datetime
import time


def cria_token():
    while True:
        tokens = Token.query.filter_by(id_token=1).first()
        data_token = tokens.data
        data_atual = datetime.now()
        print(data_atual)
        periodo_seconds = abs((data_atual - data_token).total_seconds())  # total_seconds()
        periodo_hours = divmod(periodo_seconds, 3600)[0]
        periodo_min = periodo_seconds / 60

        if periodo_min > 5:
            chave = secrets.token_hex(16)
            db.drop_all()
            db.create_all()
            token = Token(token=chave)
            db.session.add(token)
            db.session.commit()
            print(f'Novo token: {chave}')
            print(periodo_min)
        else:
            print('Token válido')
            print(periodo_min)
        print('executado')
        print(periodo_hours)
        print(periodo_min)
        print(periodo_seconds)
        time.sleep(60)
        print('Executando novamente')


if __name__ == '__main__':
    cria_token()
