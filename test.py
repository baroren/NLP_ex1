    for line in lines :
        splitLine=line.split()
        for i , word in enumerate(splitLine):
            for w in range(window):
                if i+1+w< len(splitLine):
                    wordList.append([word]+[splitLine[(i+1+w)]])
                if i-w-1>=0:
                    wordList.append([word]+[splitLine[(i-w-1)]])
