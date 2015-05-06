__author__ = 'kuban'


def palindrome(word):
   for i in range(len(word)):
       if word[i] == word[len(word)-1]:
          return True
       else: return False


a=palindrome("abrba")
#print(a)

string="abrba"
print(string[::-1] == string)