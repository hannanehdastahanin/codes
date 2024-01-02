n1=input(" ")
y1=int(input(" "))
n2=input(" ")
y2=int(input(" "))
print("Hello  " + n1 +". You are "+str(1402-y1) +" years old.")
print("Hello  " + n2 +". You are "+str(1402-y2) +" years old.")
if (y1>y2):
    print(n2+ " is " +str(y1-y2)+" years older than "+n1+" . ")
else:
    print(n1+ " is " +str(y2-y1)+" years older than "+n2+".")
if (y1==y2):
    print(n1+" and "+n2+" are the same age.")
    

