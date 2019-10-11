# Nome do projeto: Gráfico de Barras sem imports 
# Linguagem: Python
# Utilizações: Variáveis, Repetições, Listas e Funções
# Autor: Rafael Lua de Sousa e Silva - rafaellua13


print('\033c')      # Comando para limpar terminal
nam = []            # Lista Nomes
tam = []            # Lista Tamanhos
lista = []          # Armazenar valores da coluna
finalAlfabeto = []  # Lista final de alfabetos

numeros = ['1','2','3','4','5','6','7','8','9','0']

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def nomes_tamanhos(quantidade):  
  for aaa in range(1,quantidade + 1):
    print()
    test = False
    nome = input('Nome da coluna {}:    '.format(aaa))
    nam.append(nome)
    while True:
      tamanho = input('Tamanho da coluna {}: '.format(aaa))
      for kar in range(len(tamanho)):
        if tamanho[kar] in numeros:
          tamanho = int(tamanho)
          tam.append(tamanho)
          test = True
          break
        else:
            print('Formato Invalido, digite um numero inteiro')
      if test == True:
        break
  print('\n\n\n')
  return tam

def numeros_eixoY(tam,quantidade): # Numeros eixo y
  vazio = ' '
  maior = max(tam)
  vetor = [vazio] * len(tam) * maior * 2
  linha = (quantidade * 2)  # Tamanho da linha
  voz = 0
  care = 0
  for b in range(maior):
    if maior - voz < 10:
      # vetor[care] = ' ' + str(maior - voz)
      vetor[care] = maior - voz
    else:
      vetor[care] = maior - voz # Somar +1 no care para mudar a coluna
    voz += 1
    care += linha
  return vetor

def adicionando_grafico(tam,vetor,quantidade):
  # Preenchendo o grafico
  lista = []
  care = 0
  nan = 1
  maior = max(tam)
  marca = '■'
  linha = (quantidade * 2)  # Tamanho da linha
  # ■ - quadrado -> Alt + 254  
  for i in range(len(tam)):
    for k in range(tam[i]):
      lista.append(tam[i])
    # print(lista)  # lista auxiliar com os valores da coluna
    care = 0
    for b in range(maior):
      if vetor[care] <= lista[0]:
        vetor[care + nan] = marca
        if care + linha < len(vetor):
          care += linha     # Mudar de linha
      elif vetor[care] > lista[0]:
        if care + linha < len(vetor):
          care += linha     # Mudar de linha
    # print(vetor)  
    nan += 2   # Mudar de coluna
    lista = []
  return vetor

def arrumando(tam,vetor,quantidade): 
  # Arrumando a formatação do grafico nos numeros menores que 10
  
  # Numeros eixo y em str
  voz = 0
  care = 0
  maior = max(tam)
  linha = (quantidade * 2)  # Tamanho da linha
  for b in range(maior):
    if maior - voz < 10:
      vetor[care] = ' ' + str(maior - voz) 
      # Em string para arrumar a formatação do grafico      
    else:
      vetor[care] = maior - voz # Somar +1 no care para mudar a coluna
    voz += 1
    care += linha
  return vetor

def esqueleto(vetor,quantidade): # Esqueleto Gráfico
  linha = (quantidade * 2)  # Tamanho da linha
  cont = 0
  for x in range(len(vetor)):
    print(vetor[x], end = ' ')
    cont += 1
    if cont == linha:
      print()
      cont = 0

def nomes_eixoX(nam): # Nomes A B C
  for z in range(len(nam)):
    if z == 0:
      print('   ',end = '')
    print(alfabeto[z], end = '   ')  
    finalAlfabeto.append(alfabeto[z])
  print('\n\n\n')
  for w in range(len(nam)):
    print(finalAlfabeto[w],'=',nam[w])
  print('\n')

def grafCalc(quantidade):
  tam = nomes_tamanhos(quantidade)
  vetor = numeros_eixoY(tam,quantidade)
  adicionando_grafico(tam,vetor,quantidade)
  vetor = arrumando(tam,vetor,quantidade)
  esqueleto(vetor,quantidade)
  nomes_eixoX(nam)

def main(): # Inicio do programa  
  quantidade = int(input('Quantidade de Colunas: '))
  grafCalc(quantidade)


########################

main()
