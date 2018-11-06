n = int(input("Enter any number "))
rev = 0
temp = n

while temp > 0:
    slice = temp%10
    rev = rev*10 + slice
    temp = temp//10

if n == rev:
    print("We have got a palindrome")
else:
    print("Naah, not a palindrome")