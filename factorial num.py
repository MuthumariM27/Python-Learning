multi=int(input("Enter your num for factorial: "))
fact=1
i=1
while i < multi:
    fact *=i
    i+=1
print(f"Factorial of {multi} is {fact}")
