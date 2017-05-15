__author__ = 'elizajasin'

def tagging (data):
    tags = []
    words = []
    # learning
    for imel in range(len(data)):
        abstract = str(data[imel]).find('abstract')
        abstract += 9
        s = ""
        r = ""
        startT = True
        startW = True
        open = False
        close = False
        word = []
        tag = []
        for isi in range(abstract, len(data[imel]), 1):
            if open:
                s += data[imel][isi]
            if close and startW:
                if data[imel][isi] != '>' or data[imel][isi] != '<':
                    r += data[imel][isi]
            if data[imel][isi] == '<':
                if startW:
                    startT = True
                s += data[imel][isi]
                startW = True
                open = True
                close = False
            if data[imel][isi] == '>':
                if startW == False:
                    startT = False
                close = True
                open = False
            if data[imel][isi] == '/':
                startW = False
                word.append(r)
                r = ""
            if startT == False:
                startT = True
                tag.append(s)
                s = ""
        print(word[1],tag[1])
        tags.append(s)
        words.append(r)
    return tags