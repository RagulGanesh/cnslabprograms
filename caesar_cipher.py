def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            is_upper = char.isupper()  # Check if it's uppercase
            offset = ord('A' if is_upper else 'a')
            result += chr(((ord(char) - offset + shift) % 26) + offset)
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

# Example usage
plaintext = "Hello, World!"
shift = 3  # You can change the shift value as needed
print("Plain Tet:", plaintext)
encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)  # Decrypt by shifting back
print("Decrypted:", decrypted_text)
