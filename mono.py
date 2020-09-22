import random
from random import shuffle
from string import printable



class Mono:
    chars = ['0',
             '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'",
             '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']',
             '^', '_', '`', '{', '|', '}', '~', ]
    keys = list(chars)
    shuffled_keys = list(chars)
    shuffle(shuffled_keys)
    maps = dict(zip(keys, shuffled_keys))
    reversed_maps = dict(zip(shuffled_keys, keys))
    cipher = []
    @staticmethod
    def encrypt(message):
        for c in message:
            if c in Mono.chars:
                Mono.cipher.append(Mono.maps[c])
            else:
                Mono.cipher.append(c)
        return "".join(Mono.cipher)

    @staticmethod
    def decrypt(cipher):
        plain_text = []
        for c in cipher:
            if c in Mono.chars:
                plain_text.append(Mono.reversed_maps[c])
            else:
                plain_text.append(c)
        return ''.join(plain_text)