def function(number):
    strnumber = str(number)
    tedad = len(strnumber)
    armstrong=sum(int(digit)** tedad for digit in strnumber)
    if armstrong==number:
        return armstrong
        
x = int(input(" "))
if function(x):
    print(f"{x} is Armstrong")
else:
    print(f"{x} is not Armstrong")
