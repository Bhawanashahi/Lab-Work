#given a n-digit number, find the sum of its.
number = int(input("enter a number"))
sumofDigits= 0
for digit in str(number):
    sumofDigits += int(digit)
    print(sumofDigits)