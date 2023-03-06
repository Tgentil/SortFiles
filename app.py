"""
Este script lê todos os arquivos na pasta de origem especificada e move aqueles que contêm 'adicone o parametro aqui' em seu nome para a pasta de destino especificada.

Parâmetros:
- pasta_origem: o caminho para a pasta de origem que contém os arquivos a serem verificados.
- pasta_destino: o caminho para a pasta de destino onde os arquivos devem ser movidos.

Exemplo de uso:
>> mover_arquivos_com_tracos('caminho/para/pasta/origem', 'caminho/para/pasta/destino')
"""

import os

# Defina os nomes das pastas de origem e destino
pasta_origem = r"caminho/para/pasta/origem"
pasta_destino = r"caminho/para/pasta/destino"

# Itere sobre todos os arquivos na pasta de origem
for nome_arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
    
    # Verifique se o nome do arquivo contém '--'
    if 'nome do parametro' in nome_arquivo:
        # Crie o caminho do arquivo de destino
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        
        # Mova o arquivo para a pasta de destino
        os.rename(caminho_arquivo, caminho_destino)
