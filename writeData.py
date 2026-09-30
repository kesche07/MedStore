from medicine import Medicine
def save_data(file_path,data):
    ''' Writes data to the file '''
    try:
        with open(file_path,"w") as file:
            for med_obj in data.values():
                file.write(str(med_obj) + "\n")
        print("Values Updated Successfully")
    except(FileNotFoundError):
        print("File not found")
    except Exception as e:
        print(f"Error in saving data: {e}")
        
