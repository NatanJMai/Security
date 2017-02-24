'''@NatanJMai'''

import sys

dct_pt = {}
file_name = sys.argv[1]

file_name = open(file_name, "r")
palavras  = file_name.read().split('\n')

for f in palavras:
    cnt = 0
    padroes = ''
    pat_word = {}

    for x in f:
        if cnt == 0:
            pat_word.update({x: cnt})
            padroes += str(cnt)
            cnt += 1
        else:
            if pat_word.get(x) == None:
                pat_word.update({x: cnt})
                padroes += str(cnt)
                cnt += 1
            else:
                padroes += str(pat_word.get(x))
    
    dct_pt.update({f: padroes})

for i,z in dct_pt.items(): print (i,": ",z)
