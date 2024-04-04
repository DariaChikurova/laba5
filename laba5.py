import random
def zadanie1():
    import random
    list = random.sample(range(1, 10), 5)
    p = int(input("Введите число: "))
    if p in list:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
        print("Исходный список:", list)

def zadanie2():
    import random
    random_list = random.choices(range(1, 10), k=10)
    print("Список случайных чисел:", random_list)
    duplicates = set()
    seen = set()
    for num in random_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    if duplicates:
        print("Повторяющиеся элементы в списке:", duplicates)
    else:
        print("В списке нет повторяющихся элементов.")


def zadanie3():
    days_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    weekens = int(input("Сколько выходных дней на неделе вы хотите? "))
    if weekens > len(days_of_week):
        print("Ошибка! Неделя состоит только из 7 дней.")
    else:
        weekends = days_of_week[-weekens:]
        workdays = days_of_week[:-weekens]
        print("Ваши выходные дни: ", weekends)
        print("Ваши рабочие дни: ", workdays)


def zadanie4():
    group1 = ['Иванов', 'Петров', 'Куклинов', 'Сидоров', 'Мельников', 'Латышева', 'Свечкова', 'Чикурова', 'Никитин', 'Сидоренко']
    group2 = ['Ларионова', 'Пономаренко', 'Иванова', 'Петрова', 'Полякова', 'Фаруди', 'Чаин', 'Сорокин', 'Задернюк', 'Фищенко']
    team1 = random.sample(group1, 5)
    team2 = random.sample(group2, 5)
    team = tuple(team1[:5] + team2[:5])
    print("Список студентов группы 1: ", group1)
    print("Список студентов группы 2: ", group2)
    print("Спортивная команда: ", team)
    print("Длина команды: ", len(team))
    sorted_team = tuple(sorted(team))
    print("Отсортированная спортивная команда: ", sorted_team)
    ivanov_count = team.count('Иванов')
    if ivanov_count > 0:
        print("Фамилия Иванов встречается в команде",ivanov_count, "раз(а).")
    else:
        print("Фамилии Иванов нет в команде.")


zadanie2()
while True:
    print('1. Угадать число')
    print('2. Повтор')
    print('3. Выходные')
    print('4. Спортивная команда')
    print('5. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        zadanie1()
    elif a == 2:
        zadanie2()
    elif a == 3:
        print(zadanie3())
    elif a == 4:
        print(zadanie4())
    elif a == 5:
        break
    else:
        print('Неверное действие')