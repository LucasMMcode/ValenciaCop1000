startNum=0
nextNum=1
print(startNum)
while (nextNum<25):
    newNum = startNum + nextNum
    startNum=nextNum
    nextNum=newNum
    print(startNum)