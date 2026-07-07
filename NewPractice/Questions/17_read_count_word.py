def countWords():

    file = open("demo.txt", "r")

    text = file.read()

    words = text.split()

    print("Total Words:", len(words))

    file.close()

countWords()