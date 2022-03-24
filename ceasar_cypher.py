alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(plain_text, shift_amount, direction_way):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if direction == "encode":    
      new_position = position + shift_amount
    else:
      new_position = position - shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

ceasar(plain_text=text, shift_amount=shift, direction_way=direction)
