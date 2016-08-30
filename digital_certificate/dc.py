import hashlib
import ast
from Crypto.PublicKey  import RSA
from Crypto            import Random
from Crypto.Hash       import SHA256


def hash(file):
    has = hashlib.sha256()
    buf = file.read()
    has.update(buf.encode('latin-1'))

    return has.digest()

def rsa(data):
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)

    publicKey = key.publickey()
    encrypted = publicKey.encrypt(data.encode(), 32)

    return (encrypted[0].decode('latin-1'), publicKey.exportKey('PEM').decode('latin-1'))

def put_file(file):
    f = open('encrypted.k', 'w')
    h = hash(file)
    file.seek(0)
    r = rsa(h.decode('latin-1'))
    f.write(file.read())
    f.write('\nBEGIN Hash\n')
    f.write(str(r[0]))
    f.write('\nEND Hash\n')
    f.write(str(r[1]) + '\n')


if __name__ == '__main__':
    f = open("file.in", 'r+', encoding='latin-1')
    put_file(f)
