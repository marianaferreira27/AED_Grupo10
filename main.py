import customtkinter
from PIL import Image, ImageTk
import CTkMessagebox
import os


# Caminho para o arquivo onde os dados serão salvos
arquivo_usuarios = ".\\files\\utilizadores.txt"

def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões# encontrar o 
    x = (screenWidth/2) - (appWidth/2)
    y= (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False)

def home():
    """
    Função com o layout da página inicial da aplicação
    """

    # Primeiro, destroi qualquer frame existente
    for widget in app.winfo_children():
        widget.destroy()

    # Renderiza a tela inicial
    labelBemVindo = customtkinter. CTkLabel(app, text="Bem-vindo ao", fg_color="transparent",
    text_color="white", font= ("Inter", 35, "bold"))
    labelBemVindo.place(x=625, y=200)

    labelBemVindo = customtkinter. CTkLabel(app, text="BigScreen", fg_color="transparent",
    text_color="white", font= ("Inter", 45, "bold"))
    labelBemVindo.place(x=635, y=240)

    btnSubscrever = customtkinter. CTkButton(app, text="Criar conta", command=criar_conta,
    width=150, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font= ("Inter", 15))
    btnSubscrever.place(x=675, y=400)

    btnIniciarSessao = customtkinter. CTkButton(app, text="Iniciar sessão", command=iniciar_sessao,
    width=150, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font= ("Inter", 15))
    btnIniciarSessao.place(x=675, y=470)

    btnIniciarSemConta = customtkinter. CTkButton(app, text="Entrar sem conta", command=abrir_sem_login,
    width=150, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font= ("Inter", 15))
    btnIniciarSemConta.place(x=675, y=540)

def lerUsers():
    """
    Lê o ficheiro de utilizadores.txt
    """
    fileUsers=open(arquivo_usuarios, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    fileUsers.close()
    return listaUsers

def criar_conta():
    """
    Função com o frame da parte de criar conta para os utilizadores.
    """

    def salvar_usuario():
        email = TxtEmail.get("1.0", "end").strip()  # Obtém o texto do campo
        conf_email = TxtConfEmail.get("1.0", "end").strip()
        password = TxtPalavraPasse.get("1.0", "end").strip()
        nome = TxtNomeProprio.get("1.0", "end").strip()
        apelido = TxtApelido.get("1.0", "end").strip()

        if not email or not conf_email or not password or not nome or not apelido:
            CTkMessagebox.CTkMessagebox(title="Erro", message="Todos os campos são obrigatórios.", icon="cancel")
            return

        if email != conf_email:
            CTkMessagebox.CTkMessagebox(title="Erro", message="Os e-mails não coincidem.", icon="cancel")
            return

        lista_users = lerUsers()
        for linha in lista_users:
            if linha.split(";")[0] == email:
                CTkMessagebox.CTkMessagebox(title="Erro", message="Já existe um utilizador com esse e-mail.", icon="cancel")
                return

        # Salvar o novo usuário no arquivo
        with open(arquivo_usuarios, "a", encoding="utf-8") as file_users:
            linha = f"{email};{password};{nome};{apelido}\n"
            file_users.write(linha)

        app.destroy()
        os.system("python users_login.py")

    frameGerir = customtkinter.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
    frameGerir.place(x=0, y=0)

    labelCriarConta = customtkinter.CTkLabel(app, text="Criar conta", fg_color="transparent",
                                             text_color="white", font=("Inter", 30, "bold"))
    labelCriarConta.place(x=650, y=90)

    labelAsterisco = customtkinter.CTkLabel(app, text="O asterisco * indica um campo obrigatório", fg_color="transparent",
                                            text_color="white", font=("Inter", 10))
    labelAsterisco.place(x=635, y=130)

    labelEndEmail = customtkinter.CTkLabel(app, text="Endereço de e-mail*", fg_color="transparent",
                                           text_color="white", font=("Inter", 15))
    labelEndEmail.place(x=590, y=180)

    TxtEmail = customtkinter.CTkTextbox(app, width=300, height=40, border_color="gray")
    TxtEmail.place(x=590, y=210)

    labelConfEmail = customtkinter.CTkLabel(app, text="Confirmar o endereço de e-mail*", fg_color="transparent",
                                            text_color="white", font=("Inter", 15))
    labelConfEmail.place(x=590, y=260)

    TxtConfEmail = customtkinter.CTkTextbox(app, width=300, height=40, border_color="gray")
    TxtConfEmail.place(x=590, y=290)

    labelPalavraPasse = customtkinter.CTkLabel(app, text="Palavra-passe*", fg_color="transparent",
                                               text_color="white", font=("Inter", 15))
    labelPalavraPasse.place(x=590, y=340)

    TxtPalavraPasse = customtkinter.CTkTextbox(app, width=300, height=40, border_color="gray")
    TxtPalavraPasse.place(x=590, y=370)

    labelNomeProprio = customtkinter.CTkLabel(app, text="Nome próprio*", fg_color="transparent",
                                              text_color="white", font=("Inter", 15))
    labelNomeProprio.place(x=590, y=420)

    TxtNomeProprio = customtkinter.CTkTextbox(app, width=300, height=40, border_color="gray")
    TxtNomeProprio.place(x=590, y=450)

    labelApelido = customtkinter.CTkLabel(app, text="Apelido*", fg_color="transparent",
                                          text_color="white", font=("Inter", 15))
    labelApelido.place(x=590, y=500)

    TxtApelido = customtkinter.CTkTextbox(app, width=300, height=40, border_color="gray")
    TxtApelido.place(x=590, y=530)

    btnCriarConta = customtkinter.CTkButton(app, text="Criar conta", command=salvar_usuario,
                                            width=150, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font=("Inter", 15))
    btnCriarConta.place(x=740, y=600)

    btnVoltar = customtkinter.CTkButton(app, text="Voltar", command=home,
                                        width=140, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font=("Inter", 15))
    btnVoltar.place(x=590, y=600)


def iniciar_sessao():
    """
    Função com o frame da parte de iniciar sessão, tanto para admins como para utilizadores.
    """

    def exibir_admin_frame():
        """
        Exibe o frame para o administrador após login bem-sucedido.
        """
        for widget in app.winfo_children():
            widget.destroy()

        # Criação do frame para o administrador
        frameAdmin = customtkinter.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
        frameAdmin.place(x=0, y=0)

        labelAdmin = customtkinter.CTkLabel(frameAdmin, text="Painel do Administrador", fg_color="transparent",
                                            text_color="white", font=("Inter", 30, "bold"))
        labelAdmin.place(x=640, y=90)

        btnGerenciarFilmes = customtkinter.CTkButton(frameAdmin, text="Gerenciar Filmes", command=gerenciar_filmes,
                                                     width=200, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font=("Inter", 15))
        btnGerenciarFilmes.place(x=590, y=200)

        btnGerenciarUtilizadores = customtkinter.CTkButton(frameAdmin, text="Gerenciar Utilizadores", command=gerenciar_utilizadores,
                                                           width=200, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font=("Inter", 15))
        btnGerenciarUtilizadores.place(x=590, y=300)

        btnGerenciarCategorias = customtkinter.CTkButton(frameAdmin, text="Gerenciar Categorias", command=gerenciar_categorias,
                                                         width=200, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font=("Inter", 15))
        btnGerenciarCategorias.place(x=590, y=400)

        btnSair = customtkinter.CTkButton(frameAdmin, text="Sair", command=home,
                                          width=200, height=50, fg_color="white", text_color="#FF0000", corner_radius=11, font=("Inter", 15))
        btnSair.place(x=590, y=500)

    def exibir_user_frame():
        """
        Exibe o frame para usuários após login bem-sucedido.
        """
        for widget in app.winfo_children():
            widget.destroy()

        # Criação do frame para o usuário
        frameUser = customtkinter.CTkFrame(app, width=1500, height=700, fg_color="#39098B")
        frameUser.place(x=0, y=0)

        labelUser = customtkinter.CTkLabel(frameUser, text="Bem-vindo ao Sistema!", fg_color="transparent",
                                           text_color="white", font=("Inter", 30, "bold"))
        labelUser.place(x=640, y=90)

        btnExplorar = customtkinter.CTkButton(frameUser, text="Explorar Filmes", command=explorar_filmes,
                                              width=200, height=50, fg_color="white", text_color="#5D0FE5", corner_radius=11, font=("Inter", 15))
        btnExplorar.place(x=590, y=200)

        btnSair = customtkinter.CTkButton(frameUser, text="Sair", command=home,
                                          width=200, height=50, fg_color="white", text_color="#FF0000", corner_radius=11, font=("Inter", 15))
        btnSair.place(x=590, y=300)

    def verificar_login():
        email = TxtEmail.get("1.0", "end").strip()
        password = TxtPalavraPasse.get("1.0", "end").strip()

        if not email or not password:
            CTkMessagebox.CTkMessagebox(title="Erro", message="Todos os campos são obrigatórios.", icon="cancel")
            return

        # Verifica se é o admin
        if email == "admin" and password == "admin":
            CTkMessagebox.CTkMessagebox(title="Admin", message="Bem-vindo, Admin!", icon="check", option_1="Ok")
            exibir_admin_frame()  # Chama a função para exibir o frame de administração
            return

        lista_users = lerUsers()
        for linha in lista_users:
            campos = linha.strip().split(";")
            if len(campos) >= 2 and campos[0] == email and campos[1] == password:
                CTkMessagebox.CTkMessagebox(title="Sucesso", message="Login realizado com sucesso!", icon="check", option_1="Ok")
                exibir_user_frame()  # Chama a função para exibir o frame do usuário
                return

        # Se não encontrar usuário válido, exibe mensagem de erro
        CTkMessagebox.CTkMessagebox(title="Erro", message="E-mail ou senha incorretos.", icon="cancel")

    # Frame de login
    frameIniciarSessao = customtkinter.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
    frameIniciarSessao.place(x=0, y=0)

    labelIniciarSessao = customtkinter.CTkLabel(app, text="Iniciar Sessão", fg_color="transparent",
                                                text_color="white", font=("Inter", 30, "bold"))
    labelIniciarSessao.place(x=640, y=90)

    labelEndEmail = customtkinter.CTkLabel(app, text="Endereço de e-mail*", fg_color="transparent",
                                           text_color="white", font=("Inter", 15))
    labelEndEmail.place(x=590, y=180)

    TxtEmail = customtkinter.CTkTextbox(app, width=300, height=40, border_color="gray")
    TxtEmail.place(x=590, y=210)

    labelPalavraPasse = customtkinter.CTkLabel(app, text="Palavra-passe*", fg_color="transparent",
                                               text_color="white", font=("Inter", 15))
    labelPalavraPasse.place(x=590, y=260)

    TxtPalavraPasse = customtkinter.CTkTextbox(app, width=300, height=40, border_color="gray")
    TxtPalavraPasse.place(x=590, y=290)

    btnVoltar = customtkinter.CTkButton(app, text="Voltar", command=home,
                                        width=140, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font=("Inter", 15))
    btnVoltar.place(x=590, y=450)

    btnIniciarSessao = customtkinter.CTkButton(app, text="Iniciar Sessão", command=verificar_login,
                                               width=140, height=50, fg_color="white", text_color="#39098B", corner_radius=11, font=("Inter", 15))
    btnIniciarSessao.place(x=750, y=450)

    
    

def abrir_sem_login():

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

    # Função para criar cada filme
    def create_movie_frame(parent, image_path, title, description, command):
        frame = customtkinter.CTkFrame(parent, width=200, height=400, corner_radius=15)
        frame.pack(side="left", padx=10, pady=10)
        frame.pack_propagate(False)

        image = Image.open(image_path).resize((200, 300))  # Carrega e redimensiona a imagem
        photo = ImageTk.PhotoImage(image)

        image_label = customtkinter.CTkLabel(frame, image=photo, text="")
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

        button = customtkinter.CTkButton(frame, text="Assistir agora", command=command)
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
    create_movie_frame(highlights_frame, "AED_GRUPO10-Mariana/images/sonic.png", "Sonic - O Filme", "Um ouriço azul veloz enfrenta desafios e inimigos.", lambda: print("Assistindo: Sonic - O Filme"))
    create_movie_frame(highlights_frame, "AED_GRUPO10-Mariana/images/mariojpg.jpg", "Super Mario Bros", "Mario e Luigi salvam o Reino dos Cogumelos.", lambda: print("Assistindo: Super Mario Bros"))
    create_movie_frame(highlights_frame, "AED_GRUPO10-Mariana/images/avatar.jpeg", "Avatar", "Uma nova jornada em Pandora cheia de aventuras.", lambda: print("Assistindo: Avatar"))
    create_movie_frame(highlights_frame, "AED_GRUPO10-Mariana/images/matrix.jpg", "Matrix", "Entre na Matrix e descubra a verdade oculta.", lambda: print("Assistindo: Matrix"))
    create_movie_frame(highlights_frame, "AED_GRUPO10-Mariana/images/batmanjpg.jpg", "Batman", "O herói sombrio enfrenta o caos em Gotham.", lambda: print("Assistindo: Batman"))

    # Adicionando filmes na seção "Recentemente Adicionados" 
    create_movie_frame(recently_added_frame, "AED_GRUPO10-Mariana/images/gladiadores.jpg", "Gladiador", "Um general romano busca vingança contra o imperador.", lambda: print("Assistindo: Gladiador"))
    create_movie_frame(recently_added_frame, "AED_GRUPO10-Mariana/images/frozen.jpg", "Frozen", "Uma princesa embarca numa aventura congelante.", lambda: print("Assistindo: Frozen"))
    create_movie_frame(recently_added_frame, "AED_GRUPO10-Mariana/images/Interstellarpng.png", "Interestelar", "Uma viagem para além das estrelas.", lambda: print("Assistindo: Interestelar"))
    create_movie_frame(recently_added_frame, "AED_GRUPO10-Mariana/images/vingadores.jpg", "Os Vingadores", "Os heróis se unem para salvar o mundo.", lambda: print("Assistindo: Os Vingadores"))
    create_movie_frame(recently_added_frame, "AED_GRUPO10-Mariana/images/Carros.jpg", "Carros", "Um carro de corrida aprende sobre a vida na Rota 66.", lambda: print("Assistindo: Carros"))

    # Adicionando filmes na seção "Populares" (sem listas)
    create_movie_frame(popular_frame, "AED_GRUPO10-Mariana/images/harrypotter.jpg", "Harry Potter", "A jornada de um jovem bruxo.", lambda: print("Assistindo: Harry Potter"))
    create_movie_frame(popular_frame, "AED_GRUPO10-Mariana/images/senhordosaneis.jpg", "O Senhor dos Anéis", "Uma missão para destruir o anel.", lambda: print("Assistindo: O Senhor dos Anéis"))
    create_movie_frame(popular_frame, "AED_GRUPO10-Mariana/images/Spiderman.jpg", "Homem-Aranha", "Um herói aprende a lidar com poderes e responsabilidades.", lambda: print("Assistindo: Homem-Aranha"))
    create_movie_frame(popular_frame, "AED_GRUPO10-Mariana/images/images.jpg", "Pantera Negra", "Um herói defende sua nação e legado.", lambda: print("Assistindo: Pantera Negra"))
    create_movie_frame(popular_frame, "AED_GRUPO10-Mariana/images/MulherMaravilha.jpg", "Mulher Maravilha", "A origem de uma poderosa guerreira.", lambda: print("Assistindo: Mulher Maravilha"))

    # Função para ajustar o scroll suave
    def smooth_scroll(event):
        scrollable_frame._scroll_canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    # Vincular o evento de rolagem do mouse ao frame scrollable
    scrollable_frame.bind("<MouseWheel>", smooth_scroll)

   

# -----Arranque da aplicação --------------------------------
# INTERFACE GRAFICA DA APLICAÇÃO 
app = customtkinter.CTk()  # invoca classe Ctk , cria a "main window"
renderWindow(1500, 700, "bigscreen")
app.configure(fg_color="#5D0FE5")
home()



app.mainloop()