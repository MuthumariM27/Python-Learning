calculate_grade=int(input("Enter your score here: "))
match calculate_grade:
    case calculate_grade if (90<=calculate_grade<=100):
        print(f"Your Grade is : 'A' It's Excellent Grade 😁")
    case calculate_grade if (80<=calculate_grade<=89):
        print(f"Your Grade is : 'B'  Very good keep doing 😃")
    case calculate_grade if (70<=calculate_grade<=79):
        print(f"Your Grade is : 'C' Good grade 😊")
    case calculate_grade if (60<=calculate_grade<=69):
        print(f"Your Grade is : 'D' Average level 😢")
    case calculate_grade if (0<=calculate_grade<=60):
        print(f"Your Grade is : 'F' Low grade 😢")
    case _ :
        print("Enter Numeric score from 1 to 100!! ")
    




