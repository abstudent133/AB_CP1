#AB 1st Ceasar Cipher Encoder and Decoder

#Capital ASCII letters start at 65 and end at 90
#Lowercase letters start at 97 and end at 122
#print(f"a = {ord("a")}")
#print(f"98 = {chr(98)}")



#message is ""
message = ""

#definition of action is(shift)
def action(shift):
    # for each letter in message
    for letter in message:
        #if letter is alpha
        if letter.isalpha():
            #ord letter + shift
            new_letter = chr(ord(letter)+shift)
            #return new message
            return new_letter
        #else
        else:
            #contiune
            contiue
    



#Show Hello this is a Caesar cipher for encoding and decoding messages. If you would like to encode a message enter 1 and if you would like to decode enter 2.
print("Hello. This is a Caesar cipher for encoding and decoding messages. If you would like to encode a message enter 1 but if you want to decode a message enter 2.")
# choice is  ask Please enter the number of the action you would like to complete:
choice = input("Please enter the number of the action you would like to complete: ")

#if they chose 1 then
if choice == 1:
    #message is what is the message you would like to encode
    
    #shift is ask choose an amount to shift the letters
    #action(shift)
    #show message
#or else they chose 2 then
    #message is what is the message you would like to decode
    #shift is what is the amount that the message was shifted
    #action(shift)
    #show message
