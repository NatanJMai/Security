from sys        import argv
from itertools  import cycle

def run():
    fs_l   = ['testcases/inputs/%s.input'  % str(x) for x in range(1, 8)]
    fd_l   = ['testcases/outputs_natan/vigenere/%s_vigenere.output' % str(x) for x in range(1, 8)]
    key    = argv[2]
    return (fs_l, fd_l, key)

def encrypt():
    fs_l, fd_l, key = run()

    for f in range(0, len(fs_l)):
        fs     = open(fs_l[f], 'rb')
        fd     = open(fd_l[f], 'wb')

        data   = fs.read()
        n_key  = ''
        genr   = cycle(key)
        for i in range(0, len(data)): n_key += genr.__next__()
        fd.write(bytes((data[x] + ord(n_key[x])) % 256 for x in range(0, len(data))))


def decrypt():
    fs_l, fd_l, key = run()

    for f in range(0, len(fs_l)):
        fs     = open(fd_l[f], 'rb')
        fd     = open('testcases/outputs_natan/vigenere/%d_decrypted.input' % (f + 1), 'wb')

        data   = fs.read()
        n_key  = ''
        genr   = cycle(key)
        for i in range(0, len(data)): n_key += genr.__next__()
        fd.write(bytes((data[x] - ord(n_key[x])) % 256 for x in range(0, len(data))))

    

if __name__ == '__main__':
    if argv[1] == '-e':
        encrypt()
    else:
        decrypt()
