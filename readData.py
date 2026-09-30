from medicine import Medicine
def read_data(file_path):
    ''' Reads Data in File '''
    try:
        file = open(file_path,"r")
        lines = file.readlines()
        file.close()
        data = {}
        
        header = f"{'Name':<20} {'Brand':<15} {'Stock':<8} {'Rate/Tab':<10} {'Rate/Strip':<12} {'Tabs/Strip':<10}"
        print(header)
        print("-" * len(header))

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 6:
                    
                obj = Medicine(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                data[obj.name] = obj
                    
                    # 4. Print the row using object attributes
                print(f"{obj.name:<20} {obj.brand:<15} {obj.stock:<8} {obj.rate_tab:<10} {obj.rate_strip:<12} {obj.tabs_per_strip:<10}")
        return data
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error in reading file: {e}")
        return {}

