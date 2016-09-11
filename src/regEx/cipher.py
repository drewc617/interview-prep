#!/usr/bin/python
# Copyright 2016 Jack Chi
# Using Python `re` regular expression to encode / decode phrases

import re


class Caesar:

    def __init__(self):
        pass

    def encode(self, phrase):
        encoded_phrase = ""
        for c in phrase:
            encoded_phrase += self.encodeOneCharacter(c)
        return encoded_phrase

    def decode(self, phrase):
        decoded_phrase = ""
        for c in phrase:
            decoded_phrase += self.decodeOneCharacter(c)
        return decoded_phrase

    def encodeOneCharacter(self, c):
        c = c.lower()
        letter_match = re.search(r'[a-z]', c)
        if not letter_match:
            return ''
        else:
            xyz_match = re.search(r'[x-z]', c) # wrap around to 'abc'
            if not xyz_match:
                return chr(ord(c) + 3)
            else:
                return chr(ord(c) - 26 + 3)

    def decodeOneCharacter(self, c):
        c = c.lower()
        abc_match = re.search(r'[a-c]', c)
        if not abc_match:
            return chr(ord(c) - 3)
        else:
            return chr(ord(c) + 26 - 3)

class Cipher:

    def __init__(self, key):
