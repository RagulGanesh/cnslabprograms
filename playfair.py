def generate_key_matrix(key):
    key = key.replace('J', 'I')  # Replace 'J' with 'I'
    key = "".join(dict.fromkeys(key))  # Remove duplicate characters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    key_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
    return key_matrix

def prepare_text(text):
    text = text.upper()
    text = text.replace('J', 'I')  # Replace 'J' with 'I'
    text = "".join(filter(str.isalpha, text))  # Remove non-alphabet characters
    text = " ".join(text[i:i+2] for i in range(0, len(text), 2))  # Group characters into pairs
    if len(text) % 2 != 0:
        text += 'X'  # Add 'X' at the end if the text length is odd
    return text

def find_char_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt(plaintext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = prepare_text(plaintext)
    
    ciphertext = ""
    for pair in plaintext.split():
        char1, char2 = pair[0], pair[1]
        row1, col1 = find_char_position(key_matrix, char1)
        row2, col2 = find_char_position(key_matrix, char2)
        
        if row1 == row2:  # Characters in the same row
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Characters in the same column
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:  # Characters in different rows and columns
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]
    
    return ciphertext

def decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = ""
    
    for pair in ciphertext.split():
        char1, char2 = pair[0], pair[1]
        row1, col1 = find_char_position(key_matrix, char1)
        row2, col2 = find_char_position(key_matrix, char2)
        
        if row1 == row2:  # Characters in the same row
            plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Characters in the same column
            plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:  # Characters in different rows and columns
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]
    
    return plaintext

if __name__ == "__main__":
    key = "KEYWORD"
    plaintext = "HELLO WORLD"

    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
