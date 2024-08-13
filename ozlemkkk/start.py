
# Dies ist ein Kommentar
# Nummerische Operatoren
# +, -, /, %, *
# **, //
# ** Potenz
# // Ganzzahldivision
mein_name = input ("Bitte geben Sie ihren Namen ein:") 

a = True
b = False
 
true = True
false = True
 
# Bitoperatoren
# Anwendungen: u.a. Kryptogtrafie, Netzwerk, effiziente Berechnungen
# Operatoren, die das Bitmuster von zwei Zahlen auswertet
# <<, >>, &, |, ^
# Bitshift-Operatoren
erg = 8 << 2
print(bin(8))
print(bin(erg))
 
erg2 = 16 >> 2 # 4
# Die beiden letzten Stellen werden verworfen, da sie nach außen geschoben werden.
erg2 = 17 >> 2 # 4
erg2 = 18 >> 2 # 4
erg2 = 19 >> 2 # 4
 
# Bitmuster vergleichen
# beide Stellen müssen 1 sein (für 1)
print(18 & 16)
# 10010
# 10000
# ==&==
# 10000
 
# mindestens eine Stelle 1 : 1
print(18 | 16)
# 10010
# 10000
# ==|==
# 10010
 
# nur bei unterschiedlichen Stellen 1
print(18 ^ 16)
# 10010
# 10000
# ==^==
# 00010
 
# Vergleichsoperatoren
# >, <, ==, !=, <=, >=
# Nummerische Vergleiche wie in JavaScript
# Strings:
"Hallo" < "hallo"
"zZzZ" < "zzzz"
 
# Buchstaben werden nacheinander verglichen
# jeder Buchstabe hat einen code point
# bei Ungleichheit der codee points gewinnt der Buchstabe mit dem niedrigeren
# code point
#
# der kleinere ord-Wert gewinnt
# code point wert in Python mit ord
print(ord('H'))
ord("Hallo"[0] < "hallo"[0])
 
"Hallo" < "Hallo1234" # Hallo1234 ist länger, vorher identische Substrings
"Hallo" < "Hallo1234"
# "Hallo" < "HaLo1234"
"Hallo" < "1234HaLo"
 
# ord('0') 48
# ord('A') 65
# ord('a') 97
 
# bei Unterschied: code point
# bei Gleichheit, aber unterschiedlicher Länge gewinnt das kürzere Wort