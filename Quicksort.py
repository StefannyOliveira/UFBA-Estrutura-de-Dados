class No:
  def __init__(self, valor):
    self.valor = valor
    self.prox = None

  def shownode(self):
    return (self.valor)

class ListaEncadeada:
  def __init__(self):
    self.head = None

  def show(self):
    if self.head is not None:
      this_no = self.head
      espaço = ''
      while this_no is not None:
        espaço = espaço + f'{this_no.shownode()}' + ' '
        this_no = this_no.prox
      print(espaço)
  
  def inserir(self, valor):
      new_no = No(valor)
      if self.head is None:
        self.head = new_no
      else:
        this_no = self.head
        while this_no.prox is not None:
          this_no = this_no.prox
        this_no.prox = new_no 

  def position(self, posicao):
    if self.head is None:
      return None
    atual = self.head
    for i in range(posicao):
      atual = atual.prox
    return atual.valor

  def quicksort(self, list, idpivo):
    if list.head is None or list.head.prox is None:
      return list

    meio = list.position(idpivo)
    antes = ListaEncadeada()
    depois = ListaEncadeada()
    
    atual = list.head
    while atual is not None:
      if atual.valor < meio:
        antes.inserir(atual.valor)
      elif atual.valor > meio:
        depois.inserir(atual.valor)
      atual = atual.prox

    antes = self.quicksort(antes, 0)
    depois = self.quicksort(depois, 0)
    antes.inserir(meio)
    atual = depois.head
    while atual is not None:
        antes.inserir(atual.valor)
        atual = atual.prox
    return antes

def main():
  lista = []
  list = ListaEncadeada()
  menor = ListaEncadeada()
  maior = ListaEncadeada()
  
  linhas = int(input())
  posicao = int(input())
  
  for _ in range(linhas - 1):
    dados = int(input())
    lista.append(dados)
    list.inserir(dados)

  for i in lista:
    if i < list.position(posicao):
      menor.inserir(i)
    else:
      maior.inserir(i)

  print(menor.head.valor, maior.head.valor, end=" ")

  
  list = list.quicksort(list, posicao)
  list.show()
  
  
if __name__ == '__main__':
  main()