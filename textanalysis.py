with open('terence.txt') as f:
    lines = f.readlines()


# print ("Length: ", len(lines))
# print ((lines[0][-2]))

# lt = lines[0].strip().split(" ")
# print (lt)
# print(len(lt))

# number of words per line
for i in range(len(lines)):
    lt = lines[i].strip().split(" ")
    print (lt, len(lt))
# total number of words
total = 0
for i in range(len(lines)):
    lt = lines[i].strip().split(" ")
    n = len(lt)
    total = total + n
print (total)
# average number of words per line
for i in range(len(lines)):
    lt = lines[i].strip().split(" ")
    average = total/len(lines)
print (average)
