lenght = 5
width = 3
print("площадь нашей комнаты{areal}")

lenght2 = 4
width2 = 2
area2 = lenght2 * width2
print("площадь нашей комнаты{areal2}")
def great(name):
    print(f"привет ,{name}")
great("олег")
def calculate_area(height,widht):
    area = lenght * width
    return area
room_area = calculate_area
print("площадь комнаты{room_area}")

def circle_area(radius):
    return 3.14 * radius**2


def max_of_three(a,b,c):
    if a > b and a > c:
        print(f"{a} больше число")
    if b > a and b > c:
        print(f"{b}  больше число")
    if c > a and b < c:
        print(f"{c} больше число")

radius = 67
a,b,c = 6,7,6
radius = circle_area(67)
max = max_of_three(a,b,c)

print(f"r: {radius}")