def max_of_three(x,y,z):
    if (no1 > no2) and (no1 > no3) :
        print(f"The maximum value is : " ,no1)
    elif (no2 > no1) and (no2 > no3) :
        print(f"The maximum value is :", no2)
    else :
        print(no3) 
no1=int(input("Enter no1 value : "))
no2=int(input("Enter no2 value : "))
no3=int(input("Enter no3 value : "))
max_of_three(no1,no2,no3)
