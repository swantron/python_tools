# sum even integers from 1 to 100
totes = 0
for number in range(1,101):
    if number % 2 == 0:
        totes += number
print(totes)
