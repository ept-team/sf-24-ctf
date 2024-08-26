import random

f = open("original_file", mode="rb")
raw_bytes = f.read()
f.close()


random_key = bytes([random.randrange(0, 256) for _ in range(0, 16)])
ct = bytearray()
for i in range(0,len(raw_bytes)):
    ct.append(raw_bytes[i] ^ random_key[i%len(random_key)])

f = open("help", "wb")
f.write(bytes(ct))
f.close()
