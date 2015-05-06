__author__ = 'kuban'


def filter_long_words(list, n):
   return [el for el in list if len(el)>n]

def filter_long_words2(list, n):
    result = []
    for el in list:
        if len(el)>n:
            result.append(el)
    return result

lista = ["mama", "tata", "syn", "corka"]
print(filter_long_words2(lista, 3))