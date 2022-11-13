from tkinter import *
from tkinter import messagebox

# Tela principal
tela_principal = Tk()
tela_principal.title("APS - Criptografia e Descriptografia")
tela_principal.geometry("800x600")
tela_principal.minsize(800, 600)
tela_principal.maxsize(800, 600)

# Funções
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
label_titulo = Label(text = "APS - Criptografia e Descriptografia", font = "Arial")

# Criptografia
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

# Descriptografia
# Entrada de dados
texto_entrada_descriptografia = Text(tela_principal, height = 10,
                                  width = 25)

# Saída de dados
texto_saida_descriptografia = Text(tela_principal, height = 10,
                                  width = 25)

# Botão de ação
botao_descriptografia = Button(tela_principal, height = 2,
                            width = 20,
                            text = "Descriptografar",
                            font = "-weight bold -size 10")

# Execução da Tela 
label_titulo.pack(ipadx=10, ipady=10)
label_titulo.place(relx=0.5, rely=0.055, anchor='n')

texto_entrada_criptografia.pack()
texto_entrada_criptografia.place(relx=0.25, rely=0.2, anchor='n')
botao_criptografia.pack(padx= 10, pady= 10)
botao_criptografia.place(relx=0.25, rely=0.5, anchor='n')
texto_saida_criptografia.pack()
texto_saida_criptografia.place(relx=0.25, rely=0.6, anchor='n')

texto_entrada_descriptografia.pack()
texto_entrada_descriptografia.place(relx=0.75, rely=0.2, anchor='n')
botao_descriptografia.pack(padx= 10, pady= 10)
botao_descriptografia.place(relx=0.75, rely=0.5, anchor='n')
texto_saida_descriptografia.pack()
texto_saida_descriptografia.place(relx=0.75, rely=0.6, anchor='n')

tela_principal.mainloop()