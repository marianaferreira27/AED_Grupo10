import customtkinter as ctk
import CTkMessagebox
import os
#isso é so uma função que envia uma
# notificação devemos simplismente mudar as variaveis para que sejam o mesmo dos que foram feito login na tela 
#principal logo essas variaveis tem de ser globais

# Nome do arquivo para armazenar os utilizadores
FILE_NAME = "utilizadores.txt"

# Função para carregar o utilizador e exibir uma mensagem de boas-vindas
def welcome_user():
    username = username_entry.get().strip()

    if not username:
        CTkMessagebox.CTkMessagebox(title="Aviso", message="Por favor, insira o nome de utilizador.", icon="cancel", option_1="Ok")
        return

    # Verifica se o ficheiro existe
    if not os.path.exists(FILE_NAME):
        CTkMessagebox.CTkMessagebox(title="Erro", message="O ficheiro de utilizadores não foi encontrado.", icon="cancel", option_1="Ok")
        return

    # Abre o ficheiro e procura pelo utilizador
    file = open(FILE_NAME, "r")
    found = False
    for line in file:
        saved_username, _ = line.strip().split("|")
        if saved_username == username:
            found = True
            break
    file.close()

    if found:
        CTkMessagebox.CTkMessagebox(title="Boas-vindas", message=f"Bem-vindo(a), {username}!", icon="check", option_1="Ok")
    else:
        CTkMessagebox.CTkMessagebox(title="Erro", message="Utilizador não encontrado.", icon="cancel", option_1="Ok")

# Função para criar o layout da interface
def create_layout(root):
    root.title("Verificação de Utilizador")
    root.geometry("400x300")

    # Título
    title_label = ctk.CTkLabel(root, text="Verificação de Utilizador", font=ctk.CTkFont(size=18, weight="bold"))
    title_label.pack(pady=10)

    # Frame do formulário
    form_frame = ctk.CTkFrame(root, fg_color="#5D0FE5")
    form_frame.pack(pady=20, padx=20, fill="x")

    ctk.CTkLabel(form_frame, text="Nome de Utilizador:", text_color="White").grid(row=0, column=0, padx=5, pady=5)
    global username_entry
    username_entry = ctk.CTkEntry(form_frame, width=250)
    username_entry.grid(row=1, column=0, padx=5, pady=5)

    # Botão para verificar e dar boas-vindas
    ctk.CTkButton(form_frame, text="Verificar Utilizador", command=welcome_user, text_color="White").grid(row=2, column=0, pady=10)

# Execução principal
root = ctk.CTk()
create_layout(root)
root.mainloop()