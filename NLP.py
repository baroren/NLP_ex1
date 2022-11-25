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
            line =re.sub("[\d]",'<!DIGIT!>',line)
            line = re.sub(r"\w*[^\x00-\x7F]+\w*", "<UNK>", line)
            line = "<S> "+line+r'<\S>'+'\n'
        #  print(line)
            lines.append(line)
    
tokens()
for line in lines :
    print (line)
