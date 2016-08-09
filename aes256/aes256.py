from Crypto.Cipher      import AES
from Crypto             import Random

data = "mensagem de teste"
key  = "12345678901234123456789012342312"

def crypt_decrypt(text):
   aes  = Random.new().read(AES.block_size)
   cph  = AES.new(key, AES.MODE_CFB, aes)
   encrypted  = cph.encrypt(text)
   print("Cript -> %s" % encrypted)

   cph2 = AES.new(key, AES.MODE_CFB, aes)
   msg2 = cph2.decrypt(encrypted)
   msg2 = msg2 = msg2.decode('utf-8')

   print("Encript -> %s\n" % msg2)

if __name__ == '__main__':
    crypt_decrypt(data)
