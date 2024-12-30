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
        count1 = 0
        for m in names:
            if m == remove1:
                names.pop(count1)
                print(names)
            else:
                count1=count1+1
    elif ask == 4:
        replace1=input("Which name would you like to replace?")
        replace2=input("What name would you like to replace " + replace1 + " with?")
        count2 = 0
        for i in names:
            if i == replace1:
                names[count2]=replace2
                print(names)
            else:
                count2=count2+1
    elif ask == 5:
        sys.exit()