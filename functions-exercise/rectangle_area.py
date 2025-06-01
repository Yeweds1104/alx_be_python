user_length = int(input("Enter the length of the rectangle: "));
user_width = int(input("Enter the width of the rectangle: "));

def rectangle_area(length, width):
    return length * width;

area = rectangle_area(user_length, user_width);
print(f"The area of the rectangle is: {area}")