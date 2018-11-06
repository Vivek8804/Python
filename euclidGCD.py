n1 = int(input("Enter a number "))
n2 = int(input("Enter another number "))


def ComputeGCD(a, b):
    if b == 0:
        return a
    else:
        return ComputeGCD(b, a % b)


print("The GCD of two numbers is", ComputeGCD(n1, n2))
