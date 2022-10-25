# composes a string with each digit increased by 3. 7-9 would result in two-digit numbers, so they restart at 0
def encode(pw):
    p_enc = ""
    for char in pw:
        p_enc += str(int(char) + 3 if int(char) < 7 else int(char) - 7)
    return p_enc


def decode(pw):
    p_dec = ""
    for char in pw:
        p_dec += str(int(char) - 3 if int(char) >= 3 else int(char) + 7)
    return p_dec

if __name__ == "__main__":
    while True:
        option = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
        match option:
            case "1":
                pw_enc = encode(input("Please enter your password to encode: "))
                print("Your password has been encoded and stored!\n")
            case "2":
                print(f"The encoded password is {pw_enc}, and the original password is {decode(pw_enc)}.\n")
            case "3":
                break
            case _:
                print("Invalid selection")
