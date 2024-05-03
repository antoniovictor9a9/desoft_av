import random

# Configurações e definições dos tamanhos dos navios e das configurações dos estados brasileiros
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES = {
    'São Paulo': {'cruzador': 1, 'torpedeiro': 2, 'destroyer': 1, 'couracado': 1, 'porta-avioes': 1},
    'Rio de Janeiro': {'cruzador': 3, 'porta-avioes': 1, 'destroyer': 1, 'submarino': 1, 'couracado': 1},
    'Bahia': {'couracado': 1, 'cruzador': 3, 'submarino': 1, 'porta-avioes': 1, 'torpedeiro': 1},
    'Paraná': {'cruzador': 1, 'porta-avioes': 1, 'couracado': 2, 'destroyer': 1, 'submarino': 1},
    'Minas Gerais': {'torpedeiro': 2, 'cruzador': 1, 'destroyer': 2, 'couracado': 1, 'submarino': 1}
}

ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CORES = {
    'reset': '\033[0m', 'vermelho': '\033[31m', 'azul': '\033[34m', 'ciano': '\033[36m'
}

def criar_tabuleiro(tamanho):
    return [['.' for _ in range(tamanho)] for _ in range(tamanho)]

def imprimir_tabuleiro(tabuleiro, mostrar_navios=False):
    print("  " + " ".join(ALFABETO[:len(tabuleiro)]))
    for i, linha in enumerate(tabuleiro):
        linha_colorida = ""
        for celula in linha:
            if celula == 'X':
                linha_colorida += CORES['vermelho'] + 'X' + CORES['reset'] + " "
            elif celula == 'O':
                linha_colorida += CORES['azul'] + 'O' + CORES['reset'] + " "
            elif celula == 'N' and mostrar_navios:
                linha_colorida += CORES['ciano'] + 'N' + CORES['reset'] + " "
            else:
                linha_colorida += '.' + " "
        print(f"{i+1:2}" + linha_colorida)

def escolher_estado():
    print("Escolha o estado para sua frota:")
    for i, estado in enumerate(PAISES.keys(), 1):
        print(f"{i}: {estado}")
    escolha = int(input("Digite o número do estado escolhido: ")) - 1
    return list(PAISES.keys())[escolha]

def pode_alocar(tabuleiro, navio, inicio, direcao, tamanho):
    x, y = inicio
    if direcao == 'horizontal':
        if y + tamanho > len(tabuleiro):
            return False
        for i in range(tamanho):
            if tabuleiro[x][y + i] != '.':
                return False
    elif direcao == 'vertical':
        if x + tamanho > len(tabuleiro):
            return False
        for i in range(tamanho):
            if tabuleiro[x + i][y] != '.':
                return False
    return True

def alocar_navio(tabuleiro, navio, inicio, direcao, tamanho):
    x, y = inicio
    if pode_alocar(tabuleiro, navio, inicio, direcao, tamanho):
        if direcao == 'horizontal':
            for i in range(tamanho):
                tabuleiro[x][y + i] = 'N'  # 'N' representa um navio
        elif direcao == 'vertical':
            for i in range(tamanho):
                tabuleiro[x + i][y] = 'N'
        return True
    return False

def alocar_navios_usuario(tabuleiro, configuracao_estado):
    for navio, quantidade in configuracao_estado.items():
        tamanho = CONFIGURACAO[navio]
        for _ in range(quantidade):
            alocado = False
            while not alocado:
                imprimir_tabuleiro(tabuleiro, mostrar_navios=True)
                print(f"Alocando {navio} (tamanho {tamanho})")
                linha = int(input("Linha: ")) - 1
                coluna = ALFABETO.index(input("Coluna: ").upper())
                direcao = input("Direção (h/v): ")
                alocado = alocar_navio(tabuleiro, navio, (linha, coluna), 'horizontal' if direcao == 'h' else 'vertical', tamanho)
                if not alocado:
                    print("Não foi possível alocar o navio. Tente novamente.")

def atacar(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 'N':  # 'N' representa um navio
        tabuleiro[linha][coluna] = 'X'  # 'X' representa um navio atingido
        return CORES['vermelho'] + "Hit!" + CORES['reset']
    elif tabuleiro[linha][coluna] == '.':
        tabuleiro[linha][coluna] = 'O'  # 'O' representa água atingida
        return CORES['azul'] + "Miss!" + CORES['reset']
    return "Already attacked!"

def verificar_vitoria(tabuleiro):
    for linha in tabuleiro:
        if 'N' in linha:
            return False
    return True

def jogo():
    tamanho_tabuleiro = 10
    tabuleiro_usuario = criar_tabuleiro(tamanho_tabuleiro)
    tabuleiro_computador = criar_tabuleiro(tamanho_tabuleiro)
    
    estado_usuario = escolher_estado()
    alocar_navios_usuario(tabuleiro_usuario, PAISES[estado_usuario])

    while True:
        imprimir_tabuleiro(tabuleiro_usuario, mostrar_navios=True)
        linha = int(input("Escolha a linha para atacar: ")) - 1
        coluna = ALFABETO.index(input("Escolha a coluna para atacar: ").upper())
        resultado = atacar(tabuleiro_computador, linha, coluna)
        print(resultado)
        if verificar_vitoria(tabuleiro_computador):
            print("Parabéns! Você venceu!")
            break

        # Simulação de turno do computador (pode ser expandido)
        linha_computador = random.randint(0, tamanho_tabuleiro - 1)
        coluna_computador = random.randint(0, tamanho_tabuleiro - 1)
        resultado_computador = atacar(tabuleiro_usuario, linha_computador, coluna_computador)
        print(f"Computador ataca: {resultado_computador}")
        if verificar_vitoria(tabuleiro_usuario):
            print("Você perdeu. O computador venceu!")
            break

if __name__ == "__main__":
    jogo()
ksdgk
dflgkd
asdasd