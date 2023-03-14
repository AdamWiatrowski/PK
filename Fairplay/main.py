def array_to_matrix(aplphabet):
    table = [[0 for i in range(5)] for j in range(5)]

    for i in range(5):
        for j in range(5):
            table[i][j] = aplphabet[i * 5 + j]

    print(table)
    return table

def make_table(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper().replace("J", "I")
    new_alphabet = [i for i in keyword] + [i for i in alphabet if i not in keyword]

    table = array_to_matrix(new_alphabet)
    return table

def split_message(message):
    message = message.replace(" ", "").upper().replace("J", "I")
    if len(message) % 2 != 0:
        message += "X"

    # podziel na pary
    pairs = [message[i:i+2] for i in range(0, len(message), 2)]

    return pairs

def get_position(char, table):
    for i in range(5):
        for j in range(5):
            if table[i][j] == char:
                return i, j

def fairplay_encrypt(keyword, message):

    table = make_table(keyword)
    pairs = split_message(message)
    ciphertext = ""

    for pair in pairs:
        x1, y1 = get_position(pair[0], table)
        x2, y2 = get_position(pair[1], table)

        if x1 == x2:
            y1 = (y1 + 1) % 5
            y2 = (y2 + 1) % 5
        elif y1 == y2:
            x1 = (x1 + 1) % 5
            x2 = (x2 + 1) % 5
        else:
            y1, y2 = y2, y1

        ciphertext += table[x1][y1] + table[x2][y2]

    return ciphertext

def fairplay_decrypt(keyword, message):

    table = make_table(keyword)
    pairs = split_message(message)
    plaintext  = ""

    for pair in pairs:
        x1, y1 = get_position(pair[0], table)
        x2, y2 = get_position(pair[1], table)

        if x1 == x2:
            y1 = (y1 - 1) % 5
            y2 = (y2 - 1) % 5
        elif y1 == y2:
            x1 = (x1 - 1) % 5
            x2 = (x2 - 1) % 5
        else:
            y1, y2 = y2, y1

        plaintext  += table[x1][y1] + table[x2][y2]

    return plaintext


print(fairplay_encrypt("HASLO", "WIADOMOSC DO ZASZYFROWANIA"))
print(fairplay_decrypt("HASLO", fairplay_encrypt("HASLO", "WIADOMOSC DO ZASZYFROWANIA")))
