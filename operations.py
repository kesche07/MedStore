import datetime
from writeData import save_data
from medicine import Medicine


def buy_pill(data_read):

    '''
    buying pills by asking the user for values
    '''
    print("-------- PURCHASING MEDICINE --------")
    customer_name = input("Enter your name:")
    purchased = []
    try:
        while True:
            med_name = input("Enter Medicine Name")

            if med_name not in data_read:
                print("Medicine not available")
                continue
            med = data_read[med_name]

            tab_type = input("Buying per tablet or per strip?").lower()
            try:
                qty = int(input(f"How many {tab_type}?"))
                if qty <= 0:
                    print("Quantity must be greater than 0. Please try again.")
                    continue
                
            except ValueError:
                print("Please enter a valid number for quantity.")
                continue

            discount = 0.0
            
            if tab_type == "strip":
                total_tabs_needed = qty * med.tabs_per_strip
                print(f"Total tablets: {total_tabs_needed}")
            
                if total_tabs_needed > med.stock:
                    print(f"Sorry, only {med.stock} tablets available. You requested {total_tabs_needed}.")
                    continue
                
                subtotal = qty * med.rate_strip
                if qty >= 2:
                    discount = subtotal * 0.05
                    subtotal -= discount
                        
            elif tab_type in ["tablet", "tab", "tabs"]:
                total_tabs_needed = qty
                if total_tabs_needed > med.stock:
                    print(f"Sorry, only {med.stock} tablets available. You requested {total_tabs_needed}.")
                    continue
                subtotal = qty * med.rate_tab
            else:
                print("Please input valid type (strip/tablet)")
                continue
            

            ## updates the stock 
            med.stock -= total_tabs_needed

            purchased.append({
                "name": med_name, 
                "brand": med.brand,  # Added 'med.' prefix
                "qty": qty,
                "unit": tab_type, 
                "discount": discount, 
                "total": subtotal
            })
            print(f"Added {med_name} to cart. Subtotal: Rs. {subtotal}")

            ans = input("Continue shopping? (Y/N): ").lower().strip()
            if ans == "n" or ans == "no":
                break

        if purchased:
            print("Thank you for purchasing")

            return customer_name,data_read,purchased
    except Exception as e:
        print(f"Error in purchasing items: {e}")

def generate_invoice(customer, items):
    ''' Generates a Unique Invoice using the customers name,
    and the current date at time of purchase '''
    print("-------- GENERATING INVOICE --------")
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    
    filename = f"Invoice_{customer}"+"_"+year+month+day+"_"+hour+minute+second+".txt"
    grand_total = 0
    
    with open(filename, "w") as f:
        f.write(f"--- VAT INVOICE ---\nCustomer: {customer}\nDate: {datetime.datetime.now()}\n")
        f.write("-" * 30 + "\n")
        for item in items:
            f.write(f"{item['name']} ({item['brand']})\n")
            f.write(f"{item['qty']} {item['unit']} | Disc: Rs.{item['discount']:.2f} | Total: Rs.{item['total']:.2f}\n")
            grand_total += item['total']
        f.write("-" * 30 + "\n")
        f.write(f"GRAND TOTAL: Rs. {grand_total:.2f}\n")
    
    print(f"\nInvoice saved as {filename}")

def restock_meds(file,data_read):
    '''
    Method to restock multiple medicines

    Also adds a medicine if the name is not found and user wants to add
    '''

    print("-------- RESTOCK INVENTORY --------")
    while True:
        med_name = input("Enter medicine name to restock")

        if med_name in data_read:
            med_obj = data_read[med_name]
            print(f"Current stock for {med_name}: {med_obj.stock}")

            try:
                to_add = int(input("Enter quantity to add"))
                if to_add>0:
                    med_obj.stock += to_add
                    save_data(file, data_read)
                    print(f"Update successful! New Stock : {med_obj.stock}")
                else:
                    print("Quantity must be positive.")
            except ValueError:
                print("Invalid input. Please enter an Integer.")
        else:
            print(f"'{med_name}' not found in inventory.")
            create_new = input("Would you like to add it as a new medicine? (y/n): ").lower().strip()
            
            if create_new == 'y':
                try:
                    #def __init__(self,name,brand,stock,rate_tab,rate_strip,tabs_per_strip):
                    brand = input("Enter Brand Name")
                    rate_tab = float(input("Enter rate per tablet"))
                    rate_strip= float(input("Enter rate per strip"))
                    tabs_per_strip= int(input("Enter Tablets per strip"))
                    stock = int(input(f"Enter initial stock for {med_name}: "))
                    
                    
                    new_med = Medicine(med_name,brand,stock,rate_tab,rate_strip,tabs_per_strip) 
                    
                    
                    data_read[med_name] = new_med
                    
                    print(f"Successfully added {med_name} to the system!")
                except ValueError:
                    print("Invalid input for price or stock. Addition cancelled.")
        save_data(file, data_read)
        ans = input("Continue restock? (Y/N): ").lower().strip()
        if ans == "n" or ans == "no":
            print("Finishing restock...")
            break
    return data_read
