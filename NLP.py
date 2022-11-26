from collections import defaultdict
import re
import pandas as pd
import numpy as np
#sub panctuiation -re.sub("[^\w\s(<S><\\S>]","",line)
#lower case the word -re.sub("[A-Z+]","[a-z]",line)
#line = re.sub(r"\w*[^\x00-\x7F]+\w*", "<UNK>", line)  # replace unknown names and phrases

#consts :
SAMPLESIZE=30

lines=[]

def tokens(line):
        line= line.strip()
        line =re.sub("[^\w\s ]",' ',line)
        for f in re.findall("([A-Z]+)", line):
            line = line.replace(f, f.lower())
        line =re.sub("\d+",' <!DIGIT!> ',line)
        line = re.sub(r"\w*[^\x00-\x7F]+\w*", "<UNK>", line)
        line = "<S> "+line+r' <\S>'+'\n'
        return line
 
def simlex(file):
    f=open (file,'r+')
    sim=set([])
    exit =False
    for text in f.readlines():
        text.split()
        text =re.sub("\d+",'',text)
        text =re.sub("[^\w\s ]",' ',text)
        text=text.split()
       
        for t in text:
            sim.add(t)
            if len((sim))>=SAMPLESIZE:
                exit =True
                break
        if exit :
            return sim
        
    return sim

simlexList=simlex("EN-SIMLEX-999.txt")
word=simlex("eng_wikipedia_2016_1M-words.txt")

print(len(word))
print(len(simlexList))
  
def co_occurrence( window_size):
    d = defaultdict(int)
    f= open("test.txt",'r+')  
    vocab = set()
    for text in f.readlines():
        text =tokens(text)
        text=text.split()
        for i in range(len(text)):
            token = text[i]
           # print(token)
            vocab.add(token)  # add to vocab
            next_token = text[i+1 : i+1+window_size]
           # print(next_token)
            for t in next_token:
                key = tuple( sorted([t, token]) )
                d[key] += 1

    # formulate the dictionary into dataframe
    vocab = sorted(vocab) # sort vocab
    df = pd.DataFrame(data=np.zeros((len(list(simlexList)), len(list(word))), dtype=np.int16),
                      index=list(simlexList),
                      columns=list(word))
    for key, value in d.items():
        if key[0] in df.index and key[1] in df.columns:
            df.loc[key[0], key[1]] = value
        if key[1] in df.index and key[0] in df.columns:
            df.at[key[1], key[0]] = value
    return df

def pmi(df, positive=True):
    col_totals = df.sum(axis=0)
    total = col_totals.sum()
    row_totals = df.sum(axis=1)
  #  print(col_totals)
    expected = np.outer(row_totals, col_totals) / total
    df = df / expected
    # Silence distracting warnings about log(0):
    with np.errstate(divide='ignore'):
        df = np.log(df)
    df[np.isinf(df)] = 0.0  # log(0) = 0
    if positive:
        df[df < 0] = 0.0
    return df

    
df2= co_occurrence(2)
print (df2)
##df5= co_occurrence(5)
#print (df5)

#ppmi =pmi(df2)
#print (ppmi)











""""
wordList2=makePairs(2)    
 
print(len(wordList2))
    
mat2 =createMat(2)

    
updateMat(mat2,wordList2)
for m in mat2:
    print(m)
wordList5=makePairs(5)  

print(len(wordList5))
mat5 =createMat(5)

    
updateMat(mat5,wordList5)
for m in mat5:
    print(m)

def createMat(window):
    mat =[]
    rowSet =set([" "])
    for line in lines :
        splitLine=line.split()
        for i , word in enumerate(splitLine):
            for w in range(window):
                rowSet.add(word)

    rowSet=sorted(set(rowSet))


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
    wordList=[]
    for line in lines :
        splitLine=line.split()
        for i , word in enumerate(splitLine):
            for w in range(window):
                if i+1+w< len(splitLine):
                    wordList.append([word]+[splitLine[(i+1+w)]])
                if i-w-1>=0:
                    wordList.append([word]+[splitLine[(i-w-1)]])
    return wordList
def updateMat(mat,wordList):
    for w in wordList:
       # print(mat[0].index(w[0]) ,mat[0].index(w[1]))
        i,j=mat[0].index(w[0]) ,mat[0].index(w[1])
        if isinstance(mat[i][j],int):
             mat[i][j]+=1
             mat[j][i]+=1
    """