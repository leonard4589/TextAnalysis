class analysisProject:
    '''Class for a text analysis project. Includes exsisting methods and new functions required to answer question.'''

    def __init__(self, filename):
        self.fname = filename
        with open(self.fname) as f:
            self.lines = f.readlines()

    '''function counts the number of lines'''
    def filelen(self):
        n = 0
        for line in self.lines:
            line = line.strip()
            print(len(line))
            if len(line) != 0:
                n = n + 1
        return n

    '''function counts the amount of stanzas'''
    def stanzact(self):
        n = 0
        for line in self.lines:
            line = line.strip()
            if line == '':
                n = n + 1
            c = n + 1
        return c

    '''function counts words per line'''
    def wordct(self):
        for i in range(len(lines)):
            lt = lines[i].strip().split(" ")
            return len(lt)

    '''function counts the amount of letters in each word'''
    def letterct(self):
        w = 0
        for line in self.lines:
            for word in line:
                word = word.strip()
                print (word, len(word))
                if len(word) != 0:
                    w = w + 1
        return w
           
    '''function finds total word count'''
    total = 0  #needs initial total
    def total(self):
        for i in range(len(lines)):
            lt = lines[i].strip().split(" ")
            n = len(lt)
            total = total + n
            return total

    '''function finds the average words per line'''
    def average(self):
        for i in range(len(lines)):
            lt = lines[i].strip().split(" ")
            average = total/len(self.lines)
            return average 

    '''function seperates and highlights where each sentence starts'''
    def sentencebreak(self):
        with open(self.fname) as f:
            fullText = f.read()
        fullText = fullText.replace('\n', ' ')
        self.sentences = fullText.split(".")
        for s in self.sentences:
            print("*:", s)

    '''function will count how many times a specific word is said within a document'''
    def countWord(self, word):
        n = 0
        for s in self.sentences:
            if word in s:
                n += 1
            return n