
def main():
    text = ""
    for line in open(r"./lorem.txt"):
        line = line.strip()
        line = line.strip('\n')
        text += line

    text = text.replace(".", " ")
    text = text.replace(";", " ")
    text = text.replace(",", " ")
    textlist = text.split(" ")
    #print textlist

    dic = {}
    for line in textlist:
        if line in dic:
            dic[line] += 1
        else:
            dic[line] = 1
    for line in dic:
        if dic[line] <= 1:
            print line
    
    #print "over"

    
    
if __name__ == "__main__":
    main()
