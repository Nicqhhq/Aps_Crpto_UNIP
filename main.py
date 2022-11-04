from tkinter import *
from tkinter import messagebox

# Tela principal
tela_principal = Tk()
tela_principal.title("APS - Criptografia e Descriptografia")
tela_principal.geometry("800x600")
tela_principal.minsize(800, 600)
tela_principal.maxsize(800, 600)

# FUNÇÕES
# Mensagem de informação
def msg_informacao(_texto):
    messagebox.showinfo("Informação", format(_texto, str))

# Mensagem de aviso
def msg_aviso(_texto):
    messagebox.showwarning("Aviso!", format(_texto, str))

# Mensagem de erro
def msg_erro(_texto):
    messagebox.showerror("Erro!", format(_texto, str))

# Título da página
label_titulo = Label(text = "Criptografia e Descriptografia", font = "Arial")

# Entrada de dados
texto_entrada_criptografia = Text(tela_principal, height = 10,
                                  width = 25)

# Saída de dados
texto_saida_criptografia = Text(tela_principal, height = 10,
                                  width = 25)

# Botão de ação
botao_criptografia = Button(tela_principal, height = 2,
                            width = 20,
                            text = "Criptografar",
                            font = "-weight bold -size 10")
                            #command = lambda:Take_input())

label_titulo.pack(ipadx=10, ipady=10)
texto_entrada_criptografia.pack()
botao_criptografia.pack(padx= 10, pady= 10)
texto_saida_criptografia.pack()

tela_principal.mainloop()