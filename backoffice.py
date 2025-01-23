import customtkinter as ctk
from tkinter import messagebox
import CTkMessagebox


class MovieManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Filmes")
        self.root.geometry("800x600")

        self.movies = []  # Lista para armazenar os filmes

        # Título
        title_label = ctk.CTkLabel(root, text="Gerenciador de Filmes", text_color="Black", font=ctk.CTkFont(size=18, weight="bold"))
        title_label.pack(pady=10)

        # Frame para o formulário de entrada
        form_frame = ctk.CTkFrame(root, fg_color="#5D0FE5")
        form_frame.pack(pady=20)

        ctk.CTkLabel(form_frame, text="Título:", text_color="White").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = ctk.CTkEntry(form_frame, width=250)
        self.title_entry.grid(row=1, column=0, padx=5, pady=5)

        ctk.CTkLabel(form_frame, text="Gênero:", text_color="White").grid(row=2, column=0, padx=5, pady=5)
        self.genre_entry = ctk.CTkEntry(form_frame, width=250)
        self.genre_entry.grid(row=3, column=0, padx=5, pady=5)

        ctk.CTkLabel(form_frame, text="Ano de Lançamento:", text_color="White").grid(row=4, column=0, padx=5, pady=5)
        self.year_entry = ctk.CTkEntry(form_frame, width=250)
        self.year_entry.grid(row=5, column=0, padx=5, pady=5)

        ctk.CTkButton(form_frame, text="Adicionar Filme", command=self.add_movie, text_color="White").grid(row=6, column=0, pady=10)

        # Lista de filmes
        self.tree = ctk.CTkScrollableFrame(root, width=750, height=300)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Header da lista
        header_frame = ctk.CTkFrame(self.tree)
        header_frame.pack(fill="x")

        ctk.CTkLabel(header_frame, text="Título", width=250, anchor="w").grid(row=0, column=0, padx=5)
        ctk.CTkLabel(header_frame, text="Gênero", width=250, anchor="w").grid(row=0, column=1, padx=5)
        ctk.CTkLabel(header_frame, text="Ano de Lançamento", width=250, anchor="w").grid(row=0, column=2, padx=5)

        self.tree_items_frame = ctk.CTkFrame(self.tree)
        self.tree_items_frame.pack(fill="both", expand=True)

        # Botões de ação
        action_frame = ctk.CTkFrame(root)
        action_frame.pack(pady=10)

        ctk.CTkButton(action_frame, text="Remover Filme", command=self.remove_movie).grid(row=0, column=0, padx=5)

    def refresh_tree(self):
        # Limpa os itens atuais na lista
        for widget in self.tree_items_frame.winfo_children():
            widget.destroy()

        # Adiciona os filmes à lista
        for index, movie in enumerate(self.movies):
            row_frame = ctk.CTkFrame(self.tree_items_frame)
            row_frame.pack(fill="x", pady=2)

            ctk.CTkLabel(row_frame, text=movie["title"], width=250, anchor="w").grid(row=0, column=0, padx=5)
            ctk.CTkLabel(row_frame, text=movie["genre"], width=250, anchor="w").grid(row=0, column=1, padx=5)
            ctk.CTkLabel(row_frame, text=str(movie["year"]), width=250, anchor="w").grid(row=0, column=2, padx=5)

            # Botão para selecionar o filme
            remove_button = ctk.CTkButton(row_frame, text="Remover", command=lambda idx=index: self.remove_movie(idx))
            remove_button.grid(row=0, column=3, padx=5)

    def add_movie(self):
        title = self.title_entry.get().strip()
        genre = self.genre_entry.get().strip()
        year = self.year_entry.get().strip()

        if not title or not genre or not year:
            CTkMessagebox.CTkMessagebox(title="Aviso!", message="Preencha Os Campos", icon="cancel", option_1="Ok")
            return

        try:
            year = int(year)
        except ValueError:
            CTkMessagebox.CTkMessagebox(title="Aviso!", message="O ano de lançamento deve ser um número.", icon="cancel", option_1="Ok")
            return

        self.movies.append({"title": title, "genre": genre, "year": year})
        self.refresh_tree()

        self.title_entry.delete(0, ctk.END)
        self.genre_entry.delete(0, ctk.END)
        self.year_entry.delete(0, ctk.END)

    def remove_movie(self, index):
        if index < len(self.movies):
            del self.movies[index]
            self.refresh_tree()

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modos: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Cores: "blue", "dark-blue", "green"

    root = ctk.CTk()
    app = MovieManagerApp(root)
    root.mainloop()
