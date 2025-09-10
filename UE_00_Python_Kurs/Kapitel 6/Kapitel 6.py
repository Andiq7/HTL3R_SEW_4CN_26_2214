#Frage 1
bereich = range(4, 11)
for zahl in bereich:
    print(zahl)
print()

#Frage 2
i = 0
while i < 5:
    print(i)
    i += 1
print()

#Frage 3
preis = 59.99
if preis <= 20:
     preis = preis - 0.4 * preis # 40% Rabatt
elif preis > 60:
     preis = preis - 0.1 * preis # 10% Rabatt
else:
     preis = preis - 0.25 * preis # 25% Rabatt
print(preis)