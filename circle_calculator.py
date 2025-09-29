import math

while True:
    try:
        radius = float(input("Enter radius of the circle: "))
        break
    except ValueError:
        print("Please enter a valid number!")

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Circumference of the circle is:", circumference)
print("Area of the circle is:", area)
