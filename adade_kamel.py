def kamel(num):
    d = [i for i in range(1, num) if num % i == 0]
    return sum(d) == num
def adadekamel(start, end):
    adadekamell = [num for num in range(start, end + 1) if kamel(num)]
    return adadekamell
x = int(input(" "))
start = int(input(" "))
end = int(input(" "))
if kamel(x):
    print("complete number")
else:
    print("not complete number.")
baze = adadekamel(start,end)
if baze:
    print(baze)
else:
    print("Not Found!")
