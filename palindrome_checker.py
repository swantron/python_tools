# collect input
string = input('enter string: ')

# define function
def palindrome(string):
  # ensure input is legit
  if type(string) != str:
    return(False)
    print('enter a string')
  string = string.lower()
  string = string.replace(' ','')
  reversed = ''
  length = len(string)
  for i in range(length, 0, -1):
      reversed += string[i-1]
  if string == reversed:
    return(True)
  else:
    return(False)

# unit tests
assert(palindrome('food') == False)
assert(palindrome('madam') == True)
assert(palindrome('1') == True)
assert(palindrome('cool looc') == True)
assert(palindrome(False) == False)
assert(palindrome(123) == False)
assert(palindrome('madam im adam') == True)

# call function
if palindrome(string) == True:
  print(f' {string} is a palendrome')
else:
  print(f' {string} is not palendromea')
