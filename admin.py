import customtkinter
import customtkinter as ctk
from PIL import Image
import CTkMessagebox
import os
from tkinter import messagebox

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


def gerenciar_filmes():
    """
    Exibe a interface de Gerenciar Filmes dentro da área cinzenta (tabview).
    """
    tab_filmes = customtkinter.CTkTabview(app, width=1000, height=500, fg_color="grey", bg_color="white")
    tab_filmes.place(x=240, y=125)

    labelGerNotificacoes = customtkinter. CTkLabel(app, text="Gerenciar Notificacoes", bg_color="grey",
    text_color="white", font= ("Inter", 20))
    labelGerNotificacoes.place(x=280, y=125)

    # Limpa widgets existentes no tabview
    tabview = customtkinter.CTkTabview(app, width=1000, height=500, fg_color="grey", bg_color="white")
    tabview.place(x=240, y=125)

    # Adiciona um tab para "Filmes"
    tab_filmes = tabview.add("Gerenciar Filmes")

    # Adiciona a interface de MovieManagerApp dentro do tab_filmes
    movie_manager = MovieManagerApp(tab_filmes)


class MovieManagerApp:
    def __init__(self, root):
        self.movies = []
        self.file_path = ".\\files\\filmes.txt"

        # Carrega os filmes do arquivo no início
        self.load_movies_from_file()

        # Frame para o formulário de entrada
        form_frame = ctk.CTkFrame(root, fg_color="#5D0FE5", width=800, height=100)
        form_frame.pack(pady=10)

        ctk.CTkLabel(form_frame, text="Título:", text_color="White").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.title_entry = ctk.CTkEntry(form_frame, width=200)
        self.title_entry.grid(row=1, column=0, padx=5, pady=5)

        ctk.CTkLabel(form_frame, text="Gênero:", text_color="White").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.genre_entry = ctk.CTkEntry(form_frame, width=200)
        self.genre_entry.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(form_frame, text="Ano:", text_color="White").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.year_entry = ctk.CTkEntry(form_frame, width=100)
        self.year_entry.grid(row=1, column=2, padx=5, pady=5)

        ctk.CTkButton(form_frame, text="Adicionar", command=self.add_movie, text_color="White", width=100).grid(row=1, column=3, padx=10, pady=5)

        # Lista de filmes
        self.tree = ctk.CTkScrollableFrame(root, width=800, height=200, fg_color="white")
        self.tree.pack(padx=10, pady=10)

        # Header da lista
        header_frame = ctk.CTkFrame(self.tree, fg_color="lightgrey")
        header_frame.pack(fill="x")

        ctk.CTkLabel(header_frame, text="Título", width=200, anchor="w").grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkLabel(header_frame, text="Gênero", width=200, anchor="w").grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkLabel(header_frame, text="Ano", width=100, anchor="w").grid(row=0, column=2, padx=5, pady=5)

        self.tree_items_frame = ctk.CTkFrame(self.tree)
        self.tree_items_frame.pack(fill="both", expand=True)

        # Botões de ação
        action_frame = ctk.CTkFrame(root, fg_color="transparent")
        action_frame.pack(pady=10)

        ctk.CTkButton(action_frame, text="Remover Todos", command=self.remove_all_movies, text_color="White").pack(pady=5)

        # Atualiza a lista inicial de filmes
        self.refresh_tree()

    def load_movies_from_file(self):
        """Carrega filmes do arquivo."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    title, genre, year = line.strip().split(";")
                    self.movies.append({"title": title, "genre": genre, "year": int(year)})

    def save_movies_to_file(self):
        """Salva os filmes no arquivo."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            for movie in self.movies:
                file.write(f"{movie['title']};{movie['genre']};{movie['year']}\n")

    def refresh_tree(self):
        """Atualiza a exibição da lista de filmes."""
        # Limpa os itens atuais na lista
        for widget in self.tree_items_frame.winfo_children():
            widget.destroy()

        # Adiciona os filmes à lista
        for index, movie in enumerate(self.movies):
            row_frame = ctk.CTkFrame(self.tree_items_frame, fg_color="white")
            row_frame.pack(fill="x", pady=2)

            ctk.CTkLabel(row_frame, text=movie["title"], width=200, anchor="w").grid(row=0, column=0, padx=5)
            ctk.CTkLabel(row_frame, text=movie["genre"], width=200, anchor="w").grid(row=0, column=1, padx=5)
            ctk.CTkLabel(row_frame, text=str(movie["year"]), width=100, anchor="w").grid(row=0, column=2, padx=5)

            # Botão para remover o filme individualmente
            remove_button = ctk.CTkButton(row_frame, text="Remover", command=lambda idx=index: self.remove_movie(idx), width=100)
            remove_button.grid(row=0, column=3, padx=5)

    def add_movie(self):
        """Adiciona um filme à lista e ao arquivo."""
        title = self.title_entry.get().strip()
        genre = self.genre_entry.get().strip()
        year = self.year_entry.get().strip()

        if not title or not genre or not year:
            CTkMessagebox.CTkMessagebox(title="Aviso!", message="Preencha todos os campos.", icon="cancel", option_1="Ok")
            return

        try:
            year = int(year)
        except ValueError:
            CTkMessagebox.CTkMessagebox(title="Aviso!", message="O ano deve ser um número.", icon="cancel", option_1="Ok")
            return

        self.movies.append({"title": title, "genre": genre, "year": year})
        self.save_movies_to_file()  # Salva os dados no arquivo
        self.refresh_tree()

        self.title_entry.delete(0, ctk.END)
        self.genre_entry.delete(0, ctk.END)
        self.year_entry.delete(0, ctk.END)

    def remove_movie(self, index):
        """Remove um filme individualmente e atualiza o arquivo."""
        if index < len(self.movies):
            del self.movies[index]
            self.save_movies_to_file()  # Atualiza o arquivo
            self.refresh_tree()

    def remove_all_movies(self):
        """Remove todos os filmes e atualiza o arquivo."""
        self.movies.clear()
        self.save_movies_to_file()  # Atualiza o arquivo
        self.refresh_tree()

def gerenciar_utilizadores():
    """
    Exibe a interface de Gerenciar Utilizadores dentro da área cinzenta (tabview).
    """
    # Criação da aba/tabview
    tabview = customtkinter.CTkTabview(app, width=1000, height=500, fg_color="grey", bg_color="white")
    tabview.place(x=240, y=125)

    tab_utilizadores = tabview.add("Gerenciar Utilizadores")

    FILE_NAME = ".\\files\\utilizadores.txt"

    def load_users():
        users = {}
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                for line in file:
                    email, password, first_name, last_name = line.strip().split(";")
                    users[email] = {
                        "password": password,
                        "first_name": first_name,
                        "last_name": last_name
                    }
        return users

    def save_users(users):
        """Salva os utilizadores no arquivo."""
        with open(FILE_NAME, "w") as file:
            for email, data in users.items():
                file.write(f"{email};{data['password']};{data['first_name']};{data['last_name']}\n")

    def delete_user(email):
        """Apaga um utilizador e atualiza a lista."""
        users = load_users()
        if email in users:
            del users[email]
            save_users(users)
            refresh_user_list()
            CTkMessagebox.CTkMessagebox(title="Sucesso", message="Utilizador apagado com sucesso!", icon="check", option_1="Ok")
        else:
            CTkMessagebox.CTkMessagebox(title="Erro", message="Utilizador não encontrado.", icon="cancel", option_1="Ok")

    def refresh_user_list():
        """Atualiza a lista de utilizadores na interface."""
        # Limpa os widgets existentes no frame
        for widget in users_frame.winfo_children():
            widget.destroy()

        users = load_users()

        for email, data in users.items():
            user_frame = ctk.CTkFrame(users_frame, fg_color="#E0E0E0")
            user_frame.pack(fill="x", pady=5, padx=10)

            user_label = ctk.CTkLabel(user_frame, text=f"{data['first_name']} {data['last_name']} ({email})", anchor="w")
            user_label.pack(side="left", padx=10)

            delete_button = ctk.CTkButton(user_frame, text="Remover", width=100, fg_color="#FF4C4C", 
                                          command=lambda e=email: delete_user(e))
            delete_button.pack(side="right", padx=10)

    # Configuração da interface
    users_title = ctk.CTkLabel(tab_utilizadores, text="Utilizadores Registrados", 
                               font=ctk.CTkFont(size=14, weight="bold"), text_color="white")
    users_title.pack(pady=10)

    users_frame = ctk.CTkFrame(tab_utilizadores, fg_color="#FFFFFF")
    users_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # Atualiza a lista de utilizadores ao carregar
    refresh_user_list()



def gerenciar_categorias():
    """
    Exibe a interface de Gerenciar Categorias com base no arquivo "categorias2.txt" 
    e sincroniza categorias com "filmes.txt".
    """
    FILE_FILMES = ".\\files\\filmes.txt"
    FILE_CATEGORIAS = ".\\files\\categorias.txt"

    def sync_categories_from_filmes():
        """Sincroniza as categorias únicas do arquivo 'filmes.txt' para 'categorias.txt'."""
        categories = set()
        if os.path.exists(FILE_FILMES):
            with open(FILE_FILMES, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(";")
                    if len(parts) > 1:  # Certifica-se de que há um campo de categoria
                        categories.add(parts[1])

        # Adiciona as categorias ao arquivo 'categorias2.txt'
        with open(FILE_CATEGORIAS, "w", encoding="utf-8") as file:
            file.write("\n".join(sorted(categories)) + "\n")

    def load_categories():
        """Carrega as categorias do arquivo 'categorias.txt'."""
        categories = []
        if os.path.exists(FILE_CATEGORIAS):
            with open(FILE_CATEGORIAS, "r", encoding="utf-8") as file:
                categories = [line.strip() for line in file]
        return categories

    def save_new_category(category_name):
        """Adiciona uma nova categoria ao arquivo 'categorias.txt'."""
        categories = load_categories()
        if category_name not in categories:
            with open(FILE_CATEGORIAS, "a", encoding="utf-8") as file:
                file.write(f"{category_name}\n")
            refresh_category_list()
            CTkMessagebox.CTkMessagebox(title="Sucesso!", message=f"Categoria '{category_name}' adicionada com sucesso!", icon="check", option_1="Ok")
        else:
            CTkMessagebox.CTkMessagebox(title="Erro", message="Categoria já existe.", icon="cancel", option_1="Ok")

    def remove_category(category_name):
        """Remove uma categoria do arquivo 'categorias.txt'."""
        categories = load_categories()
        if category_name in categories:
            categories.remove(category_name)
            with open(FILE_CATEGORIAS, "w", encoding="utf-8") as file:
                file.write("\n".join(categories) + "\n")
            refresh_category_list()
            CTkMessagebox.CTkMessagebox(title="Sucesso!", message=f"Categoria '{category_name}' removida com sucesso!", icon="check", option_1="Ok")
        else:
            CTkMessagebox.CTkMessagebox(title="Erro", message="Categoria não encontrada.", icon="cancel", option_1="Ok")

    def refresh_category_list():
        """Atualiza a lista de categorias na interface."""
        # Limpa os widgets existentes no frame
        for widget in categories_frame.winfo_children():
            widget.destroy()

        categories = load_categories()

        for category in categories:
            category_frame = ctk.CTkFrame(categories_frame, fg_color="#E0E0E0")
            category_frame.pack(fill="x", pady=5, padx=10)

            category_label = ctk.CTkLabel(category_frame, text=category, anchor="w")
            category_label.pack(side="left", padx=10)

            delete_button = ctk.CTkButton(category_frame, text="Remover", width=100, fg_color="#FF4C4C", 
                                          command=lambda c=category: remove_category(c))
            delete_button.pack(side="right", padx=10)

    def add_category():
        """Adiciona uma nova categoria com base no campo de entrada."""
        category_name = category_entry.get().strip()
        if not category_name:
            CTkMessagebox.CTkMessagebox(title="Aviso", message="O nome da categoria não pode estar vazio.", icon="warning", option_1="Ok")
            return

        save_new_category(category_name)
        category_entry.delete(0, ctk.END)

    # Sincroniza categorias do arquivo 'filmes.txt' para 'categorias.txt'
    sync_categories_from_filmes()

    # Criação da aba/tabview
    tabview = customtkinter.CTkTabview(app, width=1000, height=500, fg_color="grey", bg_color="white")
    tabview.place(x=240, y=125)

    tab_categorias = tabview.add("Gerenciar Categorias")

    # Campo para adicionar novas categorias
    add_frame = ctk.CTkFrame(tab_categorias, fg_color="#5D0FE5")
    add_frame.pack(pady=10, padx=20, fill="x")

    category_label = ctk.CTkLabel(add_frame, text="Adicionar Categoria:", text_color="white")
    category_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    category_entry = ctk.CTkEntry(add_frame, width=300)
    category_entry.grid(row=0, column=1, padx=10, pady=5)

    add_button = ctk.CTkButton(add_frame, text="Adicionar", command=add_category, width=100, fg_color="#4CAF50", text_color="white")
    add_button.grid(row=0, column=2, padx=10, pady=5)

    # Exibição da lista de categorias
    categories_frame = ctk.CTkFrame(tab_categorias, fg_color="#FFFFFF")
    categories_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # Atualiza a lista de categorias ao carregar
    refresh_category_list()



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