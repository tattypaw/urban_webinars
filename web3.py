#Попробуйте реализовать функцию вывода задач по приоритету, а также ф-цию удаления задач))



tasks = []

# ANSI-коды — это последовательности символов,

# которые терминалы могут интерпретировать для изменения внешнего вида текста.

# Они начинаются с \033[ (или \x1b[ в другом формате)

# и следуют за ними коды цветов и атрибутов.

GREEN = '\033[92m'

RED = '\033[91m'

YELLOW = '\033[93m'

BOLD = '\033[1m'

UNDERLINE = '\033[4m'

RESET = '\033[0m'



def add_task(task_name, *args, priority='Normal', **kwargs):

    """

    Добавляет новую задачу в список задач с произвольными дополнительными параметрами.

    - task_name: название задачи

    - *args: дополнительные параметры задачи

    - priority: приоритет задачи (по умолчанию 'Normal')

    - **kwargs: дополнительные именованные параметры

    """

    task = {

        'name': task_name,

        'priority': priority,

        'completed': False,

        'additional': args,  # Дополнительные параметры сохраняем в виде кортежа

        'extra_info': kwargs  # Именованные параметры сохраняем в виде словаря

    }



    tasks.append(task)

    print(f'Task {BOLD}{YELLOW}{task_name}{RESET} added with priority {priority}. Extra info: {kwargs}')



def list_tasks(show_completed=False):

    """

    Выводит список всех задач.

    - show_completed: если True, показывает выполненные задачи

    """

    print(f'\n{BOLD}{UNDERLINE}List tasks:{RESET}')

    for index, task in enumerate(tasks):

        status = f'{GREEN}Completed{RESET}' if task['completed'] else f'{RED}In the process{RESET}'

        if not task['completed'] or show_completed:

            extra_info = []

            for k, v in task['extra_info'].items():  # Заменяем генераторное выражение на цикл

                extra_info.append(f'{k}: {v}')

            extra_info_str = ', '.join(extra_info)  # Собираем строку с дополнительной информацией

            print(f'{index + 1}. {task["name"]} [{task["priority"]}] - {status} | {extra_info_str}')



def complete_task(task_index):

    """

    Отмечает задачу как выполненную.

    - task_index: индекс задачи (начинается с 1 для удобства пользователя)

    """

    task = tasks[task_index - 1]

    task['completed'] = True

    print(f'Task {GREEN}{task["name"]}{RESET} marked as completed')







def search_task(keyword):

    """

    Ищет задачи по ключевому слову в названии.

    - keyword: ключевое слово для поиска

    """

    found = False

    print("\nTasks found:")

    for task in tasks:

        if keyword.lower() in task['name'].lower():

            extra_info = []

            for k, v in task['extra_info'].items():  # Заменяем генераторное выражение на цикл

                extra_info.append(f'{k}: {v}')

            extra_info_str = ', '.join(extra_info)  # Собираем строку с дополнительной информацией

            print(f'- {task["name"]} [{task["priority"]}] | {extra_info_str}\n')

            found = True

    if not found:

        print(f'No tasks with this keyword were found')



def remove_completed_recursive(index=0):

    """

    Рекурсивно удаляет все выполненные задачи и возвращает количество удаленных задач.

    - index: текущий индекс для проверки, по умолчанию начинается с 0

    """

    if index >= len(tasks):

        return 0

    removed_count = 0

    if tasks[index]['completed']:

        print(f"{BOLD}{RED}Deleting a completed task:{RESET} {YELLOW}{tasks[index]['name']}{RESET}")

        tasks.pop(index)

        removed_count = 1

        removed_count += remove_completed_recursive(index)

    else:

        removed_count += remove_completed_recursive(index + 1)

    return removed_count


def find_priority(priority_key):

    """

    Выводит задачи заданного приоритета.

    - priority_key: ключевое слово для задания искомого приоритета

    """

    found = False

    print(f'\nTasks with priority "{priority_key}" found:')

    for task in tasks:

        if priority_key.lower() in task['priority'].lower():

            extra_info = []

            for k, v in task['extra_info'].items():  # Заменяем генераторное выражение на цикл

                extra_info.append(f'{k}: {v}')

            extra_info_str = ', '.join(extra_info)  # Собираем строку с дополнительной информацией

            print(f'- {task["name"]} | {extra_info_str}\n')

            found = True

    if not found:

        print(f'No tasks with this priority were found')


def delete_task():
    """
    спрашивает номер задачи в списке и удаляет ее с согласия пользователя

    """
    list_tasks()

    number_of_task = int(input('\nInput number of task that you want to delete: '))

    if number_of_task <= 0 or number_of_task > len(tasks):

        print(f'\n{UNDERLINE}{BOLD}Task is not exist!{RESET}')

    else:

        answer = input(f'\nWould You delete {RED}{tasks[number_of_task - 1]["name"]} | {tasks[number_of_task - 1]["priority"]}{RESET}? (1 - Yes / any key - No) ')

        if  answer == '1':

            tasks.pop(number_of_task - 1)

            print(f'\n{GREEN}Task deleted{RESET}')


# Примеры использования Task Manager с произвольными параметрами

# Добавление задач с произвольными параметрами

add_task("Buy food", 'Urgent', priority="High", location="Supermarket", due_date="2024-09-20")

add_task("Write a report", 'High priority', priority="Low", department="HR", project="Quarterly Review")

add_task("Prepare for the webinar", 'Important', priority="Medium", speaker="John Doe")

add_task("Call a coworker", 'Routine', priority="High", contact="Jane Smith")

add_task("Call a friends", 'Routine', priority="Low")



# Вывод списка задач

list_tasks()



# Отметка задач как выполненных

complete_task(1)

complete_task(2)



# Вывод списка задач, включая выполненные

list_tasks(show_completed=True)



# Поиск задач по ключевому слову

search_task('call')



# Удаление всех выполненных задач и получение количества удаленных задач

removed_tasks = remove_completed_recursive()



# Вывод списка задач после удаления выполненных

list_tasks()



# Вывод количества удаленных задач

print(f"\n{BOLD}{UNDERLINE}Total removed tasks:{RESET} {removed_tasks}")

# Добавление задач с приоритетом High

add_task("Mother's birthday", 'Urgent', priority="High", location="Restaurant", date="2024-09-29")

# Вывод задач с приоритетом High

find_priority("High")

# Удаление задачи по индексу

delete_task()


