def EvenOddSum():
    a=[]
    n=int(input("Enter n value: "))
    for i in range(n):
        num=int(input("Number: "))
        a.append(num)
    even=[]
    odd=[]
    for j in a:
        if(j%2==0):
            even.append(j)
        else:
            odd.append(j)
    print("Even Numbers: ",even)
    print("Odd Numbers: ",odd)
    print("Sum of even: ",sum(even))
    print("Sum of odd: ",sum(odd))
EvenOddSum()
