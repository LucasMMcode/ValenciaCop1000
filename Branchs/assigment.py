Hours=int(input("Enter the KW hours used:"))
if(Hours<=1000):
    owed=Hours*7.633/100
else:
    owed=1000*7.633/100
    owed=owed+((Hours-1000)*9.259/100)

print("Amount owed is", owed)