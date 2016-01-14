
def main():
    x = (17**39)**11
    #print x
    strx = str(x)
    #print strx
    #print strx[32:]

    answer = ""
    for i in xrange(len(strx)):
        if i != 0 and i % 33 == 0:
            answer += strx[i - 1]
    print answer
    
if __name__ == "__main__":
    main()
