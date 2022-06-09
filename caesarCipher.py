# Basic caesar cipher
# info here https://en.wikipedia.org/wiki/Caesar_cipher

message = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG !"
LETTERS_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
output = []
outputMsg = ''

# This is the cypher code
def cipher_message(msg):
    lenghtOfLetters = len(LETTERS_LIST);
    # Iterate over the string
    for element in msg:
        if (element in LETTERS_LIST):
            currentIndex = LETTERS_LIST.index(element.upper());
            shiftedIndex = currentIndex - 3;
            if(shiftedIndex > lenghtOfLetters):
                shiftedIndex = shiftedIndex - lenghtOfLetters;
            newLetter = LETTERS_LIST[shiftedIndex];
        else:
            newLetter = element;
        output.append(newLetter)
    print("Cipher message =  " + outputMsg.join(output))
#end of the cypher code

cipher_message(message);
