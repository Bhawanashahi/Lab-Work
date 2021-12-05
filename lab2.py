# find BMI of a person where take mass and height as input as input from the user
# BMI = mass in kg / (height in m)2
M = int(input("enter the mass of person in kg:"))
H = int (input("enter the height of the person in meter:"))
BMI = (M / (H * H))
print(f"the BMI value of a person is {BMI}:")