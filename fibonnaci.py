def fibonnaci_seq(n):
    if n==1 or n==0:
        return n
    else:
        return fibonnaci_seq(n-2)+fibonnaci_seq(n-1)

number= int(input("Enter your number: "))
if number<0:
    print("Not valid.")
i= 0
for i in range(0, number):
    print(fibonnaci_seq(i))