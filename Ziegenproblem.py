from random import randint
import random



'''
Ziegenproblem:
Das Ziegenproblem geht auf eine Spielsituation bei einer amerikanischen Spielshow zurück.
Erstes Programm für einen automatischen Durchlauf ohne Eingabe.
Zweites Programm für einen einmaligen Durchlauf mit Eingabe.
'''



'''
Für viele runden und automatisiert
Line 20
'''

'''
anzahlSpiele = int(input("Wiederholungen?\n"))
zaehlerSpiele = 0
zaehlerAutos = 0

listeAuto = []
listeKandidat1 = []
listeKandidat2 = []
listeZiege = []

while zaehlerSpiele < anzahlSpiele:
    # Tür für das Auto
    tuerAuto = randint(1, 3)
    # Liste hinter welcher Tür das auto war
    listeAuto.append(tuerAuto)

    # Wahl des Kandidaten (da es automatisch wiederholt wird, auf eingabe verzichten)
    tuerKandidat = randint(1, 3)
    # Liste welche Tür als erstes gewählt wurde
    listeKandidat1.append(tuerKandidat)

    # Liste für die Türen hinter der Ziegen sein können. Zum vergleichen + ausgabe
    tuerZiege = [1, 2, 3]

    # If bedingungen: 1. Wenn die Wahl und die Lösung gleich sind, 2. wenn die wahl und die lösung unterschiedlich sind
    if tuerAuto == tuerKandidat:
        tuerZiege.remove(tuerAuto)
        muenze = randint(0, 1)
        # Welche Tür ausgewählt wurde als Tür mit Ziege
        listeZiege.append(tuerZiege[muenze])
        # Liste verwalten: Die Möglichen Türen hinzufügen, die geöffnete entfernen
        tuerZiege.remove(tuerZiege[muenze])
        tuerZiege.append(tuerAuto)
        tuerZiege.sort()

    if tuerAuto != tuerKandidat:
        tuerZiege.remove(tuerAuto)
        tuerZiege.remove(tuerKandidat)
        # Welche Tür ausgegeben wurde als Tür mit Ziege
        listeZiege.append(tuerZiege[0])
        # Liste verwalten: Die Möglichen Türen hinzufügen, die geöffnete entfernen
        tuerZiege.append(tuerAuto)
        tuerZiege.append(tuerKandidat)
        tuerZiege.remove(tuerZiege[0])
        tuerZiege.sort()

    # Nach änderung der wahl fragen
    tuerKandidat = random.choice(tuerZiege)
    # liste welche tür als zweites gewählt wurde
    listeKandidat2.append(tuerKandidat)

    if tuerAuto == tuerKandidat:
        zaehlerAutos = zaehlerAutos + 1
        zaehlerSpiele = zaehlerSpiele + 1

    else:
        zaehlerSpiele = zaehlerSpiele + 1

print(f'Spiele: {zaehlerSpiele}')
print(f'Autos: {zaehlerAutos}')
print(f'Türen Autos : {listeAuto}')
print(f'Erste Wahl  : {listeKandidat1}')
print(f'Offene Türen: {listeZiege}')
print(f'Zweite Wahl : {listeKandidat2}')

auto_wahl1 = len([1 for i in range(anzahlSpiele) if listeAuto[i] == listeKandidat1[i]])
auto_wahl2 = len([1 for i in range(anzahlSpiele) if listeAuto[i] == listeKandidat2[i]])
print(f'Wahl 1 richtig: {auto_wahl1}')
print(f'Wahl 2 richtig: {auto_wahl2}')
'''




'''
Für eine Runde und Nutzer eingabe:
Line: 99
'''


# Liste für eine zufällige Wahl
tuerAuto = [1, 2, 3]
tuerAuto = random.choice(tuerAuto)
print(tuerAuto)

# Wahl des Kandidaten
tuerKandidat = int(input("Wähle eine Tür (1, 2, 3)\n"))

# Liste für die Türen hinter der Ziegen sein können. Zum vergleichen + ausgabe
tuerZiege = [1, 2, 3]

# If bedingungen: 1. Wenn die Wahl und die Lösung gleich sind, 2. wenn die wahl und die lösung unterschiedlich sind
if tuerAuto == tuerKandidat:
    tuerZiege.remove(tuerAuto)
    # print(tuerZiege)
    muenze = randint(0, 1)
    print(muenze)
    print(f'Hinter Tür {tuerZiege[muenze]} befindet sich eine Ziege!')
    # Liste verwalten: Die Möglichen Türen hinzufügen, die geöffnete entfernen
    tuerZiege.remove(tuerZiege[muenze])
    tuerZiege.append(tuerAuto)
    tuerZiege.sort()
    # print(tuerZiege)


if tuerAuto != tuerKandidat:
    tuerZiege.remove(tuerAuto)
    tuerZiege.remove(tuerKandidat)
    # print(tuerZiege)
    print(f'Hinter Tür {tuerZiege[0]} befindet sich eine Ziege!')
    # Liste verwalten: Die Möglichen Türen hinzufügen, die geöffnete entfernen
    tuerZiege.append(tuerAuto)
    tuerZiege.append(tuerKandidat)
    tuerZiege.remove(tuerZiege[0])
    tuerZiege.sort()
    # print(tuerZiege)

# Nach änderung der wahl fragen
tuerKandidat = int(input(f"Willst du bei deiner Wahl bleiben oder umwählen?{tuerZiege}\n"))

if tuerAuto == tuerKandidat:
    print("Glückwunsch! Du hast ein Auto gewonnen!")

else:
    print("Du hast eine Ziege gewonnen!")

