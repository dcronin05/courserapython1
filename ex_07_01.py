def wordsfile():

    name = input("Enter file name: ")
    wordsfile = open(name, 'r')

    for words in wordsfile:
        print(words.strip().upper())

wordsfile()