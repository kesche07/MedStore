
from readData import read_data
from writeData import save_data
from operations import buy_pill,generate_invoice,restock_meds

file = "inventory.txt"
print( "="*10)
print("Welcome to MedStore Pvt. Ltd")
while True:
    print("What Can we get started for you?")
    print("1. Buy Medicine \n2. Restock Supply \n3. Show Stock \n4. End")
    try:
        choice = int(input("Select Option"))
        

        if choice == 1:
            my_data = read_data(file)
            result = buy_pill(my_data)
            if result: # Only run if result is NOT None/empty
                name, new_data, cart = result
                save_data(file, new_data)
                invoice = input("Generate Invoice? {Y/N}")
                if invoice in ["Yes","yes","y","Y"]:
                    generate_invoice(name,cart)
        elif choice == 2:
            my_data = read_data(file)
            updated_data = restock_meds(file,my_data)
        elif choice == 3:
            my_data = read_data(file)

        elif choice == 4:
            cont = input("Are you Sure you want to end? {Y/N}").lower().strip()
            if cont == "y" or cont == "yes":
                print("Thank you for using our service!")
                break
            
        else:
            print("Please choose a valid Option.")
            continue
    except ValueError:
        print("Please Enter a Valid Number")
        continue

    
        
