class No:
    def __init__(self, dado): # O(1)
        self.dado = dado
        self.proximo = None

 # Implementa uma estrutura de dados fundamental de lista encadeada, insertion sort
 # usada para guardar o histórico de estados do texto. Cada vez que você altera algo, o estado anterior é "empilhado".
class Pilha:
    def __init__(self): # O(1)
        self.topo = None

    def esta_vazia(self): # O(1)
        return self.topo is None

    def push(self, dado): # O(1)
        novo = No(dado)
        novo.proximo = self.topo
        self.topo = novo

    def pop(self): # O(1)
        if self.esta_vazia():
            return None
        dado = self.topo.dado
        self.topo = self.topo.proximo
        return dado

    def limpar(self): # O(1)
        self.topo = None

# cérebro do editor
class EditorTexto:
    def __init__(self): # O(1)
        self.texto = ""
        self.undo = Pilha()
        self.redo = Pilha()

    def escrever(self, texto): # O(1)
        # salva estado atual antes de alterar
        self.undo.push(self.texto)
        self.texto += texto

        # Toda nova ação limpa o redo 
        self.redo.limpar() # O(1)

    def apagar(self, n): # O(1)
        self.undo.push(self.texto)
        self.texto = self.texto[:-n]
        self.redo.limpar()

    def desfazer(self): # O(1)
        estado_anterior = self.undo.pop()
        if estado_anterior is not None:
            self.redo.push(self.texto)
            self.texto = estado_anterior

    def refazer(self): # O(1)
        estado = self.redo.pop()
        if estado is not None:
            self.undo.push(self.texto)
            self.texto = estado

    def mostrar(self): # O(1)
        return self.texto


editor = EditorTexto() # O(1)
