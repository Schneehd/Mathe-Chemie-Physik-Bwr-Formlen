import time 


def spam_long():
    for spam in range(1):
        time.sleep(1)

def spam():
    for spam in range(1):
        time.sleep(0.15)

def space():
    for space in range(3):
        print()
space()

def clear():
    for clear in range(100):
        print()
clear()

def space_short():
    print()
space_short()

def physik_clear():
    for clear in range(100):
        print()
physik_clear()
def Bwr():
        while True:
         clear()
         spam()
         skip = input("Bitte Enter drücken wenn du nicht Bwr berechnen willst ('Bwr' wenn du Bwr Formeln brauchst) ")
         if skip == "":
             break
         elif skip == "Bwr":
            clear()
            print("AUSWAHL BWR")
            print()
            spam()
            formel = input("Welche Formel Brauchst du? ")
            if formel == "Prozentrechnung":
                while True:
                    prozent = input("Wie viel Prozent? ")
                    if prozent == "":
                        print("Error, Es muss eine Zahl enthalten sein")
                    else:
                        prozent = float(prozent)
                        if prozent > 0:
                            print()
                            betrag = input("Was ist der Betrag? ")
                            print()
                            betrag = float(betrag)
                            if betrag == "":
                                print("Error, Es muss eine Zahl enthalten sein")
                            else:
                                if betrag > 0:
                                    plus_minus = input("Willst du + oder - Rechnen? ")
                                    if plus_minus == "+":
                                        answer_add = (betrag * prozent) / 100
                                        answer_add = float(answer_add)
                                        answer_all = answer_add + betrag
                                        answer_add = round(answer_add, 2)
                                        answer_all = round(answer_all, 2) 
                                        space()
                                        print(f"Es wurden {answer_add} € addiert ")
                                        space()
                                        print(f"Der neue Betrag ist {answer_all} € ")
                                        space()
                                        quitt = input("Willst du Aufhören Prozente zu berechnen? (y um zu bestätigen")
                                        if quitt == "y":
                                            clear()
                                            break
                                    elif plus_minus == "-":
                                        answer_add = (betrag * prozent) / 100
                                        answer_all = betrag - answer_add
                                        answer_add = round(answer_add, 2)
                                        answer_all = round(answer_all, 2)
                                        space()
                                        print(f"Es wurden {answer_add} € abgezogen ")
                                        space()
                                        print(f"Der neue Betrag ist {answer_all} €")
                                        space()
                                        quitt = input("Willst du Aufhören Prozente zu berechnen? (y um zu bestätigen")
                                        if quitt == "y":
                                            clear()
                                            break
                                else:
                                    print("Der Betrag muss über 0 sein")
                                    spam_long()
                        else:
                            print("Es muss über 0 Prozent sein")
                            spam_long
            elif formel == "Einakaufskalkulation":
                 while True:
                        Listeneinkaufspreis = input("Was ist der Listeneinkaufspreis? ")
                        spam()
                        anzahl = input("Wie viel Ware wird gekauft?")
                        spam()
                        Liefererrabatt = input("Gibt es ein Lieferrabatt? (wenn ja wie viel? ")
                        spam()
                        Lieferskonto = input("Gibt es ein Lieferskono? (wenn ja wie viel?) ")
                        spam()
                        Bezugskosten = input("Gibt es Bezugskosten? (wenn ja wie viel?) ")
                        spam()
                        Listeneinkaufspreis = float(Listeneinkaufspreis)
                        anzahl = float(anzahl)
                        Liefererrabatt = float(Liefererrabatt)
                        Lieferskonto = float(Lieferskonto)
                        Bezugskosten = float(Bezugskosten)
                        if Listeneinkaufspreis > 0:
                            if anzahl > 0:
                                preis = Listeneinkaufspreis * anzahl
                                preis = float(preis)
                                rabatt = (preis * Liefererrabatt) / 100
                                rabatt = float(rabatt)
                                Zieleinkaufspreis = preis - rabatt
                                Zieleinkaufspreis = float(Zieleinkaufspreis)
                                skonto = (Zieleinkaufspreis * Lieferskonto) / 100
                                skonto = float(skonto)
                                Bareinkaufspreis = Zieleinkaufspreis - skonto
                                Bareinkaufspreis = float(Bareinkaufspreis)
                                Einstandspreis = Bezugskosten + Bareinkaufspreis
                                Einstandspreis = float(Einstandspreis)
                                preis = round(preis, 2)
                                rabatt = round(rabatt, 2)
                                Zieleinkaufspreis = round(Zieleinkaufspreis, 2)
                                skonto = round(skonto, 2)
                                Bareinkaufspreis = round(Bareinkaufspreis, 2)
                                Bezugskosten = round(Bezugskosten, 2)
                                Einstandspreis = round(Einstandspreis, 2)
                                spam()
                                clear()
                                print("____________________________________________________________________")
                                print(f"|Listeneinkaufspreis | {preis} €                                   ")
                                print(f"|Lieferrabatt        | {rabatt} €                                  ")
                                print(f"|____________________|_____________________________________________")
                                print(f"|Zieleinkaufspreis   | {Zieleinkaufspreis} €                       ")
                                print(f"|Lieferskonto        | {skonto} €                                  ")
                                print(f"|____________________|_____________________________________________")
                                print(f"|Bareinkaufspreis    | {Bareinkaufspreis} €                        ")
                                print(f"|Bezugskosten        | {Bezugskosten} €                            ")
                                print(f"|____________________|_____________________________________________")
                                print(f"|Einstandspreis      | {Einstandspreis} €                          ")
                                print("|____________________|_____________________________________________")   
                                quitt = input("Willst du Aufhören Einkaufskalkulation zu brechnen? (y um zu bestätigen")
                                if quitt == "y":
                                    clear()
                                    break       
            elif formel == "Verkaufskalkulation":
                       while True:
                        selbstkostenpreis = input("Was ist der Selbstkostenpreis? ")
                        spam()
                        gewinn = input("Was ist der Gewinn? ")
                        spam()
                        rabatt = input("gibt es ein Rabatt? (wenn ja wie viel?) ")
                        spam()
                        skonto = input("gibt es ein sknoto? (wenn ja wie viel?) ")
                        spam()
                        selbstkostenpreis = float(selbstkostenpreis)
                        if selbstkostenpreis > 0:
                            gewinn = float(gewinn)
                            rabatt = float(rabatt)
                            skonto = float(skonto)
                            gewinn_add = (selbstkostenpreis * gewinn) / 100
                            gewinn_add = float(gewinn_add)
                            Barverkaufspreis = gewinn_add + selbstkostenpreis
                            Barverkaufspreis = float(Barverkaufspreis)
                            skonto_geteilt = 100 - skonto
                            skonto_geteilt = float(skonto_geteilt)
                            skonto_add = (Barverkaufspreis * skonto) / skonto_geteilt
                            skonto_add = float(skonto_add)
                            Zielverkaufspreis = skonto_add + Barverkaufspreis
                            Zielverkaufspreis = float(Zielverkaufspreis)
                            rabatt_geteilt = 100 - rabatt
                            rabatt_add = (rabatt * Zielverkaufspreis) / rabatt_geteilt
                            rabatt_add = float(rabatt_add)
                            Listenverkaufspreis = rabatt_add + Zielverkaufspreis
                            Listeneinkaufspreis = float(Listenverkaufspreis)
                            selbstkostenpreis = round(selbstkostenpreis, 2)
                            gewinn_add = round(gewinn_add, 2)
                            Barverkaufspreis = round(Barverkaufspreis, 2)
                            skonto_add = round(skonto_add, 2)
                            Zielverkaufspreis = round(Zielverkaufspreis, 2)
                            rabatt_add = round(rabatt_add, 2)
                            Listenverkaufspreis = round(Listenverkaufspreis, 2)
                            print(f"__________________________________________________________________")
                            print(f"|Selbstkostenpreis  | {selbstkostenpreis} €                       ")
                            print(f"|Gewinn             | {gewinn_add} €                              ")
                            print(f"|___________________|_____________________________________________")
                            print(f"|Barverkaufspreis   | {Barverkaufspreis} €                        ")
                            print(f"|Kundenskonto       | {skonto_add} €                              ")
                            print(f"|___________________|_____________________________________________")
                            print(f"|Zielverkaufspreis  | {Zielverkaufspreis} €                       ")
                            print(f"|Kundenrabatt       | {rabatt_add} €                              ")
                            print(f"|___________________|_____________________________________________")
                            print(f"|Listenverkaufspreis| {Listenverkaufspreis} €                     ")
                            print(f"|___________________|_____________________________________________")
                        else:
                            print("Der Selbstkostenpreis muss über 0 sein")
                            quitt = input("Willst du Aufhören Verkaufskalkulation zu berechnen? (y um zu bestätigen")
                            if quitt == 'y':
                                clear()
                                break
            elif formel == "help":
                clear()
                space()
                print("Prozentrechnung um Prozenteauszurechnen")
                space()
                print("Verkaufskalkulation um verkaufskalkulation auszurechnen")
                space()
                print("Einkaufskalkulation um Einkaufskalkulation auszurechnen")        
                wait = input("")            
            else:
                clear()
                space()
                print("help für Hilfe")
                wait = input("")
         elif skip == "help":
             clear()
             print("Bwr für Bwr Formeln")
             space()
             print("Durch skippen um auswahl für alle Formeln zu haben ")
             space()
             print("Physik für Physik Formeln")
             wait = input()   
             clear()
      
Bwr()
def Physik():
    while True:
        physik_clear()
        spam()
        skip = input("Bitte Enter drücken wenn du nicht Bwr berechnen willst ('Bwr' wenn du Bwr Formeln brauchst) ")
        if skip == "":
            break
        elif skip == "Physik":
            physik_clear()
            print("PHYSIK")
            space()
            formel = input("welche Formel brauchst du?")
            if formel == "Gewichtsumrechnung":
              def Gewichtsumrechnung():
                print("")
                if formel == "Gewichtsumrechnung":
                    spam()
                    space()
                    print()
                    while True:
                        print("von welcher einheit in welche einheit willst du Umrechnen? ")
                        space()
                        print()
                        Einhheit_von = input("von welcher einheit? ")
                        spam()
                        Einheit_in = input ("in welcher Einheit? ")
                        if Einhheit_von == "kg":
                         if Einheit_in == "t":
                            spam()
                            Gewicht = input("Wie viel Kg? ")
                            Gewicht = float(Gewicht)
                            if Gewicht > 0:
                                ergebnis = Gewicht / 1000
                                print(f"Es sind {ergebnis} T")
                                wait = input()
                            else:
                                print("Das Gewicht muss über 0 sein")
                                spam()
                         elif Einheit_in == "g":
                            Gewicht = input("Wei viel Kg?")
                            Gewicht = float(Gewicht)
                            if Gewicht > 0:
                                ergebnis = Gewicht * 1000
                                print(f"Es sind {ergebnis} g ")
                                wait = input()
                            else:
                                print("Das Gewicht muss über 0 sein")
                                spam()
                        elif Einhheit_von == "t":
                         if Einheit_in == "kg":
                             Gewicht = input("Wie vielt t? ")
                             Gewicht = float(Gewicht)
                             if Gewicht > 0:
                                ergebnis =  1000 * Gewicht
                                print(f"Es sind {ergebnis} kg")
                                wait = input()
                             else:
                                 print("Das Gewicht muss über 0 sein")
                                 time.sleep(0.15)
                         elif Einheit_in == "g":         
                            Gewicht = input("Wie vielt t? ")
                            Gewicht = float(Gewicht)
                            if Gewicht > 0:
                                ergebnis =  100_000_0 * Gewicht
                                print(f"Es sind {ergebnis} g")
                                wait = input()
                            else:
                                print("Das Gewicht muss über 0 sein")
                        elif Einhheit_von == "g":
                            if Einheit_in == "kg":
                             Gewicht = input("Wie viel g? ")
                             Gewicht = float(Gewicht)
                             if Gewicht > 0:
                              ergebnis = Gewicht / 1000
                              print(f"Es sind {ergebnis} kg")
                              wait = input()
                             else:
                                 print("Das Gewicht muss über 0 sein")
                            elif Einheit_in == "t":
                                Gewicht = input("Wie viel g? ")
                                Gewicht = float(Gewicht)
                                if Gewicht > 0:
                                    ergebnis = Gewicht / 100_000_0
                                    print(f"Es sind {ergebnis} t")
                                    wait = input()
                                else:
                                    print("Das Gewicht muss über 0 sein")
                                    wait = input()
                                    spam()
                        else:
                            print("Es gibt nur 'g' 'kg' 't' zum umrechnen")
                            wait = input()
                            spam()
                        Gewichtsumrechnung()
                elif formel == "Dichte":
                 def Dichte():
                    physik_clear()
                    print()
                    print("Alle Einheiten selber umrechnen")
                    space()
                    while True:
                        volumen = input("Was ist das Volumen? (v) ")
                        spam()
                        masse = input("was ist die masse? (m) ")
                        volumen = float(volumen)
                        masse = float(masse)
                        if volumen > 0:
                            if masse > 0:
                                ergebnis = masse / volumen
                                print(f"Die Dichte ist {ergebnis} p")
                                quitt = input("Willst du aufhören Dichte zuberechnen? (y um zu bestätigen) ")
                                if quitt == "y":
                                    clear()
                                    break
                            else:
                                print("Die Massee muss über 0 sein")
                                spam()
                        else:
                            print("Das Volumen muss über 0 sein")
                            spam()    
                        Dichte()
                elif formel == "quit":
                    clear()
                    break
                elif formel == "help":
                    space_short()
                    print("'Gewichtsumrechnung' für Gewichtsumrechnung")
                    space_short()
                    print("'Dichte'für Ausrechnung der Dichte")
                    space_short()
                    print("'Whub' um Whub zu berechnen")
                    space_short()
                    wait = input()
                    clear()
                elif formel == "Whub":
                 def Whub():
                    abfrage_einheit = input("Hast du Fg? ('ja' wenn du es hast |'nein' wenn nicht) ")
                    if abfrage_einheit == "ja":
                        Fg = input("Was ist Fg? (Fg = Gewichtskraft)  ")
                        spam()
                        h = input("Was ist h? (h = Höhe ")
                        Fg = float(Fg)
                        h = float(h)
                        if Fg > 0:
                            if h > 0:
                                Whub = Fg * h 
                                Whub = float(Whub)
                                spam()
                                print(f"Whub ist {Whub}")
                                spam()
                                return Whub
                            else:
                                print("h muss muss über 0 sein ")
                        else:
                            print("Fg muss muss über 0 sein ")
                        quitt = input("Willst du Aufhören Whub zu berechnen? (y um zu bestätigen ")
                        if quitt == "y":
                            clear()
                            break
                    elif abfrage_einheit == "nein":
                        m = input("Was ist m? (m = Masse) ")
                        spam()
                        g = input("Was ist g? (g = Ortsfaktor) ")
                        spam()
                        h = input("Was ist h? (h = Höhe) ")
                        spam()
                        m = float(m)
                        g = float(g)
                        h = float(h)
                        if m > 0:
                            if g > 0:
                                if h > 0:
                                 Whub = m * g * h 
                                 Whub = float(Whub)
                                 spam()
                                 print(f"Whub ist {Whub}")
                                 spam()
                                 return Whub
                                else:
                                    print("h muss muss über 0 sein ")
                            else:
                                print("g muss muss über 0 sein ")
                        else: 
                            print("g muss muss über 0 sein")
                        quitt = input("Willst du Aufhören Whub zu berechnen? (y um zu bestätigen")
                        if quitt == "y":
                            clear()
                            break
                Whub()                            
                                    
    Physik()
def main():
    clear()
    while True:
        Fach = input("Aus welchen Fach brauchst du die Formel? ")
        if Fach == "Bwr":
         Bwr()
        elif Fach == "Physik":
         Physik()
        elif Fach == "help":
         clear()
         print("Bwr eingben für zugang zu die Formeln in Bwr zubekommen")
         space()
         print("Physik eingeben für zugang zu die Formeln in Physik zubekommen")
         space()
         wait = input()
main()