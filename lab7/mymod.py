def newton(n, k):
    if n == k:
        return 0
    if k == 0:
        return 1
    if n == 0:
        return 1
    else:
        return (k+1)*newton(n-1, k) + (n-k)*newton(n-1,k-1)
def pascal(n):
    '''
    Function to print Pascal's triangle
    '''
    temp = n
    t1 = [1]
    t2 = [0]
    for i in range(max(n,0)):
        for _ in range(0,temp):
            print(" ", end='')
        
        print(t1)
        t1=[l+r for l,r in zip(t1+t2, t2+t1)]
        temp -= 1
    return n>=1

def euler(n):
    '''
    Function to print Euler's triangle
    '''
    n1 = 0
    print("n/k ", end='')
    for _ in range(0,n+1):
        print(n1, ' ', end = '')
        n1+=1
    print("")
    
    for step in range(n+1):
        
        print(step,' ', end=' ')

        for tmp in range(n+1): 
            
            val = newton(step, tmp)         
            print(val, ' ', end = '')
            
        
        print('')
        


    

