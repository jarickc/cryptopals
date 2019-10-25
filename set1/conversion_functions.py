import codecs


def hex2sixty_four(hex_val):
    return codecs.encode(codecs.decode(hex_val, 'hex'), 'base64').decode()[:-1]
