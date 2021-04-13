def exercicio1():
  list = []
  soma = 0
  while len(list) < 3:
    entrada = int(input("Nota: "))
    list.append(entrada)
  for nota in list:
    soma += nota
  media = soma / len(list)
  return f"media do aluno é: {media}"


def exercicio2 (N):
  lista []
  while len(lista) < N:
  lista.append_(input(f"{len(lista) + 1}" numero: "))
  return lista

                      
                      
   def exercicio_3():
  entrada = input(" coloque 'a' para Globo, 'b' para SBT e 'z' para finalizar: ")
  while entrada != 'z':
    if entrada == 'Z':
      break
    elif entrada == 'a':
      print("Globo")
    elif entrada == 'b':
      print("SBT")
    else:
      print("Inválido")
      break
    entrada = input()
exercicio_3()

                      
def exercicio4():
    media_dos_alunos = []
    reprovados = []
    i = 0
    while i < len(media_dos_alunos):
        if float(media_dos_alunos[i]) < 7:
            reprovados.append(media_dos_alunos[i])
        i += 1
    if len(reprovados) > len(media_dos_alunos) * 0.25:
        return ('Professor Coxa')
    else:
        return ('Professor Padrão')
