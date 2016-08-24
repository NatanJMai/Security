import hashlib
#import Crypto
import ast
from Crypto.PublicKey import RSA
from Crypto           import Random
from Crypto.Hash       import SHA256


def hash(file):
    has = SHA256.new()
    buf = file.read()

    has.update(buf)
    return has.digest()

def rsa(data):
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)

    publicKey = key.publickey()
    encrypted = publicKey.encrypt(data.encode(), 32)

    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
    return (encrypted[0].decode(), publicKey.exportKey('PEM'))



def put_file(file):
    rs = rsa(hash(file))
    #print(str(rs[0]))
    file.write('-----BEGIN HASH-----\n')
    file.write(str(rs[0]))
    file.write('\n-----END HASH-----\n')
    file.write(str(rs[1]))


if __name__ == '__main__':
    f = open("file.in", 'r')
    hash(f)
    #put_file(f)
