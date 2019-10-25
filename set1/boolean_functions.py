def xor_hex_str(input_1, input_2):
    int_1 = int(input_1, 16)
    int_2 = int(input_2, 16)
    return hex(int(int_1 ^ int_2))[2:]

