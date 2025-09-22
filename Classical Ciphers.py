def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr(((a * (ord(char) - shift) + b) % 26) + shift)
        else:
            result += char
    return result

def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Invalid key: 'a' must be coprime with 26")
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((a_inv * ((ord(char) - shift) - b)) % 26 + shift)
        else:
            result += char
    return result
def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            offset = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char) - shift + offset) % 26 + shift)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            offset = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char) - shift - offset) % 26 + shift)
            key_index += 1
        else:
            result += char
    return result
def transposition_encrypt(text, key):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(text):
            ciphertext[col] += text[pointer]
            pointer += key
    return ''.join(ciphertext)

def transposition_decrypt(ciphertext, key):
    num_cols = int(len(ciphertext) / key)
    num_rows = key
    num_shaded_boxes = (num_cols * num_rows) - len(ciphertext)
    plaintext = [''] * num_cols
    col, row = 0, 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)
def main():
    print("Classical Cipher Tool")
    print("1. Caesar")
    print("2. Affine")
    print("3. Vigenère")
    print("4. Transposition")

    choice = input("Choose cipher (1-4): ")
    mode = input("Encrypt or Decrypt? (e/d): ").lower()
    message = input("Enter message: ")

    if choice == "1":
        key = int(input("Enter Caesar key: "))
        result = caesar_encrypt(message, key) if mode == 'e' else caesar_decrypt(message, key)
    
    elif choice == "2":
        a = int(input("Enter 'a' (coprime with 26): "))
        b = int(input("Enter 'b': "))
        result = affine_encrypt(message, a, b) if mode == 'e' else affine_decrypt(message, a, b)

    elif choice == "3":
        key = input("Enter keyword: ")
        result = vigenere_encrypt(message, key) if mode == 'e' else vigenere_decrypt(message, key)

    elif choice == "4":
        key = int(input("Enter key (integer): "))
        result = transposition_encrypt(message, key) if mode == 'e' else transposition_decrypt(message, key)

    else:
        result = "Invalid choice."

    print("Result:", result)

if __name__ == "__main__":
    main()
