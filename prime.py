n = int(input("Enter a number "))
'''factors = 0
for num in range(1, n + 1):
    if n % num == 0:
        factors += 1
if factors == 2:
    print("{} is prime".format(n))
else:
    print("{} is not a prime".format(n))'''

for i in range(2, n):
    if n % i == 0:
        print("Hey {} is not prime".format(n))
        break
else:
    print("Hey {} is a Prime".format(n))
