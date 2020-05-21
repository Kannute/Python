
class Stack:

    def __init__(self, existing_stack = 0):

        '''
        Tworzenie pustego stosu, jezeli nie podano argumentu, bedacego stosem.
        Inicjalizacje istniejacym stosem, jezeli podany argument jest instancja klasy Stos.
        '''

        if(isinstance(existing_stack, Stack)):
            self.variables = existing_stack.variables
        elif(existing_stack == 0):
            self.variables = []

    def add(self, variable_to_add):
        '''
        Add a variable to stack
        '''
        self.variables.append(variable_to_add)
    
    def erase_variable(self, variable_to_erase):
        '''
        Erase a variable from stack
        '''
        if variable_to_erase in self.variables :
            self.variables.remove(variable_to_erase)
        else:
            print("Could not remove variable - it does not exist in stack")

    def add_stack(self, stack_to_add):
        '''
        Add another stack
        '''
        if(isinstance(stack_to_add, Stack)):
            self.variables += stack_to_add.variables
        else:
            print("Conflicting types of stacks")

    def print_stack(self):
        '''
        Prints values of stack
        '''
        print(f"{self.variables}")

    def size(self):
        '''
        Returns size of stack
        ''' 
        return len(self.variables)

print("Base stack:")
test1 = Stack()
test1.variables.append(1)
test1.variables.append(2)
test1.add(4)
test1.add(5)
test1.print_stack()
print(test1.size())

'''Proszę napisać klasę implementującą stos, klasa ma obsługiwać możliwość tworzenia pustego stosu bądź inicjalizacji istniejącym stosem
 (obiektem klasy), dodawania i usuwania elementu, dodawania elementów innego stosu, zwracania rozmiaru i wypisywania stosu.
Następnie proszę napisać klasę dziedziczącą po klasie stosu i implementującą stos posortowany (rosnąco lub malejąco). 
W tym przypadku element/elementy innego stosu można do stosu dodać pod warunkiem zachowania porządku sortowania.
Proszę sprawdzić jaki jest średni rozmiar posortowanego stosu, który wypełniamy całkowitymi liczbami losowymi z przedziału [0,100]
 losując 100 wartości (średnia po 100 powtórzeniach) (3.(3)p
''' 

class DerivedStack(Stack):
    def add(self, variable_to_add):
        '''
        Sorted stack class
        '''
        if self.size() == 0 :
            self.variables.append(variable_to_add)

        elif(variable_to_add >= self.variables[self.size() -1 ]):
            self.variables.append(variable_to_add)
        
        else:
            print("Variable cannot be appended to sorted stack")
print("Derived stack: ")
test2 = DerivedStack()
test2.add(1)
test2.add(2)
test2.print_stack()
print("Trying to add 1 to the stack:")
test2.add(1)