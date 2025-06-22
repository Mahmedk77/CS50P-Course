paid=0
amountDue=50
while amountDue>0:
    paid=int(input("Coin Input: "))
    amountDue= amountDue-paid
    if paid in [25,10,5] and amountDue>0:
        print("Amount Due:",amountDue)
owendAmount=abs(amountDue)
print("Change Owend:",owendAmount)