import customtkinter
from PIL import Image
import CTkMessagebox
import os

# Caminho para o arquivo onde os dados serão salvos
arquivo_usuarios = "usuarios.txt"

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


# -----Arranque da aplicação --------------------------------
# INTERFACE GRAFICA DA APLICAÇÃO 
app = customtkinter.CTk()  # invoca classe Ctk , cria a "main window"
renderWindow(1500, 700, "bigscreen")
app.configure(fg_color="#5D0FE5")

framePagInicial = customtkinter.CTkFrame(app, width = 1500, height = 700, fg_color="#5D0FE5")
framePagInicial.place(x=0, y=0)

frameMenu = customtkinter.CTkFrame(app, width = 1500, height = 40, fg_color="black", corner_radius=0)
frameMenu.place(x=0, y=0)

imageLabel = customtkinter.CTkImage(Image.open("images\header.jpg"), size=(1500, 400))
labelImg = customtkinter.CTkLabel(app, image = imageLabel, text = "", width = 1500, height=400 )
labelImg.place(x= 0, y=40)

imageMenu = customtkinter.CTkImage(Image.open("images\icons\menu.png"), size=(25, 25))
labelMenu = customtkinter.CTkLabel(app, image = imageMenu, text = "", width = 32, height=32, fg_color="black")
labelMenu.place(x= 10, y=5)

imageUser = customtkinter.CTkImage(Image.open(r"images\icons\user.png"), size=(25, 25))
labelUser = customtkinter.CTkLabel(app, image = imageUser, text = "", width = 32, height=32, fg_color="black")
labelUser.place(x= 1455, y=5)

app.mainloop()