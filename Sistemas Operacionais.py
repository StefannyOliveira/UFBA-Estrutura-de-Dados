#Prática 01.03 - Sistemas Operacionais
#Você deve implementar o algoritmo Round Robin (RR) de escalonamento em um Sistema Operacional (SO). Esse algoritmo executa da seguinte maneira:
#  1- Cada processo no sistema tem um custo de execução representado por Unidades de Processamento (UP);
#  2 - Cada novo processo é enviado para uma fila de "pronto" que contém processos que estão aptos para serem executados;
#  3 - A CPU libera um limite de tempo (quantum) para cada processo. 
#Se um processo está executando e precisa de mais UP que o quantum liberado pela CPU, ele executa até o limite e depois volta para o final da fila de pronto com as UPs necessárias para concluir sua tarefa.
#A primeira linha informa quantas linhas em sequência devem ser lidas. 
#A segunda linha contém duas informações importantes: o quantum da CPU e o máximo de UP que seu código vai processar. 
#A próxima linha contém os IDs dos processos. A última linha contém todas as UPs necessárias por processo.
#Ao final do máximo de UP, seu código deve imprimir a fila atual e as respectivas UPs restantes.


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
        
  def remover(self):
    if self.frente is None:
      return
    no = self.frente
    self.frente = no.prox
    if self.frente is None:
      self.tras = None
    del no

def main():

  x = int(input())
  quantum, maximo_up = [int(i) for i in input().split()]
  ids = [int(i) for i in input().split()]
  ups_necessarias = [int(i) for i in input().split()]

  fila = Fila()
  for i in ids:
    fila.inserir(i)
    
  ups = Fila()
  for i in ups_necessarias:
    ups.inserir(i)

  while maximo_up > 0 and ups.frente is not None:
    atual_ups = ups.frente.valor
    atual_fila = fila.frente.valor
    if maximo_up < quantum:
      atual_ups = atual_ups - maximo_up
      maximo_up = 0
      ups.remover()
      ups.inserir(atual_ups)
      fila.remover()
      fila.inserir(atual_fila)
      break
    if atual_ups <= quantum:
      maximo_up = maximo_up - atual_ups
      ups.remover()
      fila.remover()
    else:
      maximo_up = maximo_up - quantum
      atual_ups = atual_ups - quantum
      ups.remover()
      ups.inserir(atual_ups)
      fila.remover()
      fila.inserir(atual_fila)
    
   
  fila.show()
  ups.show()
  

if __name__ == '__main__':
  main()
