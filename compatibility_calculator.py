# this is dumb
name1 = input("input your name? \n")
name2 = input("input another name? \n")
f
both = (name1 + name2).lower()
xl = 0
xo = 0
xv = 0
xe = 0
xt = 0
xr = 0
xu = 0
xl = both.count('l')
xo = both.count('o')
xv = both.count('v')
xe = both.count('e')
xt = both.count('t')
xr = both.count('r')
xu = both.count('u')

first = xl + xo + xv + xe
last = xt + xr + xu + xe

xscore = str(last)+str(first)
score = int(xscore)

if score < 10 or score > 90:
    print(f"Your score is {score}, great.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, okay.")
else:
    print(f"Your score is {score}, bad.")
