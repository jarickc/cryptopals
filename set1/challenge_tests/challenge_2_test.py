from pass_fail import compare_equal
from boolean_functions import  xor_hex_str

input_1 = "1c0111001f010100061a024b53535009181c"
input_2 = "686974207468652062756c6c277320657965"
output  = "746865206b696420646f6e277420706c6179"

result = xor_hex_str(input_1, input_2)
compare_equal(result, output, verbose=True)