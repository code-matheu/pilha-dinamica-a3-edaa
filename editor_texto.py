import tkinter as tk
from tkinter import filedialog

# Classe que cria a janela visual e conecta os botões à lógica
class EditorTextoGUI:

    def __init__(self, text_editor):
        self.editor = text_editor
        self.root = tk.Tk()
        self.root.title("Editor de Texto")
        self.root.geometry("900x550")
        self.root.minsize(700, 450)
        self.root.configure(bg="#fdf6e3")

        self.filepath = None


        menu_bar = tk.Frame(self.root, bg="#eee8d5", height=26, relief="raised", bd=1)
        menu_bar.pack(fill="x")

        tk.Button(
            menu_bar,
            text="Salvar",
            bg="#eee8d5", # Mantendo o menu discreto
            activebackground="#e0e0e0",
            font=("MS Sans Serif", 9),
            padx=10,
            relief="flat",
            command=self.save
        ).pack(side="left")

        tk.Button(
            menu_bar,
            text="Sair",
            bg="#eee8d5",
            activebackground="#e0e0e0",
            font=("MS Sans Serif", 9),
            padx=10,
            relief="flat",
            command=self.root.destroy
        ).pack(side="left")

        tk.Frame(self.root, height=2, bg="#d3d0c8").pack(fill="x")


        editor_border = tk.Frame(self.root, bg="#d3d0c8") # Borda externa pastel
        editor_border.pack(fill="both", expand=True, padx=6, pady=6)

        inner_border = tk.Frame(editor_border, bg="#eee8d5", relief="sunken", bd=2)
        inner_border.pack(fill="both", expand=True)

        editor_frame = tk.Frame(inner_border)
        editor_frame.pack(fill="both", expand=True)

        scroll = tk.Scrollbar(editor_frame)
        scroll.pack(side="right", fill="y")

        self.text_widget = tk.Text(
            editor_frame,
            font=("Courier New", 12),
            wrap="word",
            yscrollcommand=scroll.set,
            relief="flat",
            padx=6,
            pady=6,
            bg="#e6f7ff",
            fg="#000000"
        )
        self.text_widget.pack(fill="both", expand=True)

        scroll.config(command=self.text_widget.yview)


        entry_frame = tk.Frame(self.root, bg="#eee8d5", relief="raised", bd=2)
        entry_frame.pack(fill="x", padx=0, pady=0, side="bottom")

        tk.Label(entry_frame, text="Adicionar texto:", bg="#eee8d5", fg="#555555",
                 font=("MS Sans Serif", 9)).pack(side="left", padx=8)

        self.entry = tk.Entry(entry_frame, font=("MS Sans Serif", 10), relief="sunken", bd=2, bg="#ffffff")
        self.entry.pack(side="left", fill="x", expand=True, padx=6, pady=4)

        # Sincroniza o ENTER do teclado com a função de adicionar
        self.entry.bind('<Return>', self.add_text_from_entry)

        self.entry_button = tk.Button(
            entry_frame,
            text="Adicionar",
            relief="raised",
            bd=3,
            bg="#fff9c4",
            activebackground="#fff59d",
            command=self.add_text_from_entry
        )
        self.entry_button.pack(side="right", padx=10)


        toolbar = tk.Frame(self.root, bg="#eee8d5", relief="raised", bd=2)
        toolbar.pack(fill="x", side="bottom")

        btn_style = {
            "font": ("MS Sans Serif", 9),
            "relief": "raised",
            "bd": 3,
            "padx": 8,
            "pady": 4,
            "bg": "#fff9c4",
            "activebackground": "#fff59d"
        }

        self.undo_button = tk.Button(toolbar, text="Desfazer", command=self.undo, **btn_style)
        self.undo_button.pack(side="left", padx=5)

        self.redo_button = tk.Button(toolbar, text="Refazer", command=self.redo, **btn_style)
        self.redo_button.pack(side="left", padx=5)

        self.newline_button = tk.Button(toolbar, text="Quebra", command=self.add_newline, **btn_style)
        self.newline_button.pack(side="left", padx=5)

        self.root.mainloop()

    # Pega o texto do input, manda a classe EditorTexto, processa e limpa o input
    def add_text_from_entry(self, _event=None):
        text = self.entry.get()
        self.editor.escrever(text)
        self.update_text()
        self.entry.delete(0, "end")

    def undo(self):
        self.editor.desfazer()
        self.update_text()

    def add_newline(self):
        self.editor.escrever("\n")
        self.update_text()

    def redo(self):
        self.editor.refazer()
        self.update_text()

    def save(self):
        self.filepath = filedialog.asksaveasfilename(defaultextension="txt")
        if self.filepath:
            with open(self.filepath, "w") as file:
                file.write(self.editor.mostrar())
    # Esta é a função de sincronia, apaga o conteúdo visual da tela (self.text_widget) e redesenha a partir da lógica (self.editor.mostrar())
    def update_text(self):
        self.text_widget.delete("1.0", "end")
        self.text_widget.insert("1.0", self.editor.mostrar())


from main import EditorTexto
editor = EditorTexto()
gui = EditorTextoGUI(editor)