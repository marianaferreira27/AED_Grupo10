import customtkinter
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Caminho para o arquivo onde os dados serão salvos
arquivo_usuarios = ".\\files\\utilizadores.txt"
favoritos = []
catalogo_filmes = ".\\files\\filmes.txt"

def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False)

def home():

    # Primeiro, destroi qualquer frame existente
    for widget in app.winfo_children():
        widget.destroy()

    # Configuração inicial do CustomTkinter
    customtkinter.set_appearance_mode("dark")  # Modo escuro
    customtkinter.set_default_color_theme("blue")  # Tema azul

    # Frame base com cor de fundo
    base_frame = customtkinter.CTkFrame(app, fg_color="#5D0FE5")
    base_frame.pack(fill="both", expand=True)

    # Título principal
    main_title_label = customtkinter.CTkLabel(
        base_frame,
        text="Big Screen Movies",
        font=customtkinter.CTkFont(size=24, weight="bold"),
        text_color="white"
    )
    main_title_label.pack(pady=10)

    # Scrollable Frame
    scrollable_frame = customtkinter.CTkScrollableFrame(base_frame, width=1100, height=600, fg_color="#5D0FE5")
    scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

    frame_topo = ctk.CTkFrame(app)
    frame_topo.pack(pady=10, padx=10, fill="x")

    btn_perfil = ctk.CTkButton(frame_topo, text="Perfil", command=pagina_perfil)
    btn_perfil.pack(side="right", padx=5)

    # Função para criar cada filme
    def create_movie_frame(parent, image_path, title, description):
        frame = customtkinter.CTkFrame(parent, width=200, height=400, corner_radius=15)
        frame.pack(side="left", padx=10, pady=10)
        frame.pack_propagate(False)

        try:
            image = Image.open(image_path).resize((200, 300))  # Carrega e redimensiona a imagem
            photo = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            photo = None

        image_label = customtkinter.CTkLabel(frame, image=photo, text="")
        if photo:
            image_label.image = photo  # Armazena a referência da imagem
        image_label.pack(pady=(10, 5))

        title_label = customtkinter.CTkLabel(frame, text=title, font=customtkinter.CTkFont(size=18, weight="bold"), text_color="white")
        title_label.pack(pady=(5, 0))

        description_label = customtkinter.CTkLabel(
            frame,
            text=description,
            font=customtkinter.CTkFont(size=14),
            wraplength=180,
            justify="center",
            text_color="white"
        )
        description_label.pack(pady=(5, 10))

        # Define o objeto do filme com as informações
        filme = {
            "titulo": title,
            "sinopse": description,
            "categoria": "Desconhecida",
            "lancamento": "Desconhecido",
            "avaliacoes": []
        }

        button = customtkinter.CTkButton(frame, text="Avalie agora", command=lambda: exibir_detalhes(filme))
        button.pack(pady=5)

        return frame

    # Função para criar seções dinâmicas de filmes
    def create_movie_section(parent, section_title):
        # Adiciona o título da seção
        section_label = customtkinter.CTkLabel(
            parent,
            text=section_title,
            font=customtkinter.CTkFont(size=35, weight="bold"),
            text_color="white",
            anchor="w"
        )
        section_label.pack(fill="x", pady=(10, 0))

        # Frame da seção
        section_frame = customtkinter.CTkFrame(parent, fg_color="#5D0FE5")
        section_frame.pack(fill="x", pady=10)

        return section_frame

    # Criando as seções
    highlights_frame = create_movie_section(scrollable_frame, "Destaques")
    recently_added_frame = create_movie_section(scrollable_frame, "Recentemente Adicionados")
    popular_frame = create_movie_section(scrollable_frame, "Populares")

    # Adicionando filmes na seção "Destaques"
    create_movie_frame(highlights_frame, "images/filmes/sonic.png", "Sonic - O Filme", "Um ouriço azul veloz enfrenta desafios e inimigos.")
    create_movie_frame(highlights_frame, "images/filmes/mariojpg.jpg", "Super Mario Bros", "Mario e Luigi salvam o Reino dos Cogumelos.")
    create_movie_frame(highlights_frame, "images/filmes/avatar.jpeg", "Avatar", "Uma nova jornada em Pandora cheia de aventuras.")
    create_movie_frame(highlights_frame, "images/filmes/matrix.jpg", "Matrix", "Entre na Matrix e descubra a verdade oculta.")
    create_movie_frame(highlights_frame, "images/filmes/batmanjpg.jpg", "Batman", "O herói sombrio enfrenta o caos em Gotham.")

    # Adicionando filmes na seção "Recentemente Adicionados"
    create_movie_frame(recently_added_frame, "images/filmes/gladiadores.jpg", "Gladiador", "Um general romano busca vingança contra o imperador.")
    create_movie_frame(recently_added_frame, "images/filmes/frozen.jpg", "Frozen", "Uma princesa embarca numa aventura congelante.")
    create_movie_frame(recently_added_frame, "images/filmes/Interstellarpng.png", "Interestelar", "Uma viagem para além das estrelas.")
    create_movie_frame(recently_added_frame, "images/filmes/vingadores.jpg", "Os Vingadores", "Os heróis se unem para salvar o mundo.")
    create_movie_frame(recently_added_frame, "images/filmes/Carros.jpg", "Carros", "Um carro de corrida aprende sobre a vida na Rota 66.")

    # Adicionando filmes na seção "Populares"
    create_movie_frame(popular_frame, "images/filmes/harrypotter.jpg", "Harry Potter", "A jornada de um jovem bruxo.")
    create_movie_frame(popular_frame, "images/filmes/senhordosaneis.jpg", "O Senhor dos Anéis", "Uma missão para destruir o anel.")
    create_movie_frame(popular_frame, "images/filmes/Spiderman.jpg", "Homem-Aranha", "Um herói aprende a lidar com poderes e responsabilidades.")
    create_movie_frame(popular_frame, "images/filmes/images.jpg", "Pantera Negra", "Um herói defende sua nação e legado.")
    create_movie_frame(popular_frame, "images/filmes/MulherMaravilha.jpg", "Mulher Maravilha", "A origem de uma poderosa guerreira.")

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

def carregar_filmes():
    """
    Lê o ficheiro de filmes e retorna uma lista de dicionários com os dados.
    Formato do ficheiro esperado:
    Título;Categoria;Lançamento;Sinopse
    """
    filmes = []
    if os.path.exists(catalogo_filmes):
        with open(catalogo_filmes, "r", encoding="utf-8") as f:
            for linha in f:
                dados = linha.strip().split(";")
                if len(dados) == 4:  # Certifica-se de que a linha tem os 4 campos
                    filmes.append({
                        "titulo": dados[0],
                        "categoria": dados[1],  # Categoria ainda é carregada, mas não exibida
                        "lancamento": dados[2],
                        "sinopse": dados[3]
                    })
    return filmes

def exibir_detalhes(filme):
    # Remove todos os widgets para exibir os detalhes do filme
    for widget in app.winfo_children():
        widget.destroy()

    frame_detalhes = ctk.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
    frame_detalhes.pack(fill="both", expand=True)

    # Título do filme
    label_titulo = ctk.CTkLabel(frame_detalhes, text=f"{filme['titulo']}", font=("Arial", 24), text_color="white")
    label_titulo.pack(pady=10)

    # Exibe a data de lançamento (campo [2])
    label_lancamento = ctk.CTkLabel(frame_detalhes, text=f"Lançamento: {filme['lancamento']}", font=("Arial", 18), text_color="white")
    label_lancamento.pack(pady=5)

    # Sinopse do filme
    label_sinopse = ctk.CTkLabel(frame_detalhes, text=f"Sinopse: {filme['sinopse']}", font=("Arial", 16), text_color="white", wraplength=700)
    label_sinopse.pack(pady=10)

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

    # Botão para voltar
    btn_voltar = ctk.CTkButton(frame_detalhes, text="Voltar", command=home, width=200)
    btn_voltar.pack(pady=20)

def adicionar_favorito(filme):
    if filme not in favoritos:
        favoritos.append(filme)
        salvar_dados()
        messagebox.showinfo("Favoritos", f"'{filme}' foi adicionado aos favoritos.")

# Inicia a aplicação
app = customtkinter.CTk()
renderWindow(1500, 700, "Big Screen Movies")
app.configure(fg_color="#5D0FE5")
home()
app.mainloop()
