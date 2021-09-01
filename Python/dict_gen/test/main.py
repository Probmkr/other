import numpy as np

def gen(length):
    dictlist = []
    gen_one(length, dictlist)

def gen_one(length, dictlist):
    pass

dictcol = 20
for i in range(dictcol):
    for k in range(0x20, 0x7f):
        for j in range(i+1):
            print(bytearray.fromhex(np.base_repr(i, 16)).decode())
