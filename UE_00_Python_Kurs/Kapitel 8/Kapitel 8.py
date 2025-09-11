#Frage 1
zahlen = [1, 6, 36, 7, 22, 80]
summe = zahlen[0] + zahlen[-1]
print(summe, '\n')

#Frage 2
zeichenketten = ['Apfel', 'Käse', 'Pizza', 'lecker', 'Kuchen', 'Eis']
print(zeichenketten[0] + zeichenketten[-2], '\n')

#Frage 3
rezept = ['Eyer', 'Quag', 'Vanille-Zucker', 'Butter', 'Milch', 'Mehhl', 'Leitungswasser', 'Öl', 'Scokolad', 'Streusel', 'Kakao']
rezept[0] = 'Eier'
rezept[1] = 'Quark'
rezept[5] = 'Mehl'
rezept[8] = 'Schokolade'
print(rezept, '\n')

#Frage 4
zahlen = [5, 2, 9, 1, 7]

for i in range(len(zahlen)):
    for j in range(len(zahlen) - 1):
        if zahlen[j] > zahlen[j + 1]:
            zahlen[j], zahlen[j + 1] = zahlen[j + 1], zahlen[j]

print(zahlen)