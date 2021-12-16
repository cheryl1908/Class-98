f= open("text.txt")
fileLines = f.readlines()
for line in fileLines:
    print(line)


introString = "My name is Shwetha, I am a coding teacher at WHJ"

words = introString.split(',')
print(words)

def greet(name):
    print("Hello, "+ name + ". How are you?")

greet("Cheryl")