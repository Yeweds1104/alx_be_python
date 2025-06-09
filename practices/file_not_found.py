file_name = input("Enter file name to open and read: ")
try:
    f = open(file_name)
except FileNotFoundError:
    print("Sorry. File doesn't exist!")
else:
    print(f.read())
    f.close()
finally:
    print("Finally program executed!")