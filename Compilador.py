x = input().split() 
branco = ""
for i in x:
  if i != " ":
    branco += i
    
class No:
  def __init__(self, valor):
    self.valor = valor
    self.prox = None

class Pilha:
  def __init__(self):
    self.topo = None

  def push(self):
    for i in branco:
      if i in '([{':
        new_no = No(i)
        new_no.prox = self.topo
        self.topo = new_no
        
  def pop(self):
    if self.topo is None:
      return None
    else:
      this_no = self.topo
      self.topo = self.topo.prox
      del this_no

def main():
  pilha = Pilha()
  pilha.push()

  for i in branco:
    if branco[0] in ')]}':
      print('Invalido')
      break
    if i in ')]}':
      if pilha.topo is None:
        print('Valido')
        return
      elif (pilha.topo.valor == '(' and i == ')') or (pilha.topo.valor == '[' and i == ']') or (pilha.topo.valor == '{' and i == '}'):
        pilha.pop()
      else:
        print('Invalido')
        return

  if pilha.topo is None:
    print('Valido')
    
if __name__ == '__main__':
  main()