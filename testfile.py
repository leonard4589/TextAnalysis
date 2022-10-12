from Class import*

tFile = analysisProject("Trumpin.txt")
bFile = analysisProject("Bidinin.txt")
oFile = analysisProject("Obamain.txt")
rFile = analysisProject("Reaganin.txt")

'''Trump's inauguration speech'''
# print("Total number of lines in Trump's speech: ", tFile.filelen())
# print("Total number of stanzas in Trump's speech: ", tFile.stanzact())
# print("Number of words per line in Trump's speech: ", tFile.wordct())
# print("Total number of characters in Trump's speech: ", tFile.letterct())
# print("Average amount of characters per word in Trump's speech: ", tFile.averagew())
# print("Total number of words in Trump's speech: ", tFile.total())
# print("Average amount of words per line in Trump's speech: ", tFile.average())
# print("The following sentences are seperated and hightlighted where they start in Trump's speech: ", tFile.sentencebreak())

'''Bidin's inauguration speech'''
# print("Total number of lines in Bidin's speech: ", bFile.filelen())
# print("Total number of stanzas in Bidin's speech: ", bFile.stanzact())
# print("Number of words per line in Bidin's speech: ", bFile.wordct())
# print("Total number of characters in Bidin's speech: ", bFile.letterct())
# print("Average amount of characters per word in Bidin's speech: ", bFile.averagew())
# print("Total number of words in Bidin's speech: ", bFile.total())
# print("Average amount of words per line in Bidin's speech: ", bFile.average())
# print("The following sentences are seperated and hightlighted where they start in Bidin's speech: ", bFile.sentencebreak())

'''Obama's inauguration speech'''
# print("Total number of lines in Obama's speech: ", oFile.filelen())
# print("Total number of stanzas in Obama's speech: ", oFile.stanzact())
# print("Number of words per line in Obama's speech: ", oFile.wordct())
# print("Total number of characters in Obama's speech: ", oFile.letterct())
# print("Average amount of characters per word in Obama's speech: ", oFile.averagew())
# print("Total number of words in Obama's speech: ", oFile.total())
# print("Average amount of words per line in Obama's speech: ", oFile.average())
# print("The following sentences are seperated and hightlighted where they start in Obama's speech: ", oFile.sentencebreak())

'''Reagan's inauguration speech'''
# print("Total number of lines in Reagan's speech: ", rFile.filelen())
# print("Total number of stanzas in Reagan's speech: ", rFile.stanzact())
# print("Number of words per line in Reagan's speech: ", rFile.wordct())
# print("Total number of characters in Reagan's speech: ", rFile.letterct())
# print("Average amount of characters per word in Reagan's speech: ", rFile.averagew())
# print("Total number of words in Reagan's speech: ", rFile.total())
# print("Average amount of words per line in Reagan's speech: ", rFile.average())
# print("The following sentences are seperated and hightlighted where they start in Reagan's speech: ", rFile.sentencebreak())

'''Comparison between each speech'''
print("Average amount of characters per word in Trump's speech: ", tFile.averagew())
print("Average amount of characters per word in Bidin's speech: ", bFile.averagew())
print("Average amount of characters per word in Obama's speech: ", oFile.averagew())
print("Average amount of characters per word in Reagan's speech: ", rFile.averagew())