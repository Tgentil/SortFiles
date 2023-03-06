# SortFiles

Este script Python é usado para mover arquivos de uma pasta de origem para uma pasta de destino, com base em um nome do parametro que você especifica. O script irá procurar em todos os nomes de arquivos na pasta de origem e mover qualquer arquivo que contenha o nome do parametro para a pasta de destino. Isso pode ser útil para organizar arquivos com base em determinados padrões no nome do arquivo.

## Como usar

1. Baixe ou clone este repositório para o seu computador.
2. Abra o arquivo `app.py` e configure as seguintes variáveis de acordo com suas necessidades:
   - `pasta_origem`: o caminho para a pasta de origem que contém os arquivos a serem verificados.
   - `pasta_destino`: o caminho para a pasta de destino onde os arquivos devem ser movidos.
   - `nome do parametro`: o curinga que você deseja procurar no nome do arquivo.
3. Salve o arquivo `mover_arquivos.py` e execute-o em um terminal com o comando `python app.py`.
4. O script irá mover todos os arquivos que contêm o nome do parametro na pasta de origem para a pasta de destino.

## Exemplo de uso

Suponha que você tenha uma pasta de origem com vários arquivos de log em formato `.txt`, e você deseja mover todos os arquivos que contêm a palavra "erro" em seu nome para uma pasta de destino separada. Para fazer isso, siga estas etapas:

1. Configure as variáveis `pasta_origem` e `pasta_destino` em `app.py` para apontar para as pastas de origem e destino apropriadas em seu computador.
2. Defina o nome do parametro como "erro" na variável `nome do parametro`.
3. Salve o arquivo `app.py` e execute-o em um terminal com o comando `python app.py`.
4. O script irá mover todos os arquivos que contêm a palavra "erro" em seu nome da pasta de origem para a pasta de destino.

## Notas

- Certifique-se de usar os caminhos reais das pastas de origem e destino em `app.py`.
- O nome do parametro pode ser qualquer string que você desejar procurar no nome do arquivo.
- Se nenhum arquivo for encontrado na pasta de origem com o nome do parametro, o script não fará nada.
- O script irá mover o arquivo inteiro, incluindo o nome do arquivo. Se você quiser renomear o arquivo ao movê-lo, você pode fazer isso adicionando código para alterar o nome do arquivo antes de chamar `os.rename`.
