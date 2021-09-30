def checkStackSequence(pushseq, popseq):
    stack = []
    j = 0
    for i in range(len(pushseq)):
        stack.append(pushseq[i])
        list.append("push "+str(i+1))
        while stack != [] and stack[-1] == popseq[j]:
            stack.pop()
            list.append("pop")
            j = j+1
            
    if stack == []:
        return True
    else:
        return False

list = []

pushseq = [1,2,3,4,5] 
popseq = [4,5,3,2,1]

if checkStackSequence(pushseq, popseq):
    print("yes")
    print(list)
else:
    print("no")
