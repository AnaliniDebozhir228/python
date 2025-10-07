# file = open('example.txt', 'r', encoding="utf-8")
# content = file.read()
# file.close()

# print(content)

# #  r - чтение - read
# #  w - запись/создание - write
# #  a - добавления в конец файла
# #  r+ - чтение и запись

# with open('output.txt', 'w', encoding="utf-8") as file:
#      file.write("Салям алексус\n")
#      file.write("Малял алексус\n")

# with open('output.txt', 'a', encoding="utf-8") as file:
#      file.write('Калял алексус, кста она всегда внизу будет')

# with open("output.txt", "r", encoding="utf-8") as file:
#      content = file.read()
#      print('Весь файл: ')
#      print(content)

# with open("example.txt", "r", encoding="utf-8") as file:
#      line1 = file.readline()
#      line2 = file.readline()
#      print("Первая стока: ", line1)
#      print("Вторая стока: ", line2)

# #чвитает все строки как элементы списка
# with open("example.txt", "r", encoding="utf-8") as file:
#      lines = file.readlines()
#      print('Все строки как список: ')
#      for line in lines:
#           print(line.strip())
# sum = 0

# with open("numbers.txt", "r", encoding="utf-8") as file:
#       line1 = file.readline()
#       line2 = file.readline()
#       line3 = file.readline()
#       line4 = file.readline()
#       line5 = file.readline()
#       line6 = file.readline()
#       line7 = file.readline()
#       line8 = file.readline()
#       line9 = file.readline()
#       line10 = file.readline()

# sum = int(line1)+int(line2)+int(line3)+int(line4)+int(line5)+int(line6)+int(line7)+int(line8)+int(line9)+int(line10)
# print(sum)

with open('greentings.txt', 'w', encoding="utf-8") as file:
      file.write("Салям алексус\n")
      file.write("Малял алексус\n")
      file.write("Халял алексус\n")
      file.write("Галял алексус\n")
      file.write("Салял алексус\n")

with open('greentings.txt', 'r', encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("numbers.txt", "r", encoding="utf-8") as file:
      lines = file.readlines()
      sum = sum(int(line.strip()) for line in lines)    
print(sum) 
          