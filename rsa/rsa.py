import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

publicKey = key.publickey()
encrypted = publicKey.encrypt('this messagethis messagethis messagethis messagethis messagethis messagethisthis messagethis messagethis messagethis messagethis', 32)

print(encrypted)

decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
print(decrypted)
