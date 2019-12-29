def num_even_digits(n):
    n=list(str(n))
    count=0
    for i in n:
        if int(i)%2 ==0:
           count+=1
    return count
print(num_even_digits(864000123))
