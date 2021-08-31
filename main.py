import logo

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

logo.print_logo()


def caesar_cipher(text_message, shift_amount, activity):
    if shift_amount > 25:
        shift_amount = shift_amount % 25
    if activity == "encode":
        encoded_message = ""
        for letter in text_message:
            temporary_variable = 0
            for alphabet in alphabets:
                if letter == alphabet:
                    index = alphabets.index(letter)
                    index += shift_amount
                    encoded_message += alphabets[index]
                    temporary_variable += 1
            if temporary_variable == 0:
                encoded_message += letter
        print(encoded_message)
    elif activity == "decode":
        decoded_message = ""
        for letter in text_message:
            temporary_variable = 0
            for alphabet in alphabets:
                if letter == alphabet:
                    index = alphabets.index(letter)
                    if shift_amount == 0:
                        index = index
                    elif index >= shift_amount:
                        index = index - shift_amount
                    elif shift_amount > index:
                        index = shift_amount - index
                        index = 26 - index
                    decoded_message += alphabets[index]
                    temporary_variable += 1
            if temporary_variable == 0:
                decoded_message += letter
        print(decoded_message)


def main():
    running = True
    while running:
        activity = input("Type 'encode' to encrypt, type 'decode' to decrypt...\n")
        message = input("Type your message: ").lower()
        shift = int(input("Type the shift amount: "))
        caesar_cipher(message, shift, activity)
        decision = input("Do you want to run this code again?(Yes/No)\n").lower()
        if decision == "no":
            running = False


if __name__ == "__main__":
    main()
