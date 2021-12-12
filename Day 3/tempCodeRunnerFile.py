#WAP which accepts marks oof four subjects and display total marks.
#percentage and grade
m1 = int(input("enter the marks of first subject"))
m2 = int(input("enter the marks of second subject"))
m3 = int(input("enter the marks of third subject"))
m4 = int(input("enter the marks of fourth subject"))
marks= (m1+m2+m3+m4//400*100)
print(marks)
if marks > 85 and marks <=100:
    print("congrats ! you scored grade A")
elif marks > 60 and marks <85:
    print("congrats ! you scored grade B+")
elif marks > 40 and marks <=60:
    print("congrats ! you scored grade B")
elif marks > 30 and marks <= 40:
    print("congrats ! you scored grade C")
else:
    print("sorry you are fail")