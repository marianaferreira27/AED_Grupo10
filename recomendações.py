import customtkinter as ctk
import CTkMessagebox
import os

# Configurações iniciais
ctk.set_appearance_mode("System")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Cores: "blue", "dark-blue", "green"

# Nome do arquivo para armazenar os filmes
FILE_NAME = "filmes.txt"

# Lista de filmes disponíveis
available_movies = [
    {"filme": "Inception", "genero": "Sci-Fi", "descricao": "A mind-bending thriller about dreams within dreams."},
    {"filme": "The Godfather", "genero": "Crime", "descricao": "The story of a powerful mafia family."},
    {"filme": "Toy Story", "genero": "Animation", "descricao": "The adventures of toys that come to life."},
    {"filme": "The Dark Knight", "genero": "Action", "descricao": "Batman faces the Joker in a battle for Gotham."},
    {"filme": "Pulp Fiction", "genero": "Crime", "descricao": "Interwoven stories of crime and redemption."}
]

# Função para carregar os filmes do ficheiro
def load_movies():
    movies = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                usuario, filme, genero, rating = line.strip().split("|")
                movies.append({"usuario": usuario, "filme": filme, "genero": genero, "rating": float(rating)})
    return movies

# Função para salvar os filmes no ficheiro
def save_movie(usuario, filme, genero, rating):
    with open(FILE_NAME, "a") as file:
        file.write(f"{usuario}|{filme}|{genero}|{rating}\n")

# Função para recomendar filmes com base no gênero
def recommend_movies(genre):
    recommendations = [movie for movie in available_movies if movie["genero"] == genre]
    return recommendations

# Função para abrir detalhes do filme no aplicativo
def open_movie_details(frame, movie):
    for widget in frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(frame, text=movie['filme'], font=ctk.CTkFont(family="Inter", size=18, weight="bold"), text_color="white").pack(pady=5)
    ctk.CTkLabel(frame, text=f"Gênero: {movie['genero']}", font=ctk.CTkFont(family="Inter", size=14), text_color="white").pack(pady=5)
    ctk.CTkLabel(frame, text=movie['descricao'], font=ctk.CTkFont(family="Inter", size=14), text_color="white", wraplength=300, justify="left").pack(pady=10)

# Função para exibir os filmes recomendados
def display_recommendations(frame, genre_var, details_frame):
    for widget in frame.winfo_children():
        widget.destroy()

    genre = genre_var.get().strip()

    if not genre:
        CTkMessagebox.CTkMessagebox(title="Erro", message="Selecione um gênero.", icon="cancel", option_1="Ok")
        return

    recommendations = recommend_movies(genre)

    if not recommendations:
        ctk.CTkLabel(frame, text="Nenhum filme encontrado para este gênero.", text_color="white").pack(pady=10)
    else:
        for movie in recommendations:
            movie_label = ctk.CTkLabel(frame, text=f"{movie['filme']} ({movie['genero']})", font=ctk.CTkFont(family="Inter", size=14, weight="bold"), text_color="white", cursor="hand2")
            movie_label.pack(anchor="w", padx=5, pady=2)
            movie_label.bind("<Button-1>", lambda e, m=movie: open_movie_details(details_frame, m))

# Função para criar o layout da interface
def create_layout():
    app = ctk.CTk()  # Instanciando o customtkinter em uma função separada

    app.title("Sistema de Recomendação de Filmes")
    app.geometry("400x500")

    # Frame principal compacto
    main_frame = ctk.CTkFrame(app, fg_color="#5D0FE5")
    main_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Título
    title_label = ctk.CTkLabel(main_frame, text="Sistema de Recomendação de Filmes", text_color="white", font=ctk.CTkFont(family="Inter", size=30, weight="bold"))
    title_label.pack(pady=5)

    # Seletor de gênero
    ctk.CTkLabel(main_frame, text="Selecione um Gênero:", text_color="white", font=ctk.CTkFont(family="Inter", size=16)).pack(pady=5)
    genre_var = ctk.StringVar()
    genre_dropdown = ctk.CTkComboBox(main_frame, values=list(set([movie["genero"] for movie in available_movies])), variable=genre_var, width=200)
    genre_dropdown.pack(pady=5)

    # Botão para exibir recomendações
    ctk.CTkButton(main_frame, text="Recomendar", command=lambda: display_recommendations(recommendation_frame, genre_var, details_frame), text_color="white", fg_color="#39098B", font=ctk.CTkFont(family="Inter", size=14), width=100).pack(pady=10)

    # Frame para recomendações
    global recommendation_frame
    recommendation_frame = ctk.CTkFrame(main_frame, fg_color="#5D0FE5", height=150)
    recommendation_frame.pack(pady=10, padx=10, fill="both")

    # Frame para detalhes do filme
    global details_frame
    details_frame = ctk.CTkFrame(main_frame, fg_color="#5D0FE5", height=150)
    details_frame.pack(pady=10, padx=10, fill="both")

    app.mainloop()  # Iniciar o loop principal do aplicativo

# Execução principal
create_layout()  # Agora chamamos a função para criar e rodar a interface



