#Prática 01.01 - Detecta Ciclo
#Implemente uma função que detecta ciclos em uma lista encadeada.
#A primeira linha representa quantas linhas você deve ler na sequência. A próxima linha contêm todos os nós da lista com seus respectivos valores. 
#As demais linhas contêm as relações (encadeamento) entre os nós. Essa entrada representa o primeiro exemplo ilustrado anteriormente.

a = int(input())
b = [int(x) for x in input().split()]

class No:
  def __init__(self, valor):
    self.valor = valor
    self.prox = None

  def shownode(self):
    return (self.valor)
    
class ListaEncadeada:
  def __init__(self):
    self.head = None

  def add_fim(self):
    for i in b:
      new_no = No(i)
      if self.head is None:
        self.head = new_no
      else:
        this_no = self.head
        while this_no.prox is not None:
          this_no = this_no.prox
        this_no.prox = new_no 

  def detectar_ciclo(self):
      no_1 = self.head
      no_2 = self.head
      while no_2 is not None and no_2.prox is not None:
        no_1 = no_1.prox
        no_2 = no_2.prox.prox
        if no_1 == no_2:
          print('Ciclo')
          return
      print('Sem Ciclo')
          

def main():
  lista = ListaEncadeada()
  lista.add_fim()  

  #criar ciclo
  for i in range(a - 1):
    x, y = [int(z) for z in input().split()]
    this_x = lista.head
    this_y = lista.head
    while this_x.valor != x:
      this_x = this_x.prox
    while this_y.valor != y:
      this_y = this_y.prox
    this_x.prox = this_y

  lista.detectar_ciclo()
            
if __name__ == '__main__':
  main()
