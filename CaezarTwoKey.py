cryptMode = 'E'
alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
startMessage = 'dima'.upper()

numberKey = 3
stringKey = 'ALAHAKBAR'

def remove(stringKey):
    alpha = list()
    for l in stringKey:
        if l in alphaList:
            if l not in alpha:
                alpha.append(l)
    return alpha

def createAlphabet(stringKey, key):
    alpha = remove(stringKey)
    index = key
    for i in alpha:
        alphaList[] = alphaList.index(i)
        alphaList[index] = i
        index += 1





def encryptDecrypt(mode, message, key, stringKey,  final = ""):
    alpha = createAlphabet(key, stringKey)
    print(alpha)
    for symbol in message:
        if mode == 'E':
            final += alpha[(alpha.index(symbol) + key)%26]
        else: 
            final += alpha[(alpha.index(symbol) - key)%26]
    return final

message = encryptDecrypt(cryptMode, startMessage, stringKey,  numberKey)
print("Final message:", message)