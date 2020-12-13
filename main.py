# print('hello  world!')
# imie='Radek'
# wiek=31
# print('1.hello ' +imie+ '!')
# print('2.hello ' +imie+ ' mam ' + str(wiek) + 'lat')
# print('3.hello {} mam {} lata '.format(imie, 33))
# print(f'4.hello {imie} mam {wiek} lata ')
# print('5.hello', imie, ' mam ', wiek)
# owoc=input('podaj Twój ulubiony owoc!')
# print(f'lubisz owoc {owoc}')
# imie, nazwisko = 'Radek', 'Woz'

# 1. Stwórz program który odbierze od użytkownika jego imię i nazwisko a następnie
# wyświetli powitanie na konsoli typu "Witaj XXXX xxxx" korzystajac
# z imienia i nazwiska podanego przez uzytkownika
# imie,nazwisko=input('podaj swoje imię: '), input('podaj swoje nazwisko: ')
# ##imie=input('podaj swoje imię: ')
# ##nazwisko=input('podaj swoje nazwisko: ')
# print(f'Witaj {imie} {nazwisko}!')

# imie=input('podaj imie:')
# print(type(imie))
# a='teks'
# b=1
# c=1.5
# d= None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# liczba=input('daj liczbę:')
# print(type(liczba))
# liczba = int(liczba)
# print(type(liczba))
# print(1/liczba)

# x = 10 / 3
# print(x)
# print(round(x, 2))

# 2. Napisz program który odbierze od użyszkodnika jego masę i wzrost
# Masa będzie podawana w kilogramach a wzrost w metrach. Program ma
# obliczyć i wyświetlić na konsoli BMI zaokraglone do 2 miejsc po przecinku
# Wzór : masa/(wzrost*wzrost)
# masa = float(input('daj mase w kg:\n'))
# wzrost = float(input('daj wzrost w metrach:\n'))
# wzrostKwadrat = (wzrost * wzrost)
# bmi = round(masa / wzrostKwadrat, 2)
# print('BMI to: ', bmi)

# #instrukcje warunkowe
# x=-1
# print(f'x={x}')
# if x<0:
#     print(f'x={x} jest ujemne')
#     if x ==-1:
#         print(f'x={x} jest ujemne i jest -1')
#     elif x == 0:
#         print(f'x={x} jest ujemne i mniejsz od -1')
# elif x==0:
#     print(f'x={x} jest rowne 0')
# else:
#     print(f'x={x} nie jest ujemne')
#
# print('koniec')

# 3. Napisz program który pobierze od użyszkodnika wzrost i masę, wyświetli
# zaokraglane bmi do 2 miejsc po przecinku i wyswietli komentarz wg. skali na wikipedii

# https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a
# masa = float(input('daj mase w kg:\n'))
# wzrost = float(input('daj wzrost w metrach:\n'))
# wzrostKwadrat = (wzrost * wzrost)
# x = round(masa / wzrostKwadrat, 2)
# print('BMI to: ', x)
# opis = None
# if x<16.0:
#     opis = 'wygłodzenie'
# elif x<17:
#     opis = 'wychudzenie '
# elif x<18.5:
#     opis = 'niedowaga'
# elif x<25:
#     opis = 'pożądana masa ciała'
# elif x<30:
#     opis = 'nadwaga'
# elif x<35:
#     opis = 'otyłość I stopnia'
# elif x<40:
#     opis = 'otyłość II stopnia (duża)'
# else:
#     opis = 'otyłość III stopnia (chorobliwa)'
#
# print('taki BMI to: ', opis)

# for x in range(10):
#     print(x)


# 4. Wyświetl liczby z zakresu 1-100 wyświetlając obok czy dana liczba jest parzysta
# #czy nie.
# for x in range(1,101):
#     if x%2==0:
#         print(f'{x} parzyste')
#     else:
#         print(f'{x} jest nieparzyste')

# 5. Napisz symulator lokaty. Program ma przez zmienne przyjąć:
#  - kwotę lokowaną
#  - czas trwania lokaty w miesiącach
#  - oprocentowanie w skali roku
# Symulator ma dla każdego miesiąca wypisywać który jest to miesiąc oraz ile aktualnie mamy
# na koncie

# liczbaMiesiecy=12
# kwota = 100000
# oproc = 3
# podatekBelki = 1 - 0.19
# for x in range(1, liczbaMiesiecy + 1):
#     kwota = (((kwota * oproc/100)/12)*podatekBelki) + kwota
#     print(f'w miesiacu nr {x} wartosc depozytu to {round(kwota,2)}')

# x=10
# while x>0:
#     print(x)
#     #x=x-1
#     x=-1


# 5. Napisz program który będzie wypisywał kolejne potęgi liczby 2 aż potęga przekroczy
# wartość zdefiniowaną w osobnej zmiennej.
#
# wynik=0
# potega=1
# while True:
#     print(pow(2,potega))
#     potega=potega+1

#
# wynik=0
# potega=1
# limit=2000
# while True:
#     wynik=pow(2,potega)
#     print(wynik)
#     potega+=1
#     if wynik>limit:
#         break

#
# wynik=0
# potega=1
# limit=2000
# while wynik<limit:
#     wynik=pow(2,potega)
#     print(wynik)
#     potega+=1
#
# x=2000
#
# #5
# limit = 2000
# x= 2
# y= x
# while x < limit:
#     print(x)
#     x = x*y

# 6
# 6. Napisz symulator kredytu. Symulator ma przez zmienne przyjąć:
# - kwotę kredytu
# - oprocentowanie w skali roku
# - wysokość raty
# Program ma wyswietlać kolejne miesiace oraz stan kredytu do zapłaty.
# Przy każdym miesiącu należy doliczyć odsetki oraz odjąć ratę.
# Program ma działać tak długo aż kredyt zostanie w całości spłacony.
# Pamiętaj że ostatnia rata może być wyższa niż pozostała do spłaty kwota - nie powinniśmy
# wtedy wchodzić na ujemny stan kredytu.

# kwota = 150000
# oproc = 0.01
# rata = 2000
# odsetki = 0
# liczbaRat = 0
# print(f'kwota startowa: {kwota}')
# while kwota>0:
#     liczbaRat+=1
#     odsetki = (kwota * oproc/12)
#     kwota = kwota + odsetki
#     if(kwota > rata):
#         kwota -= rata
#     else:
#         kwota = 0
#     print(f'rata nr {liczbaRat}, kwota pozostala: {kwota}, aktualna rata: {rata}, naliczone odsetki {odsetki}')

# for y in range(11):
#     for x in range(11):
#         print(y, x)
#
# tekst= "  Ala ma kota, a ja nie mam psa  "
#
# print(tekst.upper())
# print(tekst.lower())
# print(tekst.title())
# print(tekst.replace('ja', 'XXXXX'))
# print(tekst.count('a'))
# print(tekst.strip())
# print(tekst.title())
# print(tekst.split())
# print(len(tekst))
# print(len('jakiś tekst'))
# lista=[1, 4, 223, 23432]
# print(len(lista))
#
# csv='1;sdasdas;23123;fffff;'
# print(csv.split(';'))
#
# for literka in tekst:
#     print(literka)
#
# print('hajs '*7)
#
# tekst= "Ala ma kota, a ja nie mam psa  "
# print(tekst[2])
# print(tekst[2:])
# print(tekst[2:10])
# print(tekst[-3])
#
# print(tekst.find('p'))

# 7. Napisz program który dla pliku którego nazwę podamy przez zmienną wykona działanie:
#   wyświetlenie aktywnych linii - czyli tych które nie zaczynają się od znaku #
#   wyświetlany ma byc numer linii oraz kod znajdujący się w tej linii

# komentarz
# x=1 #komentarz
#     #komentarz
# activeLine = 0
# for linia in open('main.py',encoding='utf-8'):
#     x+=1
#     l = linia.strip()
#     if len(l) > 0 and l[0] != '#':
#         activeLine+=1
#         print(x, linia)
# print('activeLine: ', activeLine)

# lista = list()
# lista=[]
# lista=['siała', 'baba', 'mak', 1, 4, 'coś']
# lista.append('na końcu')
# lista[1]='dziad'
# lista.insert(2, 'po dziadzie')
# lista.remove('dziad')
# lista[1]=None
# del lista[1]
# print(lista)
# print(lista[2])
# print(lista[0:2])
# for e in lista:
#     print(e)
#
# lista=['siała','baba','mak',1,4,'coś']
# lista[1]=None
# lista.remove('dziad')
# print(lista)
# del lista[1]
# print(lista)

# 8. Napisz program który utworzy listę zawierającą 10 kolejnych potęg liczby 2.
#   Następnie przeiteruj po tej liście i wyswietl jej kolejne elementy na konsoli
#
# x=0
# potega=1
# lista=[]
# for i in range(1,11):
#     lista.append(pow(2,i))
#
# for j in lista:
#     print(j)
# print(lista)


# 9. Napisz program który odczyta plik zawodnicy.csv i dla każdego zawodnika
# wyświetli jego imię, wzrost, masę oraz obliczone BMI.
#
# plik = open('zawodnicy.csv',encoding='utf-8')
# print(plik)
#
# for linia in plik:
#     #print(linia)
#     index = 0
#     wzorst = 0
#     waga = 0
#     for osoba in linia.split(';'):
#         if (index == 0):
#             print(f'Nr {osoba}')
#         if(index == 1):
#             print(f'imie {osoba}')
#         elif(index == 2):
#             print(f'wzrost {osoba}')
#             wzorst = float(osoba)
#         elif (index == 3):
#             print(f'waga {osoba}')
#             waga = float(osoba)
#             print(f'BMI to {waga/wzorst*wzorst}')
#
#         index+=1


# 9.A Napisz program który odczyta plik zawodnicy.csv i dla każdego zawodnika
# wyświetli jego imię, wzrost, masę oraz obliczone BMI.


# for linia in open('zawodnicy.csv',encoding='utf-8'):
#     if len(linia.strip())>0:
#         lista=linia.strip().split(';')
#         masa=float(lista[3].replace(',','.'))
#         wzrost=float(lista[2].replace(',','.'))
#         bmi=round(masa/pow(wzrost,2),2)
#         print(lista[1],wzrost,masa,bmi)

# tekst='siała baba mak'
# if 'bab' in tekst:
#     print('jest')

# lista=['siala','baba','mak']
# if 'bab' in lista:
#     print('znaleziono')
# else:
#     print('nie znaleziono')
#
# lista=['siala','baba','mak']
# for element in lista:
#     if 'bab' in element:
#         print(f'znaleziono w {element}')
#     else:
#         print('nie znaleziono')
#
# lista=['siala','baba','mak']
# print(lista)
# print( ';'.join(lista)  )
# if 'bab' in ' '.join(lista):
#     print('jest bab')

# lista=[1,2,3,4,5]
# lista2=[]
# for e in lista:
#     lista2.append(e*2)
# print(lista2)

# lista=[1,2,3,4,5,6,7,8,9,10]
# lista2=[e*2 for e in lista]
# print(lista2)
#
# lista=[1,2,3,4,5,6,7,8,9,10]
# lista2=[e*2 for e in lista if e>5]
# print(lista2)

# 9. Stwórz taką listę:
# lista=['siała','baba','mak']
# Korzystając z list składanych przepisz tą listę do innej listy ale powiększając każdy element
# do dużych liter.

# lista=['siała','baba','mak']
# lista2=[e.upper() for e in lista]
# print(lista2)


# 10. Stwórz listę która będzie zawierała pod postacią list kolejne linie z pliku zawodnicy.csv
# Czyli chcemy otrzymać listę list - czytli każdy element listy tez jest listą.
# Postaraj się użyć tutaj list składanych. Nie ładuj do listy wynikowej linii bez danych
# Następnie przeiteruj po wynikowej liście list i wyświetl każdy element na konsoli.

# lista2 = []
#
# for linia in open('zawodnicy.csv',encoding='utf-8'):
#     if len(linia.strip())>0:
#         lista=linia.strip().split(';')
#         lista[3]=float(lista[3].replace(',', '.'))
#         lista[2]=float(lista[2].replace(',', '.'))
#         lista.append(round(lista[3]/pow(lista[2],2),2))
#         lista2.append(lista)
# print(lista2)
#
# lista3=[e.strip().split(';') for e in open('zawodnicy.csv', encoding='utf-8') if len(e.strip())>0]
# for e in lista3:
#     print(e)
# print(lista3)

#
# lista=[e for e in open('zawodnicy.csv',encoding='utf-8') ]
# print(lista)

# lista=[e for e in open('zawodnicy.csv',encoding='utf-8') if len(e.strip())>0]
# print(lista)

# lista=[e.strip().split(';') for e in open('zawodnicy.csv',encoding='utf-8') if len(e.strip())>0]
# for e in lista:
#     print(e)


# sortowanie
#
# lista = ['Adam', 'Zenek', 'Radek', 'Baba']
# lista.sort()
# print(lista)
#
# lista.sort(reverse=True)
# print(lista)
#
#
# lista = ['Adam', 'Zenek', 'Radek', 'Baba']
# lista.sort()
# lista.reverse()
# print(lista)
#
#
# lista = ['Adam', 'Zenek', 'Radek', 'Baba', '123']
# lista.sort()
# print(lista)
#
#
# lista_list = [
#     ['B',3],
#     ['C',1],
#     ['A',2]
# ]
#
# from operator import itemgetter
# print(lista_list)
# lista_list.sort()
# print(lista_list)
# lista_list.sort(key=itemgetter(0))
# print(lista_list)
# lista_list.sort(key=itemgetter(1))
# print(lista_list)

# 11. Wyświetl listę list danych pochodzących z zawodnicy.csv w taki sposob by
# zawodnicy ci byli posortowani malejąco po masie.
#
# from operator import itemgetter
# lista=[e.strip().split(';') for e in open('zawodnicy.csv',encoding='utf-8') if len(e.strip())>0]
# for e in lista:
#     e[2]=float(e[2].replace(',', '.'))
#     e[3] = float(e[3].replace(',', '.'))
# lista.sort(key=itemgetter(3), reverse=True)
# for e in lista:
#     print(e)
# print(lista)

# lista = [1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 1]
# print(len(lista))
# print(sum(lista), (lista), min(lista))
# print(lista.count(1))

# 12. Wyświetl średnią wartość dla listy: lista=[1,2,3,4,5,6,7,8,9,1,1,1,1,1]

# lista=[1,2,3,4,5,6,7,8,9,1,1,1,1,1]
# print(  sum(lista)/len(lista)  )
# tuple
# krotka=(1,2,3,4,1,1,1)
# #krotka[3]=6 #fuuu
# #lista.sort() # fuuu
# #print(krotka[0:3])
# #print(krotka.count(1))
# lista=list(krotka)
# print(type(krotka),type(lista))
# lista.sort()
# krotka=tuple(lista)
# print(krotka)
#
# zestaw={1,2,1,2,1,1,1,1,3}
# zestaw.add(4)
# print(zestaw)
#
# lista=[1,2,3,1,2,3,4,1,2,3,4]
# zestaw=set(lista)
# lista=list(zestaw)
# print(lista)

#
# lista=[1,2,3,1,2,3,4,1,2,3,4]
# lista=list(set(lista))
# print(lista)
#
# zestaw={1,1,1,1,1,2,3,4}
# zestaw.remove(4)
# print(zestaw)

# set
# zestaw={
#     (1,'A'),
#     (1,'B'),
#     (2,'A'),
#     (1,'A')
# }
# print(zestaw)
#
# dist
# slownik=dict()
# slownik['ABC']='Bulbulator'
# slownik['EFG']='Wihajster'
# slownik['HIJ']='Przyczłap do bulbulatora'
# slownik['ABC']='Taki teges'
# del slownik['HIJ']
# print(slownik)
# print(slownik['ABC'])

# for k in slownik.keys():
#     print(k,slownik[k])

# for w in slownik.values():
#     print(w)

# 13. Wczytaj dane z zawodnicy.csv w do słownika w taki sposób by kluczem było imię a wartością
# krotka zawierająca wzrost i masę. Następnie przeiteruj po słowniku i wyświetl z niego dane.

# lista = [e.strip().split(';') for e in open('zawodnicy.csv', encoding='utf-8') if len(e.strip()) > 0]
#
# slownik = dict()
# for l in lista:
#     krotka = (l[2], l[3])
#     slownik[l[1]] = krotka
#
# for k in slownik.keys():
#     print(k, slownik[k])
# print(slownik)
#
# slownik2 = dict()
# for e in open('zawodnicy.csv', encoding='utf-8'):
#     if len(e.strip()) > 0:
#         l = e.strip().split(';')
#         slownik2[l[1]] = (l[2], l[3])
#
# print(slownik)


# slownik=dict()
# slownik['NIETOPERZ']='COŚ'
# slownik['PARÓWKA']='COŚ'
# if 'NIETOPERZ' in slownik.keys():
#     print('mamy nietoperza')

# 14. Wyświetl posortowane malejąco po ilości wystąpień wszystkie słowa z Pana Tadeusza....

# Tadeusz 1300
# Pan 1123

# 1) Odczytać plik i każdą z jego linii rozbić na słowa które następnie dodajemy do listy
#    W liście takiej jedno słowo może pojawiać się wielokrotnie
# 2) Iterujemy po liście z powtórzeniami i usuwamy jakieś dziwne znaki typu !?>> i unifikujemy do jednej wielkości
# 3) Tworzymy pusty słownik
# 4) Iterujemy słowo po słowie z naszej listy i jeśli w słowniku nie występuje jeszcze wartość dla klucza takiego
#    jak dane słowo to dodajemy wpis do słownika pod takim kluczem i wartością 1, jeśli natomiast słowniku występuje
#    już wartość pod takim kluczem to zwiększamy go o 1
# 5) Przerób słownik na listę list lub krotek
# 6) Posortuj wg krotności wystąpień
# 7) Wyświetl wynik na konsoli.

### text = [e.strip().split(' ') for e in open('tadzio.txt', encoding='utf-8') if len(e.strip()) > 0]
### print(text)
# import time
# początek = time.time();
# niechciane = [',', '!', '.', '?', '—', ':']
# lista = list()
# slownik = dict()
# for linia in open('tadzio.txt', encoding='utf-8'):
#     if len(linia.strip()) > 0:
#         for n in niechciane:
#             linia = linia.replace(n,'')
#         linia=linia.lower()
#         lista_wyrazow_w_lini = linia.strip() .split()
#         for wyraz in lista_wyrazow_w_lini:
#             lista.append(wyraz)
#             if wyraz in slownik.keys():
#                 slownik[wyraz] += 1
#             else:
#                 slownik[wyraz] = 1
#
# wynik = list()
# for k in slownik:
#     #if(len(k)> 1):
#         wynik.append([k, slownik[k]])
#
# from operator import itemgetter
# wynik.sort(key=itemgetter(1))
# print(wynik)
#
# koniec = time.time()
# print(koniec-początek)

# wersja od porwadzącego

# import time
# from operator import itemgetter
#
# poczatek=time.time()
# lista=[]
# niechciane=[',','!','…',';','.',':','?','-','—']
# for linia in open('tadzio.txt',encoding='utf-8'):
#     if len(linia.strip())>0:
#         for n in niechciane:
#             linia=linia.replace(n,'')
#         linia=linia.lower()
#         for e in linia.split():
#             lista.append(e)
#
# slownik=dict()
# for slowo in lista:
# #    x=lista.count(slowo) # fuuuuu, złożoność obliczeniowa!
#     if slowo not in slownik.keys():
#         slownik[slowo]=1
#     else:
#         slownik[slowo]=slownik[slowo]+1
#
# wynik=[]
# for k in slownik:
#    #print(k,slownik[k])
#     wynik.append(  (k,slownik[k])  )
# wynik.sort(key=itemgetter(1),reverse=True)
# # for w in wynik:
# #     print(w)
# koniec=time.time()
# print(koniec-poczatek)

#
# try:
#     print(1/0)
#     print('coś jeszcze')
# except Exception as e:
#     print(f'nie dziel przez zero: {e}')

#
# try:
#     print(1/0)
#     print('coś jeszcze')
# except IOError:
#     print('I/O error')
# except ZeroDivisionError:
#     print('nie dziel przez zero')
# except Exception as e:
#     print(f'jakiś wyjątek: {e}')

# raise Exception('to jest mój wyjątek')

# 15. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.
# Zadbaj o to by w przypadku pojawienia się wyjątku program nie przerywal pętli.

# for x in range(-10, 11):
#     try:
#         print(x, 1/x)
#     except ZeroDivisionError:
#         print('nie dziel przez zero')

# def witacz():
#     print('witajcie wszyscy')
# ##przesłanianie, nie ma przeciążania
# def witacz(imie):
#     print(f'siema {imie}')
# # witacz()
# witacz('Radek')
# def witacz(imie, nazwisko):
#     print(f'siema {imie} {nazwisko}')
# witacz('Radek', 'Woz')
#
# def dajKoze():
#     return 'koza'
# print(dajKoze())

# def dajliczbe():
#     try:
#         pass
#     except:
#         #obsługa wyjątku
#         return -1
#     return 13

# 16. Napisz funkcję która przyjmie wzrost i masę a zwróci zaokraglone do 2 miejsc
# po przecinku BMI. Jeśli wzrost zostanie podany w centymetrach zamiast metrach
# to wyrzuć odpowiedni wyjątek.

# def bmi(w,m):
#     if w>3:
#         raise Exception('podałeś wzrost w cm zamiast w m')
#     b=m/pow(w,2)
#     return round(b,2)
#
# print ( bmi(1.76,80) )
# print ( bmi(176,80) )
# def obliczBMI(wzrost, masa):
#     try:
#         if wzrost > 2.5:
#             raise Exception('Wzrost w CM, podaj w metrach!!!')
#     except Exception as e:
#         print(f'Wyjątek: {e}')
#         return -1
#     wynik = round(masa/pow(wzrost, 2),2)
#     print(f'BMI dla masy {masa} i wzrostu {wzrost} to {wynik}')
#     return wynik
#
# obliczBMI(1.9, 90)

# 17. Napisz funkcje która przez argument przyjmie nazwę pliku csv
# a następnie zwróci dane ze wskazanego pliku csv w postaci tablicy tablic.
# funkcja nie powinna zwracać pustych linii

# def readCSVasTable(plik):
#     wynik = list()
#     lista = list()
#     for linia in open(plik, encoding='utf-8'):
#         if len(linia.strip()) > 0:
#             lista=linia.strip().split(';')
#             lista[0] = int(lista[0])
#             lista[3] = float(lista[3].replace(',', '.'))
#             lista[2] = float(lista[2].replace(',', '.'))
#             #lista.append(round(lista[3]/pow(lista[2],2),2))
#             wynik.append(lista)
#     print(wynik)
#     return (wynik)
#
# readCSVasTable('zawodnicy.csv')

# 17.(Prowadzącego) Napisz funkcja która przez argument przyjmie nazwę pliku csv
# a następnie zwróci dane ze wskazanego pliku csv w postaci tablicy tablic.
# funkcja nie powinna zwracać pustych linii
#
# def parser(filename):
#     return [e.strip().split(';') for e in open(filename,encoding='utf-8') if len(e.strip())>0]
#
# for e in parser('zawodnicy.csv'):
#     print(e)
#
# import csv
# #csv reader -- otwieramy kolejne linijki pliku jako listy
# with open('zawodnicy.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ';')
#     #next(csv_reader) #<-- csv reader jest generatorem, więc za pomocą next mogę przeskoczyć jedną linijkę ręcznie
#     for row in csv_reader:
#         print(row)
#
# def witacz(x, imie = 'Nieznajomy'):
#     print(f'Witaj {imie}')
#     print(f'x {x}')
# witacz(111)

# 18. Do rozwiązania z ćwiczenia 17 dodaj jeszcze opcjonalny argument encoding który
#  będzie przekazywany do open. W przypadku braku podania kodowania chcemy przyjąć utf-8

# def parser(filename, enc='utf-8'):
#     """To jest help do naszej wspalaniej funkcji
#     autor RW
#     """
#     print(f'kodowanie={enc}')
#     return [e.strip().split(';') for e in open(filename, encoding=enc) if len(e.strip())>0]
#
# for e in parser('zawodnicy.csv'):
#     print(e)
#
# help(parser)

# def pomnoz(x):
#     return x*2
#
# def podziel(x):
#     return x/2
#
# def printuj(fun,y):
#     print( fun(y)  )
#
# printuj(pomnoz,10)
# printuj(podziel,10)
# printuj(11,1)
#
# def funkcja(y):
#     def podfunkcja(x):
#         return x*2
#     return podfunkcja(y)
#
# print(funkcja(10))

# def funkcja():
#     def podfunkcja(x):
#         return x*2
#     return podfunkcja
#
# podf=funkcja()
# print(podf(40))
#
# def funkcja():
#     def podfunkcja(x):
#         return x*2
#     return podfunkcja
#
# podf=funkcja()
# print(podf(40))
#
# def doopakowania():
#     print('czynności')
#
# def dekorator(fun):
#     def opakowujaca():
#         print('opakowanie przed')
#         fun()
#         print('opakowanie po')
#     return opakowujaca
#
# dek=dekorator(doopakowania)
# dek()
#
# def dekorator(fun):
#     def opakowujaca():
#         print('opakowanie przed')
#         fun()
#         print('opakowanie po')
#     return opakowujaca
#
# @dekorator
# def doopakowania():
#     print('czynności')
#
# doopakowania()

# import time
# def dekorator(fun):
#     def opakowujaca():
#         przed=time.time()
#         fun()
#         po=time.time()
#         print(f'czas działania funkcji {po-przed}')
#     return opakowujaca
#
# @dekorator
# def doopakowania():
#     print('czynności')
#     time.sleep(3)
#
# doopakowania()

# 19. Stwórz dwie funkcje. Jedna ma zwracać powiększony tekst który otrzyma przez argument,
#    druga ma zwracać pomniejszony tekst który otrzyma jako argument. Dodaj funkcję
#    która będzie przyjmować przez argument inną funkcję oraz ciąg tekstowy do obróbki,
#    który po obrobieniu przez funkcję z argumentu zostanie wyświetlony na konsoli.

# def powieksz(tekst):
#     return tekst.upper()
#
#
# def pomniejsz(tekst):
#     return tekst.lower()
#
# def przyjmujaca(fun,param):
#     print(fun(param))
#
# przyjmujaca(powieksz, 'Radek')
# przyjmujaca(pomniejsz, 'Radek')

# 20. Stwórz funkcje która będzie posiadała dwie funkcje wewnętrzne. Jedna
#    ma zwracać powiekszony otrzymany ciąg znaków, druga pomniejszony otrzymany
#    ciąg znaków. Funkcja zewnętrzna ma zwracać funkcję powiększającą gdy zostanie
#    jej podana przez argument wartość 1 a pomniejszającą gdy zostanie jej podana przez
#    argument wartość 2. Odbierz obiekt funkcji wewnętrznej poprzez wywołanie
#    funkcji zewnętrznej i zastosuj otrzymaną funkcję na ciągu tekstowym.
#
# def zewnetrzna(arg):
#     def powieksz(tekst):
#         return tekst.upper()
#     def pomniejsz(tekst):
#         return tekst.lower()
#     if arg == 1:
#         return powieksz
#     else:
#         return pomniejsz
#
# funk1 = zewnetrzna(1)
# print(funk1('Radek'))
# funk1 = zewnetrzna(2)
# print(funk1('Radek'))

# def funkcja(*args):
#     for a in args:
#         print(a)
# funkcja(1,2,3,4)
# funkcja('koza','nietoperz',13)
#
# def funkcja(**kwargs):
#     for k in kwargs:
#         print(k, kwargs[k])
# funkcja(param1= 'koza', param2= 'nietoperz',p3=13)

# 21 Stwórz funkcję która wydrukuje na konsoli sumę wartości przekazanej do niej jako *args.
#
# def funkcja(*args):
#     # suma = 0
#     # for a in args:
#     #     suma += a
#     print(sum(args))
# funkcja(1,2,3,4,444)
#
# def funkcja(param, *args):
#     print(param + sum(args))
#
# funkcja(0,1,2,3,4,444)

# 22. Stwórz funkcję która przyjmie przez argument mnożnik oraz elementy typu *args.
#     Funkcja ma dla każdego elementu typu args wyświetlić na konsoli wynik jego mnożenia
#     przez mnożnik

# def funkcja(mnoznik, *liczby):
#         for i in liczby:
#             print(mnoznik * i)
#
# funkcja(10,1,2,3,4,5)

# 23. Stwórz funkcję "parse" która będzie otrzymywała przez argumenty wartość tekstową
#    oraz *args funkcji. Funkcja ta ma zastosować każdą z otrzymanych przez *args funkcji na
#    wartości tekstowej którą następnie wypisze na konsoli.
#
#    Dodaj funkcję "powieksz" i
#   "podziel" które mają zwracacać otrzymane przez argument dane odpowiednio po powiększeniu
#   i podzieleniu tekstu na słowa. Wywołaj funkcję "parse" przekazując do niej ciąg tekstowy
#   składający się z więcej niż 1 słowa oraz funkcje "powieksz" i "podziel"

# def parse(tekst, *funkcje):
#     for f in funkcje:
#         print(f(tekst))
#
# def powieksz(tekst):
#     return tekst.upper()
# def pomniejsz(tekst):
#     return tekst.lower()
# def a(tekst):
#     return tekst.capitalize()
# def b(tekst):
#     return tekst.title()
# def podziel(tekst : str):
#     return tekst.split()
#
# parse('RadeK AbCdE', powieksz, pomniejsz,a,b, podziel)

#
# def funkcja():
#     wynik=[e for e in range(100)]
#     return wynik
#
# for i in funkcja():
#     print(i)
#
# def elementy():
#     yield 'element 1'
#     yield 'element 2'
#     yield 'element 3'
#     yield 'element 4'
#
#
# for e in elementy():
#     print(e)


# import time
# def elementy():
#     yield 'element 1'
#     time.sleep(1)
#     yield 'element 2'
#     time.sleep(1)
#     yield 'element 3'
#     time.sleep(1)
#     yield 'element 4'
#
#
# for e in elementy():
#     print(e)

# def myrange(n):
#     for x in range(n):
#         yield x*10
#
# for e in myrange(40):
#     print(e)


# def elementy():
#     yield 'element 1'
#     yield 'element 2'
#     yield 'element 3'
#     yield 'element 4'
#
#
# e=elementy()
# print(next(e))
# print(next(e))
#
# def funkcja():
#     x=0
#     while True:
#         x+=1
#         yield x*10
#
# # for e in funkcja():
# #     print(e)
#
# f=funkcja()
# for x in range(10):
#     print(next(f))
# f=funkcja()
# print('####',next(f))

# 24. Stwórz generator które będzie podawał kolejne dni tygodnia. Przeiteruj po nim.
#
# def podawajDni():
#     list = ['pon', 'wt', 'sr', 'czw', 'pt', 'sb', 'nd']
#     for i in list:
#         yield i
#
# f=podawajDni()
# for e in range(1,4):
#     print(e, next(f))
#
# print('###', next(f))
# print('###', next(f))
# print('###', next(f))

# 25. Stwórz generator który będzie podawał nieskończenie wiele liczb parzystych.
#    Przetestuj go pobierając kilka wartości i wyswietlając je na konsoli
# def podawajNieskonczenieWieleLiczbParzystych():
#     liczba = 0
#     while True:
#         liczba += 2
#         yield liczba
#
# f = podawajNieskonczenieWieleLiczbParzystych()
# for e in range(1, 111111):
#     print(next(f))

# plik=open('zawodnicy.csv')
# linia=plik.readline()
# print(linia)
# linia=plik.readline()
# print(linia)
# linia=plik.readline()
# print(linia)
# linia=plik.readline()
# print(linia)

# 26.Napisz funkcję która będzie czytała plik którego nazwę podamy jako argument
#   LINIA PO LINII tak długo aż znajdzie ciąg tekstowy podany jej jako drugi argument.
#   linię ze znalezioną wartością należy wyświetlić

# def czytajLiniePoLini(nazwaPliku, poszukiwany):
#     plik = open(nazwaPliku)
#     linia = ''
#     while True:
#         linia = plik.readline()
#         if poszukiwany in linia:
#             print(linia)
#             break
# czytajLiniePoLini('zawodnicy.csv', 'Krzysiek')

# 27. Stwórz generator który bedize podawał kolejne linie z pliku tekstowego
#    którego nazwę podamy jako argument generatora. Przetestuj generator pobierając kilka linii.
#    Generator nie powinien wczytywać całego pliku od razu, a w miarę żądania kolejnych elementów
#    powinien wczytywać kolejne linie z pliku. Użycie funkcji readlines() na obiekcie pliku
#    będzie tu więc niewłaściwe, ponieważ wczytuje ona od razu cały plik, a to mogłoby
#    doprowadzić do przepełnienia pamięci. Przykład czytania pliku linia po linii

# def kolejneLinie(nazwaPliku):
#     plik = open(nazwaPliku)
#     while True:
#         linia = plik.readline()
#         if not linia:
#             break
#         yield linia.strip()
#
# gen = kolejneLinie('zawodnicy.csv');
#
# try:
#     while 1:
#         print(next(gen))
# except StopIteration:
#     print('Koniec!!!!')
# except Exception as e:
#     print(f'Inny błąd: {e}')

# plik=open('zawodnicy.csv')
# linia=plik.readline()
# print(linia)
# linia=plik.readline()
# print(linia)
# plik.seek(3)
# linia=plik.readline()
# print(linia)
# linia=plik.readline()
# print(linia)

# print( len( plik.readlines() ) )
#
# plik=open('zawodnicy.csv')
# calosc=plik.read()
# print(calosc)
# print(len(calosc))
#
# plik=open('peppa.jpg',mode='rb')
# for x in range(10):
#     kawalek=plik.read(2)
#     print(kawalek)
#
# help(open)

# plik=open('plik.txt', mode='w', encoding='utf-8')
# for x in range(10):
#     plik.write((f'jakaś linia numer {x}\n'))


# 28. Napisz funkcję która przyjmie przez argumenty nazwy pliku wejsciowego i wyjsciowego.
#   Funckcja ma dzialac w ten sposob ze zaczytuje plik wejsciowy (zawodnicy.csv) i
#   wyrzuca dane do pliku wyjściowego ale z obliczonym bmi. Czyli przepisujemy ale z dodaniem
#   jednej kolumny.

# def przepisz(plikWej, plikWyj):
#     plik1 = open(plikWej, encoding='utf-8')
#     plik2 = open(plikWyj, mode='w', encoding='utf-8')
#     wynik = [e.strip().replace(',', '.').split(';') for e in plik1 if len(e.strip()) > 0]
#     for w in wynik:
#         wzrost = float(w[2])
#         masa= float(w[3])
#         bmi = str(round(masa/pow(wzrost, 2), 2))
#         w.append(bmi)
#         print(w)
#         plik2.write(';'.join(w) + "\n")
#     plik2.close()
#
# przepisz('zawodnicy.csv', 'zawodnicy2.csv')

# 29. Stwórz funkcję która zapisze do pliku w formacie CSV wszystkie
#    argumenty wraz z wartościami przekazne do funkcji jako **kwargs
# wywołanie:
# funkcja(param1= 'samolot', param2= 'nietoperz')
# fukcja(param1='nietoperz', param2='samolot', param3= 'koza', param4= 'nietoperz', p5='sdsd')
# zawartość pliku CSV
# param1;nietoperz
# param2;samolot

# def fukcja(**kwargs):
#     plik = open('kwargs.csv', mode='w', encoding='utf-8')
#     for k in kwargs:
#         plik.write(k + ';' + kwargs[k] + "\n")
#         plik.write(f'{k};{kwargs[k]}\n')
#     plik.close()
#
# fukcja(param1='nietoperz', param2='samolot', param3= 'koza', param4= 'nietoperz', p5='sdsd')

# import modul
# print(modul.monozenie(2, 2))
#
# import modul as m
# print(m.monozenie(2, 2))

# from modul import monozenie, dzielenie
# from modul import *
# print(monozenie(2, 2))

# def moja():
#     print('funkcja moja z głównego pliku')
# from modul import moja
#
# moja()

# 30. Stwórz moduł który będzie zawierał generator podający nieskończenie wiele
#    potęg liczby dwa (zaczynając od pierwszej potęgi)
# from modul import potegi2
# gen = potegi2()
# for i in range(1, 12):
#     print(i, next(gen))

# import bajery
# f=bajery.generator_poteg_liczby_2()
# for x in range(20):
#     print(next(f))

# import bajery
# f=bajery.generator_poteg(5)
# for x in range(10):
#     print(next(f))

# from pakiet.podmodul import pisz
# pisz()
# from pakiet.podpakiet.ppm import pisze
# pisze()


# http://jsystems.pl/static/blog/python/dane.json
# http://jsystems.pl/Universe/samaTabelka.do

#
# podslownik=dict()
# podslownik['pole']='wartość w podsłowniku'
#
# slownik=dict()
# slownik['tekst']='jakaś wartość tekstowa'
# slownik['lista']=[1,2,3,4,5]
# slownik['slownik']=podslownik
#
# print(slownik)
# print(slownik['tekst'])
# for e in slownik['lista']:
#     print(e)
# print(slownik['slownik']['pole'])

# import requests
# response=requests.get('http://jsystems.pl/static/blog/python/dane.json')
# print(response.status_code)
# if response.status_code==200:
#     dane=response.json()
#     print(dane)
#
#
# import requests
# response=requests.get('http://jsystems.pl/static/blog/python/dane.json')
# print(response.status_code)
# if response.status_code==200:
#     dane=response.json()
#     print(dane['imie'])
#     print(dane['adres']['miasto'])
#     for e in dane['jezyki']:
#         print(e)

#
# import requests
# dane=dict()
# response=requests.post('http://jsystems.pl/static/blog/python/dane.json',
#                        data=dane, headers={"Content-Type":"application/json"}, auth=('user','pass'))
# print(response.status_code)


# 31. Odwołaj się do usługi sieciowej znajdującej się pod:
#    http://jsystems.pl/Universe/samaTabelka.do
#    Wyświetl na konsoli informacje o gwarantowanych terminach szkoleń z kategorii python (data,miasto, tytul szkolenia)
#
# import requests
# response=requests.get('http://jsystems.pl/Universe/samaTabelka.do')
# print(response.status_code)
# if response.status_code == 200:
#     lista=response.json()
#     print(lista)
#
#     wynik=[(e['termin'], e['miasto'], e['tytul_szkolenia']) for e in lista if "python" in e['tytul_szkolenia'].lower() and e['terminyGwarantowany'] == 1]
#     for w in wynik:
#         print(w)
#
#     ##moje
#     ## for dict in lista:
#     ##     for k in dict:
#     ##         #print(k, dict[k])
#     ##         if 'python' in dict['tytul_szkolenia'].lower() and dict['terminyGwarantowany'] == 1 and dict['miasto'] == 'Warszawa':
#     ##             print(k, dict[k])
#
# import requests
# response=requests.get('http://jsystems.pl/Universe/samaTabelka.do')
# if response.status_code==200:
#     lista=response.json()
#     wynik=[]
#     for e in lista:
#         if "python" in e['tytul_szkolenia'].lower() and e['terminyGwarantowany']==1:
#             wiersz=(e['termin'],e['miasto'],e['tytul_szkolenia'])
#             wynik.append(wiersz)
#     for w in wynik:
#         print(w)

# import psycopg2
# polaczenie=psycopg2.connect(host="jsystems.pl",database="szkolenie510",user="szkolenie510",password="szkolenie510",port=5432)
# polaczenie.close

# polaczenie=psycopg2.connect(host="localhost", database="postgres", user="postgres", password="1qazXSW@", port=5432)
#
# kursor=polaczenie.cursor()
# sql='select * from pracownicy'
# kursor.execute(sql)
# for w in kursor:
#     print('row', w, 'email', w[3])
# polaczenie.close()

# import psycopg2
# # #polaczenie=psycopg2.connect(host="jsystems.pl",database="szkolenie510",user="szkolenie510",password="szkolenie510",port=5432)
# polaczenie=psycopg2.connect(host="localhost",database="postgres",user="postgres",password="1qazXSW@",port=5432)
# kursor=polaczenie.cursor()
# try:
#     sql=f"insert into pracownicy(imie,nazwisko,email) values('Stefan','Kowalski','stefan@kowalski.pl')"
#     kursor.execute(sql)
#     sql=f"insert into pracownicy(imie,nazwisko,email) values('Janusz','Kowalski','janusz@kowalski.pl')"
#     kursor.execute(sql)
#     polaczenie.commit()
# except Exception as e:
#     print(e)
#     polaczenie.rollback()
# polaczenie.close()


# 32. Napisz funkcję która przyjmie przez argumenty imię, nazwisko, email. Funkcja ma wstawić nowy wiersz do tabelki
#    pracownicy a następnie wypisać na konsoli wszystkie dane z tej tabeli.
#
#
# import psycopg2
# def dodajPracownika(i, n, e):
#     polaczenie = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="1qazXSW@",port=5432)
#     kursor = polaczenie.cursor()
#     try:
#         sql = f"insert into pracownicy(imie,nazwisko,email) values('{i}','{n}','{e}')"
#         kursor.execute(sql)
#         polaczenie.commit()
#         sql = 'select * from pracownicy'
#         kursor.execute(sql)
#         for w in kursor:
#             print('row', w, 'email', w[3])
#     except Exception as e:
#         print(e)
#         polaczenie.rollback()
#     polaczenie.close()
#
# dodajPracownika('Radek1','woz1','aaaa1@aaaaa.pl')

# KLASY i OBIEKTY
# Klasa to np. projekt samochodu, a obiekt to konretny egzemplarz samochodu zbudowany na podstawie projektu

#
# class Samochod:
#     numer_rejestracyjny=None
#     def jedz(self):
#         print('wrooom!')
#
# s=Samochod()
# s.numer_rejestracyjny='WE 968RP'
# s2=Samochod()
# s2.numer_rejestracyjny='WWL 12345'
# print(s.numer_rejestracyjny)
# print(s2.numer_rejestracyjny)
#
# s=Samochod()
# s.jedz()
# s2=Samochod()
# s.jedz()

# class Samochod:
#     numer_rejestracyjny=None
#     marka=None
#     def wypisz_dane(self):
#         print(self.numer_rejestracyjny,self.marka)
#     def __init__(self):
#         print('tworzenie obiektu')
#
# s=Samochod()
# s.numer_rejestracyjny='ABC 12334'
# s.marka='Renault'
# s.wypisz_dane()
#
# class Owoc:
#     rodzaj=None
#     kolor=None
#     def __init__(self):
#         print('konstruktor!')
#
# o=Owoc()
# o.rodzaj='Jabłko'
# o.kolor='Czerwony'
# print(o.rodzaj, o.kolor)


#
# class Owoc:
#     rodzaj=None
#     kolor=None
#     def __init__(self,r,k):
#         self.rodzaj=r
#         self.kolor=k
#
# #o=Owoc() #fuuu
# o=Owoc('Jabłko','Czerwony')
# print(o.rodzaj, o.kolor)


# 33. Stwórz klasę Samochod posiadającą pola marka, model i rejestracja.
#   Klasa ta powinna posiadać konstruktor umożliwiajacy uzupelnienie wszystkich
#   pól tego obiektu. Klasa powinna też posiadać metodę "wyświet;" wypisującą
#   dane z opbiektu na konsoli. Stwórz dwa obikety tej klasy i korzystając
#   z metody "wyswietl" wypisz ich dane na konsoli.

# class Samochod:
#     # marka = None
#     # model = None
#     # rejestracja=None
#
#     def __init__(self, marka, model, rejestracja):
#         self.marka = marka
#         self.model = model
#         self.rejestracja = rejestracja
#
#     def wyswietl(self):
#         print(f'marka = {self.marka}, model = {self.model}, nr rej= {self.rejestracja}')
#
# s1 = Samochod('Reno', 'Laguna', 'wasd1234')
# s2 = Samochod('Ford', 'Kaaaa', 'asdf7654')
#
# s1.wyswietl()
# s2.wyswietl()
# s1.wymyslone='wartość'
# print(s1.wymyslone)
# print(s2.wymyslone) #fuuu


# class Owoc:
#     rodzaj=None
#     kolor=None
#     def __init__(self,r,k):
#         self.rodzaj=r
#         self.kolor=k
#     def serializuj(self):
#         return f"rodzaj={self.rodzaj}, kolor={self.kolor}"
#
# o=Owoc('Pomarańcza','pomarańczowa')
# print(o)
# print(o.serializuj())

#
# class Owoc:
#     rodzaj=None
#     kolor=None
#     def __init__(self,r,k):
#         self.rodzaj=r
#         self.kolor=k
#     def __str__(self):
#         return f"rodzaj={self.rodzaj}, kolor={self.kolor}"
#         #return "przykład"
#
# o=Owoc('Pomarańcza','pomarańczowa')
# print(o)
# #print(o.serializuj())

# 34. W klasie Samochod przesłoń metodę __str__ i przerób metodę wyświetl w taki sposób
#    by korzystała z metody __str__

# class Samochod:
#     marka = None
#     model = None
#     rejestracja = None
#
#     def __init__(self, ma, mo, re):
#         self.marka = ma
#         self.model = mo
#         self.rejestracja = re
#
#     def __str__(self):
#         return f"'marka'='{self.marka}', 'model'='{self.model}', 'rejestracja'='{self.rejestracja}'"
#
#     def wyswietl(self):
#         print(self)
#
#
# s1 = Samochod('Renault', 'Kadjar', 'WE 968RP')
# s2 = Samochod('Skoda', '120L', 'WE 12345')
# print(s1)
# print(s2)
# s2.wyswietl()


#
# class Owoc:
#     __rodzaj=None
#     __kolor=None
#     def __init__(self,r,k):
#         #self.__rodzaj=r
#         self.__kolor=k
#         self.set_rodzaj(r)
#     def __str__(self):
#         return f"rodzaj={self.__rodzaj}, kolor={self.__kolor}"
#     def set_rodzaj(self,ro):
#         if len(ro)<3:
#             raise Exception('Wartość pola rodzaj jest za krótka')
#         self.__rodzaj=ro
#     def get_rodzaj(self):
#         return self.__rodzaj
#
#
# # o=Owoc('Żywota Twojego','je ZUS')
# # o.rodzaj='Czeresnia'
# # o.__rodzaj='Grejfrut'
# # print(o.__rodzaj)
# # print(o)
# # o=Owoc('Mandarynka','pomarańczowa')
# # o.set_rodzaj('P')
# # print(o)
# # print(o.get_rodzaj())
# o=Owoc('M','pomarańczowa')

# 35. Zadbaj o to by w klasie Samochod wszystkie pola były przywatne, ale by istniały
#    metody typu setter służące do ustawiania wartości w polach. Zadbaj o to by
#    wszystkie przypisania wartości wewnątrz klasy do pól były wykonywane za pośrednictwem
#    setterów. Zadbaj o to by nie dało się stworzyc samochodu z rejestracja o długości
#    innej niż 7-8 znaków, nie powinno też dać się tego ustawić przez setter na wartość krótszą
#    lub dłuższą.


# class Samochod:
#     __marka = None
#     __model = None
#     __rejestracja = None
#
#     def __init__(self, ma, mo, re):
#         self.set_marka(ma)
#         self.set_model(mo)
#         self.set_rejestracja(re)
#
#     def __str__(self):
#         return f'marka={self.__marka}, model={self.__model}, rejestracja={self.__rejestracja}'
#
#     def wyswietl(self):
#         print(self)
#
#     def set_marka(self, x):
#         self.__marka = x
#
#     def set_model(self, x):
#         self.__model = x
#
#     def set_rejestracja(self, x):
#         if len(x) < 7 or len(x) > 8:
#             raise Exception(f'Wartość pola rejestracja ma {len(x)} znakow jest inna niz 7-8 znakow')
#         self.__rejestracja = x
#
# s1 = Samochod('Renault', 'Kadjar', 'WE 968RP')
# print(s1)
# s2 = Samochod('Skoda', '120L', 'aasdsdad')
# print(s2)
# #s1.set_rejestracja('ABC')

# 36. Stwórz klasę Pracownik posiadajaca takie pola jakie są kolumny w tabeli
#    pracownicy. Stwórz funkcję która zwróci wszystkie dane z tabeli pracownicy
#    w postaci listy obiektów klasy Pracownik. Klasa ta powinna posiadać metodę __str__
#    przesłoniętą  i konstruktor sparametryzowany.

# class Pracownik:
#     id_pracownika = None
#     imie = None
#     nazwisko = None
#     email = None
#
#     def __init__(self, id, im, na, em):
#         self.id_pracownika = id
#         self.imie = im
#         self.nazwisko = na
#         self.email = em
#
#     def __str__(self):
#         return f'id_pracownika={self.id_pracownika}, imie={self.imie}, nazwisko={self.nazwisko}, email={self.email}'
#
#
# import psycopg2
#
#
# def pobierz_pracownikow():
#     polaczenie = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="1qazXSW@",
#                                   port=5432)
#     kursor = polaczenie.cursor()
#     wynik = list()
#     try:
#         sql = 'select * from pracownicy'
#         kursor.execute(sql)
#         for w in kursor:
#             wynik.append(Pracownik(w[0], w[1], w[2], w[3]))
#     except Exception as e:
#         print(e)
#         polaczenie.rollback()
#     kursor.close()
#     polaczenie.close()
#     return wynik
#
#
# lista = pobierz_pracownikow()
# for e in lista:
#     print(e)


#
# class Klasa:
#     pole1=None
#     @staticmethod
#     def cos():
#         print('hello!')
#
#
#     def cos_innego(self):
#         print('coś innego!')
#
# Klasa.cos()
# k=Klasa()
# k.cos_innego()
#
# class Samochod:
#     def jedz(self):
#         print('wroom!')
#
# class SuperSamochod(Samochod):
#     def turbo(self):
#         print('włączam turbo!')
#
# s=Samochod()
# s.jedz()
#
# ss=SuperSamochod()
# ss.jedz()
# ss.turbo()


#
# class A:
#     def funkcja_w_a(self):
#         print('hello tu funkcja w A')
# class B:
#     def funkcja_w_b(self):
#         print('hello tu funkcja w B')
#
# class C(A,B):
#     pass
#
# c=C()
# c.funkcja_w_a()
# c.funkcja_w_b()

#
#
# class A:
#     def funkcja_w_a(self):
#         print('hello tu funkcja w A')
# class B:
#     def funkcja_w_b(self):
#         print('hello tu funkcja w B')
#
# class C(A,B):
#     def funkcja_w_a(self):
#         print('hello tu przesłonięta funkcja z A')
#         super().funkcja_w_a()
#
# c=C()
# c.funkcja_w_a()
# c.funkcja_w_b()

#
# class A:
#     def funkcja(self):
#         print('tu funkcja z A')
#
# class B:
#     def funkcja(self):
#         print('tu funkcja z B')
#
# class C(B,A):
# #class C(A,B):
#     pass
#
# c=C()
# c.funkcja()

#37. Stwórz klasę Samochod i do niej dodaj metodę jedz() która będzie wyświetlała jakiś napis na konsoli,
#    oraz pola marka, model, rejestracja.
#    Do klasy Samochod dodaj tez konstruktor sparametryzowany uzupelniajacy wszystkie pola.
#    Stwórz klasę "Działo" która będzie posiadała metodę strzelaj(). Stwórz klasę Czolg która będzie
#    dziedziczyla zarowno po klasie Samochod jak i Dzialo. Stwórz obiekt klasy Czolg i wywolaj na nim
#    metody jedz() i strzelaj(). Zwróć uwagę na to jak trzeba wywolać konstruktor obiektu klasy Czolg.
#    Sprawdz czy zmiana kolejności dziedziczenia wpływa na sposób wywołania konstruktora. Sprawdz czy dodanie
#    bezparametrowego konstruktora do klasy Czolg zmienia zachowanie.
#
# class Samochod:
#     __marka = None
#     __model = None
#     __rejestracja = None
#
#     def __init__(self, ma, mo, re):
#         self.set_marka(ma)
#         self.set_model(mo)
#         self.set_rejestracja(re)
#
#     def __str__(self):
#         return f'marka={self.__marka}, model={self.__model}, rejestracja={self.__rejestracja}'
#
#     def set_marka(self, x):
#         self.__marka = x
#
#     def set_model(self, x):
#         self.__model = x
#
#     def set_rejestracja(self, x):
#         if len(x) < 7 or len(x) > 8:
#             raise Exception(f'Wartość pola rejestracja ma {len(x)} znakow jest inna niz 7-8 znakow')
#         self.__rejestracja = x
#
#     def jedz(self):
#         print('jedzie')
#
# class Dzialo:
#     a = None
#     b = None
#     c = None
#     def strzelj(self):
#         print('strzela')
#
#     def __init__(self):
#         print('konstruktor 0 Dzialo')
#     def __init__(self, a, b, c):
#         print('konstruktor 3 Dzialo')
#         self.a = a
#         self.b = b
#         self.c = c
#
# class Czolg(Dzialo, Samochod) :
#     def __init__(self):
#         print('konstruktor 0 Czolg')
#
#
# #c =Czolg('Leopard', '2a4', '1234567')
# c =Czolg()
# c.jedz()
# c.strzelj()
# print(c)

# # public inteface Moj{
# #     metoda()
# # }
# #
# # public class Moja implements Moj{
# #     metoda(){
# #
# #     }
# # }

# from abc import ABC, abstractmethod
#
# class UrzadzenieStrzelajace(ABC):
#     @abstractmethod
#     def strzelaj(self):
#         pass
#
# class Kalasznikow(UrzadzenieStrzelajace):
#     def strzelaj(self):
#         print('jeb jeb jeb jeb!')
#
# class Bazuka(UrzadzenieStrzelajace):
#     def strzelaj(self):
#         print('JEB!')
#
# class Pistolet(UrzadzenieStrzelajace):
#     def strzelaj(self):
#         print('pach pach!')
#
# k=Kalasznikow()
# b=Bazuka()
# p=Pistolet()
# bron=[k,b,p]
# for b in bron:
#     b.strzelaj()

#38. Stwórz klasę abstrakcyjną Restauracja która bedzie posiadała abstrakcyjną metodę serwuj_danie.
#    Stwórz klasy: RestauracjaChinska, RestauracjaWloska i RestauracjaPolska. Wymuś posiadanie
#    implementacji metody abstrakcyjnej serwuj_danie we wszystkich tych klasach ale o różnej implemnetacji.
#    Powolaj do zycia obiekty tych klas, a następnie na rzecz każdego z tych obiektów wywolaj funkcję serwuj_danie.

#
# from abc import ABC, abstractmethod
#
# class Restauracja(ABC):
#     @abstractmethod
#     def serwuj_danie(self):
#         pass
#
# class RestauracjaChinska(Restauracja):
#     def serwuj_danie(self):
#         print('kurczak w cieście!')
#
# class RestauracjaWloska(Restauracja):
#     def serwuj_danie(self):
#         print('pizza!')
#
# class RestauracjaPolska(Restauracja):
#     def serwuj_danie(self):
#         print('schabowy!')
#
# c = RestauracjaChinska()
# w = RestauracjaWloska()
# p = RestauracjaPolska()
# rest = [c, w, p]
# for b in rest:
#     b.serwuj_danie()
#

#
# class Singleton:
#     pass
#
# a=Singleton()
# b=Singleton()
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# print(a is b)


#
# class Singleton:
#     __instancja=None
#     def __new__(self, *args, **kwargs):
#         if self.__instancja is None:
#             print('inicjalizacja singletona')
#             self.__instancja=super().__new__(self,*args,**kwargs)
#         return self.__instancja
#
# a=Singleton()
# b=Singleton()
# print(id(a))
# print(id(b))
# print(a is b)

# class Singleton:
#     __instancja=None
#     polaczenie=None
#     def __new__(self, *args, **kwargs):
#         if self.__instancja is None:
#             print('inicjalizacja połączenia')
#             self.polaczenie='connected to Oracle'
#             self.__instancja=super().__new__(self,*args,**kwargs)
#         return self.__instancja
#
# a=Singleton()
# b=Singleton()
# print(a.polaczenie)
# print(b.polaczenie)

#39. Stwórz singleton który będzie posiadał pole reprezentujące połączenie. Podczas inicjalizacji singletona
#    należy zainicjalować połączenie. Dodaj metodę która zwróci połączenie i wykorzystaj to połączenie
#    do pobrania i wyświetlenia na konsoli danych z tabeli pracownicy
#
# import psycopg2
#
# class Singleton:
#     __instancja=None
#     polaczenie=None
#     def __new__(self, *args, **kwargs):
#         if self.__instancja is None:
#             print('inicjalizacja połączenia')
#             self.__instancja=super().__new__(self,*args,**kwargs)
#             self.polaczenie = psycopg2.connect(host="localhost", database="postgres", user="postgres",
#                                                password="1qazXSW@", port=5432)
#         return self.__instancja
#     def dajPoloczenie(self):
#         return self.polaczenie
#
# a=Singleton()
# print(a.dajPoloczenie())
# print(a.polaczenie)
# def pobierz_pracownikow():
#     b = Singleton()
#     kursor = b.dajPoloczenie().cursor()
#     wynik = list()
#     try:
#         sql = 'select * from pracownicy'
#         kursor.execute(sql)
#         for w in kursor:
#             wynik.append(w)
#     except Exception as e:
#         print(e)
#         b.dajPoloczenie().rollback()
#     kursor.close()
#     b.dajPoloczenie().close()
#     for e in wynik:
#         print(e)
#     return wynik
#
# pobierz_pracownikow()


from abc import ABC,abstractmethod

class Samochod(ABC):
    @abstractmethod
    def jedz(self):
        pass

class SamochodSportowy(Samochod):
    def jedz(self):
        print('jedzie samochód sportowy')
class Limuzyna(Samochod):
    def jedz(self):
        print('jedzie limuzyna')
class SamochodMiejski(Samochod):
    def jedz(self):
        print('jedzie samochód miejski')

class FabrykaSamochodow(ABC):
    @abstractmethod
    def produkuj_samochod(self):
        pass

class FabrykaSportowych(FabrykaSamochodow):
    def produkuj_samochod(self):
        return SamochodSportowy()

class FabrykaLimuzyn(FabrykaSamochodow):
    def produkuj_samochod(self):
        return Limuzyna()

class FabrykaMiejskich(FabrykaSamochodow):
    def produkuj_samochod(self):
        return SamochodMiejski()

fabryka=None
rodzaj='limuzyna'
if rodzaj=='miejski':
    fabryka=FabrykaMiejskich()
elif rodzaj=='sportowy':
    fabryka=FabrykaSportowych()
elif rodzaj=='limuzyna':
    fabryka=FabrykaLimuzyn()
else:
    raise NotImplementedError(f'nie ma fabryki dla typu {rodzaj}')

samochod=fabryka.produkuj_samochod()
samochod.jedz()

