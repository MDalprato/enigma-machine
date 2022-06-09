# caesar cipher decipher
# info here https://en.wikipedia.org/wiki/Caesar_cipher


# This is the decypher code

def decipher_message(msg, attempt):

    LETTERS_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lenghtOfLetters = len(LETTERS_LIST)

    if(attempt > lenghtOfLetters):
        print("Attempts are more than letter, cannot proceed");
        return;
    for i in range(attempt):
        output = []
        outputMsg = ''
        for element in msg:
            if (element in LETTERS_LIST):
                currentIndex = LETTERS_LIST.index(element.upper())
                shiftedIndex = currentIndex + i
                if(shiftedIndex >= lenghtOfLetters):
                    shiftedIndex = shiftedIndex - lenghtOfLetters
                newLetter = LETTERS_LIST[shiftedIndex]
            else:
                newLetter = element
            output.append(newLetter)
        print("Attempt: " + str(i) + ", value: " + outputMsg.join(output))


secret_message = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD !"
# this is how deep will be the attempt in order to decipher the message
decipher_message(secret_message, 10)
