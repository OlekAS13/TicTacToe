import random

# plansza to lista wypelniona X lub O, na poczatku same spacje
# zerowy element planszy bedzie zawsze spacja, zeby sprawdzic
# czy plansza jest juz cala zapelniona
plansza = []
for i in range(10):
    plansza.append(' ')

def rysujPlansze():
    print('\n\n\n\n\n\n============================================\n\n')
    print('       |       |')
    print('   ' + plansza[1] + '   |   ' + plansza[2] + '   |   ' + plansza[3])
    print('      1|      2|      3')
    print('-----------------------')
    print('       |       |')
    print('   ' + plansza[4] + '   |   ' + plansza[5] + '   |   ' + plansza[6])
    print('      4|      5|      6')
    print('-----------------------')
    print('       |       |')
    print('   ' + plansza[7] + '   |   ' + plansza[8] + '   |   ' + plansza[9])
    print('      7|      8|      9')

def czyPusteMiejsce(pozycja):
    return plansza[pozycja] == ' '

#    if plansza[pozycja] == ' ':
#        return True
#    else:
#        return False

def wstawZnak(litera, pozycja):
    plansza[pozycja] = litera

def czyWygrana(litera, plansza):
    return (plansza[1] == litera and plansza[2] == litera and plansza[3] == litera) or \
    (plansza[4] == litera and plansza[5] == litera and plansza[6] == litera) or \
    (plansza[7] == litera and plansza[8] == litera and plansza[9] == litera) or \
    (plansza[1] == litera and plansza[4] == litera and plansza[7] == litera) or \
    (plansza[2] == litera and plansza[5] == litera and plansza[8] == litera) or \
    (plansza[3] == litera and plansza[6] == litera and plansza[9] == litera) or \
    (plansza[1] == litera and plansza[5] == litera and plansza[9] == litera) or \
    (plansza[3] == litera and plansza[5] == litera and plansza[7] == litera)

def czyPlanszaPelna():
    return plansza.count(' ') == 1

#    if plansza.count(' ') == 1:
#       return True
#    else:
#        return False

def ruchGracza():
    while True:
        try:
            pozycja = input('Podaj pozycje dla krzyzyka (1-9): ')
            pozycja = int(pozycja)
            if pozycja > 0 and pozycja < 10:
                if czyPusteMiejsce(pozycja):
                    wstawZnak('X', pozycja)
                    break
                else:
                    rysujPlansze()
                    print('\nPozycja zajeta.')
            else:
                rysujPlansze()
                print('\nPozycja musi byc z zakresu (1-9).')
        except:
            rysujPlansze()
            print('\nMusisz wprowadzic liczbe.')


def losujPozycje(lista):
    losowaPozycja = random.randrange(0,len(lista))
    return lista[losowaPozycja]


def ruchKomp():
    mozliweRuchy = []
    for pozycja in range(1, 10):
        if plansza[pozycja] == ' ':
            mozliweRuchy.append(pozycja)
    
    for ruch in mozliweRuchy:
        kopiaPlanszy = plansza.copy()
        kopiaPlanszy[ruch] = 'O'
        if czyWygrana('O', kopiaPlanszy):
            wstawZnak('O', ruch)
            return
    
    for ruch in mozliweRuchy:
        kopiaPlanszy = plansza.copy()
        kopiaPlanszy[ruch] = 'X'
        if czyWygrana('X', kopiaPlanszy):
            wstawZnak('O', ruch)
            return

    mozliweNarozniki = []
    for naroznik in mozliweRuchy:
        if naroznik in [1,3,7,9]:
            mozliweNarozniki.append(naroznik)
    if len(mozliweNarozniki) > 0:
        wstawZnak('O', losujPozycje(mozliweNarozniki))
        return
    
    if 5 in mozliweRuchy:
        wstawZnak('O', 5)
        return
    
    mozliweKrawedzie = []
    for krawedz in mozliweRuchy:
        if krawedz in [2,4,6,8]:
            mozliweKrawedzie.append(krawedz)
    if len(mozliweKrawedzie) > 0:
        wstawZnak('O', losujPozycje(mozliweKrawedzie))
        return


input('Witaj w grze Kolko i Krzyzyk!\nNacisnij Enter aby zaczac.')
rysujPlansze()
print('\n')

while True:
    ruchGracza()
    rysujPlansze()
    print('\n')
    
    if czyWygrana('X', plansza):
        print('X wygrywa!')
        break
    
    if czyPlanszaPelna():
        print('Remis!')
        break

    ruchKomp()
    rysujPlansze()
    print('\n')
    if czyWygrana('O', plansza):
        print('O wygrywa!')
        break
