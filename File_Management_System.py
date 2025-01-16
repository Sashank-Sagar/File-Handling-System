import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name {filename}: Created Successfully!")
    
    except FileExistsError:
        print(f"File name {filename}: already exists!")
    
    except Exception as e:
        print("Error Occurred!")

def view_all_files():
    try:
        files = os.listdir()
        if not files:
            print("No file found!")
        else:
            print("Files in directory:")
            for file in files:
                print(file)
    
    except Exception as e:
        print("Error Occurred!")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    
    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print("Error Occurred!")

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"Content of '{filename}' :\n{content}")
    
    except FileExistsError:
        print(f"{filename} doesn't exist!")
    
    except Exception as e:
        print("Error Occurred!")
    
def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content = input('Enter Data to add : ')
            f.write(content + "\n")
            print(f"Content added to {filename} successfully! ")
    
    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print("Error Occurred!")


def main():
    while True:
        print("FILE MANAGEMENT SYSTEM :")
        print("1: Create file")
        print("2: Edit file")
        print("3: Read file")
        print("4: Delete file")
        print("5: View all files")
        print("6: Exit")
        
        user_input = input("Enter option (1-6) to perform: ")

        if user_input == '1':
            filename = input("Enter the file name you want to create: ")
            create_file(filename)
        
        elif user_input == '2':
            filename = input("Enter the file name you want to edit: ")
            edit_file(filename)
        
        elif user_input == '3':
            filename = input("Enter the file name you want to read: ")
            read_file(filename)
        
        elif user_input == '4':
            filename = input("Enter the file name you want to delete: ")
            delete_file(filename)
        
        elif user_input == '5':
            view_all_files()
        
        elif user_input == '6':
            print("Closing ........")
            break
        
        else:
            print("Invalid Input! Please enter a valid option (1-6)")

if __name__ == "__main__":
    main()