class Zlicz:
    ''' 
    Klasa obslugujaca zlicanie linijek, slow i znakow z pliku
    '''
    def __init__(self, filename):
        '''
        Inicjalizacja winna zawierac nazwe pliku do obslugi
        '''
        self.filename = filename
        self.nbr_words = 0
        self.nbr_chars = 0
        self.nbr_lines = 0
        self.zliczanie()
        
    def zliczanie(self):
        '''
        Funkcja zliczajaca linijki, slowa i znaki z zainicjalizowanego pliku
        '''
        file = open(self.filename)

        for line in file:

            line = line.strip("\n")
            words = line.split()

            self.nbr_lines +=1
            self.nbr_words += len(words)
            self.nbr_chars += len(line)

        file.close()

    @staticmethod   
    def wc(filename, *filenames):

        '''
        Metoda statyczna imitujaca linuxowe $wc. 
        Moze przyjac 1 lub wiecej plikow do obslugi.
        Tworzy nowe obiekty klasy Zlicz i obsluguje każdy z nich.
        '''
        
        obj_list = []
        obj_list.append(Zlicz(filename))

        print("$wc ", end='')
        for name in filenames:
            obj_list.append(Zlicz(name))
        
        for obj in obj_list:
            print(obj.filename, end=' ')
        print()

        sum_words = 0
        sum_chars = 0
        sum_lines = 0

        for obj in obj_list:
            sum_words += obj.nbr_words
            sum_chars += obj.nbr_chars
            sum_lines += obj.nbr_lines
            print(obj.nbr_lines, ' ', obj.nbr_words, ' ', obj.nbr_chars)
        print(sum_lines,' ', sum_words,' ', sum_chars, " razem")

#Zlicz.wc("zad1.py", "zad2.py")


