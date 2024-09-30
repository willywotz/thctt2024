import hashlib

def caesar_decode(encoded_string, shift):
    decoded_string = ''
    for char in encoded_string:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decoded_string += chr(shifted)
        else:
            decoded_string += char
    return decoded_string

def generate_md5_hash(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash

if __name__ == "__main__":
    ciphertext = "wnwwnwn Sgzhkzmc Bxadq Sno Szkdms wnwwnwn"
    for shift in range(26):
        decoded_string = caesar_decode(ciphertext, shift)
        if "Thailand" in decoded_string:
            md5_result = generate_md5_hash(decoded_string)
            final_flag = f"THCTT24{{{md5_result}}}"
            print(f"Shift {shift} found: {final_flag}")
            break
