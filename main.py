from queue import PriorityQueue


class Agente:
    def __init__(self, grafo, inicio, objetivo):
        self.grafo = grafo
        self.inicio = inicio
        self.objetivo = objetivo

    def busca_custo_uniforme(self):
        fila_prioridade = PriorityQueue()
        fila_prioridade.put((0, self.inicio, []))
        visitados = set()

        while not fila_prioridade.empty():
            (custo, estado_atual, caminho_atual) = fila_prioridade.get()

            if estado_atual == self.objetivo:
                return caminho_atual + [estado_atual]

            if estado_atual in visitados:
                continue

            visitados.add(estado_atual)

            for proximo_estado in self.grafo[estado_atual]:
                custo_proximo_estado = self.grafo[estado_atual][proximo_estado]
                caminho_proximo_estado = caminho_atual + [estado_atual]
                fila_prioridade.put((custo + custo_proximo_estado, proximo_estado, caminho_proximo_estado))

        return None


grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

agente = Agente(grafo, 'A', 'D')
caminho = agente.busca_custo_uniforme()

if caminho is not None:
    print('Caminho encontrado: {}'.format(caminho))
else:
    print('Não foi possível encontrar um caminho.')
