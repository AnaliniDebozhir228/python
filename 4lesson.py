# book = {
#     "Title": "1984",
#     "author": "Джордж Оруэл",
#     "year": "1949",
#     "garne": "Антиутопия"
# }

# player = {
#     "name": "NagibatorMamok228",
#     "id": 1,
#     "age": 11,
#     "city": 17,
#     "isAlive": True,
#     "damage": 999.9
# }

# print(player["name"])
# print(player.get("class", "Не найдено")) #бЕЗ ОШИБКИ
# player["damage"] = 1000
# print(player)

# if "name" in player:
#     print("О великий",(player["name"]))
# if "HP" not in player:
#     print("ты сдох")

# removed_value = player.pop("city")
# last_item = player.popitem()
# print("Удалили эту штуку", last_item)
# print(player.keys())
# print(player.values())
# print(player.items())

# for key in player.keys():
#     print(key)

# for value in player.values():
#     print(value)

# for key, value in player.items():
#     print(f"Ключ {key}, значение: {value}")
    
# students = [
#     {"name": "Андрей", "age": 15, "grades": [5,5,5,4,4,5]},
#     {"name": "Ярик", "age": 17, "grades": [2,2,3,4,4,5]},
#     {"name": "Тимур", "age": 15, "grades": [4,4,5,4,4,5]},
# ]
# print(students[0]["age"])
# print(students[1]["name"])

# for student in students:
#     print(student["name"])
slova = {
    "apple": "Яблоко", 
    "Fortnite": "Аутизм", 
    "Sybay": "Привет мой дорогой друг", 
    "Coffe": "Кофе", 
    "Banana": "Банан"
}

for _ in iter(int, 1):
    ass = input("Ведите слово:").strip().lower()
    if ass == "quit":
        print("пшл нафг")
        break
    if ass in slova:
        print(f"Первод: {slova[ass]}")
    else:
        print("Таке нема")
        vibor = input("добавить иль нет?").strip().lower()
        if vibor == "Да":
            dobav_pere = input(f"ведите перевод {ass}: ").strip()
            slova[ass] = dobav_pere
            print("Добавил брад")
        else:
            print("Пшл нфг")