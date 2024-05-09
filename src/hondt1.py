def posmax(lista):
    assert lista!=[]
    max=lista[-1]
    pmax=len(lista)-1
    for pos in range(pmax-1,-1,-1):
        val=lista[pos]
        if val>max:
            max=val
            pmax=pos
    return pmax

def hondt(votos,lugares):
    res=[0 for i in range(len(votos))]
    coefs=votos[:]
    for disp in range(lugares,0,-1):
        prox=posmax(coefs)
        res[prox]=res[prox]+1
        coefs[prox]=votos[prox]/(res[prox]+1)
    return res

hondt([100,80,30,20],9)

""" A ideia é muito simples: havendo vários mandatos para atribuir, se há  n
  listas concorrentes, cada uma com  $v_n$
  votos, e a cada uma já foram atribuídos  $a_n$
  mandatos (no início  $a_n$ é obviamente $0$) então o próximo mandato é 
  atribuído à lista com o máximo valor de $\frac{v_n}{1+a_n}$. """