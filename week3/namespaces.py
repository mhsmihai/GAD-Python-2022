# def my_function():
#     global msg
#     msg = "Hello"
#     # print(msg)
#     return None
#
#
# my_function()
# print(msg)
# print(my_function())
# print(msg)
global total
# total = 0

# def my_function():
#     def my_second_function():
#         global msg
#         msg = "hello444"
#         return None
#
#     my_second_function()
#     print(locals(), 'locale la nivel de my function')
#     print(globals(), 'global la nivel de my function')
#     msg = "Hello1"
#     print(f"functia principala {msg}")
#     return None


def functie2():
    # print(msg, '>>>>')
    # print(locals(), 'locale la nivel de functie2')
    total = 1
    return total

# my_function()
print(functie2())
# print(msg)
# print(globals())
# print(locals())
