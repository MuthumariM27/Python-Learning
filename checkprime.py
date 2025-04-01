def check_prime(num):
    if num == 0 and num == 1:
        print(f"{num} Its not a prime no")
        return
    elif num >=2:
        for i in range(2,num):
            if(num % i) == 0:
                print(f"{num} Its not a prime no")
                return
        else:
            print (f"{num} Its a prime no")
prime = int(input("Enter your no :"))
check_prime(prime)
