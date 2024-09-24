# Картотека сотрудников (список словарей)

employees = [

    {"name": "Валерий", "position": "Менеджер", "department": "Продажи"},
    {"name": "Олег", "position": "Менеджер", "department": "Продажи"},
    {"name": "Ольга", "position": "Разработчик", "department": "ИТ"},
    {"name": "Владислав", "position": "Менеджер", "department": "Продажи"},
    {"name": "Владимир", "position": "Разработчик", "department": "ИТ"},
    {"name": "Анна", "position": "Бухгалтер", "department": "Финансы"},
]

def find_name(name):
    '''
    Ф-ция ищет имена в картотеке и возвращает имена
    '''
    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee
    return None

def filtred_position(position):
    '''
    Ф-ция для фильтрации по должности
    '''
    filtred_emp = []
    for i in employees:
        if i["position"].lower() == position.lower():
            filtred_emp.append(i)
    return filtred_emp

def count_employe(depart):
    '''
    Посчет количиства сотрудников в отделе
    :return:
    '''
    count = 0
    for emp in employees:
        if emp["department"].lower() == depart.lower():
            count += 1
    return count

def add_employ(name):
    '''
    Ф-ция добавления содрудника
    '''
    dict = {}
    dict['name'] = name
    dict['position'] = input(f'Введите должность сотрудника с именем {name}:')
    dict['department'] = input(f'Введите отдел сотрудника с именем {name}:')
    consent = input('Всё верно? (1 - Да, 0 - Нет)')
    if consent == '1':
        employees.append(dict)
        return True
    else:
        return False

def main():
    while True:
        print('\nМеню:')
        print('1. Поиск по имени:')
        print('2. Фильтрация по должности :')
        print('3. Подсчет количества персонала в отделе:')
        print('4. Добавление сотрудника ')
        print('5. Выход')
        choice = input('Выберите действие: ')
        if choice == '1':
            name = input('Введите имя сотрудника: ')
            employee = find_name(name)
            if employee:
                print(
                    f'Найден сотрудник {employee["name"]} должность {employee["position"]} отдел {employee["department"]}')
            else:
                print('Сотрудник не найден')
        elif choice == '2':
            position = input('Введите должность: ')
            filtred_emp = filtred_position(position)
            if filtred_emp:
                print(f'Сотрудники с такой должностью:')
                for emp in filtred_emp:
                    print(f'Имя {emp["name"]} Отдел {emp["department"]}')
                else:
                    print('с такой должностью сотрудников нет')
        elif choice == '3':
            depart = input('Введите отдел: ')
            count = count_employe(depart)
            print(f'Количество сотрудников в отдле {depart}: {count}')
        elif choice == '4':
            name = input('Введите имя сотрудника: ')
            if add_employ(name):
                print(f'Добавлен сотрудник: ')
                print(f'Имя = {employees[len(employees)-1]["name"]}')
                print(f'Должность = {employees[len(employees)-1]["position"]}')
                print(f'Отдел = {employees[len(employees)-1]["department"]}')
            else:
                print('Сотрудник не добавлен')
        elif choice == '5':
            print("Выход из программы")
            break
        else:
            print("Не верный ввод пункта меню")

if __name__ == "__main__":
    main()