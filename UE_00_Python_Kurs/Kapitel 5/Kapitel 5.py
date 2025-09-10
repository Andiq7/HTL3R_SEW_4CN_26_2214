#Frage 1
alt = 18
def altersbeschränkung(alter):
    if alter > 13 and not alter >= 18:
        return True
    else:
        return False
print(altersbeschränkung(18), "\n")

#Frage 2
geschwindigkeit = 64
if geschwindigkeit > 70:
     print('Fahrzeug ist über dem Geschwindigkeitslimit.')
else:
     print('Fahrzeug ist unter dem Geschwindigkeitslimit.\n')

#Frage 3
print(18 <= 18)
print(18 < 18)
print(-5 > -20)
print(-20 > -12)