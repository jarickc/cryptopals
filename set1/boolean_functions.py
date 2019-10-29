import binascii
from Crypto.Util.strxor import strxor
from Crypto.Util.strxor import strxor_c


def xor_hex_str_eq_len(input_1, input_2):
    out_1 = binascii.unhexlify(input_1)
    out_2 = binascii.unhexlify(input_2)
    return strxor(out_1, out_2)


def xor_hex_str_w_key(input_1, key):
    out_1 = binascii.unhexlify(input_1)
    return strxor_c(out_1, key)
