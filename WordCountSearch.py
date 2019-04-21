data = []
with open('output.txt', 'r', encoding='utf-8')as f:
    for line in f:
        data.append(line.strip())


wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
for word in wc:
    print(word, wc[word])

while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    if word in wc:
        print(word, 'appeared', wc[word], 'times')
    else:
        print('this word has 0 count')