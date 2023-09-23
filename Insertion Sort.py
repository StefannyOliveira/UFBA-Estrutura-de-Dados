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
  
  def insertion(self, valor):
    no = No(valor)
    if self.frente is None:
        self.frente = no
        self.tras = no
    else:
      if valor <= self.frente.valor:
          no.prox = self.frente
          self.frente = no
      elif valor >= self.tras.valor:
          self.tras.prox = no
          self.tras = no
      else:
          atual = self.frente
          while atual.prox is not None and valor > atual.prox.valor:
              atual = atual.prox
          no.prox = atual.prox
          atual.prox = no
        
def main():
    fila = Fila()
    #entrada = Fila()
    entradas = []

    linhas = int(input())

    iterações = int(input())

    for _ in range(linhas - 1):
        dados = int(input())
        #entrada.inserir(dados)
        entradas.append(dados)

    #print('Dados de entrada:', end=' ')
    #entrada.show()

    x = 0
    for valor in entradas:
        x = x + 1
        fila.insertion(valor)
        #print('Iteração:', end=' ')
        if x == iterações:
          break
    fila.show()

if __name__ == '__main__':
    main()