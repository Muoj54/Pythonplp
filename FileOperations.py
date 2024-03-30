def write_to_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("The slow brown fox did not attempt to jump over the low fence\n")
            file.write("56316893\n")
            file.write("The earth has a diameter of 12,742 kilometres\n")
        print("A new file was created")
    except PermissionError:
        print("Permission denied. Unable to create or write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("The file was written Successfully!")
def read_from_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Contents of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found. Unable to read from the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("The file was read successfully.")
def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("This is anew line that I appended\n")
            file.write("The earth has a circumference of 40075 kilometres!\n")
            file.write("That is all, folks!\n")
        print("Content added successfully.")
    except PermissionError:
        print("Permission denied. Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Items appended successfully.")
if __name__ == "__main__":
    write_to_file()
    print()
    read_from_file()
    print()
    append_to_file()
