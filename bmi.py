weight=float(input("enter your weight"))
height=float(input("enter your height in meters"))
bmi=weight/(height*height)
if bmi>=15 and bmi<21:
    print("you are underweight")
elif bmi>=21 and bmi<27.5:
    print("you have a normal weight")
elif bmi>=27.5 and bmi < 33:
    print("you are overweight")
else:
    print("you are obesed")
print(f"your Body Mass Index is {bmi}")
