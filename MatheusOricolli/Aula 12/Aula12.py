#TKINTER

#Componentes Widgets
# tk: Tk() # Janela
# lb: Label() # Rótulo
# bt: Button() # Botão
# et: Entry() # Caixa de texto 

import tkinter as tk
from tkinter import messagebox

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha primeira Janela GUI")
janela.configure(bg="#C8A2C8") #Cor de fundo
janela.geometry("400x200") #Largura x Altura

#2 . Criar a função do botão (Evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão")

# 3. Criar os componentes
lbl_titulo = tk.Label(janela, text="Bem-Vindo a nossa aula de Tkinter", font=("Arial", 14, "bold"), bg="#C8A2C8", fg="#FFFFFF")
btn_clique = tk.Button(janela, text="Clique Aqui!", font=("Arial", 11), bg= "#C8A2C8", fg="#FFFFFF", command=mostrar_mensagem )
btn_close = tk.Button(janela, text="Fechar", font=("Arial", 14, "bold"), bg="#FFFFFF", command=janela.destroy)

# 4. Posicionar os componentes
lbl_titulo.pack(pady=20) # 'pady' adiciona um espacamento vertical
btn_clique.pack(pady=10)
btn_close.pack(pady=5)

# 5. Rodar o loop da interface
janela.mainloop()

