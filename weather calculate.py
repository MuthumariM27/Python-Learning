weathtemp=float(input("Hai dude!!! What's the weather today:"))
if weathtemp <= 10:
    print(f"{weathtemp} °C is too cold!! Wear a warm coat and scarf!!")
elif weathtemp > 10 and weathtemp < 25:
    print(f"{weathtemp} °C is mild cold!! Wear A light jacket bro!!")
elif weathtemp >25:
    print(f"{weathtemp} °C is so hot!!! Wear T-shirt that would be perfect!!")
else:
    print(f"{weathtemp} It's a Correct weater bro!!")
