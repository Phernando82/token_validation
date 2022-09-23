import sys
import subprocess

def iniciar_programa():
    arquivos = ['gera_token.py', 'app.py']
    processos = []

    for arquivo in arquivos:
        processo = subprocess.Popen([sys.executable, arquivo])
        processos.append(processo)

    # neste ponto todos os scripts estão rodando em background ao mesmo tempo. 
    # Para esperar todos eles terminarem:

    for processo in processos:
        processo.wait()


if __name__=='__main__':
    iniciar_programa()