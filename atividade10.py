#função 1 

'''def multiplo_de_5 (N):
    for number in range(int(N)):
        if number % 5 == 0 and number % 2 != 0:
                  print(number)
'''

#função 2 

def funcao2():
  numero_entradas = int(input("Digite o numero de entradas: "))
  lista = []
  i = 0
  while i < numero_entradas:
    lista.append(input("Adicione na lista aqui: "))
    i += 1
  return lista

print (funcao2())

#função 3
def numeros_de_numeros(list):
    numeros_maiores_5 = 0
    for number in list:
        if numero > 5:
            numero_5 += 1
    return numeros_maiores_5

#colocar numero na lista 
list = []
print(numeros_de_numeros(list))

#função 4

def futebol():
 opcao = input("insira aqui sua opção:")
while opcao != 'z':
  if opcao == 'a':
    print("PSG")
elif opcao == 'b':
print ("Bayer")
elif opcao == 'd':
 break
opcao = imput()

print (futebol())
