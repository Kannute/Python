### --------------- ZAD 1 --------------- ###
print("Zadanie 1:")
class WrongLength(Exception):
    pass
class NoPitagorem(Exception):
    pass
class SomethingElse(Exception):
    pass

def IsPitagorem(lista, n):
    try:
        if n > len(lista):
            raise WrongLength
        num = 0
        i = 0
        p = 0
        for i in range(0,n):
            if(i+4 == n):
                a = lista[i]
                b = lista[i+1]
                c = lista[i+2]
                d = lista[i+3]
                if(a**2 + b**2 + c**2 == d**2):
                    num += 1
                    if(a%2==0):
                        p+=1
                    if(b%2==0):
                        p+=1
                    if(c%2==0):
                        p+=1
                    if(d%2==0):
                        p+=1
                    print("For quadriple ", a, b, c, d, "number of even values:", p)
                    p = 0
                    break
            elif(i+3 == n):
                a = lista[i]
                b = lista[i+1]
                c = lista[i+2]
                if(a**2 + b**2 == c**2):
                    num += 1
                    if(a%2==0):
                        p+=1
                    if(b%2==0):
                        p+=1
                    if(c%2==0):
                        p+=1
                    print("For triple ", a, b, c, "number of even values:", p)
                    p = 0
                break
            else:
                a = lista[i]
                b = lista[i+1]
                c = lista[i+2]
                d = lista[i+3]
                if(a**2 + b**2 + c**2 == d**2):                           
                    num += 1
        
                    if(a%2==0):
                        p+=1
                    if(b%2==0):
                        p+=1
                    if(c%2==0):
                        p+=1
                    if(d%2==0):
                        p+=1
                    print("For quadriple ", a, b, c, d, "number of even values:", p)
                    p = 0
                    
                elif(a**2 + b**2 == c**2):
                    num += 1
                    if(a%2==0):
                        p+=1
                    if(b%2==0):
                        p+=1
                    if(c%2==0):
                        p+=1
                    print("For triple ", a, b, c, "number of even values:", p)
                    p = 0                    
                  
        if(num == 0):
            raise NoPitagorem
        else:
            print("Found", num, "Pythagorean triples or/and quadriples")

            
    except SomethingElse:
        print("Something went wrong..")
    except WrongLength:
        print("Given n is exceeds the length of list!")
    except NoPitagorem:
        print("The list does not contain any Pythagorean triples or quadriples")

#l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
#l=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
#l=(1,2,3,4,5,6,7,8,9)

IsPitagorem(l,16)

### --------------- ZAD 2 --------------- ###
print("\nZadanie 2:")
class NotSorted(Exception):
    pass

class NotNumbers(Exception):
    pass

def IsSorted(lista):
    flag = True
    i = 1
    while i < len(lista): 
        if(lista[i] < lista[i - 1]): 
            flag = False
        i += 1
    return flag


def fun1(n, lista):
    try:  
        for i in range(n):
            if(isinstance(lista[i], int)):
                    if(IsSorted(lista)):
                        
                        temp1 = lista[0]
                        temp2 = lista[n-1]
                        R = temp2 - temp1
                        Vavg = lista[n//2]
                        
                        val_list = [R, Vavg]
                        return val_list
                    else:
                        raise NotSorted                            
            else:
                raise NotNumbers
    except SomethingElse:
        print("Given length is wrong!")
    except NotSorted:
        print("The list or tulpe is not sorted!")
    except NotNumbers:
        print("A member of given parameters is not a number!")

lista1 = [1,2,4,5,6]
krotka1 = (1,3,4,12, 11)
lista2 = ["s", 2, 3, 4,5]
wynik = fun1(5, lista1)

if(wynik):
    print("Rozstep:", wynik[0], "Wartosc srodkowa:", wynik[1])

### --------------- ZAD 3 --------------- ###
def samplefun(x):
    return x**2

print("\nZadanie 3:")
class WrongN(Exception):
    pass

def Simpson(f, a, b, n):
    try:
        if a > b:
            raise WrongRange
        if n%2 != 0: 
            raise WrongN

        h = (b - a) / float(2*n)
        sum1 = 0

        for i in range(1, 2*n - 1):
            sum1 += f(i)
        sum1 *= 4

        sum2 = 0
        for i in range(2, 2*n - 2): 
            sum2 += f(i)
        sum2 *= 2

        s = (h/3)*(f(0) + sum1 + sum2 + f(2*n))

        return s

    except SomethingElse:
        print("Something went wrong..")
    except WrongN:
        print("Wrong number of ranges!")
    except WrongRange:
        print("Wrong range!")

wynik = Simpson(samplefun, -100, 100, 50)
print("Dla funkcji x^2:", wynik)

### --------------- ZAD 4 --------------- ###
print("\nZadanie 4:")
class WrongRange(Exception):
    pass
class NoRoots(Exception):
    pass
class Indefinite(Exception):
    pass

def bisection(func, a,b): 
    acc = 1e-7
    try:

        if (func(a) * func(b) >= 0): 
            raise WrongRange

        i = a
        while(i >= b):
            try: 
                func(i)
            except Indefinite:
                print("The function is indefinite!")
            i+= acc
           
        c = a 
        while ((b-a) >= acc): 

            c = (a+b)/2
   
            if (func(c) == 0.0): 
                break
   
            if (func(c)*func(a) < 0): 
                b = c 

            else: 
                a = c 

        if(func(c) == 0.0):      
            print("The value of root is : ","%.2f"%c)
        else:
            raise NoRoots 

    except SomethingElse:
        print("Something bad happened")
    except WrongRange:
        print("Given range is wrong!")
    except NoRoots:
        print("The function has no roots in given range!")

def function(x):
    return x+1
    #return (x-2)*(x-2)/(x-1)-2

bisection(function, -2, 0)