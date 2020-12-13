print('wczytano modul - modul.py')

def monozenie(a,b):
    return a*b

def dzielenie(a,b):
    if b == 0:
        b = 1
    return a/b

def moja():
    print('funkcja moja z modułu')

#30
def potegi2():
    i = 0;
    while True:
        i += 1
        yield pow(2, i)