import turtle
import tkinter as tk

# Dicionário de cores em português para inglês - a biblioteca turtle só reconhece as cores em inglês
cores_traduzidas = {
    "Vermelho": "red",
    "Azul": "blue",
    "Verde": "green",
    "Amarelo": "yellow",
    "Preto": "black",
    "Branco": "white",
    "Roxo": "purple",
    "Laranja": "orange"
}

# Função para desenhar a forma selecionada
def desenhar_forma():
    #pega as informações de forma e cores escolhidas no menu
    forma = forma_var.get()
    cor = cores_traduzidas.get(cor_var.get()) 

    #Configurações do desenho
    turtle.clearscreen()
    turtle.bgcolor("#f0f0f0")
    turtle.color(cor)
    turtle.speed(2)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.begin_fill()

    #Desenho das formas
    if forma == "Quadrado":
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif forma == "Triângulo":
        for _ in range(3):
            turtle.forward(100)
            turtle.left(120)
    elif forma == "Círculo":
        turtle.circle(50)

    turtle.end_fill()

# Interface gráfica
# Cria a janela principal
janela = tk.Tk()
janela.title("Draw.shapes")
janela.resizable(False, False)

# Define o tamanho fixo da janela
largura_janela = 400
altura_janela = 300

# Centraliza a janela na tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
janela.configure(bg="#dbeafe")

# Define o menu na janela
forma_var = tk.StringVar(value="")
cor_var = tk.StringVar(value="")

# Título
tk.Label(janela, text="Escolha uma forma e uma cor", font=("Helvetica", 16, "bold"), bg="#dbeafe").pack(pady=10)

# Ajuste de forma e cor da janela
frame_forma = tk.Frame(janela, bg="#dbeafe")
frame_forma.pack(pady=5)
tk.Label(frame_forma, text="Forma:", font=("Arial", 12), bg="#dbeafe").pack(side="left")
tk.OptionMenu(frame_forma, forma_var, "Quadrado", "Triângulo", "Círculo").pack(side="left")

frame_cor = tk.Frame(janela, bg="#dbeafe")
frame_cor.pack(pady=5)
tk.Label(frame_cor, text="Cor:", font=("Arial", 12), bg="#dbeafe").pack(side="left")
tk.OptionMenu(frame_cor, cor_var, *cores_traduzidas.keys()).pack(side="left")

# Botão "desenhar"
tk.Button(janela, text="Desenhar Forma", font=("Arial", 12, "bold"), bg="#2563eb", fg="white", padx=10, pady=5, command=desenhar_forma).pack(pady=15)

# Inicia o loop da interface
janela.mainloop()