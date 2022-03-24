# runs the ceasar cypher

# define alphabet twice
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# define cipher function
def caesar(start_text, shift_amount, cipher_direction):
  final_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      slot = alphabet.index(char)
      new_slot = slot + shift_amount
      final_text += alphabet[new_slot]
    else:
      final_text += char
  print(f"{cipher_direction}d message: {final_text}")

# stop / go logic
quit_or_not = False
while not quit_or_not:

  direction = input("input 'encode' to encrypt, input 'decode' to decrypt:\n")
  text = input("input your message:\n").lower()
  shift = int(input("input the shift number:\n"))
  # cap out at max number of letters
  shift = shift % 26
  # call actual function
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  # determine if we call again
  quit = input("input 'yes' to cipher more or 'no' to end.\n")
  if quit == "no":
    quit_or_not = True
    print("👍")
