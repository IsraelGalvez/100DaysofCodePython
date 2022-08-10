import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decode_encode(word, shift):
    word_result = ""
    for letter in word:
        if letter in alphabet:
            index_letter = alphabet.index(letter)  
            word_result += alphabet[index_letter - shift]
        elif letter == " ":
            word_result += " "
        else:
            word_result += letter
    return word_result

def ceasar_cipher():
    run = "yes"
    print(art.logo)
    while run == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == "encode":
            text = input("Type your message:\n").lower()
            shift = (int(input("Type the shift number:\n"))) 
            shift = shift % 26
            encrypted_word = decode_encode(text, shift * -1)
            print(f"Here's the encoded result: {encrypted_word}")
        elif direction == "decode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26
            decoded_word = decode_encode(text , shift)
            print(f"Here's the decoded result: {decoded_word}")
        run = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if run == "no":
            print("Goodbye")

ceasar_cipher()
