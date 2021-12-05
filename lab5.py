#given the number of stuentsin each class, print the smallest possible number of desks
#when a desk is used for a two students.
a=int(input("enter number of student in class A"))
b=int(input("enter number of student In class B"))
c=int(input("enter number of student in class C"))
desksInA=a//2
desksInA=b//2
desksInA=c//2
if a % 2 !=0:
    desksInA+=1
if b % 2 !=0:
    desksInB+=1
if c % 2 !=0:
    desksInC+=1
total=desksInA+desksInB+desksInC
print(f"The total number of desks required is {total}")