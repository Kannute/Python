import random as r

#zad1
def fun1(a):
    size = r.randint(0,20)
    dic = {}
    if size == 0:
        return dic
    while len(dic) < size:
        key = r.random()
        key = round(key,3)
        dic.setdefault(key, format(eval(a.format(key)), '.3f'))
    print(dic)
    return dic

#string1 = '5+{}'
#fun1(string1)

#zad2
def fun2(*a):
    lista=[]
    for i in a:
        for j in i:
            for l in a:
                if j not in l:
                    break
            else:
                if j not in lista:
                    lista.append(j)              
    print(lista)
    return lista
    
    
#fun2((1,2,3,4,6), [2,4,5,3,6], (2,4,5,1,11,6))

#zad3
def fun3(seq1, seq2, p=True):
    if p == True:
        lista1 =[(seq1[i], seq2[i]) for i in range(min(len(seq1), len(seq2))) ]
        print(lista1)
        return lista1
        
    if p == False:
        lista2=[(seq1[i], seq2[i]) if i < min(len(seq1), len(seq2)) else (None,seq2[i]) if len(seq2)>len(seq1) else (seq1[i], None) for i in range(max(len(seq1),len(seq2)))]
        print(lista2)
        return lista2
#fun3([1,2,3,4,5], [1,2,3,4,5,6])
#fun3([1,2,3,4,5], [1,2,3,4,5,6], False)

#zad4
def fun4(*a):
    for i in a:        
        for j in i:            
            print(min(j))
            return min(i)

def fun5(fun4, *a):
    fun4(a)

#fun5(fun4,[6,5,42,4])

#zad5
def fun6(kwota, b=(10,5,2)):
    lista = []
    for i in b:
        if kwota >0:
            j = kwota//i
            kwota = kwota - j*i
            lista.append((i,j))
    lista.append(('reszta', kwota))
    print(lista)
    return lista    

#fun6(452)

