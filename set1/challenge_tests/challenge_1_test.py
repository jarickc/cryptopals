from conversion_functions import hex2sixty_four
from pass_fail import compare_equal, compare_not_equal, all_pass

num_tests = 2
hex_val = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

output = hex2sixty_four(hex_val)

results = [False] * num_tests
results[0] = compare_equal(output, b64, verbose=False)
results[1] = compare_not_equal(output, "SSdtIGtpbGxpbmcge", verbose=False)
all_pass(results)