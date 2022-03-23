# define function
def prime_checker(number):
    found_prime = True
    for i in range(2, number):
        if number % i == 0:
            found_prime = False
    if found_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
# call function
n = int(input("Check this number: "))
prime_checker(number=n)
