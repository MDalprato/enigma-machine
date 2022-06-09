#Basic caesar cipher
import array as arr

message = "Hello";
LETTERS_LIST = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

# Iterate over the string
for element in message:
    print(element, end=' ');
    currentIndex = LETTERS_LIST.index(element.upper());
    shiftedIndex = currentIndex + 3;
    newLetter = LETTERS_LIST[shiftedIndex]
    print("element = " + element + ", new = " + newLetter);
print("\n")