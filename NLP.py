

with open("test.txt",'r+') as f:
    lines = f.readlines()
    for line in lines:
        line= line.strip()
        line = "<S> "+line+" <\S>"+"\n"
        print(line)
