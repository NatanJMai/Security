from sys import argv

def run():
    fs_l = ['testcases/inputs/%s.input'  % str(x) for x in range(1, 8)]
    fd_l = ['testcases/outputs_natan/ceasar/%s_ceasar.output' % str(x) for x in range(1, 8)]
    key  = int(argv[1])
    return (fs_l, fd_l, key)

'''
python3 cesar.py 17 -e && for i in 1 2 3 4 5 6 7; do diff outputs/$i.input.ceasar.17 outputs_natan/$i.output; done
'''

def encrypt():
    fs_l, fd_l, key = run()
    for f in range(0, len(fs_l)):
        fs   = open(fs_l[f], 'rb')
        fd   = open(fd_l[f], 'wb')

        data = fs.read()
        fd.write(bytes((x + key) % 256 for x in data))

def decrypt():
    fs_l, fd_l, key = run()
    for f in range(0, len(fs_l)):
        fs = open(fd_l[f], 'rb')
        fd = open('testcases/outputs_natan/ceasar/%d_decrypted.input' % (f + 1), 'w')

        data = fs.read()
        for x in data: fd.write(chr((x - key) % 256))

if __name__ == '__main__':
    if '-h' in argv or 'help' in argv:
        print('python3 <cesar.py> <key> <option: -e/-d>')
        print('Run it in the same path of testcases folder.')

    elif argv[2] == '-e':
        encrypt()
    else:
        decrypt()
