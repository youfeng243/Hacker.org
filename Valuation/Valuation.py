#coding=utf-8
#calstr = "93752xxx746x27x1754xx90x93xxxxx238x44x75xx08750912738x8461x8759383xx328x4x4935903x6x5550360535004x0xx945958961296x267x8842xxx5x6xx61x4x48482x80xxx83316843x7x4x83x9521731xxx25x51xx457x6x5x9698222x771237745034x5133592x27xx8x87xx35221x36x0x50x23x7x63x998418xx"

def main():
    calstr = "93752xxx746x27x1754xx90x93xxxxx238x44x75xx08750912738x8461x8759383xx328x4x4935903x6x5550360535004x0xx945958961296x267x8842xxx5x6xx61x4x48482x80xxx83316843x7x4x83x9521731xxx25x51xx457x6x5x9698222x771237745034x5133592x27xx8x87xx35221x36x0x50x23x7x63x998418xx"
    i = 0
    #calstr = calstr[0:i]+calstr[i + 1: ]
    #print calstr
    mysum = 0
    while True:
        if i >= len(calstr):
            break
        if calstr[i] >= '0' and calstr[i] <= '9':
            mysum += int(calstr[i])
            i += 1
        elif calstr[i] == 'x':
            calstr = calstr[0:i] + calstr[i+1:]
            i -= 2
            if i < 0:
                i = 0
        
                
    print mysum

if __name__ == "__main__":
    main()
