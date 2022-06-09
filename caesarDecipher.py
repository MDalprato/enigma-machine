# Basic caesar cipher
# info here https://en.wikipedia.org/wiki/Caesar_cipher


message = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD !"
LETTERS_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
output = []
outputMsg = ''

# Iterate over the string
for element in message:
    if (element in LETTERS_LIST):
        currentIndex = LETTERS_LIST.index(element.upper());
        shiftedIndex = currentIndex - 3;
        lenghtOfLetters = len(LETTERS_LIST);
        if(shiftedIndex > lenghtOfLetters):
            shiftedIndex = shiftedIndex - lenghtOfLetters;
        newLetter = LETTERS_LIST[shiftedIndex];
    else:
        newLetter = element;
    output.append(newLetter)

print("Cipher message =  " + outputMsg.join(output))
