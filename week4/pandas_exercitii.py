import pandas

# dataset = {
#     'masini': ["BMW", "Dacia", "Ford"],
#     "culoare": ["rosu", "negru", "gri"]
# }
#
# variabila = pandas.DataFrame(dataset)
# print(variabila)

# culori = ["rosu", "negru", "gri"]
# variabila = pandas.Series(culori, index=['x', 'y', 'z'])
# # print(variabila[0])
# print(variabila["z"], variabila[2])

# dataset = {"BMW": "rosu", "Dacia": "negru", "Ford": "gri"}
# variabila = pandas.Series(dataset, index=["Dacia", "Ford"])
# print(variabila)

dataset = {
    'masini': ["BMW", "Dacia", "Ford"],
    "culoare": ["rosu", "negru", "gri"]
}
variabila = pandas.DataFrame(dataset, index=['producator1', 'producator2', 'producator3'])
# print(variabila.loc[0])
# print(variabila.loc[[0, 2]])
# print(variabila.loc["producator1"])
print(pandas.options.display.max_rows)
