size = int(input("Enter the size of the pattern: "));
col = size;
while size > 0:
    for i in range(col):
        print("*", end="");
    print("\n");
    size -= 1;