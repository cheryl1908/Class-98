def countWordsFromFile():
    fileName=input("Enter the file name: ")
    noOfWords=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        noOfWords=noOfWords+len(words)
    print("The no of words in the file: ", noOfWords)

countWordsFromFile()