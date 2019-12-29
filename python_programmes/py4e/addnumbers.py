'''
import re

#load file and parse
filename = input('Enter file name: ')
handle = open(filename).read()
nums = re.findall('\d+',handle)

#Calculate Total
runningtot = 0
for num in nums:
    runningtot += int(num)
print(runningtot)
'''

import re
print( sum( [ int(n) for n in re.findall('[0-9]+',open(input("Enter file name: ")).read()) ] ) )
