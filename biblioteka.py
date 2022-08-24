
print("Biblioteka Filmów i Seriali")
print(" ")


class BibliotekaFilmow:
    def __init__(self,tytul,rok_wydania,gatunek,liczba_otworzen):
        self.tytul= tytul
        self.rok_wydania= rok_wydania
        self.gatunek= gatunek
        self.liczba_otworzen= liczba_otworzen
        self.liczba_otworzen= 0
    def __str__(self):
        return f'{self.tytul},{self.rok_wydania}, '

    def play(self, step=1):
        self.liczba_otworzen += step

class BibliotekaSeriali(BibliotekaFilmow):
    def __init__(self, numer_odcinka,numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka= numer_odcinka
        self.numer_sezonu= numer_sezonu
    
    def __str__(self):
        return f'{self.tytul},S{self.numer_sezonu}, E{self.numer_odcinka}'

movie= BibliotekaFilmow(tytul= 'Pulp Fiction',rok_wydania= '1994', gatunek= 'Gangsterski', liczba_otworzen= 0)
movie1= BibliotekaFilmow(tytul= 'Matrix',rok_wydania= '2000',gatunek= 'Fantasy', liczba_otworzen= 0)
movie2= BibliotekaFilmow(tytul= 'Terminator',rok_wydania= '1984',gatunek= 'Wojenny', liczba_otworzen= 0)
movie3= BibliotekaFilmow(tytul= 'X-men',rok_wydania= '2010',gatunek= 'Przygodowy ', liczba_otworzen= 0)

series= BibliotekaSeriali(tytul= 'The Simpsons',numer_sezonu= int(1), numer_odcinka=int(1),rok_wydania= '2010',gatunek= 'Przygodowy ', liczba_otworzen= 0)
series1= BibliotekaSeriali(tytul= 'The Simpsons',numer_sezonu= int(1), numer_odcinka=int(5),rok_wydania= '2010',gatunek= 'Przygodowy ', liczba_otworzen= 0)
series2= BibliotekaSeriali(tytul= 'The Simpsons',numer_sezonu= int(1), numer_odcinka=int(3),rok_wydania= '2010',gatunek= 'Przygodowy ', liczba_otworzen= 0)
series3= BibliotekaSeriali(tytul= 'Pokemon',numer_sezonu= int(1), numer_odcinka=int(1),rok_wydania= '2010',gatunek= 'Przygodowy ', liczba_otworzen= 0)
series4= BibliotekaSeriali(tytul= 'Pokemon',numer_sezonu= int(11), numer_odcinka=int(11),rok_wydania= '2010',gatunek= 'Przygodowy ', liczba_otworzen= 0)

filmy= [movie,movie1,movie2,movie3]
seriale= [series,series1,series2,series3,series4]
biblioteka=[filmy,seriale]



def get_movies():
     print("Sortowanie tytułów filmów alfabetycznie")
     by_tytul = sorted(filmy, key=lambda BibliotekaFilmow: BibliotekaFilmow.tytul)
     for a in by_tytul:
         print (a.tytul, a.rok_wydania)
    

def get_series():
     print('Sortowanie Serialów alfabetycznie: ')
     by1_tytul= sorted(seriale, key=lambda BibliotekaSeriali: BibliotekaSeriali.tytul)
     for i in by1_tytul:
        print(i.tytul,"E0",i.numer_odcinka,"S0",i.numer_sezonu)

def search(szukany_tytul):
    for nazwa in biblioteka:
        if nazwa == szukany_tytul:
            return nazwa
        
search('Pokemon')
get_movies()
get_series()
    

