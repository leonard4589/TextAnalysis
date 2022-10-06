class analysisProject:
    '''Class for a text analysis project. Includes exsisting methods and new functions required to answer question.'''

    def __init__(self, filename):
        self.fname = filename
        with open(self.fname) as f:
            self.lines = f.readlines()

'''function counts the number of lines'''
    def filelen(self):
       n = len(self.lines)
       return n

'''function counts words per line'''
    def wordct(self):
        for i in range(len(lines)):
            lt = lines[i].strip().split(" ")
            return len(lt)

'''function finds total word count'''
    total = 0 '''needs initial total'''
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
