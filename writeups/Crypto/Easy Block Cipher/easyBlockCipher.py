import random

flag = b"SF24{REDACTED}"
  
random_key = bytes([random.randrange(0, 256) for _ in range(0, 10)])

def crypt_block(block, key):
    retval = bytearray()
    for i in range(0,10):
        retval.append(block[i] ^ key[i])
    return bytes(retval)

def boxCrypto(block_size, block_count, pt, key):
    ct = []
    tempBlock = []
    currKey = key
    for i in range(block_count):
        currKey = crypt_block(pt[i*block_size:(i*block_size)+block_size], currKey)
        ct.append(currKey)
    print(ct)

BLOCK_SIZE = 10
pt = flag[::-1] + (BLOCK_SIZE - (len(flag) % BLOCK_SIZE)) * b'\x00'
pt = pt[::-1]
block_count = int(len(pt) / BLOCK_SIZE)
print("Flag length is %d" % len(flag))
print("Encrypting %d blocks..." % block_count)
boxCrypto(BLOCK_SIZE, block_count, pt, random_key)
#Flag length is 35
#Encrypting 4 blocks...
#[b'\\\xb1\xb9\xab\x17k\xdc\xdc\x97B', b'\x0c\xdd\x8a\x98$X\xe8\xe9\xa4\x1d', b'H\xed\xe4\xaf{\x14\xdb\xdd\xcfB', b'\x11\xdd\x91\xdd$_\xe8\xa4\xee?']
