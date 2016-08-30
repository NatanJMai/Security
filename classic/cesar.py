from sys import argv

key  = int(argv[1])
data = "So sei que nao sei"

def main():
    new_d = ''
    for i in data: new_d +=  chr((ord(i) + key) % 256)
    print(new_d)

if __name__ == '__main__':
    main()
