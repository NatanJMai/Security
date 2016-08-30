import hashlib
import Crypto
import ast
from Crypto.PublicKey import RSA
from Crypto           import Random

f = open("encrypted.k", 'r')

def hash(file):
    f.seek(0)
    text = ''
    for i in f:
        if ('BEGIN' in i) or ('END' in i):
            break
        text += i

    has = hashlib.sha256()
    has.update(text[:-1].encode('latin-1'))

    return has.digest()

def rsa(key, data):
    publicKey = RSA.importKey(key)
    encrypted = publicKey.encrypt(data.encode(), 32)
    return encrypted[0]


def get_public_key():
    key = ''
    for l in f:
        if 'BEGIN PUBLIC KEY' in str(l):
            key += str(l)
            break

    for l in f:
        if 'END PUBLIC KEY' in str(l):
            key += str(l)
            break

        key += str(l)
    return key

def get_hash_c():
    hah = ''
    f.seek(0)
    for l in f:
        if 'BEGIN Hash' in str(l):
            break

    for l in f:
        if 'END Hash' in str(l):
            break
        hah += str(l)
    return hah.encode('latin-1')[:-1]

def get_file():
    key    = get_public_key()
    hash_c = get_hash_c()
    hah    = hash(f)
    rs     = rsa(key, hah.decode('latin-1'))


    if str(rs) == str(hash_c):
        print("Assinatura válida")
    else:
        print("Assinatura inválida")


if __name__ == '__main__':
    get_file()
    #put_file(f)
