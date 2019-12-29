spam = ['apples', 'bananas', 'tofu', 'cats']

output = ''

for i in range(len(spam)):
    if i == len(spam)-1:
        output += 'and ' + spam[i]
    else:
        output += spam[i] + ', '

print(output)
    
