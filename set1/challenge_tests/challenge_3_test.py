from boolean_functions import xor_hex_str_w_key
from char_freq_order import char_freq_dict

enc_test_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
output_dict = {}
for key in range(0, 256):
    try:
        output_dict[key] = xor_hex_str_w_key(enc_test_str, key).decode("ascii")
        print(output_dict[key])
    except:
        pass

eng_letter_order = char_freq_dict["english"]

score = [0]*256
for i in range(0, 256):
    if i in output_dict:
        score_weight = 26
        for letter in eng_letter_order:
            score[i] += output_dict[i].count(letter)*score_weight
            score_weight -= 1

print(score.index(max(score)))
print(output_dict[score.index(max(score))])


