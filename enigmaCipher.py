#Hi! This program replicates the Enigma cipher from Nazi Germany during
#World War II. The rotors, reflectors, and plugboard settings are authentic
#and the output is given according to cryptographic conventions.

#Rotors
I = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q', 0, 0]
II = ['AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E', 0, 0]
III = ['BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V', 0, 0]
IV = ['ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J', 0, 0]
V = ['VZBRGITYUPSDNHLXAWMJQOFECK', 'Z', 0, 0]

rotors = [I,II,III]

#Reflectors
rA = 'EJMZALYXVBWFCRQUONTSPIKHGD'
rB = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
rC = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

reflector = rB

A=ord('A')
a=ord('a')
Z=ord('Z')
z=ord('z')

#Plugboard
plugboard='FW DL NX BV KM RZ HY IQ EC JU'
temp={}
for pair in plugboard.split():
    temp[pair[0]]=pair[1]
    temp[pair[1]]=pair[0]
for i in range(A,Z+1):
    if chr(i) not in plugboard:
        temp[chr(i)]=chr(i)
plugboard=temp

NUMBERS={'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
def sanitize(message):
    sanitized = ''
    message = message.lower()
    #Makes the entire string lowercase
    for symbol in message:
        if symbol >= 'a' and symbol <= 'z':
            sanitized += symbol
        #Checks if the symbol in the message is in the alphabet; if not, the character is not added
        elif symbol >= '0' and symbol <='9':
            sanitized+=NUMBERS[symbol]
    return sanitized

def groom(encrypted, size=5):
#Prepares the string for display
  counter = 1
  #Initializes the counter variable
  groomed = ""
  for symbol in encrypted:
    groomed += symbol
    if counter%size == 0:
      groomed += " "
    #Adds a space every 5th letter
    counter += 1
    #Counts the number of iterations
  return groomed.upper()

def throughPb(letter, rotor=['','',0]):
    return plugboard[chr((ord(letter)-rotor[2]-A)%26+A)]

def throughRef(letter, reflector, prevRot=['','',0]):
    return reflector[(ord(letter)-A-prevRot[2])%26]
    
def forwardRot(letter, nextRot, prevRot=['','',0]):
    return nextRot[0][(ord(letter)-A+nextRot[2]-prevRot[2])%26]

def backwardRot(letter, nextRot, prevRot=['','',0]):
    letter = chr((ord(letter)+nextRot[2]-prevRot[2]-A)%26+A)
    return chr(A+nextRot[0].index(letter))

def rotorStep(rotor1, rotor2, rotor3):
    rotor3[2]+=1
    rotor3[2]%=26
    if rotor3[2] == (2+ord(rotor3[1])-A)%26:
        rotor2[2]+=1
        rotor2[2]%=26 #double stepping on the second rotor
    if ((rotor2[2] == (1+ord(rotor2[1])-A)%26) and
       (rotor3[2] != (3+ord(rotor3[1])-A)%26)):
        rotor2[2]+=1
        rotor2[2]%=26
        rotor1[2]+=1
        rotor1[2]%=26 #double stepping on the third rotor
    return [rotor1,rotor2,rotor3]

def prepRot(rotors, offset1, offset2, offset3,
            ring1, ring2, ring3):
    
    rotor1,rotor2,rotor3=rotors
    rotor1[2] = (rotor1[2]+ord(offset1)-A-ring1+1)%26
    rotor2[2] = (rotor2[2]+ord(offset2)-A-ring2+1)%26
    rotor3[2] = (rotor3[2]+ord(offset3)-A-ring3+1)%26
    rotor1[1] = chr((ord(rotor1[1])-ring1-A)%26+A)
    rotor2[1] = chr((ord(rotor2[1])-ring2-A)%26+A)
    rotor3[1] = chr((ord(rotor3[1])-ring3-A)%26+A)
    rotor1[3] = ring1
    rotor2[3] = ring2
    rotor3[3] = ring3
    return [rotor1,rotor2,rotor3]

first = 0
    
def encrypt(message, rotors, ref, offset1, offset2,
            offset3, ring1, ring2, ring3):
    [rotor1,rotor2,rotor3] = prepRot(rotors, offset1, offset2,
                                    offset3,ring1, ring2, ring3)
    message=sanitize(message).upper()
    encrypted=''
    count = 0
    for letter in message:
        if count == 0 and ((rotor2[2] == (1+ord(rotor2[1])-A)%26) and
       (rotor3[2] == (1+ord(rotor3[1])-A)%26)): #edge case: start in triple step position
          rotor3[2]+=1
          rotor3[2]%=26
          rotor2[2]+=1
          rotor2[2]%=26
          rotor1[2]+=1
          rotor1[2]%=26
        else:
          [rotor1,rotor2,rotor3]=rotorStep(rotor1, rotor2, rotor3)
        letter=throughPb(letter)
        letter=forwardRot(letter, rotor3)
        letter=forwardRot(letter, rotor2, rotor3)
        letter=forwardRot(letter, rotor1, rotor2)
        letter=throughRef(letter, ref, rotor1)
        letter=backwardRot(letter, rotor1)
        letter=backwardRot(letter, rotor2, rotor1)
        letter=backwardRot(letter, rotor3, rotor2)
        letter=throughPb(letter, rotor3)
        encrypted+=letter
        count += 1
    return groom(encrypted)

secret="AAAAA"
encrypted=encrypt(secret,rotors,rB,'A','A','A',1,1,1)

print(encrypted)
