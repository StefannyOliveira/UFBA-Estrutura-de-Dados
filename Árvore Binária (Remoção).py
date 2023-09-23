#Prática 02.02 - Árvore Binária (remoção)
#1 -Implementar a estrutura de dados árvore binária incluindo, minimamente, as funções listadas abaixo:
#  Add (INT) - Adiciona um inteiro na árvore;
#  Remove (INT) - Remove um inteiro da árvore;
#2 - Ler um vetor de inteiros e armazená-lo em uma árvore binária:
#  Os valores devem ser armazenados com "Add(...)";
#  Os elementos devem ser preenchidos da seguinte maneira: se o valor da chave for menor que a raiz, insira na subárvore à esquerda; caso contrário, insira à direita;
#3 - Ler um novo vetor com os valores que serão removidos:
#  A remoção deve acontecer usando o algoritmo explicado em sala de aula;
#  A remoção não deve acontecer nesse momento da leitura dos dados;
#4 - Ler um valor que será usado como chave de busca:
#  Execute a função "em-ordem" e imprima os valores encontrados até o número informado para pesquisa;
#  Execute as remoções listadas na Etapa 2;
#  Execute a função "em-ordem" e imprima os valores encontrados até o número informado para pesquisa;
#  Se o número não for encontrado, seu código deve imprimir todos os elementos "em-ordem";

class No:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None

  def shownode(self):
    return(self.valor)

class ArvoreBinaria:
  def __init__(self):
    self.raiz = None

  def adicionar(self, atual, no):
    if self.raiz is None:
      self.raiz = no
    else:
      if atual.valor <= no.valor:
        if atual.direita:
          self.adicionar(atual.direita, no)
        else:
          atual.direita = no
      else:
        if atual.esquerda:
          self.adicionar(atual.esquerda, no)
        else:
          atual.esquerda = no

  def remover(self, atual, no, pai=None):
      if atual is None:
          return None
  
      if no.valor < atual.valor:
          atual.esquerda = self.remover(atual.esquerda, no, atual)
      elif no.valor > atual.valor:
          atual.direita = self.remover(atual.direita, no, atual)
      else:
          if atual.esquerda is None and atual.direita is None:
              if pai is not None:
                  if pai.esquerda is not None and pai.esquerda.valor ==   atual.valor:
                      pai.esquerda = None
                  elif pai.direita is not None and pai.direita.valor ==   atual.valor:
                      pai.direita = None
              return None
          elif atual.esquerda is None:
              if pai is not None:
                  if pai.esquerda is not None and pai.esquerda.valor ==   atual.valor:
                      pai.esquerda = atual.direita
                  else:
                      pai.direita = atual.direita
              return atual.direita
          elif atual.direita is None:
              if pai is not None:
                  if pai.esquerda is not None and pai.esquerda.valor ==   atual.valor:
                      pai.esquerda = atual.esquerda
                  else:
                      pai.direita = atual.esquerda
              return atual.esquerda
          else:
              mm = self.maior_menor(atual.esquerda)
              atual.valor = mm.valor
              atual.esquerda = self.remover(atual.esquerda, mm, atual)
  
      return atual

  def maior_menor(self, no):
      while no.direita:
          no = no.direita
      return no

  
  def in_order(self, atual, no):
    if atual is None:
      return
    else:
      self.in_order(atual.esquerda, no)
      if atual.valor <= no.valor:
        print(f'{atual.valor} ', end='')
      self.in_order(atual.direita, no)

  

def main():

  x = int(input())

  arvore = ArvoreBinaria()
  
  entrada = [int(i) for i in input().split()]
  for i in entrada:
    no = No(i)
    arvore.adicionar(arvore.raiz, no)
    
  remocao = [int(i) for i in input().split()]
  pesquisa = int(input())

  arvore.in_order(arvore.raiz, No(pesquisa))
  print()
  
  for i in remocao:
    no = No(i)
    arvore.remover(arvore.raiz, no)

  
  arvore.in_order(arvore.raiz, No(pesquisa))
  print()

if __name__ == '__main__':
  main()
