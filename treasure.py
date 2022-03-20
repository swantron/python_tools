# define map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# display map
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# prompt for input
position = input("Where do you want to put the treasure? ")

# turn input into list
pos = list(position)

# map from list
map[int(pos[1])-1][int(pos[0])-1] = 'X'

# update map
print(f"{row1}\n{row2}\n{row3}")
