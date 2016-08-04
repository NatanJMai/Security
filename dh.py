import random, sys
from threading import Thread

bas = 3
mod = 17

class threads(Thread):
   def __init__(self, conn, addr):
      Thread.__init__(self)
      self.conn = conn
      self.addr = addr

   def run(self):
       pass



def start():
    #pvt = random.randint(1, 30)
    pvt = int(sys.argv[1])
    dha = (bas ** pvt) % mod
    print("A chave é %d" % dha)
    input("> ")


if __name__ == '__main__':
    start()
