##Exercício1
'''
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("o número é par")
else:
    print("o número é ímpar")
    '''
##Exercício2
'''
numero = int(input("Digite um número: "))
if numero  > 10:
    print("o número é maior que 10")
elif numero < 10:
    print("o número é menor que 10")
else:
    print("o número é igual a 10")
'''

##Exercício3
'''
idade = int(input("Digite sua idade: "))
if idade  >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
'''

##Exercício4

'''
idade = int(input("Digite sua idade: "))
if idade <16:
    print("Voto proibido")
elif idade>=18 and idade <70:
    print("Voto obrigatório")
else:
    print("Voto opcional")
'''

##Exercício5
'''
numero = int(input("Digite um número: "))
if numero  > 0:
    print("o número é positivo")
elif numero < 0:
    print("o número é negativo")
else:
    print("o número é igual a 0")
'''

# Exercício6
'''
nota = float(input("Digite sua nota de 0 a 10: "))
if nota >=0 and nota<=10:

    if nota >=9 and nota <=10:
        print("Nota A")
    elif nota >=7 and nota <=8:
        print("Nota B")
    elif nota >=5 and nota <= 6:
        print("Nota C")
    elif nota >=3 and nota <=4:
        print("Nota D")
    else:
        print("Nota E")
else:
    print("Digite uma nota válida!")
  '''

# Exercício7
'''
idade = int(input("Digite sua idade: "))

if idade <=12 or idade>=60:
     print("Tem direito ao desconto!")
else:
    print("Não tem direito ao desconto!")
'''

# Exercício8
'''
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado1+lado3 > lado2 and lado2+lado3> lado1:
    if lado1 == lado2 == lado3:
        print("É equilátero!")
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 ==lado3 != lado1:
        print("É isóceles!")
    else:
        print("É escaleno!")
else:
    print("As medidas passadas não formam um triangulo!")
 '''

# Exercício9
'''
valor = float(input("Digite o valor do produto: "))
if valor <100:
    desconto = 5/100
elif valor <=500:
    desconto = 10/100
elif valor >500:
    desconto = 15/100
else:
    print("Digite um valor válido!!!")

valorFinal = valor - (valor*desconto)
print(f"O valor final do produto é igual a: R${valorFinal:.2f}")
'''

# Exercício10
'''
ano = int(input("Digite o ano a ser verificado: "))
if ano % 4 == 0 and ano % 100 == 0:
    if ano % 400 == 0:
        print("É bissexto")
    else:
        print("Não é bissexto")
 
elif ano % 4 !=0:
    print("Não é bissexto")
else:
    print("É bissexto")
'''

# Exercício11:
'''
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/ (altura**2)

if imc < 18.5:
    print("Baixo peso")
elif 24.9> imc >18.5:
    print("Normal")
elif 29.9>imc>25:
    print("Sobrepeso")
elif 34.9>imc>30:
    print("Obesidade ")
elif 39.9> imc >35:
    print("Obesidade mórbida tipo 1")
else:
    print("Obesidade mórbida tipo 2")
'''

# Exercício12
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1> n2 > n3 or n1 == n2 >n3 or n1 > n2 == n3:
    ordem = "Decrescente"
elif n1 < n2 < n3 or n1 < n2 == n3 or n1 == n2 < n3 :
    ordem = "Crescente"
else:
    ordem = "Misturada ou os números são iguais"

print(f"A ordem dos números {n1}, {n2}, {n3} é {ordem}")
'''

# Exercício13
'''
temperatura = float(input("Digite a temperatura em C°: "))

if temperatura <10:
    classificacao = "frio"
elif 25 > temperatura >= 10:
    classificacao = "aconchegante"
elif 40 > temperatura >= 25:
    classificacao = "quente"
elif temperatura>=40:
    classificacao = "muito quente"
else:
    print("Digite uma temperatura válida!")

print(f"A temperatura em {temperatura}° está {classificacao}")
'''

# Exercício14
'''
data = input("Digite a data no formato dd/mm/aaaa: ")
dataConvertida = f"{data[:2]}-{data[3:5]}-{data[6:10]}"
print(dataConvertida)
'''

# Exercício15
'''
import re

print("REGRAS DA SENHA:\n\nMÍNIMO DE 8 CARACTERES\nPELO MENOS UM CARACTERE ESPECIAL(@#$%&)\nPELO MENOS UM NÚMERO\nPELO MENOS UMA LETRA MAíUSCULA (A-Z)\nPELO MENOS UMA LETRA MINÚSCULA (a-z)")
senha = input("\n\nDigite sua senha: ")

condicao = True


if len(senha) <8:
    condicao = False
    print("A senha não pode possuir menos de 8 caracteres!!!")


if not re.search("[a-z]", senha):
    condicao = False
    print("A senha precisa tera ao menos uma letra minúscula!!!")

if not re.search("[@#$%&]", senha):
    condicao = False
    print("A senha precisa ter ao menos um caractere especial!!!")

if not re.search("[A-Z]", senha):
    condicao = False
    print("A senha precisa ter ao menos uma letra maíuscula!!!")

if not re.search(r"\d", senha):
    condicao = False
    print("A senha precisa ter ao menos um número!!!")

if condicao == True:
    print("Senha válida!!!")'''



# Exercício16

'''
numero = int(input("Digite um número: "))
if numero < 0:
    print("Não existe raiz de número negativo!")
elif numero >100:
    print("Número muito grande, reduza para um valor abaixo de 100")
else:
    raiz = numero**(1/2)
        
    print(f"A raíz do número é igual a {raiz:.0f}")


'''

#Exercicio17

'''from datetime import datetime
import re

data = input("Digite a data dd/mm/aaaa:\n")
dataNum = f"{data[:2]} {data[3:5]} {data[6:len(data)]}"
dia = data[:2]
mes = data[3:5]
ano = data[6:len(data)]
ehCorreto = True
if not re.match(r"\d",dataNum):
    print("Digite uma data apenas com números")
else:
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if ano % 4 == 0 and ano % 100 == 0:
        if ano % 400 == 0:
            ehBissexto = True
        else:
            ehBissexto = False
    elif ano % 4 != 0:
        ehBissexto = False
    else:
        ehBissexto= True

    if 1 <= mes <= 12:
        if ehBissexto:
            diaLimite = 29
        else:
            diaLimite = 28

        if mes == 2:
            if dia>diaLimite:
                ehCorreto = False
                print(f"O mês {mes} possui até {diaLimite} dias")

        if mes == 1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            if dia > 31:
                ehCorreto = False
                print(f"O mês {mes} possui até 31 dias ")

        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 30:
                ehCorreto = False
                print(f"O mês {mes} possui até 30 dias ")
    else:
        print("Digite um mês de 1 a 12!!!")
        ehCorreto = False
if ehCorreto:
    data = datetime(ano,mes,dia)
    dataConvertida=data.strftime("%d-%m-%Y")
    print(dataConvertida)
'''

#Exercício18

'''operacao = input("Digite a operação: ")
resultado = eval(operacao)

print(f"{operacao} = {resultado:.2f}")'''

#Exercício19

'''import re

cpf = input("Digite seu CPF: 000.000.000-00\n")
ehValido = True

if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',cpf):

    cpfNum = f"{cpf[:3]}{cpf[4:7]}{cpf[8:11]}{cpf[12:14]}"
    listaNum = []
    for el in cpfNum:
        listaNum.append(int(el))

    primeiroDigito = ((listaNum[0]*10)+(listaNum[1]*9)+(listaNum[2]*8)+(listaNum[3]*7)+(listaNum[4]*6)+(listaNum[5]*5)+(listaNum[6]*4)+(listaNum[7]*3)+(listaNum[8]*2))
    segundoDigito  = ((listaNum[0]*11)+(listaNum[1]*10)+(listaNum[2]*9)+(listaNum[3]*8)+(listaNum[4]*7)+(listaNum[5]*6)+(listaNum[6]*5)+(listaNum[7]*4)+(listaNum[8]*3)+(listaNum[9]*2))
    if len(cpfNum) == 11:
    
        
        if primeiroDigito % 11 <2:
            if listaNum[9] !=0:
                ehValido = False
        else:
            resto1 = primeiroDigito % 11 
            if listaNum[9] != abs(resto1 - 11):
                ehValido = False

        if segundoDigito % 11 < 2:
            if listaNum[10] !=0:
                ehValido = False
        else:
            
            resto2 = segundoDigito % 11 
            if listaNum[10] != abs(resto2 - 11):
                ehValido = False
    else:
        ehValido = False
else:
    ehValido = False

if ehValido == True:
    print("O CPF é válido!")
else:
    print("O CPF não é válido!")
'''
