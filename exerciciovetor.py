
vetora = [2, 4, 6, 8, 9]
vetorb = [1, 3, 5, 7, 8]
vetorc = []
print
def menu():
    print('''
        MENU:

        [1] - leia os vetores A E B
        [2] - Ver Resultado vetor C
        [3] - Digite o indice que deseja comparar
        [4] - Sair
    ''')
    print(menu)
    return menu()
int(input('Escolha uma opção: '))
lerVetores = 1
verResultado = 2
digIndice = 3
menu = 4
def digIndice():
    for i in vetora[0]:
        i = input(print ('escreva o indice que deseja comparar de 0 a 4'))
    
    if vetora [0] % 2 == 0:
            vetorc [0] = vetora[0]*vetorb[0]
    elif vetora[0] % 2 != 0:
            vetorc [0] = vetora[0]
    return digIndice()
def verResultado():
      print(vetorc)
      return verResultado()

