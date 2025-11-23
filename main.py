class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


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

editor.escrever("Olá")
print(editor.mostrar())
editor.escrever(" Mundo")
print(editor.mostrar())  # Olá Mundo

editor.desfazer()
print(editor.mostrar())  # Olá

editor.refazer()
print(editor.mostrar())  # Olá Mundo

editor.apagar(5)
print(editor.mostrar())  # Olá
editor.desfazer()
print(editor.mostrar()) # Olá Mundo
editor.desfazer()
print(editor.mostrar())
editor.desfazer()
print(editor.mostrar())
