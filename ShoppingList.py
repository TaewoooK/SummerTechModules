shopList = []
bol2 = True

print("Welcome to the your shopping list!")

while bol2 == True:
    choice = input("Would you like to remove or add an item?: ")
    if choice == "add":
        item = input("Type in an item: ")
        shopList.append(item)
    elif choice == "remove":
        if len(shopList) >= 1:
            remove = input("Which item would you like to remove?: ")
            for i in range(0, len(shopList)):
                if shopList[i] == remove:
                    shopList.remove(remove)
                    break
        else:
            print("You have 0 items")
    else:
        print("Invalid Input")

    print("Your Shopping List:")
    for i in range(0, len(shopList)):
        print(i+1, end="") 
        print(".", shopList[i])

    finish = input("Would you like to continue? \"yes\" or \"no\": ")
    if finish == "no":
        bol2 = False
        print("Have a nice day!")

    
