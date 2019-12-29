# Lucky draw programme
import random
oldlist = []
newlist=[]
print('Enter the entries one by one. Enter nothing when finished.')

while True:
    entry=input()
    if entry=='':
        break
    oldlist += [entry]


print('Here is the list after lucky draw.')

for i in range(len(oldlist)):
    value = random.randint(0,len(oldlist)-1)
    newlist += [oldlist[value]]
    del(oldlist[value])

for i in range(len(newlist)):
    print('Index ' + str(i) +' item is ' + newlist[i])
