from tkinter import *
from tkinter import messagebox
import criptografia

# Tela principal
tela_principal = Tk()
tela_principal.title("APS - Criptografia e Descriptografia")
tela_principal.geometry("800x600")
tela_principal.minsize(800, 600)
tela_principal.maxsize(800, 600)

# Funções
# Mensagem de informação
def msg_informacao(_texto):
    messagebox.showinfo("Informação", format(_texto))

# Mensagem de aviso
def msg_aviso(_texto):
    messagebox.showwarning("Aviso!", format(_texto))

# Mensagem de erro
def msg_erro(_texto):
    messagebox.showerror("Erro!", format(_texto))

def validacao(_texto):
    ret = True

    if len(_texto.strip()) == 0:
        ret = False
        msg_erro("Informe uma mensagem de entrada valido!!")
    elif len(_texto) > 128:
        ret = False
        msg_erro("A quantidade de caracteres não podem ultrapassar 128 caracteres!!")
    
    return ret

def botao_entrada_cripto():
    texto = texto_entrada_criptografia.get(1.0, "end-1c").strip()
    if validacao(texto):
        texto_saida_criptografia.delete(1.0,"end")
        texto_saida_criptografia.insert(1.0, criptografia.criptografar(texto))
        texto_entrada_criptografia.delete(1.0,"end")
    

def botao_entrada_descripto():
    texto = texto_entrada_descriptografia.get(1.0, "end-1c").strip()
    if validacao(texto):
        texto_saida_descriptografia.delete(1.0,"end")
        texto_saida_descriptografia.insert(1.0, criptografia.descriptografar(texto))
        texto_entrada_descriptografia.delete(1.0,"end")

# Título da página
label_titulo = Label(text = "APS - Criptografia e Descriptografia", font = "-family arial -weight bold -size 22")

# Criptografia
# Entrada de dados
label_entrada_criptografia = Label(text = "Entrada", font = "-family arial -weight bold -size 12")
texto_entrada_criptografia = Text(tela_principal, height = 10,
                                  width = 25)

# Saída de dados
label_saida_criptografia = Label(text = "Saída", font = "-family arial -weight bold -size 12")
texto_saida_criptografia = Text(tela_principal, height = 10,
                                  width = 25)

# Botão de ação
botao_criptografia = Button(tela_principal, height = 2,
                            width = 20,
                            text = "Criptografar",
                            font = "-family arial -weight bold -size 10",
                            command = botao_entrada_cripto)

# Descriptografia
# Entrada de dados
label_entrada_descriptografia = Label(text = "Entrada", font = "-family arial -weight bold -size 12")
texto_entrada_descriptografia = Text(tela_principal, height = 10,
                                  width = 25)

# Saída de dados
label_saida_descriptografia = Label(text = "Saída", font = "-family arial -weight bold -size 12")
texto_saida_descriptografia = Text(tela_principal, height = 10,
                                  width = 25)

# Botão de ação
botao_descriptografia = Button(tela_principal, height = 2,
                            width = 20,
                            text = "Descriptografar",
                            font = "-weight bold -size 10",
                            command = botao_entrada_descripto)

# Execução da Tela
def run(): 
    label_titulo.pack(ipadx=10, ipady=10)
    label_titulo.place(relx=0.5, rely=0.055, anchor='n')

    label_entrada_criptografia.pack()
    label_entrada_criptografia.place(relx=0.25, rely=0.15, anchor='n')
    texto_entrada_criptografia.pack()
    texto_entrada_criptografia.place(relx=0.25, rely=0.2, anchor='n')
    botao_criptografia.pack(padx= 10, pady= 10)
    botao_criptografia.place(relx=0.25, rely=0.5, anchor='n')
    label_saida_criptografia.pack()
    label_saida_criptografia.place(relx=0.25, rely=0.6, anchor='n')
    texto_saida_criptografia.pack()
    texto_saida_criptografia.place(relx=0.25, rely=0.65, anchor='n')

    label_entrada_descriptografia.pack()
    label_entrada_descriptografia.place(relx=0.75, rely=0.15, anchor='n')
    texto_entrada_descriptografia.pack()
    texto_entrada_descriptografia.place(relx=0.75, rely=0.2, anchor='n')
    botao_descriptografia.pack(padx= 10, pady= 10)
    botao_descriptografia.place(relx=0.75, rely=0.5, anchor='n')
    label_saida_descriptografia.pack()
    label_saida_descriptografia.place(relx=0.75, rely=0.6, anchor='n')
    texto_saida_descriptografia.pack()
    texto_saida_descriptografia.place(relx=0.75, rely=0.65, anchor='n')

    tela_principal.mainloop()

if __name__ == "__main__":
    run()