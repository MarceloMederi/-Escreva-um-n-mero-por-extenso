import time

def titulo():
    print("#" * 19)
    print("Número por extenso")
    print("#" * 19)

def conversor():
    numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte")

    while True:
    
        entrada = input("Informe um número para ser escrito:")
        if entrada == "":
            print("Você digitou uma entrada vazia. Digite um número inteiro.")
            return
        try:
            numero = int(entrada)
            if numero > 20:
                print("Número inválido. Digite um número entre 0 e 20.")
            else:
                print(numeros_por_extenso[numero])
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.") 
            return
            
            

while True:
    titulo()
    conversor()
