def compare_equal(a, b, verbose=0):
    if a == b:
        if verbose:
            print("Wow such coding!")
        return 1
    else:
        if verbose:
            print("Much defeat, try again.")
        return 0


def compare_not_equal(a, b, verbose=0):
    if a != b:
        if verbose:
            print("Wow such coding!")
        return 1
    else:
        if verbose:
            print("Much defeat, try again.")
        return 0


def all_pass(results_array):
    for element in results_array:
        if not element:
            print("Much defeat, try again.")
            return 0
    print("Wow such coding!")
    return 1
