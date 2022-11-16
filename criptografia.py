
criptografar = True
descriptografar = False
alfabeto_ascii = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 224, 225, 227, 226, 228, 233, 232, 234, 235, 243, 242, 244, 245, 246, 237, 236, 238, 239, 250, 249, 251, 252, 241, 253, 255, 231, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 192, 193, 194, 195, 196, 201, 200, 202, 203, 211, 210, 213, 214, 205, 204, 206, 207, 218, 217, 219, 220, 209, 221, 199, 49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 185, 178, 179, 32, 163, 162, 172, 167, 91, 93, 123, 125, 60, 62, 44, 46, 58, 59, 47, 92, 124, 176, 170, 186, 39, 34, 33, 64, 35, 36, 37, 168, 38, 42, 40, 41, 45, 95, 61, 43, 180, 96, 94, 126]

# frase = input('Digite sua frase a ser enviada')
def criptografar(frase):
    traducao_frase = [ord(character) for character in frase]
    res = ""
    for val in traducao_frase: 
     res = res + chr(val) 
    chave = len(str(res))
    codigos = ""
    for val in alfabeto_ascii: 
     codigos = codigos+ chr(val) 
    frase_final = ''
    for c in frase:
        posicao = codigos.find(c)
        if posicao == -1:
            frase_final += c
        else:
            nova_posicao = posicao + chave 
            nova_posicao = nova_posicao % len(codigos)
            frase_final += codigos[nova_posicao:nova_posicao+1]
            frase_final_ascii = [ord(character) for character in frase_final]
            
            characters = "'[] "

    for x in range(len(characters)):
            frase_final_ascii = str(frase_final_ascii).replace(characters[x],"")
    return str(frase_final)

# frase = input('Digite sua frase a ser enviada')
def descriptografar(frase):
    traducao_frase = [ord(character) for character in frase]
    res = ""
    for val in traducao_frase: 
     res = res + chr(val) 
    chave = len(str(res))
    codigos = ""
    for val in alfabeto_ascii: 
     codigos = codigos+ chr(val) 
    frase_final = ''
    for c in frase:
        posicao = codigos.find(c)
        if posicao == -1:
            frase_final += c
        else:
            nova_posicao = posicao - chave 
            nova_posicao = nova_posicao % len(codigos)  
            frase_final += codigos[nova_posicao:nova_posicao+1]
            frase_final_ascii = [ord(character) for character in frase_final]
    
    return frase_final

#print('***********************************************************')
#escolha = input('Deseja Criptografar(1) uma mensagem ou Descriptografar(2) ?\n Escolha 1 Para Criptografar e 2 Para Descriptografar ')
#if escolha == "1":
#    frase = input('Digite a mensagem a ser Criptografada')
#    print('Mensagem Criptografada: ',criptografar(frase))
#else :
#     frase = input('Digite a mensagem a ser Descriptografada')
#     print('Mensagem Descriptografada: ',descriptografar(frase))