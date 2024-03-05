numArray = [0,1]
userNum = int(input('Digite o número para ser calculado: '))

def GetNum():
    global isFound
    index = 0
    for i in numArray:
        if i == userNum:
            isFound = True
            return
        elif index >= userNum and i != userNum:
            isFound = False
            return
        else:
            index += 1
            isFound = False
            numArray.append(numArray[index - 1] + numArray[index])

GetNum() 
           
if isFound:
    print('Número pertence a sequência de Fibonacci')
else:
    print('Número não pertence a sequência de Fibonacci')
