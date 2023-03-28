import Encryption
import Decryption
import KeyGen


def hashing():
    print("hashing test")


def hmac_gen():
    print("hmac test")

# KEY GENERATION MENU:
# A menu is used to select the desired key for which encryption algorith is being used
# depending on the algorithm the key length generated / stored will vary
def key_menu():
    # menu options array of algorithms for user to select specific key type required
    # this will array the length of key generated (e.g. 32 bytes or 16 bytes)
    key_options = {
        1: 'AES 256',
        2: 'AES 128',
        3: '3DES',
        4: 'Exit',
    }

    # a for loop prints the options array with correlating number
    print(">----  KEY GENERATION  ----<")
    for i in key_options.keys():
        print('[', i, ']', key_options[i])

    # user input will loop until a correct input is give (e.g. 3
    # try except statement for exception handling to mitigate errors
    while True:
        key_option = ''
        try:
            key_option = int(input('Please Select a Key: '))
        except:
            print('Wrong input. Please enter a number ...')

        if key_option == 1:
            print(KeyGen.aes256_key())
            return
        elif key_option == 2:
            print(KeyGen.aes128_key())
            return
        elif key_option == 3:
            print(KeyGen.des3_key())
            return
        elif key_option == 4:
            print('### Returning To Menu ###')
            return
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

# ENCRYPTION MENU:
# A menu is used to select the desired algorith (e.g. AES256) being used
# this encryption will grab the relevant key for encryption
def encryption_menu():
    # user check to ensure there is input data in the relevant file
    # Loops until user inputs "y"
    x = 1
    print("please enter [y] when message is in /home/raspberry/Desktop/***/RAW-File")
    while x == 1:
        check = input(">>> ")
        if check == "y":
            x = 0
        else:
            print("please enter valid input")

    # menu options array of algorithms for user to select
    encryption_options = {
        1: 'AES 256',
        2: 'AES 128',
        3: '3DES',
        4: 'Exit',
    }

    # a for loop prints the options array with correlating number
    print(">----  ENCRYPTION  ----<")
    for i in encryption_options.keys():
        print('[', i, ']', encryption_options[i])

    # user input will loop until a correct input is give (e.g. 3
    # try except statement for data validation
    while True:
        crypt_option = ''
        try:
            crypt_option = int(input('Please Select an Encryption Algorithm: '))
        except:
            print('Wrong input. Please enter a number ...')

        # when an option is selected the program will grab the RAW data to be encrypted for the relevant algorithm
        # the encryption import and algorithm function is then called with a RAW data passed through
        if crypt_option == 1:
            f = open('/home/raspberry/Desktop/AES256/RAW-File', 'r')
            message = f.read()
            print(Encryption.aes_256(message))
            return
        elif crypt_option == 2:
            f = open('/home/raspberry/Desktop/AES128/RAW-File', 'r')
            message = f.read()
            print(Encryption.aes_128(message))
            return
        elif crypt_option == 3:
            f = open('/home/raspberry/Desktop/3DES/RAW-File', 'r')
            message = f.read()
            print(Encryption.des3(message))
            return
        elif crypt_option == 4:
            print('### Returning To Menu ###')
            return
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


# DECRYPTION MENU:
# A menu is used to select the desired algorith (e.g. AES256) being used
# this  will grab the relevant key for algorithm and pass it to the decryption function
def decryption_menu():
    # user check to ensure there is input data in the relevant file
    # Loops until user inputs "y"
    x = 1
    print("please enter [y] when message is in /home/raspberry/Desktop/***/ENCRYPTED-File")
    while x == 1:
        check = input(">>> ")
        if check == "y":
            x = 0
        else:
            print("please enter valid input")

    # menu options array of algorithms for user to select
    decryption_options = {
        1: 'AES 256',
        2: 'AES 128',
        3: '3DES',
        4: 'Exit',
    }

    # a for loop prints the options array with correlating number
    print(">----  DECRYPTION  ----<")
    for i in decryption_options.keys():
        print('[', i, ']', decryption_options[i])

    # user input will loop until a correct input is give (e.g. 3
    # try except statement for data validation
    while True:
        crypt_option = ''
        try:
            crypt_option = int(input('Please Select an Encryption Algorithm: '))
        except:
            print('Wrong input. Please enter a number ...')

        # when an option is selected the program will grab the Encrypted data to be
        # encrypted for the relevant algorithm.
        # the encryption import and algorithm function is then called with a RAW data passed through
        if crypt_option == 1:
            f = open('/home/raspberry/Desktop/AES256/ENCRYPTED-File', 'rb')
            encodedfile = f.read()
            print(Decryption.aes_256(encodedfile))
            return
        elif crypt_option == 2:
            f = open('/home/raspberry/Desktop/AES128/ENCRYPTED-File', 'rb')
            encodedfile = f.read()
            print(Decryption.aes_128(encodedfile))
            return
        elif crypt_option == 3:
            f = open('/home/raspberry/Desktop/3DES/ENCRYPTED-File', 'rb')
            encodedfile = f.read()
            print(Decryption.des3(encodedfile))
            return
        elif crypt_option == 4:
            print('### Returning To Menu ###')
            return
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

# MAIN MENU
# this menu selection is broken down into the  functionality a user interacting with the HSM would require
# menu function creates an array of menu selections and displays them
def main_menu():
    menu_options = {
        1: 'Hashing',
        2: 'Generate HMAC',
        3: 'Generate Key',
        4: 'Encrypt',
        5: 'Decrypt',
        6: 'Exit',
    }

    print(">----  MENU  ----<")
    for i in menu_options.keys():
        print('[', i, ']', menu_options[i])


# main code acts as the main menu for user interaction
# user input will loop until a correct input is give (e.g. 4)
# try except statement for data validation, with each option calling the relevant function
if __name__ == "__main__":
    while True:
        main_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        if option == 1:
            hashing()
        elif option == 2:
            hmac_gen()
        elif option == 3:
            key_menu()
        elif option == 4:
            encryption_menu()
        elif option == 5:
            decryption_menu()
        elif option == 6:
            print('### Exiting HSM ###')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 5.')
