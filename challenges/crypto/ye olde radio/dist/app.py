#!/usr/bin/python3
from secret import FLAG
from time import time
from random import choices
from Crypto.Util.number import getPrime, bytes_to_long


class Challenge:

    def __init__(self):
        self.reset()
        self.gen()

    def __repr__(self):
        return (self.n, self.c).__repr__()
    
    def reset(self):
        self.m = "".join(choices("abcdefghijklmnopqrstuvwxyz", k=8)).encode()

    def gen(self):
        self.n = getPrime(1024)*getPrime(1024)
        self.e = 0x101
        self.c = pow(bytes_to_long(self.m), self.e, self.n)

    def validate(self, m):
        return m == self.m


if __name__ == "__main__":
    tval = time()
    ch = Challenge()
    while True:
        print("1. authenticate thy own identity")
        print("2. exuent and revisit thee odd radio later")
        ui = input(">> ")
        if ui.startswith('1'):
            curr = time()
            if (curr - tval) > 15:
                print("thy time is long over! resetting mine values")
                ch.reset()
                tval = curr
            ch.gen()
            print(ch)
            resp = str(input(">> ")).encode()
            if ch.validate(resp[:8]):
                print("thou are forsooth worthy of this flag")
                print(FLAG)
                exit(0)
            else:
                print("thou shall not pass! (to mine flag)")
        elif ui.startswith('2'):
            exit(1)
        else:
            print("thou hast entered an invalid input! how dare thou!!")
