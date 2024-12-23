import sys
names=["Ronak", "Neev", "Adhiraj","Kavyen", "Vihaan" ]
while True:
    ask = int(input("1.See all names in the list\n2.Add a name to the list\n3.Remove a name from the list\n4.Change the name in the list\n5.Exit"))
    if ask == 1:
        print(names)
    elif ask == 2:
        add1=input("What name do you want to add to the list?")
        names.append(add1)
        print(names)
    elif ask == 3:
        remove1=input("Which name would you like to remove?")
        names.remove(remove1)
        print(names)
    elif ask == 4:
        replace1=input("Which name would you like to replace?")
        replace2=input("What name would you like to replace " + replace1 + " with?")
        count = 0
        for i in names:
            if i == replace1:
                names[count]=replace2
                print(names)
            else:
                count=count+1
    elif ask == 5:
        sys.exit()