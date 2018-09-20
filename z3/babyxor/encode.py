#!/usr/bin/env python3

import base64

def encrypt(plaintext, key):
    plaintext += '|'
    plaintext += key
    key = key*(len(plaintext)//len(key))
    key += key[:len(plaintext)-len(key)]

    cipher = ''.join(chr(ord(i)^ord(j)) for i,j in zip(plaintext, key))
    cipher = base64.b64encode(cipher.encode('ascii'))
    return cipher.decode('ascii')

if __name__ == '__main__':
    import sys
    key = sys.argv[1]
    plaintext = sys.argv[2]
    print(encrypt(plaintext, key))
