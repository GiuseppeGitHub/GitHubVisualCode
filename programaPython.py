''' Programa creat per José Luis Martíon
    Amb data de 20/02/2022'''

import random

numAleatori = random.randint(1,10)
#Creació de menú
def MenuOpcions():
    print('''
ENTRA 'a' PER ADIVINAR UN NÚMERO
ENTRA 'b' PER SABER SI UN ANY ÉS DE TRASPAS
ENTRA 'c' PER SABER SI UN NÚMERO ÉS PRIMER
ENTRA 'd' PER CALCULAR EL MCD ENTRE DOS NÚMEROS
ENTRA 'o' PER SORTIR
    ''')

MenuOpcions()
tecla=None
#Creació de les accions
while(tecla!='o'):
    tecla=input('Entra una tecla: ')
    if (tecla=='a'):
        print("ENTRA UN NÚMERO DEL 1 AL 10 I ET DIRÉ SI L'HAS ENCERTAT: ")
        numUsuari=int(input())
        while numAleatori != numUsuari:
            print("NO L'HAS ENCERTAT, TORNA-HO A PROVAR: ")
            numUsuari=int(input())
        print("L'HAS ENCERTAT!!")
    if (tecla=='b'):
        any = int(input("ENTRA UN ANY: "))
        if (any % 4 == 0 and any % 100 != 0 or any % 400 == 0):
            print('ÉS UN ANY DE TRASPÀS')
        else:
            print('NO ÉS UN ANY DE TRASPÀS')
    if (tecla=='c'):
        i = 2
        numero = int(input('ENTRA UN NÚMERO: '))
        while numero % i != 0 and i<= numero /2:
            i+=1
        if (numero%i ==0):
            print('NO ÉS UN NÚMERO PRIMER')
        else:
            print('ÉS UN NÚMERO PRIMER')
    if (tecla=='d'):
        primerNumero=int(input('ENTRA UN NÚMERO:'))
        segonNumero=int(input('ENTRA UN SEGON NÚMERO: '))
        while segonNumero !=0:
            aux=segonNumero
            segonNumero=primerNumero%segonNumero
            primerNumero=aux
        print(F'EL MÀXIM COMÚ DIVISOR ÉS {primerNumero}')

