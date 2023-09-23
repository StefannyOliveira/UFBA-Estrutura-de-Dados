
class No:
  def __init__(self, valor):
    self.valor = valor
    self.prox = None

  def shownode(self):
    return str(self.valor)

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

  def find(self, atual, valor):
        no = atual
        while no is not None:
            if no.valor == valor:
                return no
            no = no.prox
        return None
  
  def minimo(self, no):
    if no is None:
      return None
    else:
      menor = no.valor
      atual = no.prox
      while atual is not None:
          if atual.valor < menor:
              menor = atual.valor
          atual = atual.prox
      return menor

  def troca(self, atual, atual2):
    numero = atual.valor
    atual.valor = atual2.valor
    atual2.valor = numero


  def selection_sort(self, iteraçoes ):
   if self.frente is None:
     return self
   atual = self.frente
   i = 0
   while i < iteraçoes:
     menor = self.minimo(atual)
     if atual.valor != menor:
       self.troca(atual, self.find(atual, menor))
     atual = atual.prox
     i += 1
   return self
  
def main():
  ordem = Fila()
  
  linhas = int(input())
  
  iteracoes = int(input())

  for _ in range(linhas - 1):
    dados = int(input())
    ordem.inserir(dados)
  
  x = 1
  while x < iteracoes:
    x = x + 1
    ordem.selection_sort(iteracoes)
    if x == iteracoes:
      break
    
      
  ordem.show()
  
if __name__ == '__main__':
  main()
  