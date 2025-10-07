# legth1 = 5
# width1 = 3
# area1 = legth1 * width1
# print(f"Площадь: {area1}")

# def great():
#     """Эта шфункция пишет приет"""
#     print("Пшл нфг чмо")

# great()

# def great(name):
#     """Эта шфункция пишет приет"""
#     print(f"Пшл нфг {name} чмо")

# great("Андрей")
# great("Ярик")
# great("Тимур")

# def introduce(name, age, city):
#     """Докс"""
#     print(f"Имя: {name} Возраст: {age} Город: {city}")

# introduce("Андрей", 15, "Симферополь")

# def caculate_area(lengt, width):
#     area = lengt * width
#     return area

# room_area = caculate_area(5, 3)
# print(f"Площадь: {room_area}")

# def order(age):
#     if age >= 18:
#         return True
#     else:
#         return False
    
def circle_area(radius):
    return 3.14 * radius**2

def max_of_three(a,b,c):
    max = 0
    if a>b and a>c:
        max = a
        return max
    elif b>a and b>c:
        max = b
        return max
    else:
         max = c
         return max
radius = 5
a,b,c = -2,-6,-1212
area = circle_area(15)
max = max_of_three(a,b,c)

print(f"Радиус: {area}, наибольшие {max}")