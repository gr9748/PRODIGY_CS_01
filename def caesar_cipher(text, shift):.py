def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26)
                               + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def encrypt(message, shift):
    return caesar_cipher(message, shift)

def decrypt(ciphertext, shift):
    return caesar_cipher(ciphertext, -shift)

def main():
    message = input("Enter the message to encrypt/decrypt: ")
    shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))

    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)

    print("\nEncrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
