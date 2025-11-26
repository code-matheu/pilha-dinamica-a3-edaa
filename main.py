class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

 # Implementa uma estrutura de dados fundamental de lista encadeada, insertion sort
 # usada para guardar o histórico de estados do texto. Cada vez que você altera algo, o estado anterior é "empilhado".
class Pilha:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def push(self, dado):
        novo = No(dado)
        novo.proximo = self.topo
        self.topo = novo

    def pop(self):
        if self.esta_vazia():
            return None
        dado = self.topo.dado
        self.topo = self.topo.proximo
        return dado

    def limpar(self):
        self.topo = None

# cérebro do editor
class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.undo = Pilha()
        self.redo = Pilha()

    def escrever(self, texto):
        # salva estado atual antes de alterar
        self.undo.push(self.texto)
        self.texto += texto

        # Toda nova ação limpa o redo
        self.redo.limpar()

    def apagar(self, n):
        self.undo.push(self.texto)
        self.texto = self.texto[:-n]
        self.redo.limpar()

    def desfazer(self):
        estado_anterior = self.undo.pop()
        if estado_anterior is not None:
            self.redo.push(self.texto)
            self.texto = estado_anterior

    def refazer(self):
        estado = self.redo.pop()
        if estado is not None:
            self.undo.push(self.texto)
            self.texto = estado

    def mostrar(self):
        return self.texto


editor = EditorTexto()
