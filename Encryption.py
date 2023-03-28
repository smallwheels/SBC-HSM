import mbedtls as mbed
import secrets

# this function will round the message length to a specified blockchain length
# e.g. a 55 byte message in a 16 byte CBC wil be rounded to 64 bytes
def round_multiple(num, multiple):
    return ((num-1) | (multiple-1))+1

# >------- AES 256 -------<
def aes_256(message):
    # this first part of the process pads the desired message with the first block of 16 (with 16 bytes)
    # to avoid part of the message being missing during decryption (due to missing IV)
    # then finds the length of the message and pads it to the correct length as a multiple of 16 (see for loop)
    # null bytes are used (\x00) as they can be removed during decryption
    iv_padding = ""
    for i in range(16):
        iv_padding += "\x00"
    block_limit = round_multiple(len(message.rstrip()), 16)

    # the minimum length of input for AES in general in 48 so a check is here in case of very small input
    if block_limit < 48:
        block_limit = 48

    # the filler is then calculated and generated based on the cipher block limit found
    # this is then combined with the IV and message (stripped to avoid any blank space)
    # null bytes are used (\x00) as they can be removed during decryption
    filler_len = block_limit - len(message.rstrip())
    filler = ""
    for i in range(filler_len):
        filler += "\x00"
    padded_message = iv_padding + message.rstrip() + filler

    # the function then takes a generated key and generates an IV (this IV is different for every message)
    # then encrypts the padded message (in byte format) in the correct algorithm
    f = open('/home/raspberry/Desktop/AES256/AES256-Key', 'r')
    plainkey = f.read()
    encodedkey = bytes(plainkey, 'utf-8')

    # initialisation vector entropy generation is done by secrets.py
    # and truncated to a max size of 16 bytes
    entropy = secrets.randbits(150)
    plainiv = str(entropy)[:16]
    encodediv = bytes(plainiv, 'utf-8')

    # AES cipher encryption is done in Cipher Block Chain mode for security with a 256bit Key
    # this then encrypts the padded message in a byte format
    c = mbed.cipher.AES.new(encodedkey, mbed.cipher.MODE_CBC, encodediv)
    enc = c.encrypt(bytes(padded_message, 'utf-8'))

    # the encrypted is then written to the ENCRYPTED-File and returned to main.py
    with open('/home/raspberry/Desktop/AES256/ENCRYPTED-File', 'wb') as f:
        f.write(enc)
    print("[ ENCRYPTION COMPLETE ]")
    return enc


# >------- AES 128 -------<
def aes_128(message):
    # this first part of the process pads the desired message with the first block of 16 (with 16 bytes)
    # to avoid part of the message being missing during decryption (due to missing IV)
    # then finds the length of the message and pads it to the correct length as a multiple of 16 (see for loop)
    # null bytes are used (\x00) as they can be removed during decryption
    iv_padding = ""
    for i in range(16):
        iv_padding += "\x00"
    block_limit = round_multiple(len(message.rstrip()), 16)

    # the minimum length of input for AES in general in 48 so a check is here in case of very small input
    if block_limit < 48:
        block_limit = 48

    # the filler is then calculated and generated based on the cipher block limit found
    # this is then combined with the IV and message (stripped to avoid any blank space)
    # null bytes are used (\x00) as they can be removed during decryption
    filler_len = block_limit - len(message.rstrip())
    filler = ""
    for i in range(filler_len):
        filler += "\x00"
    padded_message = iv_padding + message.rstrip() + filler

    # the function then takes a generated key and generates an IV (this IV is different for every message)
    # then encrypts the padded message (in byte format) in the correct algorithm
    f = open('/home/raspberry/Desktop/AES128/AES128-Key', 'r')
    plainkey = f.read()
    encodedkey = bytes(plainkey, 'utf-8')

    # initialisation vector entropy generation is done by secrets.py
    # and truncated to a max size of 16 bytes
    entropy = secrets.randbits(150)
    plainiv = str(entropy)[:16]
    encodediv = bytes(plainiv, 'utf-8')

    # this AES cipher encryption is done in Cipher Block Chain mode for security with a 128bit Key
    # making it less secure than aes 256, this then encrypts the padded message in a byte format
    c = mbed.cipher.AES.new(encodedkey, mbed.cipher.MODE_CBC, encodediv)
    enc = c.encrypt(bytes(padded_message, 'utf-8'))

    # the encrypted is then written to the ENCRYPTED-File and returned to main.py
    with open('/home/raspberry/Desktop/AES128/ENCRYPTED-File', 'wb') as f:
        f.write(enc)
    print("[ ENCRYPTION COMPLETE ]")
    return enc


# >------- 3DES -------<
def des3(message):
    # des3 is a more insecure encryption due to the smaller block size
    # this first part of the process pads the desired message with the first block of 8 (with 8 bytes)
    # to avoid part of the message being missing during decryption (due to missing IV)
    # then finds the length of the message and pads it to the correct length as a multiple of 8 (see for loop)
    # null bytes are used (\x00) as they can be removed during decryption
    iv_padding = ""
    for i in range(8):
        iv_padding += "\x00"

    # initialisation vector entropy generation
    entropy = secrets.randbits(150)
    plainiv = str(entropy)[:8]
    encodediv = bytes(plainiv, 'utf-8')
    block_limit = round_multiple(len(message.rstrip()), 8)

    # the minimum length is still implemented to ensure security
    if block_limit < 48:
        block_limit = 48

    # the filler is then calculated and generated based on the cipher block limit found
    # this is then combined with the IV and message (stripped to avoid any blank space)
    # null bytes are used (\x00) as they can be removed during decryption
    filler_len = block_limit - len(message.rstrip())
    filler = ""
    for i in range(filler_len):
        filler += "\x00"
    padded_message = iv_padding + message.rstrip() + filler

    # the function then takes a generated key and generates an IV (this IV is different for every message)
    # then encrypts the padded message (in byte format) in the correct algorithm
    f = open('/home/raspberry/Desktop/3DES/3DES-Key', 'r')
    plainkey = f.read()
    encodedkey = bytes(plainkey, 'utf-8')

    # the function then generates an IV (this IV is different for every message)
    # then encrypts the padded message (in byte format) in the correct algorithm
    entropy = secrets.randbits(150)
    plainiv = str(entropy)[:16]
    encodediv = bytes(plainiv, 'utf-8')

    # 3DES cipher encryption
    c = mbed.cipher.DES3.new(encodedkey, mbed.cipher.MODE_CBC, encodediv)
    enc = c.encrypt(bytes(padded_message, 'utf-8'))

    # the encrypted is then written to the ENCRYPTED-File
    with open('/home/raspberry/Desktop/3DES/ENCRYPTED-File', 'wb') as f:
        f.write(enc)
    print("[ ENCRYPTION COMPLETE ]")
    return enc
