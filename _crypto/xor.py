#!/usr/bin/env python3

def xor(data, key):
    return bytearray(a^b for a,b in zip(*map(bytearray, [data, key])))

data = b'\x10O\x1d"\x17\x0bn\x04\x18E\x13.\x00\x0e\n\x06-O\x18\x1c+\t\x0cM<O\x05*\x02\x1a;\x17\x13E\x16,\x0fS\x17H3\x00\x1dN0\x07\x0cO2P'
key = "YouCanNeverCatchJohnDoe!".encode('utf-8')

print(xor(data,key))
