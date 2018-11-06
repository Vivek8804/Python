string = input("Enter any string ")
print("Entered string is", string)


def reverse(string):
    rev = ""
    for i in string:
        rev = i + rev
    print("Reversed String is", rev)


reverse(string)

