# A simple text encryption exercise using the Caesar Cipher technique.
# The Caesar Cipher for `shift = 3` cyclically shifts every letter of the word by 3 positions:
# a -> d, b -> e, c -> f, ..., x -> a, y -> b, z -> c

# Implement the encryption logic by shifting each alphabet character

def encrypt_text(text):
    encrypted = ""
    for char in text:
        if char.isalpha():  # check if the character is an alphabet
            shift = 3
            # TODO: Use the correct ASCII values to shift the character and add it to 'encrypted'
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            # Hint 1: ord('A') = 65, ord('a') = 97
            # Hint 2: you can use modulo (%) operator to create a cycle
        else:
            encrypted += char  # keep non-alphabet characters unchanged
    return encrypted

# Example text to encrypt
original_text = "Hello, Python!"
# The encrypted_text function call and print statement should be the same as in the solution
encrypted_text = encrypt_text(original_text)
print(encrypted_text)  # The correct output after implementing the TODO should be 'Khoor, Sbwkrq!'
