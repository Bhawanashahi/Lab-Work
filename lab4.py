#take input for number of apple and people and divide accordingly
apples= int(input("enter the number of apple"))
people=int(input("enter the number of people"))
divide= apples // people
basket= apples % people
print(f"each peerson gets {divided} apples and {basket} apples are remaining in the basket")