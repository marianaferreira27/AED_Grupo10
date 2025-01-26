import customtkinter
from PIL import Image

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
    # App centrada no screen, em função das suas dimensões
    x = (screenWidth/2) - (appWidth/2)
    y= (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False)

def toggleMenu():
    """
    Alterna a visibilidade do menu lateral
    """
    global menu_visivel
    
    if menu_visivel:
        menuLateral.place_forget()
    else:
        menuLateral.place(x=0, y=40)

    menu_visivel = not menu_visivel

def mostrarHome():
    """
    Exibe a página inicial e esconde as outras.
    """
    framePerfil.place_forget()
    framePopulares.place_forget()
    frameRecentes.place_forget()

    frameHome.place(x=0, y=40)

def mostrarPerfil():
    """
    Exibe a página de perfil e esconde as outras.
    """
    frameHome.place_forget()
    framePopulares.place_forget()
    frameRecentes.place_forget()

    framePerfil.place(x=0, y=40)

def mostrarPopulares():
    """
    Exibe a página de populares e esconde as outras.
    """
    frameHome.place_forget()
    framePerfil.place_forget()
    frameRecentes.place_forget()

    framePopulares.place(x=0, y=40)

def mostrarRecentes():
    """
    Exibe a página de recentes e esconde as outras.
    """
    frameHome.place_forget()
    framePerfil.place_forget()
    framePopulares.place_forget()

    frameRecentes.place(x=0, y=40)

# -----Arranque da aplicação --------------------------------
# INTERFACE GRAFICA DA APLICAÇÃO 
app = customtkinter.CTk()
renderWindow(1500, 700, "bigscreen")
app.configure(fg_color="#5D0FE5")

# Frame "home"
frameHome = customtkinter.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
frameHomeLabel = customtkinter.CTkLabel(frameHome, text="Página Inicial", font=("Arial", 24), text_color="white")
frameHomeLabel.pack(padx=20, pady=20)

# Frame "perfil"
framePerfil = customtkinter.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
framePerfilLabel = customtkinter.CTkLabel(framePerfil, text="Página de Perfil", font=("Arial", 24), text_color="white")
framePerfilLabel.pack(padx=20, pady=20)

# Frame "populares"
framePopulares = customtkinter.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
framePopularesLabel = customtkinter.CTkLabel(framePopulares, text="Populares", font=("Arial", 24), text_color="white")
framePopularesLabel.pack(padx=20, pady=20)

# Frame "recentes"
frameRecentes = customtkinter.CTkFrame(app, width=1500, height=700, fg_color="#5D0FE5")
frameRecentesLabel = customtkinter.CTkLabel(frameRecentes, text="Recentes", font=("Arial", 24), text_color="white")
frameRecentesLabel.pack(padx=20, pady=20)

# Menu no topo
frameMenu = customtkinter.CTkFrame(app, width=1500, height=40, fg_color="black", corner_radius=0)
frameMenu.place(x=0, y=0)

# Imagem do cabeçalho
imageLabel = customtkinter.CTkImage(Image.open("images\\header.jpg"), size=(1500, 400))
labelImg = customtkinter.CTkLabel(app, image=imageLabel, text="", width=1500, height=400)
labelImg.place(x=0, y=40)

# Ícone do menu
imageMenu = customtkinter.CTkImage(Image.open("images\\icons\\menu.png"), size=(25, 25))
buttonMenu = customtkinter.CTkButton(
    app,
    image=imageMenu,
    text="",
    width=32,
    height=32,
    fg_color="black",
    hover_color="#444"
)
buttonMenu.place(x=10, y=5)

# Quando a imagem do menu for clicada, chama o toggleMenu
buttonMenu.configure(command=toggleMenu)

# Criação do menu lateral
menuLateral = customtkinter.CTkFrame(app, width=200, height=660, fg_color="#2C2F3F", corner_radius=0)

# Adicionando botões ao menu lateral
botaoHome = customtkinter.CTkButton(menuLateral, command=mostrarHome, text="Home", width=200, height=40, corner_radius=0, fg_color="#4D5B7C", hover_color="#6C7D8D")
botaoHome.grid(row=0, column=0, padx=0, pady=5)

botaoPerfil = customtkinter.CTkButton(menuLateral, command=mostrarPerfil, text="Perfil", width=200, height=40, corner_radius=0, fg_color="#4D5B7C", hover_color="#6C7D8D")
botaoPerfil.grid(row=1, column=0, padx=0, pady=5)

botaoPopulares = customtkinter.CTkButton(menuLateral, command=mostrarPopulares, text="Populares", width=200, height=40, corner_radius=0, fg_color="#4D5B7C", hover_color="#6C7D8D")
botaoPopulares.grid(row=2, column=0, padx=0, pady=5)

botaoRecentes = customtkinter.CTkButton(menuLateral, command=mostrarRecentes, text="Recentes", width=200, height=40, corner_radius=0, fg_color="#4D5B7C", hover_color="#6C7D8D")
botaoRecentes.grid(row=3, column=0, padx=0, pady=5)

botaoSair = customtkinter.CTkButton(menuLateral, text="Sair", width=200, height=40, corner_radius=0, fg_color="#4D5B7C", hover_color="#6C7D8D")
botaoSair.grid(row=4, column=0, padx=0, pady=5)

# Variável de controle para visibilidade do menu
menu_visivel = False

# Exibe a página inicial por padrão
mostrarHome()

# Iniciar a aplicação
app.mainloop()
