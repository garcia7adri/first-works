shoes_available={41:2,38:2,39:4,40:3}
while (True):
    choice=int(input("What size are you looking for: "))
    if choice < 0:
        break
    if shoes_available[choice]>0:
        shoes_available[choice]-=1
        print("Your shoes were bought")
    else:
        print("Shoes are not longer available.")
    print ("New stock: ",shoes_available)

