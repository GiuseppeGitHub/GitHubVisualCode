''' Programa creat per José Luis Martíon
    Amb data de 20/02/2022'''

import random

numAleatori = random.randint(1,10)

def MenuOpcions():
    print('''
PULSA 'a' PER ADIVINAR UN NÚMERO
PULSA 'b' PER SABER SI UN ANY ÉS DE TRASPAS
PULSA 'c' PER SABER SI UN NÚMERO ÉS PRIMER
PULSA 'd' PER CALCULAR EL MCD ENTRE DOS NÚMEROS
PULSA 'o' PER SORTIR
    ''')

MenuOpcions()
tecla=None
while(tecla!='o'):
    tecla=input('Entra una tecla: ')
    if (tecla=='a'):
        numUsuari=input("ENTRA UN NÚMERO DEL 1 AL 10 I ET DIRÉ SI L'HAS ENCERTAT: ")
        while numAleatori != numUsuari:
            numUsuari=input("NO L'HAS ENCERTAT, TORNA-HO A PROVAR: ")
    if (tecla=='b'):
        any = input("ENTRA UN ANY: ")
        if (any % 4 == 0 and any % 100 != 0 or any % 400 == 0):
            print('ÉS UN ANY DE TRASPÀS')
        else:
            print('NO ÉS UN ANY DE TRASPÀS')
    
