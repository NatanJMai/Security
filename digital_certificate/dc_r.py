import hashlib
import Crypto
import ast
from Crypto.PublicKey import RSA
from Crypto           import Random

f = open("file.in", 'rb+')

def hash(file):
    has = hashlib.sha256()
    buf = file.read()

    has.update(buf)
    return has.hexdigest()

def rsa(data):
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)

    publicKey = key.publickey()
    encrypted = publicKey.encrypt(data.encode(), 32)

    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
    return (encrypted[0], publicKey.exportKey('PEM'))


def get_public_key():
    key = b''

    for l in f:
        if 'BEGIN HASH' in str(l):
            break

    for l in f:
        if 'END HASH' in l:
            break
        #print(l)



    for line in reversed(f.readlines()):
        if b'BEGIN PUBLIC KEY'     in line: break
        elif not b'END PUBLIC KEY' in line: key += line.rstrip()


    #print(key)

    #f.seek(0)
    #ks = f.read()
    #print(ks)
    #public_key = RSA.importKey(key)
    #print(decrypted)
    #return key


def get_hash():
    f.seek(0)
    #g = open("file.in", 'rb+')
    #print(f.readlines())


def get_file():
    k = get_public_key()
    get_hash()



if __name__ == '__main__':
    get_file()
    #put_file(f)
