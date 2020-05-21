from zad2 import Wektor

class StaticMethods:

    @staticmethod
    def InductionStream(B, S):
        return B.skalarny(S)
    
    @staticmethod
    def Lorentz(E,v,B,q):
        return q *(E + v.wektorowy(B))
            
    @staticmethod
    def LorentzWork(q,E,v):
        return q* E.skalarny(v)
    
B = Wektor(1,2,3)
S = Wektor(1,2,3)
v = Wektor(1,2,3)
E = Wektor(1,2,3)
q = 3

print(StaticMethods.InductionStream(B,S))
F = StaticMethods.Lorentz(E,v,B,q)
print(F)
print(StaticMethods.LorentzWork(q,E,v))





