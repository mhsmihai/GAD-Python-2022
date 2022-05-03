variabila = input("Introdu un numar: ")
my_int = None
# este_intreg = int(variabila)
try:
    este_intreg = int(variabila)
    print("nu exista exceptii intalnite")
    if my_int is None:
        raise ValueError
# except ValueError as e:
#     print('eroare de valoare', e)
except Exception as e:
    # print(e.__doc__)
    print('a aparut o eroare', e)
else:
    print("nu exista exceptii intalnite")
finally:
    print("se ruleaza oricum")
