# picks the lunch picker

# import
import random

# method to split string
names_string = input("Input names, separated by a comma and space:")
names = names_string.split(", ")

# choose randomly
choice = names[random.randint(0, len(names)-1)]
print(f"Your pick, {choice}.")
