def hawkID():
    return("wjzheng")

def q1(infoDict, listOfLists):
    #the largest element in listOfLists[i] if listOfLists[i] is red,
    #the smallest element in listOfLists[i] if listOfLists[i] is blue,
    #the most common element in listOfLists[i] if listOfLists[i] is green 
    #(if there is a tie for most common, take the smallest one, and use None if there are no elements)
    coloredList = []
    result = []
    smallest = None
    biggest = None
    for l in listOfLists:
        #print
        red = 0
        blue = 0
        green = 0
        for element in l:
            #print("element", element)
            if element in infoDict:
                #print("inlist", element)
                if infoDict[element] == "red":
                    red += 1
                elif infoDict[element] == "blue":
                    blue += 1
                else:
                    green += 1
            else:
                green += 1
        if red > blue and red > green:
            coloredList.append([l,"red"])
        elif blue > red and blue > green:
            coloredList.append([l,"blue"])
        else:
            coloredList.append([l,"green"])
    for f in coloredList:
        #print (f)
        common = {}
        for g in range(0,len(f)):
            #print(f[g])
            if f[g] == "blue":
                a = sorted(f[0])
                smallest = a[0]
                result.append(smallest)
            if f[g] == "red":
                a = sorted(f[0])
                biggest = a[len(a) - 1]
                result.append(biggest)
            if f[g] == "green":
                #print("f0 is", f[0])
                for l in f[0]:
                    common[l] = 0
                for i in f[0]:
                    common[i] += 1
                list_common = list(common.items())
                x = sorted(list_common)
                most_common = x[-1][0]
                for h in range(0,len(x)):
                    #print("h",h)
                    if x[h][1] == x[-1][1]:
                        most_common = x[h][0]
                        break
                    if x[0][1] == None:
                        most_common = None
                result.append(most_common)
                #print("greatest", most_common)
                #print("list common", x)
                #print("common is", )
                
    return result
#2b. The spam ones are more about spam like messages. For example, they would want you to contact certain numbers compared to nonspam that is more like everyday conversation(even though the words are poorly spelled).
#I learned that that it is pretty easy to indentify between spam and normal messages.

def q2(filename, minWordLengthToConsider = 1):
    # read all of the data from the input file
    messagelist = getWordList(filename)
    lineCounter = 0
    spamCounter = 0
    hamCounter = 0
    wordCounterSpam = 0
    wordCounterHam = 0
    uniqueSpam = {}
    uniqueHam = {}
    totalDiffHam = 0
    totalDiffSpam = 0
    #remove punct
    wordlist = []
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for index in messagelist:
        lineCounter += 1
        #print(index) // index are the words
        for elemn in index:
            #print(elemn)// elemn are the characters
            if elemn in punc:
                index = index.replace(elemn, "")
        #print(index)
        #conver words to lowercase
        index = index.lower()
        #print(index) #after lower
        wordlist.append(index.split()) #if this works, don't touch it


    for word in range(0,len(wordlist)):
        if wordlist[word][0] == 'spam':
            spamCounter += 1
            wordCounterSpam += len(wordlist[word]) -1 # does the total word include spam/ham?
            # add to dictionary
            for far in range (1,len(wordlist[word])):
                uniqueSpam[wordlist[word][far]] = 0
            for car in range (1, len(wordlist[word])):
                uniqueSpam[wordlist[word][car]] += 1
        if wordlist[word][0] == 'ham':
            hamCounter += 1
            wordCounterHam += len(wordlist[word]) -1
            for lar in range(1, len(wordlist[word])):
                uniqueHam[wordlist[word][lar]] = 0
            for mar in range(1, len(wordlist[word])):
                uniqueHam[wordlist[word][mar]] += 1
    totalDiffHam = len(uniqueHam)
    totalDiffSpam = len(uniqueSpam)
    #sort dictionary
    list_uniqueSpam = list(uniqueSpam.items())
    x = sorted(list_uniqueSpam, key = lambda item: item[1], reverse = True)
    #print(x)
    list_uniqueHam = list(uniqueHam.items())
    y = sorted(list_uniqueHam, key = lambda item: item[1], reverse = True)
    #print(y)
    # delete most common that are less than minWordLengthToConsider
    h = 0
    otherX = []
    while h < len(x):
        if len(x[h][0]) > minWordLengthToConsider:
           otherX.append(x[h])
        h += 1
    #print(otherX)
    i = 0
    otherY = []
    while i < len(y):
        if len(y[h][0]) > minWordLengthToConsider:
            otherY.append(y[i])
        i += 1
    tenHam = []
    tenSpam = []
    #otherx is spam
    #othery is ham
    for air in range(0, 9):
        tenHam.append(otherY[air][0])
        tenSpam.append(otherX[air][0])
    tenHamFrequency = []
    tenSpamFrequency = []
    print(tenHam)
    for water in range(0,9):
        tenHamFrequency.append(otherY[water][1] /hamCounter)
        tenSpamFrequency.append(otherX[water][1] / spamCounter)
    print ("number of ham {}, number of spam {} ".format(hamCounter, spamCounter))
    print ("total number of words in ham {}, total number of words in number of spam {} ".format(wordCounterHam, wordCounterSpam))
    print ("total number of unique words in ham {}, total number of unique words in number of spam {} ".format(totalDiffHam, totalDiffSpam))
    for fire in range(0,10):
        print ("'{}' appeared {} times in ham, out of {} total words in all the ham messages, the frequency would be {}".format(otherY[fire][0], otherY[fire][1], wordCounterHam, tenHamFrequency[fire]))
        
    return

def getWordList(filename):
    result = []
    fileStream = open(filename, 'r')
    for line in fileStream:
        word = line.strip()
        result.append(word)
    return result
