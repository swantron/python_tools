# define function
def fib(n):
  if type(n) == int:
    if n < 0:
      return 'invalid entry'
    elif n == 0:
      return 0
    elif n == 1:
      return 1
    else:
      return fib(n-1) + fib(n-2)
  else:
    return 'invalid entry'

# unit tests
assert(fib(-1)) == 'invalid entry'
assert(fib(0)) == 0
assert(fib(1)) == 1
assert(fib(2)) == 1
assert(fib(3)) == 2
assert(fib(7)) == 13
assert(fib('food')) == 'invalid entry'

# interact with function
thing_to_check = input('enter an integer: ')
thing = int(thing_to_check)
my_range = range(0, thing)
for x in my_range:
  print(fib(x))
