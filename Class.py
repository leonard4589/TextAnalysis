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
        for i in range(len(self.lines)):
            lt = lines[i].strip().split(" ")
            return len(lt)

    '''function counts the amount of characters in each line'''
    def letterct(self):
        total = 0
        for line in self.lines:
            line = line.replace(",", "")
            line = line.replace(" ", "")
            line = line.replace(".", "")
            line = line.replace(";", "")
            line = line.replace(":", "")
            w = len(line)
            total = total + w
            return total
            # idk why this is only doing one line and not all of them
           
    def averagew(self):
        a = self.letterct / len(self.lines) #unsupported operand type
        return a

    '''function finds total word count'''
    # total = 0  #needs initial total
    def total(self):
        total = 0
        for i in range(len(self.lines)):
            lt = self.lines[i].strip().split(" ")
            n = len(lt)
            total = total + n
            return total

    '''function finds the average words per line'''
    def average(self):
        for i in range(len(self.lines)):
            lt = self.lines[i].strip().split(" ") #why do I need this again?
            average = self.total/len(self.lines) #says that this is an unsupported operant type
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