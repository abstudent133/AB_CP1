#AB 1st Ceasar Cipher Encoder and Decoder

#Capital ASCII letters start at 65 and end at 90
#Lowercase letters start at 97 and end at 122
#print(f"a = {ord("a")}")
#print(f"98 = {chr(98)}")



#message is ""
message = ""

#definition of action is(shift)
def action(message, shift):
    new_message = ""
    for letter in message:
            #if letter is alpha
            if letter.isalpha():
                #if the letter is uppercase
                if letter.isupper():
                    #new letter is the ascii letter - 65 + the shift modulo 26 + 65
                    new_letter = chr((ord(letter) - 65 + shift) % 26 + 65)
                    #add new letter to new message
                    new_message += new_letter

                #else
                else:
                    #new letter is the ascii letter - 97 + the shift modulo 26 + 97 because it has to wrap around
                    new_letter = chr((ord(letter) - 97 + shift) % 26 + 97)
                    #add new letter to new message
                    new_message += new_letter
                
            #else
            else:
                #add letter to new message
                new_message += letter
                #contiune
                continue
    return new_message
    



#Show Hello this is a Caesar cipher for encoding and decoding messages. If you would like to encode a message enter 1 and if you would like to decode enter 2.
print("Hello. This is a Caesar cipher for encoding and decoding messages. If you would like to encode a message enter 1 but if you want to decode a message enter 2.")
message = input("Please enter the code you would like to encode or decode: ")
# choice is  ask Please enter the number of the action you would like to complete:
choice = int(input("Please enter the number of the action you would like to complete: "))

#if they chose 1 then
if choice == 1:
    #shift is ask choose an amount to shift the letters
    shift = int(input("What is the number the letters shifted by: "))
    #show message
    print(f"This is the new message: {action(message, shift)}")
#or else they chose 2 then
elif choice == 2:
    #shift is what is the amount that the message was shifted
    shift = int(input("What is the number the letters shifted by: "))
    #show message
    print(f"This is the decoded message: {action(message, -shift)}")
