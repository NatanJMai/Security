from sys import argv

key  = int(argv[1])
data = "So sei que nao sei"

def encrypt():
    new_d = ''
    for i in data: new_d +=  chr((ord(i) + key) % 256)
    print(new_d)

def decrypt():
    new_d = ''
    for i in data: new_d +=  chr((ord(i) - key) % 256)
    print(new_d)

if __name__ == '__main__':
    if argv[2] == '-e':
        encrypt()
    else:
        decrypt()
