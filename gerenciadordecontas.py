import customtkinter as ctk
import CTkMessagebox
import os

# Configurações iniciais
ctk.set_appearance_mode("System")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Cores: "blue", "dark-blue", "green"

# Nome do arquivo para armazenar os utilizadores
FILE_NAME = "utilizadores.txt"

# Função para carregar os utilizadores do ficheiro
def load_users():
    users = {}
    if os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "r")
        for line in file:
            username, password = line.strip().split("|")
            users[username] = password
        file.close()
    return users

# Função para salvar os utilizadores no ficheiro
def save_users(users):
    file = open(FILE_NAME, "w")
    for username, password in users.items():
        file.write(f"{username}|{password}\n")
    file.close()

# Função para registrar um novo utilizador
def register_user():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        CTkMessagebox.CTkMessagebox(title="Aviso", message="Preencha todos os campos.", icon="cancel", option_1="Ok")
        return

    users = load_users()

    if username in users:
        CTkMessagebox.CTkMessagebox(title="Erro", message="Utilizador já existe.", icon="cancel", option_1="Ok")
        return

    users[username] = password
    save_users(users)
    refresh_user_list()
    CTkMessagebox.CTkMessagebox(title="Sucesso", message="Utilizador registrado com sucesso!", icon="check", option_1="Ok")

    username_entry.delete(0, ctk.END)
    password_entry.delete(0, ctk.END)

# Função para autenticar login
def login_user():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        CTkMessagebox.CTkMessagebox(title="Aviso", message="Preencha todos os campos.", icon="cancel", option_1="Ok")
        return

    users = load_users()

    if username in users and users[username] == password:
        CTkMessagebox.CTkMessagebox(title="Sucesso", message="Login realizado com sucesso!", icon="check", option_1="Ok")
    else:
        CTkMessagebox.CTkMessagebox(title="Erro", message="Credenciais inválidas.", icon="cancel", option_1="Ok")

# Função para apagar um utilizador
def delete_user():
    username = username_entry.get().strip()

    if not username:
        CTkMessagebox.CTkMessagebox(title="Aviso", message="Insira o nome do utilizador a ser apagado.", icon="cancel", option_1="Ok")
        return

    users = load_users()

    if username in users:
        del users[username]
        save_users(users)
        refresh_user_list()
        CTkMessagebox.CTkMessagebox(title="Sucesso", message="Utilizador apagado com sucesso!", icon="check", option_1="Ok")
    else:
        CTkMessagebox.CTkMessagebox(title="Erro", message="Utilizador não encontrado.", icon="cancel", option_1="Ok")

    username_entry.delete(0, ctk.END)
    password_entry.delete(0, ctk.END)

# Função para exibir a lista de utilizadores
def refresh_user_list():
    for widget in users_frame.winfo_children():
        widget.destroy()

    users = load_users()

    for username in users.keys():
        ctk.CTkLabel(users_frame, text=username).pack(anchor="w", padx=10, pady=2)

# Função para criar o layout da interface
def create_layout(root):
    root.title("Gerenciador de Utilizadores")
    root.geometry("400x600")

    # Título
    title_label = ctk.CTkLabel(root, text="Gerenciador de Utilizadores", text_color="Black", font=ctk.CTkFont(size=18, weight="bold"))
    title_label.pack(pady=10)

    # Frame do formulário
    form_frame = ctk.CTkFrame(root, fg_color="#5D0FE5")
    form_frame.pack(pady=20, padx=20, fill="x")

    ctk.CTkLabel(form_frame, text="Nome de Utilizador:", text_color="White").grid(row=0, column=0, padx=5, pady=5)
    global username_entry
    username_entry = ctk.CTkEntry(form_frame, width=250)
    username_entry.grid(row=1, column=0, padx=5, pady=5)

    ctk.CTkLabel(form_frame, text="Senha:", text_color="White").grid(row=2, column=0, padx=5, pady=5)
    global password_entry
    password_entry = ctk.CTkEntry(form_frame, show="*", width=250)
    password_entry.grid(row=3, column=0, padx=5, pady=5)

    # Botões de ação
    ctk.CTkButton(form_frame, text="Registrar", command=register_user, text_color="White").grid(row=4, column=0, pady=10)
    ctk.CTkButton(form_frame, text="Login", command=login_user, text_color="White").grid(row=5, column=0, pady=5)
    ctk.CTkButton(form_frame, text="Apagar Utilizador", command=delete_user, text_color="White").grid(row=6, column=0, pady=10)

    # Exibição de utilizadores
    users_title = ctk.CTkLabel(root, text="Utilizadores Registrados", font=ctk.CTkFont(size=14, weight="bold"))
    users_title.pack(pady=10)

    global users_frame
    users_frame = ctk.CTkFrame(root, fg_color="#FFFFFF")
    users_frame.pack(pady=10, padx=20, fill="both", expand=True)

    refresh_user_list()

# Execução principal
root = ctk.CTk()
create_layout(root)
root.mainloop()
