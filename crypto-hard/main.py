with open("emoBit.txt", "r", encoding='utf-8') as file:
    raw = file.read()
    print(raw, end="\n\n")

    binary_string = raw.replace('😸', '0').replace('😺', '1')
    print("binary_string :", binary_string, end="\n\n")

    iterable_of_ints = [int(c, 2) for c in binary_string.split(' ')]
    print("iterable_of_ints :", iterable_of_ints, end="\n\n")

    flag_raw = [bytes(iterable_of_ints[i:i+4]).decode('utf-8') for i in range(0, len(iterable_of_ints), 4)]
    print("flag_raw :", flag_raw, end="\n\n")

    offset = ord(flag_raw[0]) - ord('T') # first flag string THCTT24
    print("offset :", offset, end="\n\n")

    flag = ''.join([chr(ord(c) - offset) for c in flag_raw])
    print("flag :", flag)
