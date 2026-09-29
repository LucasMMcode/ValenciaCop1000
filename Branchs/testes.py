income = float(input("Income: "))
maritalStatus = input("Marital status: ")
if maritalStatus == "s" :                     # Condition 1
   if income <= 30000 :                       # Condition 2
      tax = 0.10 * income
      print("Branch 1")
   else :
      tax = 3000 + 0.25 * (income - 30000)
      print("Branch 2")
else :
   if income <= 60000 :                       # Condition 3
      tax = 0.10 * income
      print("Branch 3")
   else :
      tax = 6000 + 0.25 * (income - 60000)
      print("Branch 4")