import mbedtls as mbed
import secrets

# this function will round the message length to a specified blockchain length
# e.g. a 55 byte message in a 16 byte CBC wil be rounded to 64 bytes
def round_multiple(num, multiple):
    return ((num-1) | (multiple-1))+1

# >------- AES 256 -------<
def aes_256(encoded_message):
    # the function the takes a generated key and decrypts the message (in byte format) in the correct algorithm
    k = open('/home/raspberry/Desktop/AES256/AES256-Key', 'r')
    plainkey = k.read()
    encodedkey = bytes(plainkey, 'utf-8')

    # initialisation vector entropy generation is done by secrets.py
    # and truncated to a max size of 16 bytes, this is needed to decrypt message
    # but will not decrypt the first block (16 bytes)
    entropy = secrets.randbits(150)
    plainiv = str(entropy)[:16]
    encodediv = bytes(plainiv, 'utf-8')

    # AES cipher blockchain encryption (function passed the key, mode and IV)
    # the encoded message uses this algorithm data to decrypt the message
    c = mbed.cipher.AES.new(encodedkey, mbed.cipher.MODE_CBC, encodediv)
    dec = c.decrypt(encoded_message)

    # all null bytes (\x00) are then removed form the message as it cna be guaranteed that these aren't required
    message = dec.strip(b'\x00')
    decode_message = message.decode('utf-8')

    # the encrypted is then written to the ENCRYPTED-File
    # the first 16 bytes are removed as this is padding for the IV
    with open('/home/raspberry/Desktop/AES256/DECRYPTED-File', 'w') as f:
        f.write(decode_message[16:])

    print("[ DECRYPTION COMPLETE ]")
    return decode_message[16:]

# >------- AES 128 -------<
# the only variation between AES 128 & 256 is the length of key used, with the longer key being more secure
def aes_128(encoded_message):
    # the function the takes a generated key and decrypts the message (in byte format) in the correct algorithm
    k = open('/home/raspberry/Desktop/AES128/AES128-Key', 'r')
    plainkey = k.read()
    encodedkey = bytes(plainkey, 'utf-8')

    # initialisation vector entropy generation is done by secrets.py
    # and truncated to a max size of 16 bytes, this is needed to decrypt message
    # but will not decrypt the first block (16 bytes)
    entropy = secrets.randbits(150)
    plainiv = str(entropy)[:16]
    encodediv = bytes(plainiv, 'utf-8')

    # AES cipher blockchain encryption (function passed the key, mode and IV)
    # the encoded message uses this algorithm data to decrypt the message
    c = mbed.cipher.AES.new(encodedkey, mbed.cipher.MODE_CBC, encodediv)
    dec = c.decrypt(encoded_message)

    # all null bytes (\x00) are then removed form the message as it cna be guaranteed that these aren't required
    message = dec.strip(b'\x00')
    decode_message = message.decode('utf-8')

    # the encrypted is then written to the ENCRYPTED-File
    # the first 16 bytes are removed as this is padding for the IV
    with open('/home/raspberry/Desktop/AES256/DECRYPTED-File', 'w') as f:
        f.write(decode_message[16:])

    print("[ DECRYPTION COMPLETE ]")
    return decode_message[16:]

# >------- 3DES -------<
# 3DES is also a cipher block chain (CBC) like AES but is considered more vulnerable
# 3DES also works in 8 byte cipher blocks
def des3(encoded_message):
    # the function the takes a generated key(s) and decrypts the message (in byte format) in the correct algorithm
    k = open('/home/raspberry/Desktop/3DES/3DES-Key', 'r')
    plainkey = k.read()
    encodedkey = bytes(plainkey, 'utf-8')

    # initialisation vector entropy generation is done by secrets.py
    # and truncated to a max size of 8 bytes, this is needed to decrypt message
    # but will not decrypt the first block (8 bytes)
    entropy = secrets.randbits(150)
    plainiv = str(entropy)[:8]
    encodediv = bytes(plainiv, 'utf-8')

    # 3DES cipher blockchain encryption (function passed the key, mode and IV)
    # the encoded message uses this algorithm data to decrypt the message
    c = mbed.cipher.DES3.new(encodedkey, mbed.cipher.MODE_CBC, encodediv)
    dec = c.decrypt(encoded_message)

    # all null bytes (\x00) are then removed form the message as it cna be guaranteed that these aren't required
    message = dec.strip(b'\x00')
    decode_message = message.decode('utf-8')

    # the encrypted is then written to the ENCRYPTED-File
    # the first 16 bytes are removed as this is padding for the IV
    with open('/home/raspberry/Desktop/3DES/DECRYPTED-File', 'w') as f:
        f.write(decode_message[8:])

    print("[ DECRYPTION COMPLETE ]")
    return decode_message[8:]

