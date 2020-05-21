import mod
import random as r
import time

def PythonMod(N):
    start_time = time.time()
    punkty = []
    trafiony = 0
    wszystkie = N*10
    for _ in range(0,N):
        x = r.uniform(0, 1)
        y = r.uniform(0, 1)
        punkty.append((x,y))
    
    kwadrat = [0.1 , 0.1]

    for _ in range(0,10):
        for punkt in punkty:
            if (punkt[0] <= kwadrat[0]):
                if (punkt[1] <= kwadrat[1]):
                    trafiony+=1
        kwadrat[0] += 0.1
        kwadrat[1] += 0.1
     
    print('Execution time: ', (time.time() - start_time))
    
    return trafiony / wszystkie
N=100000
print("Python dla N=", N, 'punktow')
procent = PythonMod(N) * 100
print('trafione punkty: ',procent,'%')

print("C dla N=", N, 'punktow')
procent = mod.met(N) * 100
print('trafione punkty: ',procent,'%')