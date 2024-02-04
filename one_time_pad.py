import math

plaintext = input("Enter the Plain Text:\n").upper()
key = input("Enter the key:\n").upper()
def encrypt(plaintext, key):
    result = ""
    if len(key) < len(plaintext):
        l = len(plaintext) - len(key)
        new_key = key + key[:l]
    else:
        new_key = key[:len(plaintext)]
    for i in range(len(plaintext)):
        char = plaintext[i]
        pi = ord(char.upper()) - 64
        ki = ord(new_key[i].upper()) - 64
        ci = pi + ki
        if ci > 26:
            new_ci = ci % 26
            result += chr(new_ci + 64)
        else:
            result += chr(ci + 64)
    return result, new_key
def decrypt(otp, key):
    result = ""
    for i in range(len(otp)):
        char = otp[i]
        ci = ord(char.upper()) - 64
        ki = ord(key[i].upper()) - 64
        pi = ci - ki
        if pi < 1:
            y = math.ceil(abs(pi) / 26)
            y1 = y * 26
            new_pi = pi + y1
            result += chr(new_pi + 64)
        else:
            result += chr(pi + 64)
    return result

encrypted_text, new_key = encrypt(plaintext, key)
decrypted_text = decrypt(encrypted_text, new_key)

print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")