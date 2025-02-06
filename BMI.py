# A simple way to calculate your BMI
height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))



final_height = height ** 2
results = weight / final_height
BMI = results
if BMI > 18.5:
    print("Above average")
elif BMI == 18.5:
    print("Average")
else:
    print("Normal")

print(f"Your BMI is {results}")

