import random

# plansza to lista wypelniona X lub O, na poczatku same spacje
# zerowy element planszy bedzie zawsze spacja, zeby sprawdzic
# czy plansza jest juz cala zapelniona



plansza = []
ruchyGracza = 0
ruchyKomp = 0
wygraneG = 0
wygraneK = 0

def rysujPlansze():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n            TIC     TAC     TOE\n============================================\n\n')
    print('       |       |                             --==Statystyki==--')
    print('   ' + plansza[1] + '   |   ' + plansza[2] + '   |   ' + plansza[3])
    print('      1|      2|      3                      Ruchy gracza: ' + str(ruchyGracza))
    print('-----------------------                      Ruchy komp: ' + str(ruchyKomp))
    print('       |       |                             Wygrane gracza: ' + str(wygraneG))
    print('   ' + plansza[4] + '   |   ' + plansza[5] + '   |   ' + plansza[6] + '                         Wygrane komp: ' + str(wygraneK))
    print('      4|      5|      6')
    print('-----------------------                      --==============--')
    print('       |       |')
    print('   ' + plansza[7] + '   |   ' + plansza[8] + '   |   ' + plansza[9])
    print('      7|      8|      9\n\n\n')

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
    global ruchyGracza
    while True:
        try:
            pozycja = input('Podaj pozycje dla X (1-9), (x aby zakończyć): ')
            if pozycja == 'x':
                raise KeyboardInterrupt
            
            pozycja = int(pozycja)
            if pozycja > 0 and pozycja < 10:
                if czyPusteMiejsce(pozycja):
                    wstawZnak('X', pozycja)
                    print(ruchyGracza)
                    ruchyGracza += 1
                    break
                else:
                    rysujPlansze()
                    print('\nPozycja zajęta.')
            else:
                rysujPlansze()
                print('\nPozycja musi być z zakresu (1-9).')
        except ValueError:
            rysujPlansze()
            print('\nMusisz wprowadzić liczbę.')


def losujPozycje(lista):
    losowaPozycja = random.randrange(0,len(lista))
    return lista[losowaPozycja]


def ruchKomp():
    global ruchyKomp
    mozliweRuchy = []
    for pozycja in range(1, 10):
        if plansza[pozycja] == ' ':
            mozliweRuchy.append(pozycja)
    
    for ruch in mozliweRuchy:
        kopiaPlanszy = plansza.copy()
        kopiaPlanszy[ruch] = 'O'
        if czyWygrana('O', kopiaPlanszy):
            wstawZnak('O', ruch)
            ruchyKomp += 1
            return
    
    for ruch in mozliweRuchy:
        kopiaPlanszy = plansza.copy()
        kopiaPlanszy[ruch] = 'X'
        if czyWygrana('X', kopiaPlanszy):
            wstawZnak('O', ruch)
            ruchyKomp += 1
            return

    mozliweNarozniki = []
    for naroznik in mozliweRuchy:
        if naroznik in [1,3,7,9]:
            mozliweNarozniki.append(naroznik)
    if len(mozliweNarozniki) > 0:
        wstawZnak('O', losujPozycje(mozliweNarozniki))
        ruchyKomp += 1
        return
    
    if 5 in mozliweRuchy:
        wstawZnak('O', 5)
        ruchyKomp += 1
        return
    
    mozliweKrawedzie = []
    for krawedz in mozliweRuchy:
        if krawedz in [2,4,6,8]:
            mozliweKrawedzie.append(krawedz)
    if len(mozliweKrawedzie) > 0:
        wstawZnak('O', losujPozycje(mozliweKrawedzie))
        ruchyKomp += 1
        return
    
def gra():
    global ruchyGracza
    global ruchyKomp
    global wygraneG
    global wygraneK

    plansza.clear()
    
    for i in range(10):
        plansza.append(' ')
    
    ruchyGracza = 0
    ruchyKomp = 0
    
    rysujPlansze()
    print('\n')

    while True:
        ruchGracza()
        rysujPlansze()
        print('\n')
        
        if czyWygrana('X', plansza):
            wygraneG += 1
            rysujPlansze()
            print('\n')
            input('X wygrywa! Naciśnij Enter aby grać.')
            break
        
        if czyPlanszaPelna():
            input('Remis! Naciśnij Enter aby grać.')
            break

        ruchKomp()
        rysujPlansze()
        print('\n')
        if czyWygrana('O', plansza):
            wygraneK += 1
            rysujPlansze()
            print('\n')
            input('O wygrywa! Naciśnij Enter aby zagrać ponownie.')
            break


def main():
    input('Witaj w grze Kółko i Krzyżyk! Naciśnij Enter aby zacząć grę.')
    
    while True:
        gra()

try:
    main()

except KeyboardInterrupt:
    print('\n\nDziękujemy za grę!')



#Author OlekAS13 15.05.2023
