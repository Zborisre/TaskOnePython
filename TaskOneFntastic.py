word = str(input("Введите текст: ")).lower()
exitword = str()
wored = int()

for i in range(len(word)):
    wored = 0
    for l in range(len(word)):
        if(word[i] == word[l]):
            wored += 1
    if(wored > 1):
        exitword += (')')
    else:
        exitword += ('(')
print(exitword)