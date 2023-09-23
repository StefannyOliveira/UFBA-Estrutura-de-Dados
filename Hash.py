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

  def ascii(self, valor, tamanho):
    soma = 0
    for caractere in valor:
        ascii = ord(caractere) - 96
        soma = soma + ascii
    resto = soma % tamanho
    return resto
    
def main():
  lista = ListaEncadeada()
  
  linhas = int(input())
  tamanho = int(input())
  posicao = int(input())
  p = []
  
  x = 0
  while x < tamanho + 1:
    palavras = input().strip()
    lista.inserir(palavras)
    p.append(palavras)
    x = x + 1
    

  rechi = [ListaEncadeada() for _ in range(tamanho)]
  for palavras in p:
    final = lista.ascii(palavras, tamanho)
    rechi[final].inserir(palavras)
  
  resultado = rechi[posicao]
  resultado.show()

if __name__ == '__main__':
  main()

