n=int(input("Enter a no. to find it's factor: "))
print("Factor of",n,"is:",end=(' '))
for i in range(2,n):
    if(n%i==0):
        print(i,end=(','))