import hashlib

char_to_emoji = {"A": "😀", "B": "😃", "C": "😄", "D": "😁", "E": "😆", "F": "😅", "G": "😂", "H": "🤣", "I": "😊", "J": "😇", "K": "🙂", "L": "🙃", "M": "😉", "N": "😌", "O": "😍", "P": "😘", "Q": "😗", "R": "😙", "S": "😚", "T": "🤗", "U": "🤩", "V": "🤔", "W": "🤨", "X": "😐", "Y": "😑", "Z": "😶", " ": " ", }
encoded_message = "🤣😆🙃🙃😍 😆😉😍😇😊 😅😍😙 😅🤩😌😌😑 🤣😀🤣😀🤣😀"

flag = "????"

emoji_to_char = {v: k for k, v in char_to_emoji.items()}

def emoji_decode(encoded_string):
    decoded_string = ''
    for emoji in encoded_string:
        if emoji in emoji_to_char:
            decoded_string += emoji_to_char[emoji]
        else:
            decoded_string += emoji
    return decoded_string

def generate_md5_hash(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash

decoded_message = emoji_decode(encoded_message)
print("Decoded Message:", decoded_message)

md5_result = generate_md5_hash(decoded_message)
flag = f"THCTT24{{{md5_result}}}"
print(f"Flag found: {flag}")
