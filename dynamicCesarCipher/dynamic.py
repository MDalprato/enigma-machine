# Dynamic caesar cipher
# info here https://en.wikipedia.org/wiki/Caesar_cipher
# This basically works in this way:  it will use the current date time as a shift constant

from datetime import datetime;
import math;

message = "PROSSIMO attacco posizione 44.281525888115794, 11.900987295767901"
LETTERS_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
output = []
outputMsg = ''


def obtainCurrentShifter():
  # Function that allow us to obtain the current shift direction of the cipher method
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S:%S");
  minutes = now.strftime("%M"); #minutes -> from 00 to max 59
  seconds = now.strftime("%S"); #seconds -> from 00 to max 59
  values = [int(minutes), int(seconds)];
  shifter = math.ceil(sum(values) / 23); #index up to 118 max value (59+59);
  return shifter;

# This is the cypher code
def cipher_message(msg):
  lenghtOfLetters = len(LETTERS_LIST);
  currentShifter =  obtainCurrentShifter();
  print("current shifter is = " + str(currentShifter))

  # Iterate over the string
  for element in msg:
      if (element.upper() in LETTERS_LIST):
          currentIndex = LETTERS_LIST.index(element.upper());
          shiftedIndex = currentIndex - obtainCurrentShifter();
          if(shiftedIndex > lenghtOfLetters):
              shiftedIndex = shiftedIndex - lenghtOfLetters;
          newLetter = LETTERS_LIST[shiftedIndex];
      else:
          newLetter = element;
      output.append(newLetter)
  print("Cipher message =  " + outputMsg.join(output))
#end of the cypher code

cipher_message(message);
