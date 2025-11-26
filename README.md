# Editor de Texto com Estrutura de Dados Dinâmica 

Uma aplicação desktop simples desenvolvida em Python que demonstra a implementação prática de estruturas de dados dinâmicas (Listas Encadeadas e Pilhas) aplicadas a um cenário real de edição de texto com interface gráfica.

## Objetivo do Projeto

Este projeto tem como foco o estudo e validação de conceitos de **Big O** e manipulação de memória através de estruturas de dados.

> **Descrição Teórica:**
> O projeto implementa uma lista encadeada simples (adaptada aqui como Pilha para o histórico de ações) e estrutura a base para validações algorítmicas, como o **Insertion Sort**. O objetivo é demonstrar a inserção e manipulação de elementos (neste contexto, caracteres ou estados do editor) na posição correta.
>
> **Análise de Complexidade:**
> *   **Geral:** O(n²)
> *   **Melhor Caso (Parcialmente Ordenada):** O(n)

## Funcionalidades

A aplicação funciona como um editor de texto funcional com estética "Retrô", possuindo as seguintes características:

*   **Edição de Texto:** Adição de texto via campo de entrada (Input) sincronizado com a tecla `Enter`.
*   **Histórico de Ações (Undo/Redo):** Implementação de **Pilhas (Stacks)** baseadas em **Listas Encadeadas (Linked Lists)** para gerenciar o histórico de alterações (`Desfazer` e `Refazer`), permitindo navegação temporal no texto.
*   **Persistência:** Funcionalidade de salvar o arquivo em formato `.txt`.
*   **Interface Gráfica (GUI):** Interface construída com `Tkinter`.

## Estrutura do Projeto

*   `main.py`: Contém a lógica das estruturas de dados (`No`, `Pilha`) e a classe lógica do editor (`EditorTexto`). É o "cérebro" que manipula os dados em memória.
*   `editor_texto.py`: Contém a interface gráfica (`EditorTextoGUI`) e a integração com o usuário. É o ponto de entrada da aplicação.
---
## Integrantes  
| Nome                            | RA          | GitHub                             |
|---------------------------------|-------------|------------------------------------|
| Gustavo Costa Dias de Oliveira  | 10724112823 | https://github.com/gustavoocosta10 |
| José Gustavo de Almeida Alve    | 10724114382 | https://github.com/Gustavoaals     |
| Leonardo                        |             |                                    |
| Matheus Bernardo de souza| 10724114182 | https://github.com/code-matheu     |
| Rafaela Araujo Fontoura da Rosa | 10724112362 | https://github.com/RafaArauj       |
| Victor Emanoel Azevedo          | 10724116745 | https://github.com/vitumakonha     |

---


## Instalação e Como Rodar

Siga os passos abaixo para executar o projeto em sua máquina local.

### Pré-requisitos

*   Python 3.x instalado.

### Passo a Passo

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    git clone git@github.com:code-matheu/pilha-dinamica-a3-edaa.git
    cd pilha-dinamica-a3-edaa
    ```

2.  **Verifique os arquivos:**
    Certifique-se de que `main.py` e `editor_texto.py` estão na mesma pasta.

3.  **Execute a aplicação:**
    O arquivo principal que inicia a interface é o `editor_texto.py`. Execute-o através do terminal:

    ```bash
    python editor_texto.py
    ```

---

## Como Usar

1.  Ao abrir o editor, digite o texto desejado no campo inferior "Adicionar texto".
2.  Pressione `Enter` no teclado, ou, clique no botão **Adicionar**.
3.  Utilize os botões **Desfazer** e **Refazer** na barra inferior para testar a estrutura de Pilha Dinâmica.
4.  Clique em **Salvar** no menu superior para gravar seu trabalho em um arquivo `.txt`.
5.  Para encerrar, clique no botão **Sair**.

---
Desenvolvido para fins acadêmicos de validação de Estruturas de Dados e Algoritmos (EDAA).