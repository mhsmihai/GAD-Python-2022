# print("Mesaj in consola")
# variabila = 1
# print("Mesajul nr {}".format(variabila))
# raspuns_utilizator = input("Care este numele tau: ")
# print(raspuns_utilizator)
#
# def functia_mea():
#     pass

#
# def suma(a: int, b: int = 1) -> (int, int):
#     """
#     :param a: primul numar
#     :param b: al doilea numar
#     :return: suma, diferenta
#     """
#     if type(a) == str:
#         return a, b
#     return a + b, a - b
#
#
# suma_mea, diferenta = suma(3, 4)
# print(suma_mea, diferenta)

# def my_function(*param_1):
#     print(type(param_1))
#     return param_1
#
#
# print(my_function("string", 'strin1', 'string2'))

# def suma_nr_infinite(param1, param2=1, *var):
#     suma = 0
#     for item in var:
#         suma += item
#     return suma
#
#
# print(suma_nr_infinite(1, 2, 3, 4, 5, 6, 7))


# def catalog(param1, *args, **kwargs):
#     print(type(kwargs))
#     return param1


# print(catalog(1, nume="Ion", prenume="Vasile", varsta="12"))
# print(catalog(1))

# def suma(a, b):
#     a = diferenta(a, b)
#     return a + b
#
#
# def diferenta(a, b):
#     return a - b
#
#
# # print(suma(diferenta(1, 2), 2))
# print(suma(1, 2))

a, b = 10, 20
# min = None
# if a < b:
#     min = a
# else:
#     min = b

# min = a if a < b else b
# print(min)

# lista_produse = ["ciocolata", 'suc', 'paine', 'mere', "apa"]
# lista_noua = []
# for x in lista_produse:
#     if "a" in x:
#         lista_noua.append(x)
# lista_noua = [x for x in lista_produse if "a" in x]
# lista_noua = [x if "a" in x else "b" for x in lista_produse]

# print(lista_noua)

# min = None
# if suma := a + b:
#     print(suma)
# else:
#     min = b
import datetime
data = '05/05/05'
print(datetime.datetime.strptime(data, '%d/%m/%y'))