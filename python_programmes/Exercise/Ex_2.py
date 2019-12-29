sentence_ori = input("Please input a sentence: ")

split = sentence_ori.split()

split.reverse()

result = ''

for i in split:
    result = result + i + ' '

print(result)
