dog = 0
mo5 = 5
mo10 = 10
let = int(input("Сколько вам лет: "))
ima = str(input("Как вас зовут: "))
m5 = int(input("Сколько у вас монет по 5 рублей: "))
m10 = int(input("Сколько у вас монет по 10 рублей: "))
с5 = m5 * mo5
c10 = m10 * mo10
sum = с5 + c10
let2 = let % 2
if (let >= 18) and (ima != "Олег") and (let2 == 0) and (sum >= 20):
    dog = (sum / 20)    
    print(dog)
else:
    print("ЭЭЭ братишка иди отсюда")