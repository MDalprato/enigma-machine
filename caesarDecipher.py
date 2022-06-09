# caesar cipher decipher
# info here https://en.wikipedia.org/wiki/Caesar_cipher

secret_message = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD !"

LETTERS_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

max_shift_attampt = 4; # this is how deep will be the attempt in order to decipher the message

# Iterate over the string

for i in range(max_shift_attampt):

  output = [];
  outputMsg = '';
  for element in secret_message:
      if (element in LETTERS_LIST):
          currentIndex = LETTERS_LIST.index(element.upper());
          shiftedIndex = currentIndex + i;
          lenghtOfLetters = len(LETTERS_LIST);
          if(shiftedIndex >= lenghtOfLetters):
              shiftedIndex = shiftedIndex - lenghtOfLetters;
          newLetter = LETTERS_LIST[shiftedIndex];
      else:
          newLetter = element;
      output.append(newLetter)
      print("Cipher secret_message =  " + outputMsg.join(output))

