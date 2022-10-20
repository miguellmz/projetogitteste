#from random import choice
#aluno1 = str(input("INSIRA O NOME DO ALUNO"))
#aluno2 = str(input("INSIRA O NOME DO ALUNO"))
#aluno3 = str(input("INSIRA O NOME DO ALUNO"))
#aluno4 = str(input("INSIRA O NOME DO ALUNO"))
#lista = [aluno1, aluno2, aluno3, aluno4]
#escolhido = choice(lista)
#print(escolhido)

#from random import shuffle
#aluno1 = str(input("INSIRA O NOME DO ALUNO"))
#aluno2 = str(input("INSIRA O NOME DO ALUNO"))
#aluno3 = str(input("INSIRA O NOME DO ALUNO"))
#aluno4 = str(input("INSIRA O NOME DO ALUNO"))
#lista = [aluno1, aluno2, aluno3, aluno4]
#shuffle(lista)
#print(lista)

#frase = "Bem vindo ao mundo do python"
#print(frase[22::1]) 

#letras = 0
#frase = "Bem vindo ao mundo do python"
#cont = frase.count(" ")
#for letra in frase:
#    letras = letras + 1
#    somaletras = letras - cont
#rint(somaletras)

#quant = 1
#frase = "eu nao sei"
#for letra in frase:
#    if (letra == " "):
 #       quant = quant + 1
#print(quant)

#frase = "eu nao sei"
#x= frase.title()
#print(x)

#frase = "eu nao sei"
#print(len(frase))

#frase = input("").strip()
#print(frase.upper()) 
#print(frase.lower())
#print(len(frase) - frase.count(" "))
#print(frase.find(" "))
# ou
#separa = frase.split()
#print(separa[0])

#cidade = input("insira o nome da cidade")
#x = "santo" in cidade
#print(x)

#cidade = input("insira o nome da cidade").strip().lower()
#palavra1 = cidade.split()
#if ( palavra1[0] == "santo"):
#    print(True)
#else:
#    print("False")


#cidade = input("insira o nome da cidade").strip()
#print(cidade[0:5].lower() == "santo")


#nome = str(input("insira seu nome: ")).lower()
#x = "silva" in nome
#print(x)

#num = int(input("inisira o numero: "))
#n = str(num)
#print(n[0])
#print(n[1])
#print(n[2])
#print(n[3])

#num = int(input("inisira o numero: "))
#u = num //1  % 10 
#d = num //10 % 10
#c = num //100 % 10
#m = num //1000 % 10
#print(u)
#print(d)
#print(c)
#print(m)

#frase = str(input("digite:")).strip().lower()
#repet = frase.count("a")
#esconti = frase.find("a")
#escontr = frase.rfind("a")
#print(repet)
#print(esconti + 1)
#print(escontr + 1)

#frase = str(input("digite:")).strip().lower()
#x = frase.split()
#print(x[0])
#print(x[len(x)-1])


#from random import randint
#from time import sleep
#nump = randint(0, 5)
#print("Vou pensar em um numero de 0 a 5. tente adivinhar...")
#num = int(input("insira um numero: "))
#print("processando...")
#sleep(2)
#if(num == nump):
 #   print("acertou o numero era {}".format(num))  
#else:
 #   print("voce perdeu, o numero era o {}".format(nump))

#ano = int(input("insira um ano: "))
#bissexto = ano % 4
#print("ano bissexto" if bissexto == 0 else "nao é bissexto")


# considere a base "z"
#from time import sleep

#from pyparsing import anyCloseTag
#print("-----ANALISADOR DE TRIANGULO------")
#x = float(input("insira a reta x: "))
#y = float(input("insira a reta y: "))
#z = float(input("insira a reta z: "))
#somador = x + y >= z
#sleep(1)
#if somador == True:
#    print("é um triangulo possivel")
#else:
    #print("nao é um possivel triangulo")

    #padrao ance
print("\033[1;30;42m Ola mundo \033[m")

