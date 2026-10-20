tacos = 0
burritos = 0
nachos = 0
drinks = 0
i = 0
tacoPrice = 2.50
burritoPrice = 2.25
nachosPrice = 2.75
drinkPrice = 2
print("Welcome to Taco Palace!")
print("Please View the menu")
print("Welcome to Taco Palace!")
def menu():
    print("\nTaco Place Menu")
    print("1.Taco       $",tacoPrice)
    print("2.Burrito    $",burritoPrice)
    print("3.Nachos     $",nachosPrice)
    print("4.Soft Drink $",drinkPrice)
    print("5.Quit\n")
    return i
def yourOrder():
    print("You ordered")
    if tacos > 1:
        print(tacos,"Tacos        $",tacos*tacoPrice)
    elif tacos == 1:
        print("1 Taco         $",tacos)
    if burritos > 1:
        print(burritos,"Burritos     $",burritos*burritoPrice)
    elif burritos == 1:
        print("1 Burrito      $",burritos)
    if nachos > 0:
        print(nachos,"Nachos       $",nachos*nachosPrice)
    if drinks > 1:
        print(drinks,"Drinks       $",drinks*drinkPrice)
    elif drinks == 1:
        print("1 Drink        $",drinks)
    total = tacos*tacoPrice+burritos*burritoPrice+nachos*nachosPrice+drinks*drinkPrice
    return total
while (i < 5):
    menu()
    i=int(input("Choose:"))
    if i==1:
        tacos+=1
        choice="\nYou have selected Taco"
        added = tacoPrice
    elif i==2:
        burritos+=1
        choice="\nYou have selected Burrito"
        added = burritoPrice
    elif i==3:
        nachos+=1
        choice="\nYou have selected Nachos"
        added = nachosPrice
    elif i==4:
        drinks+=1
        choice="\nYou have selected Soft Drink"
        added = drinkPrice
    else:
        choice=""
        added=0
    print(choice)
    print("added ", added)
total=yourOrder()

print("Your total is: $",total)