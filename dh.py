import sys

bas = 13
mod = 11

def start():
    pvt = int(sys.argv[1])
    dh1 = (bas ** pvt) % mod
    print("A chave é %d" % dh1)
    inp = int(input("> "))
    dh2 = (inp ** pvt) % mod
    print("-------------------")
    print("Final -> %d" % dh2)


if __name__ == '__main__':
    start()
