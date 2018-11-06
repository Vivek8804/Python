input = input("Enter any string ")
rev = input[::-1]
print("Reverse of input is", rev)

if input == rev:
    print("{} is a palindrome string".format(input))
else:
    print("Sorry {} is not a palindrome string".format(input))