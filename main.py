import string

file = open("C:\\Users\\shilp\\Desktop\\GatechSpring22\\MiniProjects\\WORDLE\\venv\\fiveWordsList", 'r')

def read_file(file):
    values = file.readlines()
    values.sort()
    return values

def main():
    words_allowed = list(string.ascii_lowercase)
    print("Enter the first word as ideas")
    #  TODO: Enter cases where user might make invalid input
    #  TODO: Enter case where user can ask computer for another word (just in case the user doesn't like it)
    word = "ideas"
    possible_word = []
    imprecise_located_words = [[]]

    found = False
    while not found:
        result = input("Enter the result.\nG for green\nB for uncolored\nY for yellow\nRemember to make exactly one space between each")
        result = result.split(" ")
        for i in range(len(result)):
            if (result[i].upper() == "G"):
                possible_word[i] = word[i]
            elif (result[i].upper() == "Y"):
                imprecise_located_words[i].append(word[i])
            else:
                words_allowed.remove(word[i])
        word = findNewWord(result, word, imprecise_located_words, possible_word, words_allowed)


##Let's play a game and check how the program would work...



def findNewWord(result, word, imprecise_located_words, possible_word, words_allowed):
    values = read_file(file)
    getFromMid() ##This method would find the words in file and then check if they are valid
    makeWord() ##This method will make a new word and check if that word is in the file

def makeWord(words_allowed, possible_words, imprecise_located_words, values):
    word = []
    for i in range(len(possible_words)):
        word[i] = possible_words[i]
    exists = False
    while not exists:
        # Creating a word
        for i in range(len(word)):
            if word[i] == None:
                ## Add imprecise_located words


    binarySearch(word, values)

def getFromMid(words_allowed, possible_words, imprecise_located_words, values):
    word = values[len(values) / 2]
    acceptable = False
    while not acceptable:
        for i in range(len(word)): #length of word
            if (word[i] not in words_allowed): #words_allowed --> somewhere around 26 (can we say this to be constant)
                word = getFromMid(words_allowed, possible_words, imprecise_located_words, values.remove(word))
                acceptable = True





                


if __name__ == '__main__':
    main()
