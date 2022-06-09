# caesar cipher decipher
# info here https://en.wikipedia.org/wiki/Caesar_cipher

def decipher_message(msg, attempt):
# This is the decypher code

    LETTERS_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

    lenghtOfLetters = len(LETTERS_LIST);

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
    answerIndex = input("Insert index of valid text ... ");
    print("The shift value was equal to = " + answerIndex)


secret_message = "MOLPPFJL 7QQ799L MLPFWFLKB 11.Z5Y2Z2555YY2461, YY.6XX654Z624346XY"
# this is how deep will be the attempt in order to decipher the message
decipher_message(secret_message, 10);
