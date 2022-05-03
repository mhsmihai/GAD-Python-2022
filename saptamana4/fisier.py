# file = open('data.txt', 'r+')
# r -> se citeste, nu se adauga, este valoarea cu care vine default functia open, daca fisierul nu exista, apare eroare
# w -> drept de scriere, daca fisierul nu exista il adauga
# a -> deschidem fisierul cu drept de adaugare, putem sa scriem, datele existente raman
# r+ -> deschidem fisierul cu drept de scriere, dar si de citire
# file.write('Hello2hello')
# file.close()
# file = open('data3.txt', 'w')
# try:
#     file.write('hello')
# finally:
#     file.close()
# with open('data.txt', 'w') as file:
#     file.write('curs python1\n')
#     file.write('curs python2\n')
# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)
# with open('data.txt', 'r') as file:
#     for line in list(file):
#         print(line)
# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#
#         if not line:
#             break
#         print(line)
