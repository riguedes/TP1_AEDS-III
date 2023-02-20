# Importação de bibliotecas
import os
import time

from function import encontrar_caminho

print("---------- Iniciando o programa ----------")
print("\n")

# Verificar a existência do arquivo
file_name = input("Digite o nome do arquivo de labirinto: \n")
while not os.path.isfile(file_name):
    opcao = input(f"O arquivo {file_name} não existe no diretório. Digite 1 para tentar novamente ou 0 para encerrar o programa: \n")
    if opcao == "0":
        exit()
    elif opcao == "1":
        file_name = input("Digite o nome do arquivo de labirinto: \n")
    else:
        print("Opção inválida. Digite 1 para tentar novamente ou 0 para encerrar o programa. \n")

# Inicio do tempo
inicio = time.time()

# Abrir o arquivo em modo leitura
with open(file_name, "r") as arquivo:
    conteudo = ''
    for linha in arquivo:
        conteudo += linha

# Imprimir conteúdo do arquivo
print("Imprimindo conteúdo do arquivo para visualização na tela")
print("\n")
print(conteudo)
print("\n")

# Criar coordenadas para cada caractere
coordenadas = {}
linha = 0
coluna = 0
for caractere in conteudo:
    if caractere == '\n':
        linha += 1
        coluna = 0
    else:
        coordenadas[(linha, coluna)] = caractere
        coluna += 1

# Definir os caracteres desejados
caracteres_desejados = [' ', 'S', 'E']

# Criar coordenadas para os caracteres desejados
solucao = {}
linha = 0
coluna = 0
for caractere in conteudo:
    if caractere == '\n':
        linha += 1
        coluna = 0
    else:
        if caractere in caracteres_desejados:
            solucao[(linha, coluna)] = caractere
        coluna += 1

# Definir o tempo de início da execução
tempo_inicio = time.time()

# Encontrar a solução do labirinto
inicio = None
fim = None
for coordenada, caractere in solucao.items():
    if caractere == 'S':
        inicio = coordenada
    elif caractere == 'E':
        fim = coordenada
if inicio and fim:
    caminho = encontrar_caminho(coordenadas, inicio, fim)
    if caminho:
        print("O caminho encontrado é:")
        for coord in caminho:
            print(coord, end=" ")
    else:
        print("Não foi possível encontrar um caminho.")
else:
    print("Não foi possível encontrar as coordenadas de S e E.")

# Imprimir o tempo de execução
fim_tempo = time.time()
tempo_execucao = fim_tempo - tempo_inicio
print(f"Tempo de execução: {tempo_execucao:.7f} segundos")








    






