def avval(n):
    if n < 2:
        return False
    for i in range(2, int(n//2) + 1):
        if n % i == 0:
            return False
    return True
def g(numbers):
    counter = 0
    s = 0
    for num in numbers:
        if avval(num):
            s += num
        else:
            counter += 1
    return counter, s
x = int(input("enter x: "))
a = []
for i in range(x):
    a.append(int(input("  ")))
counter, s = g(a)
print("Number of non-prime numbers: ", counter)
print("Sum of prime numbers: ", s)
