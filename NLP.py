import re
#sub panctuiation -re.sub("[^\w\s(<S><\\S>]","",line)
#lower case the word -re.sub("[A-Z+]","[a-z]",line)
#line = re.sub(r"\w*[^\x00-\x7F]+\w*", "<UNK>", line)  # replace unknown names and phrases



lines=[]
def tokens():
    with open("test.txt",'r+') as f:   
        for line in f.readlines():
            line= line.strip()
            line =re.sub("[^\w\s ]",' ',line)
            for f in re.findall("([A-Z]+)", line):
                line = line.replace(f, f.lower())
            line =re.sub("[\d]",' <!DIGIT!> ',line)
            line = re.sub(r"\w*[^\x00-\x7F]+\w*", "<UNK>", line)
            line = "<S> "+line+r' <\S>'+'\n'
            lines.append(line)
    
tokens()
wordList=[]




def createMat(window):
    mat =[]
    rowSet =set([" "])
    for line in lines :
        splitLine=line.split()
        for i , word in enumerate(splitLine):
            for w in range(window):
                rowSet.add(word)

    rowSet=sorted(set(rowSet))

    wordList.append(rowSet)
    for r in rowSet:
        if r ==' ':
            continue
        row=[]
        row.append(r)
        for i in enumerate(rowSet):
            row.append(int(0)) 
        mat.append(row)
    mat.insert(0,rowSet)
    return mat


def makePairs(window):
    for line in lines :
        splitLine=line.split()
        for i , word in enumerate(splitLine):
            for w in range(window):
                if i+1+w< len(splitLine):
                    wordList.append([word]+[splitLine[(i+1+w)]])
                if i-w-1>=0:
                    wordList.append([word]+[splitLine[(i-w-1)]])
def updateMat():
    for w in wordList:
        print(mat[0].index(w[0]) ,mat[0].index(w[1]))
        i,j=mat[0].index(w[0]) ,mat[0].index(w[1])
        if isinstance(mat[i][j],int):
             mat[i][j]+=1
             mat[j][i]+=1
    

  


makePairs(2)    

print(wordList)

    
mat =createMat(2)
for m in mat:
    print(m)
    
updateMat()
for m in mat:
    print(m)