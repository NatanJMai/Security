'''@NatanJMai'''


import sys
from math import ceil

def encrypt(content, key):
    t = bytes()
    for i in range(0, key):
        t += content[i::key]
    return t
    
def decrypt(cont, key):
    t = bytes()
    dec = ceil(len(cont)/key)
    for i in range(0, dec):
        t += cont[i::dec]
    return t


arq_name = sys.argv[1]
chave = sys.argv[2]

arq = open(arq_name, 'rb')
arq_content = arq.read()
arq.close()

adicionar = b"#"*(-len(arq_content)%int(chave))
arq_content += adicionar

cont = encrypt(arq_content, int(chave))
enc_arq = open("cript_transp"+str(chave), 'wb')
enc_arq.write(cont)
enc_arq.close()

dec_content = decrypt(cont, int(chave))
dec_arq = open("dcript_transp"+str(chave), 'wb')
dec_arq.write(dec_content)
dec_arq.close()
