def encode_pass(password):
    new_pass = ''
    for num in password:
         new_pass += str((int(num) + 3) % 10)
    return new_pass


def decode_pass(password):
    pass_nums = password.split()
    for num in pass_nums:
        num = int(num) - 3
    for num in pass_nums:
        pass_nums += str(num)
    return pass_nums


def main():
    option = 0
    while option != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            user_password = input("Please enter a password to encode: ")
            encoded_pass = encode_pass(user_password)
            print(encoded_pass)
            print("Your password has been encoded and stored!")
        if option == 2:
            decoded_pass = decode_pass(user_password)
            print(f'The encoded password is {encoded_pass}, and the original password is {user_password}')
    else:
        exit



if __name__ == "__main__":
    main()