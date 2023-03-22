def encode_pass(password):
    new_pass = ""
    for num in password:
         new_pass += str((int(num) + 3) % 10)
    return new_pass


def decode_pass(password):
    decoded_pass = ''
    for num in password:
        if num == "2":
            decoded_pass += "9"
        elif num == "1":
            decoded_pass += "8"
        elif num == "0":
            decoded_pass += "7"
        else:
            decoded_pass += str((int(num) - 3) % 10)
    return decoded_pass


def main():
    option = 0
    while option != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            user_password = input("Please enter a password to encode: ")
            encoded_pass = encode_pass(user_password)
            print("Your password has been encoded and stored!")
            print()
        if option == 2:
            decoded_pass = decode_pass(encoded_pass)
            print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.')
        if option == 3:
            break


if __name__ == "__main__":
    main()
