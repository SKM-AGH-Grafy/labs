__author__ = 'kuban'


def filter_long_words(L,n):
    res = []
    for word in L:
        if len(word) > n:
            res.append(word)
    return res
L= ['aa','aaa']
A = filter_long_words(L,2)
print (A)
