# Definir a função para encontrar o caminho
def encontrar_caminho(coordenadas, inicio, fim):
    fila = [inicio]
    visitados = set()
    pais = {}

    while fila:
        atual = fila.pop(0)
        if atual == fim:
            caminho = [atual]
            while atual in pais:
                atual = pais[atual]
                caminho.insert(0, atual)
            return caminho
        visitados.add(atual)
        lin, col = atual
        vizinhos = [(lin-1, col), (lin+1, col), (lin, col-1), (lin, col+1)]
        for vizinho in vizinhos:
            if vizinho in coordenadas and coordenadas[vizinho] not in ['#'] and vizinho not in visitados:
                fila.append(vizinho)
                pais[vizinho] = atual

    return None