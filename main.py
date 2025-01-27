import customtkinter
from PIL import Image
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

    def verificar_login():
        email = TxtEmail.get("1.0", "end").strip()
        password = TxtPalavraPasse.get("1.0", "end").strip()

        if not email or not password:
            CTkMessagebox.CTkMessagebox(title="Erro", message="Todos os campos são obrigatórios.", icon="cancel")
            return

        # Verifica se é o admin
        if email == "admin" and password == "admin":
            CTkMessagebox.CTkMessagebox(title="Admin", message="Bem-vindo, Admin!", icon="check", option_1="Ok")
            app.destroy()
            os.system("python admin.py")

        lista_users = lerUsers()
        for linha in lista_users:
            campos = linha.strip().split(";")
            if len(campos) >= 2 and campos[0] == email and campos[1] == password:
                app.destroy()
                os.system("python users_login.py")

        # Se não encontrar usuário válido, exibe mensagem de erro
        CTkMessagebox.CTkMessagebox(title="Erro", message="E-mail ou senha incorretos.", icon="cancel")

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
    """
    Ao clicar no botão de "Entrar sem conta" a aplicação com a frame "home" é destruída, e abre o ficheiro users_sem_login.py.
    Esse ficheiro é exclusivo para os usuários sem login/conta na aplicação, e, por conta disso, têm funcionalidades reduzidas.
    """
    app.destroy()
    os.system("python users_sem_login.py")


# -----Arranque da aplicação --------------------------------
# INTERFACE GRAFICA DA APLICAÇÃO 
app = customtkinter.CTk()  # invoca classe Ctk , cria a "main window"
renderWindow(1500, 700, "bigscreen")
app.configure(fg_color="#5D0FE5")
home()



app.mainloop()