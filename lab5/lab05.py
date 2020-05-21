#### zad 1 ####
print("Zad 1:")

def naturalna():
    n = 1
    yield n
    while True:
        n += 1
        yield n
    
def dzielniki(x):
    if x == 0:
        return None
    list1 = []
    for i in range(1, x//2 +1):
        if (x % i) == 0:
            list1.append(i)
    return list1

def doskonala(seq):
    for i in seq:
        if i == sum(dzielniki(i)):
            yield i        

def mniejsza(seq, x):
    for i in seq:
        if(i <= x):
            yield i
        else:
            break

for i in (doskonala(mniejsza(naturalna(),10000))):
    print(i)    



#### zad 2 ####
print("")
print("Zad 2: ")

from math import log 

def fun2():
    u=0
    x_0=1
    a=0.05
    i=1
    x=1
    
    while x<= 1.5:
        yield x, u, log(x)
        u = u + a/x
        x = x_0 + i*a
        i += 1

for i in fun2():
   print(i)
    


    
### zad 3 ###
print("")
print("Zad 3:")

def fun3(n):
    lista = []
    lista2 = []
    s = 0
    x = 1
    a = n - x
    while a >0:
        if(s + a <= n):
            s += a
            lista.append(a)
        else:
            a -= 1
        if s == n:
            s = 0
            x +=1
            a = n - x
            if lista not in lista2:
                lista3 = lista[:]
                lista2.append(lista3)
                del lista[:]
                yield lista3
            else:
                del lista[:]
        
w = 7
for i in fun3(w):
    print(i," + ", end='')
print("[",w,"]")

#### zad 4 ####

print("")
print("")
print("Zad 4: ")
import random as r


def fun4():
    n = 0
    while True:
        a = r.random()
        if( a < 0.1):
            return
        if((a - n >= 0.40) | (a-n <= 0.40)):
            n = a 
            yield n
     
for i in fun4():
    print(i)


#### zad 5 ####
print("")
print("Zad 5: ")

def MyRange(start,stop=None,step=1.):
    start = float(start)
    if stop == None:
        stop = start
        start = 0.

    while start < stop:
        if step >= 0 and start >= stop:
            return
        elif step < 0 and start <= stop:
            return
        yield start
        start = start + step

print("Casual range: ")
for i in range(8):
    print(i)


'''
print("Test1")  
for i in range(-8):
    print(i)

print("Test2")  
for i in range(1,8):
    print(i)

print("Test3")  
for i in range(8,1):
    print(i)

print("Test4")  
for i in range(1,8,2):
    print(i)

print("Test5")  
for i in range(1, 8, -2):
    print(i)

print("Test6")  
for i in range(8, 1, 2):
    print(i)

print("Test7")  
for i in range(8, 1, -2):
    print(i)
'''
print("My range: ")
for i in MyRange(8):
    print(i)

'''
print("Test1")  
for i in MyRange(-8):
    print(i)

print("Test2")  
for i in MyRange(1,8):
    print(i)

print("Test3")  
for i in MyRange(8,1):
    print(i)

print("Test4")  
for i in MyRange(1,8,2):
    print(i)

print("Test5")  
for i in MyRange(1, 8, -2):
    print(i)

print("Test6")  
for i in MyRange(8, 1, 2):
    print(i)

print("Test7")  
for i in MyRange(8, 1, -2):
    print(i)
'''