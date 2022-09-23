import sys
import subprocess

arquivos = ['app.py','gera_token.py']
processos = []

for arquivo in arquivos:
    processo = subprocess.Popen([sys.executable, arquivo])
    processos.append(processo)

# neste ponto todos os scripts estão rodando em background ao mesmo tempo. 
# Para esperar todos eles terminarem:

for processo in processos:
    processo.wait()