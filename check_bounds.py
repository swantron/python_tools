# accept inputs
print("define the bounds")

max_left = int(input('enter max left coords: '))
max_right = int(input('enter max right coords: '))
max_top = int(input('enter max top coords: '))
max_bottom = int(input('enter max bottom coords: '))

print('define the location')

x = int(input('define your x coord: '))
y = int(input('define your y coord: '))
print(max_left, max_right, max_top, max_bottom, x, y)

# define function
def bounds(max_left, max_right, max_top, max_bottom, x, y):
  if max_left < x < max_right and max_top > y > max_bottom:
    print('bounded')
    return True
  else:
    print('out of bounds')
    return False

# test function
assert bounds(1,2,3,4,5,6) == False
assert bounds(1,100,100,1,5,5) == True

# call function
bounds(max_left, max_right, max_top, max_bottom, x, y)
