from sys import argv

fs_l = ['inputs/%s.input'  % str(x) for x in range(1, 8)]
fd_l = ['outputs_natan/%s.output' % str(x) for x in range(1, 8)]
key  = int(argv[1])

'''
python3 cesar.py 17 -e && for i in 1 2 3 4 5 6 7; do diff outputs/$i.input.ceasar.17 outputs_natan/$i.output; done
'''

#fs   = open(argv[3], 'rb')
#fd   = open(argv[4], 'wb')

#data = fs.read()

def encrypt():
    for f in range(0, len(fs_l)):
        fs   = open(fs_l[f], 'rb')
        fd   = open(fd_l[f], 'wb')

        data = fs.read()
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
