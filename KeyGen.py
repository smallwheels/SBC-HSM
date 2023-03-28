import secrets

# All Key generate is done by generating a large set of cryptographically sound data (secrets.py) and
# truncating to the appropriate length based on the algorithm ([:32] = 32 bytes of data)

# this function generate an aes 256 key (32 bytes), and stores in a file
def aes256_key():
    entropy = secrets.randbits(150)
    aes256key = str(entropy)[:32]
    with open('/home/raspberry/Desktop/AES256/AES256-Key', 'w') as f:
        f.write(str(aes256key))
    print("[ KEY GENERATED ]")
    return aes256key

# this function generates a aes 128 key (16 bytes), and store in a file
def aes128_key():
    entropy = secrets.randbits(150)
    aes128key = str(entropy)[:16]
    with open('/home/raspberry/Desktop/AES128/AES128-Key', 'w') as f:
        f.write(str(aes128key))
    print("[ KEY GENERATED ]")
    return aes128key


# this function generates the 3 (8 byte) des3 keys as a single 24 bytes key, and stores in file
# this is done as a single random 24 byte key as it's more secure than 3 repeating keys (see NIST-800-67)
def des3_key():
    entropy = secrets.randbits(150)
    des3key = str(entropy)[:24]
    with open('/home/raspberry/Desktop/3DES/3DES-Key', 'w') as f:
        f.write(str(des3key))
    print("[ KEY GENERATED ]")
    return des3key
