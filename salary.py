sla = int(input("Enter the gross salary:"))
all = sla * (1/10)
ded = sla * (3/100)
net = sla + all - ded
print("The net amount is: ",net)
print("The allowance amount is: ",all)