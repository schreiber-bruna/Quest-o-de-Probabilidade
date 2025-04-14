import random
def bilhete_prob5():
    bilhete = []
    sorteados = []
    while(len(bilhete)<6):
        bilhete.append(random.randint(1,60))
    bilhete.sort()
    for i in range(5):
        if(bilhete[i]==bilhete[i+1]):
            bilhete.remove(bilhete[i+1])
            bilhete.append(random.randint(1,60))
    bilhete.sort()
            
    
    while(len(sorteados)<6):
        sorteados.append(random.randint(1,60))
    sorteados.sort()
    for i in range(5):
        if(sorteados[i]==sorteados[i+1]):
            sorteados.remove(sorteados[i+1])
            sorteados.append(random.randint(1,60))
    sorteados.sort()
    contagem = 0
    for i in range(6):
        for k in range(6):
            if (bilhete[k] == sorteados[i]):
                contagem = contagem +1
            else:
                contagem = contagem + 0
    if (contagem == 5):
        return 1
    else:
        return 0
            

def probabilidade5(x):
  awin = 0
  for i in range(x):
    if bilhete_prob5() == 1:
      awin += 1
  y = awin/x
  return y
probabilidade5(1000)
