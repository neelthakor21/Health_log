def log(cli_Name):
    print("Enter 1 for add Food and 2 for add Excersise : \n ==> ", end = "")
    c_choice = input()

    if c_choice == '1':
        value = input("Enter the Food here : \n")

        with open(cli_Name + "_food.txt", "a") as c:
            c.write("==> " + value + "\n")
            print("entered successfully!!!")

    elif c_choice == '2':
        value = input("Enter the excersise here : \n")

        with open(cli_Name + "_excersise.txt", "a") as c:
            c.write("==> " + value + "\n")
            print("Entered successfully!!!")


def retrive(cli_Name):
    print("Enter 1 for retrive food and 2 for retrive excersise : \n ==> ", end = "")
    c_choice = input()

    if c_choice == '1':
        with open(cli_Name + "_food.txt") as op:
            print(op.read())

    elif c_choice == '2':
        with open(cli_Name + "_excersise.txt") as op:
            print(op.read())



file1 = open("clients.txt", "a")
if file1.tell() == 0:
    print("You don't have any clients!!!\n So, You have to add new clients.")

    print("\nHow many client's do you want to add : ", end = "")
    noOfClients = int(input())

    for i in range(noOfClients):
        clientName = input("Enter tha name of client : ")
        file1.write(clientName)
        file1.write("\n")

    file1.close()
    

else:
    print("Enter your choice : \n 1 for add new client \n 2 for Read/Update existing clients \n ==> ", end = "")
    choice = input()

    if choice == '1':
        file1 = open("clients.txt", "a")
        print("\nHow many client's do you want to add : ", end = "")
        noOfClients = int(input())

        for i in range(noOfClients):
            clientName = input("Enter the name of client : ")
            file1.write(clientName)
            file1.write("\n")
        file1.close()
        
    elif choice == '2':
        clientName = input("Enter the client name that you want to read/update : ")

        with open("clients.txt") as op:
            for i in op:
                
                if clientName == i.rstrip('\n'):
                    print("Enter the choice : \n 1 for log data\n 2 for retrive\n ==> ", end = "")
                    cli_choice = input()

                    if cli_choice == '1':
                        log(clientName)
                    elif cli_choice == '2':
                        retrive(clientName)

                    break

