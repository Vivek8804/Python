num = int(input("Enter number to check "))
temp = num
result = 0
n = len(str(num))
while temp > 0:
    digit = temp % 10
    result += digit ** n
    temp = temp//10

if result == num:
    print("{} is an Armstrong number".format(num))
else:
    print("{} is not an Armstrong number dude".format(num))
