import customtkinter
from PIL import Image
import CTkMessagebox
import os

# Caminho para o arquivo onde os dados serão salvos
arquivo_usuarios = "files\utilizadores.txt"

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


def gerenciar_filmes():
    """
    Ao clicar no botão de "Gerenciar filmes" a aplicação abre o ficheiro backoffice.py.
    """

    tabview = customtkinter.CTkTabview(app, width=1000, height=500, fg_color="grey", bg_color="white")
    tabview.place(x=240, y=125)

    labelGerFilmes = customtkinter. CTkLabel(app, text="Gerenciar Filmes", bg_color="grey",
    text_color="white", font= ("Inter", 20))
    labelGerFilmes.place(x=280, y=125)

def gerenciar_utilizadores():
    """
    Ao clicar no botão de "Gerenciar filmes" a aplicação abre o ficheiro backoffice.py.
    """
    tabview = customtkinter.CTkTabview(app, width=1000, height=500, fg_color="grey", bg_color="white")
    tabview.place(x=240, y=125)

    labelGerUtilizadores = customtkinter. CTkLabel(app, text="Gerenciar Utilizadores", bg_color="grey",
    text_color="white", font= ("Inter", 20))
    labelGerUtilizadores.place(x=280, y=125)

def gerenciar_categorias():
    """
    Ao clicar no botão de "Gerenciar filmes" a aplicação abre o ficheiro backoffice.py.
    """
    tabview = customtkinter.CTkTabview(app, width=1000, height=500, fg_color="grey", bg_color="white")
    tabview.place(x=240, y=125)

    labelGerCategorias = customtkinter. CTkLabel(app, text="Gerenciar Categorias", bg_color="grey",
    text_color="white", font= ("Inter", 20))
    labelGerCategorias.place(x=280, y=125)

def gerenciar_notificacoes():
    """
    Ao clicar no botão de "Gerenciar filmes" a aplicação abre o ficheiro backoffice.py.
    """
    tabview = customtkinter.CTkTabview(app, width=1000, height=500, fg_color="grey", bg_color="white")
    tabview.place(x=240, y=125)

    labelGerNotificacoes = customtkinter. CTkLabel(app, text="Gerenciar Notificacoes", bg_color="grey",
    text_color="white", font= ("Inter", 20))
    labelGerNotificacoes.place(x=280, y=125)

def dashboard():
    """
    Ao clicar no botão de "Gerenciar filmes" a aplicação abre o ficheiro backoffice.py.
    """
    tabview = customtkinter.CTkTabview(app, width=1000, height=500, fg_color="grey", bg_color="white")
    tabview.place(x=240, y=125)

    labelDashboard = customtkinter. CTkLabel(app, text="Dashboard", bg_color="grey",
    text_color="white", font= ("Inter", 20))
    labelDashboard.place(x=280, y=125)

# -----Arranque da aplicação --------------------------------
# INTERFACE GRAFICA DA APLICAÇÃO 
app = customtkinter.CTk()  # invoca classe Ctk , cria a "main window"
renderWindow(1500, 700, "bigscreen")
app.configure(fg_color="#5D0FE5")

tabview = customtkinter.CTkTabview(app, width=1460, height=640, fg_color="white")
tabview.place(x=20, y=35)

labelAdmin = customtkinter. CTkLabel(app, text="ADMIN", fg_color="transparent",
text_color="white", font= ("Inter", 30, "bold"), bg_color="transparent")
labelAdmin.place(x=700, y=10)

btnGerFilmes = customtkinter. CTkButton(app, text="Gerenciar Filmes", command=gerenciar_filmes,
width=150, height=50, bg_color="white", fg_color="white", hover_color="", text_color="#39098B", corner_radius=11, font= ("Inter", 15))
btnGerFilmes.place(x=340, y=55)

btnGerUtilizadores = customtkinter. CTkButton(app, text="Gerenciar Utilizadores", command=gerenciar_utilizadores,
width=150, height=50, bg_color="white", fg_color="white", hover_color="", text_color="#39098B", corner_radius=11, font= ("Inter", 15))
btnGerUtilizadores.place(x=480, y=55)

btnGerCategorias = customtkinter. CTkButton(app, text="Gerenciar Categorias", command=gerenciar_categorias,
width=150, height=50, bg_color="white", fg_color="white", hover_color="", text_color="#39098B", corner_radius=11, font= ("Inter", 15))
btnGerCategorias.place(x=660, y=55)

btnGerNotificacoes = customtkinter. CTkButton(app, text="Gerenciar Notificações", command=gerenciar_notificacoes,
width=150, height=50, bg_color="white", fg_color="white", hover_color="", text_color="#39098B", corner_radius=11, font= ("Inter", 15))
btnGerNotificacoes.place(x=835, y=55)

btnDashboard = customtkinter. CTkButton(app, text="Dashboard", command=dashboard,
width=100, height=50, bg_color="white", fg_color="white", hover_color="", text_color="#39098B", corner_radius=11, font= ("Inter", 15))
btnDashboard.place(x=1020, y=55)

app.mainloop()