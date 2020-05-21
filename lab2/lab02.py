#zad 1 begin
def isPrime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num%i) == 0 :
                #print(num, "nie jest pierwsza")
                return False
            return True
    else:
        #print(num, "nie jest pierwsza")
        return False
#zad 1 end


#zad 2 begin
import random as r


dic1 = {}   

while len(dic1) < 50:
    i=r.randint(0,99)   
    if i not in dic1.keys():
        dic1[i] = isPrime(i)
#print(dic1)    
#zad 2 end

#zad 3 begin

lista1 = []

while len(lista1) < 100:
    i = r.randint(0,11)
    lista1.append(i)


dic2 = {}
k = 0
for i in lista1:
    dic2.setdefault(i,[]).append(lista1.index(i,k))
    k=lista1.index(i,k)+1

#print(lista1)
#print(dic2)
#zad 3 end
    

#zad 4 begin
usrinput = input("Enter a number: ")

dic3 = {}
lista2 = []
for i in range(1,int(usrinput)):
    dic3[i] = r.randint(2,15)
    lista2.append((dic3[i], i))


dic4 = {}
for i in range(1, int(usrinput)):
    dic4[dic3[i]] = i

lista2.append(dic4)
#print(lista2)
#zad 4 end

#zad 5 begin
lista3 = []
for i in range(0,100):
    lista3.append(r.randint(0,20))

even_dic = {}
odd_dic = {}

for i,j in enumerate(lista3):
    if j%2:
        odd_dic.setdefault(j,[]).append(i)
    else:
        even_dic.setdefault(j,[]).append(i)

new_dic = { x:y if [i for i in y if i%3 == 0] else (y[-1],y[0]) for x,y in odd_dic.items() }
#print(new_dic)
#zad 5 end

#zad 6 begin
dic5 = {}
dic6 = {}
for i in range(1,11):
    dic5[i]  = r.randint(1,100)
    dic6[i]  = r.randint(1,100)
#print(dic5)
#print(dic6)

for i in range(1,11):
    tmp = dic5[i]
    del dic5[i]
    dic5[tmp] = i
    tmp = dic6[i]
    del dic6[i]
    dic6[tmp] = i

print(dic6)
print(dic5)

new_dic2 = {  }
for i in dic6.keys():
    if i in dic5.keys():
        new_dic2[i] = (dic5[i], dic6[i])
if len(new_dic2) == 0:
    print("Nie ma takich samych kluczy w slownikach, nowy slownik jest pusty ")
else:
    print(new_dic2)


#zad 6 end