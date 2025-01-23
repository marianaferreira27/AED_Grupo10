import customtkinter as ctk
from tkinter import messagebox
import CTkMessagebox

# Configurações iniciais
ctk.set_appearance_mode("System")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Cores: "blue", "dark-blue", "green"

# Lista global para armazenar os filmes
movies = []

# Função para atualizar a lista de filmes
def refresh_tree():
    for widget in tree_items_frame.winfo_children():
        widget.destroy()

    for index, movie in enumerate(movies):
        row_frame = ctk.CTkFrame(tree_items_frame)
        row_frame.pack(fill="x", pady=2)

        ctk.CTkLabel(row_frame, text=movie["title"], width=250, anchor="w").grid(row=0, column=0, padx=5)
        ctk.CTkLabel(row_frame, text=movie["genre"], width=250, anchor="w").grid(row=0, column=1, padx=5)
        ctk.CTkLabel(row_frame, text=str(movie["year"]), width=250, anchor="w").grid(row=0, column=2, padx=5)

        # Botão de remover
        remove_button = ctk.CTkButton(row_frame, text="Remover", command=lambda idx=index: remove_movie(idx))
        remove_button.grid(row=0, column=3, padx=5)

# Função para adicionar um filme
def add_movie():
    title = title_entry.get().strip()
    genre = genre_entry.get().strip()
    year = year_entry.get().strip()

    if not title or not genre or not year:
        CTkMessagebox.CTkMessagebox(title="Aviso!", message="Preencha Os Campos", icon="cancel", option_1="Ok")
        return

    try:
        year = int(year)
    except ValueError:
        CTkMessagebox.CTkMessagebox(title="Aviso!", message="O ano de lançamento deve ser um número.", icon="cancel", option_1="Ok")
        return

    movies.append({"title": title, "genre": genre, "year": year})
    refresh_tree()

    title_entry.delete(0, ctk.END)
    genre_entry.delete(0, ctk.END)
    year_entry.delete(0, ctk.END)

# Função para remover um filme
def remove_movie(index):
    if index < len(movies):
        del movies[index]
        refresh_tree()

# Função para criar o layout
def create_layout(root):
    root.title("Gerenciador de Filmes")
    root.geometry("800x600")

    # Título
    title_label = ctk.CTkLabel(root, text="Gerenciador de Filmes", text_color="Black", font=ctk.CTkFont(size=18, weight="bold"))
    title_label.pack(pady=10)

    # Frame do formulário
    form_frame = ctk.CTkFrame(root, fg_color="#5D0FE5")
    form_frame.pack(pady=20)

    ctk.CTkLabel(form_frame, text="Título:", text_color="White").grid(row=0, column=0, padx=5, pady=5)
    global title_entry
    title_entry = ctk.CTkEntry(form_frame, width=250)
    title_entry.grid(row=1, column=0, padx=5, pady=5)

    ctk.CTkLabel(form_frame, text="Gênero:", text_color="White").grid(row=2, column=0, padx=5, pady=5)
    global genre_entry
    genre_entry = ctk.CTkEntry(form_frame, width=250)
    genre_entry.grid(row=3, column=0, padx=5, pady=5)

    ctk.CTkLabel(form_frame, text="Ano de Lançamento:", text_color="White").grid(row=4, column=0, padx=5, pady=5)
    global year_entry
    year_entry = ctk.CTkEntry(form_frame, width=250)
    year_entry.grid(row=5, column=0, padx=5, pady=5)

    ctk.CTkButton(form_frame, text="Adicionar Filme", command=add_movie, text_color="White").grid(row=6, column=0, pady=10)

    # Lista de filmes
    global tree
    tree = ctk.CTkScrollableFrame(root, width=750, height=300)
    tree.pack(padx=10, pady=10, fill="both", expand=True)

    # Header da lista
    header_frame = ctk.CTkFrame(tree)
    header_frame.pack(fill="x")

    ctk.CTkLabel(header_frame, text="Título", width=250, anchor="w").grid(row=0, column=0, padx=5)
    ctk.CTkLabel(header_frame, text="Gênero", width=250, anchor="w").grid(row=0, column=1, padx=5)
    ctk.CTkLabel(header_frame, text="Ano de Lançamento", width=250, anchor="w").grid(row=0, column=2, padx=5)

    global tree_items_frame
    tree_items_frame = ctk.CTkFrame(tree)
    tree_items_frame.pack(fill="both", expand=True)

    # Botões de ação
    action_frame = ctk.CTkFrame(root)
    action_frame.pack(pady=10)

    ctk.CTkButton(action_frame, text="Remover Filme", command=lambda: remove_movie(0)).grid(row=0, column=0, padx=5)

# Execução principal
root = ctk.CTk()
create_layout(root)
root.mainloop()
