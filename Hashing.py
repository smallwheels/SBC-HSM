import mbedtls as mbed
import secrets

# >------- SHA 256 -------<
def sha256_hashing(raw):
    # using the mbedtls library the raw input can be hashed in SHA256
    # hex  digest produces this has a string instead of a bytes format
    # this is then written to the SHA256 file for storage and returned to main
    h = mbed.hashlib.sha256(raw).hexdigest()
    with open('/home/raspberry/Desktop/Hashing/SHA256-File', 'w') as f:
        f.write(h)
    print("[ HASHING COMPLETE ]")
    return h


# >------- RIPMD 160 -------<
def ripemd160_hashing(raw):
    # using the mbedtls library the raw input can be hashed in RIPMD160
    # hex  digest produces this has a string instead of a bytes format
    # this is then written to the RIPMD160 file for storage and returned to main
    h = mbed.hashlib.ripemd160(raw).hexdigest()
    with open('/home/raspberry/Desktop/Hashing/RIPMD160-File', 'w') as f:
        f.write(h)
    print("[ HASHING COMPLETE ]")
    return h


# >------- Hashed Message Authentication Code - SHA 512 -------<
def hmac_gen(raw):
    # HMAC uses a bytes key to secure the hash (64 bytes is the maximum - and most secure)
    # secrets/py generates random entropy and truncates it to 64 bytes
    entropy = secrets.randbits(150)
    key = str(entropy)[:64]

    # the hmac settings are configured to the specific key and sha512 for security
    h = mbed.hmac.new(bytes(key, 'utf-8'), digestmod="sha512")
    # the raw bytes are then added to the key and hashed together
    # hex  digest produces this has a string instead of a bytes format
    h.update(raw)
    hashed = h.hexdigest()

    # this is then written to the HMAC-SHA512 file for storage and returned to main
    with open('/home/raspberry/Desktop/Hashing/HMAC-SHA512', 'w') as f:
        f.write(hashed)
    print("[ HASHING COMPLETE ]")
    return hashed
