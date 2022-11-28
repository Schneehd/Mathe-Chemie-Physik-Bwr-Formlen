import time 

def spam_long():
    for spam in range(1):
        time.sleep(1)

def spam():
    for i in range(1):
        time.sleep(0.15)

def space():
    for space in range(3):
        print()
space()

def clear():
    for clear in range(100):
        print()
clear()

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
                                         
Bwr()



def main():
    space()
    print ("WARNUNG WENN BUCHSTABEN IM ZAHLENFELD SIND KOMMT ES ZUM ABSTURTZ!")
    space()
    while True:
        Fach = input("Aus welchen Fach brauchst du die Formel? ")
        if Fach == "Bwr":
         Bwr()
main()



