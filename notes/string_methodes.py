#AB 1st String Methodes

subject = 'Computer Programming 1'

print(subject.upper())

print(subject.center(100))

#Stupid Proofing
color = input('What is your favorite color?').strip().title()
print('Wow, {color} is a great favorit color!'.format(color=color))

#f-string
print(f'I like {color} too!')
pi = 3.141592
#print(f"We all know pi is equal to {pi:3}")

sentence = 'The quick brown fox jumps over the lazy dog'
word = "jumps"
start = sentence.index(word)
length = len("lazy")
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))

