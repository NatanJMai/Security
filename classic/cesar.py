from sys import argv

fs   = open(argv[3], 'rb')
fd   = open(argv[4], 'wb')
key  = int(argv[1])
data = fs.read()

def encrypt():
    fd.write(bytes((x + key) % 256 for x in data))
    
def decrypt():
    fd.write(bytes((x - key) % 256 for x in data))

if __name__ == '__main__':
    if '-h' in argv:
        print("Usage: python3 <cesar.py> <key> <option:-e/-d> <file_input> <file_output>")

    elif argv[2] == '-e':
        encrypt()
    else:
        decrypt()
