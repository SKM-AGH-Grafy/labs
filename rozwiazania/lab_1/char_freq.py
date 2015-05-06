__author__ = 'kuban'


def char_freq(lista):
   dict = {}
   for i in range(0, len(lista)):
       if(lista[i] in dict):
           dict[lista[i]]+=1
       else:
           dict[lista[i]]=1
   return dict
print(char_freq("abbabcbdbabdbdbabababcbcbab"))


a="ala"
print(a[0])
print(a[1])
print(a[2])
print(a[3])