class No:
  def __init__(self, valor):
    self.valor = valor
    self.prox = None

  def shownode(self):
    return (self.valor)

class Fila:
  def __init__(self):
    self.frente = None
    self.tras = None

  def show(self):
    if self.frente is not None:
      this_no = self.frente
      espaço = ''
      while this_no is not None:
        espaço = espaço + f'{this_no.shownode()}' + ' '
        this_no = this_no.prox
      print(espaço)

  def inserir(self, valor):
      new_no = No(valor)
      if self.frente is None:
        self.frente = new_no
        self.tras = new_no
      else:
        self.tras.prox = new_no
        self.tras = new_no

  def troca(self, atual, atual2):
    numero = atual.valor
    atual.valor = atual2.valor
    atual2.valor = numero

  def bubble_sort(self, iter):
    if self.frente is None:
      return self
    else:
      i = 0
      while i < iter:
        i = i + 1
        atual = self.frente
        while atual.prox is not None:
          if atual.valor > atual.prox.valor:
            self.troca(atual, atual.prox)
          atual = atual.prox
      return self


def main():
  ordem = Fila()
  
  linhas = int(input())
  
  iter = int(input())

  for _ in range(linhas - 1):
    dados = int(input())
    ordem.inserir(dados)

  ordem.bubble_sort(iter)

  ordem.show()

if __name__ == '__main__':
  main()