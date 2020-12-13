def generator_poteg_liczby_2():
    p=0
    while True:
        p+=1
        yield pow(2,p)

def generator_poteg(co):
    p=0
    while True:
        p+=1
        yield pow(co,p)