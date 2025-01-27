import customtkinter as ctk
from tkinter import messagebox
import os

# Caminho para o arquivo onde os dados serão salvos
ARQUIVO_DADOS = "dados_usuarios.txt"
ARQUIVO_FILMES = "filmes.txt"

# Dados simulados
catalogo_filmes = [
    {"titulo": "Filme 1", "categoria": "Terror", "sinopse": "Sinopse do Filme 1", "lancamento": "2023-01-01", "avaliacoes": []},
    {"titulo": "Filme 2", "categoria": "Comédia", "sinopse": "Sinopse do Filme 2", "lancamento": "2022-12-01", "avaliacoes": []},
    {"titulo": "Filme 3", "categoria": "Ação", "sinopse": "Sinopse do Filme 3", "lancamento": "2021-07-15", "avaliacoes": []},
    {"titulo": "Filme 4", "categoria": "Comédia", "sinopse": "Sinopse do Filme 4", "lancamento": "2020-09-10", "avaliacoes": []},
    {"titulo": "Filme 5", "categoria": "Terror", "sinopse": "Sinopse do Filme 5", "lancamento": "2019-10-31", "avaliacoes": []}
]
favoritos = []

# Função para salvar dados no arquivo
def salvar_dados():
    with open(ARQUIVO_DADOS, "w") as f:
        f.write("Favoritos:" + ",".join(favoritos) + "\n")

# Função para carregar dados do arquivo
def carregar_dados():
    global favoritos
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            linhas = f.readlines()
            for linha in linhas:
                if linha.startswith("Favoritos:"):
                    favoritos = linha.replace("Favoritos:", "").strip().split(",")

# Função para exibir detalhes do filme
def exibir_detalhes(filme):
    for widget in app.winfo_children():
        widget.destroy()

    frame_detalhes = ctk.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
    frame_detalhes.pack(fill="both", expand=True)

    label_titulo = ctk.CTkLabel(frame_detalhes, text=f"{filme['titulo']}", font=("Arial", 24), text_color="white")
    label_titulo.pack(pady=10)

    label_categoria = ctk.CTkLabel(frame_detalhes, text=f"Categoria: {filme['categoria']}", font=("Arial", 18), text_color="white")
    label_categoria.pack(pady=5)

    label_lancamento = ctk.CTkLabel(frame_detalhes, text=f"Lançamento: {filme['lancamento']}", font=("Arial", 18), text_color="white")
    label_lancamento.pack(pady=5)

    label_sinopse = ctk.CTkLabel(frame_detalhes, text=f"Sinopse: {filme['sinopse']}", font=("Arial", 16), text_color="white", wraplength=700)
    label_sinopse.pack(pady=10)

    media_avaliacao = sum(filme['avaliacoes']) / len(filme['avaliacoes']) if filme['avaliacoes'] else 0
    label_avaliacao = ctk.CTkLabel(frame_detalhes, text=f"Avaliação Média: {media_avaliacao:.1f}", font=("Arial", 18), text_color="white")
    label_avaliacao.pack(pady=5)

    def avaliar(nota):
        filme['avaliacoes'].append(nota)
        messagebox.showinfo("Avaliação", f"Você avaliou '{filme['titulo']}' com nota {nota}.")
        exibir_detalhes(filme)

    frame_avaliar = ctk.CTkFrame(frame_detalhes)
    frame_avaliar.pack(pady=10)

    label_avaliar = ctk.CTkLabel(frame_avaliar, text="Avaliar: ", font=("Arial", 16), text_color="white")
    label_avaliar.pack(side="left", padx=5)

    for i in range(1, 6):
        btn_avaliar = ctk.CTkButton(frame_avaliar, text=str(i), command=lambda nota=i: avaliar(nota), width=40)
        btn_avaliar.pack(side="left", padx=2)

    btn_favorito = ctk.CTkButton(frame_detalhes, text="Adicionar aos Favoritos", command=lambda: adicionar_favorito(filme['titulo']), width=200, fg_color="white", text_color="#39098B")
    btn_favorito.pack(pady=10)

    btn_voltar = ctk.CTkButton(frame_detalhes, text="Voltar para o Catálogo", command=carregar_pagina_inicial, width=200, fg_color="white", text_color="#39098B")
    btn_voltar.pack(pady=20)

# Função para adicionar filme aos favoritos
def adicionar_favorito(filme):
    if filme not in favoritos:
        favoritos.append(filme)
        salvar_dados()
        messagebox.showinfo("Favoritos", f"'{filme}' foi adicionado aos favoritos.")

# Função para atualizar catálogo com filmes filtrados
def atualizar_catalogo(filmes):
    for widget in frame_catalogo.winfo_children():
        widget.destroy()

    for filme in filmes:
        btn_filme = ctk.CTkButton(frame_catalogo, text=f"{filme['titulo']} ({filme['categoria']})", command=lambda f=filme: exibir_detalhes(f))
        btn_filme.pack(pady=5)

# Página de perfil do usuário
def pagina_perfil():
    for widget in app.winfo_children():
        widget.destroy()

    frame_perfil = ctk.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
    frame_perfil.pack(fill="both", expand=True)

    label_titulo = ctk.CTkLabel(frame_perfil, text="Perfil do Usuário", font=("Arial", 24), text_color="white")
    label_titulo.pack(pady=20)

    label_favoritos = ctk.CTkLabel(frame_perfil, text="Filmes Favoritos:", font=("Arial", 18), text_color="white")
    label_favoritos.pack(pady=10)

    for favorito in favoritos:
        label_fav = ctk.CTkLabel(frame_perfil, text=favorito, font=("Arial", 16), text_color="white")
        label_fav.pack(pady=5)

    btn_voltar = ctk.CTkButton(frame_perfil, text="Voltar para Início", command=carregar_pagina_inicial, width=140, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font=("Inter", 15))
    btn_voltar.pack(pady=20)

# Função para carregar a página inicial
def carregar_pagina_inicial():
    for widget in app.winfo_children():
        widget.destroy()

    inicializar_interface()

# Função para inicializar a interface principal
def inicializar_interface():
    global frame_topo, frame_catalogo

    frame_topo = ctk.CTkFrame(app)
    frame_topo.pack(pady=10, padx=10, fill="x")

    combobox_categoria = ctk.CTkComboBox(frame_topo, values=["Todos"] + list(set([f["categoria"] for f in catalogo_filmes])))
    combobox_categoria.set("Todos")
    combobox_categoria.pack(side="left", padx=5)

    btn_filtrar = ctk.CTkButton(frame_topo, text="Filtrar", command=lambda: filtrar_filmes(combobox_categoria.get()))
    btn_filtrar.pack(side="left", padx=5)

    btn_perfil = ctk.CTkButton(frame_topo, text="Perfil", command=pagina_perfil)
    btn_perfil.pack(side="right", padx=5)

    frame_catalogo = ctk.CTkFrame(app)
    frame_catalogo.pack(pady=10, padx=10, fill="both", expand=True)

    atualizar_catalogo(catalogo_filmes)

# Interface principal
app = ctk.CTk()
app.geometry("800x600")
carregar_dados()

inicializar_interface()
app.mainloop()