import csv
from collections import namedtuple
from collections import defaultdict


class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def ask_for_input(console_output: str) -> str:
    """Функция печатает определённую просьбу о вводе и
    возвращает ввод пользователя"""
    print(console_output)
    user_input = input()
    return user_input


def file_processing() -> defaultdict:
    department = defaultdict(list)

    with open('Corp Summary.csv') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        next(file_reader)
        for row in file_reader:
            Department = namedtuple('Department', ['Branch', 'Mark', 'Salary'])
            values = Department(row["Отдел"], row["Оценка"], row["Оклад"])
            department[row["Департамент"]].append(values)

    return department


def info(dep: defaultdict):
    """Функция обрабатывает 1 пункт меню -
    находит у департамента уникальные значения отделов"""
    branches = set()
    print(bcolors.OKGREEN + 'Департамент: Отделы')
    for dep_key, rows in dep.items():
        for row in rows:
            branches.add(row.Branch)
        print(bcolors.ENDC + dep_key, end=": ")
        # print(*branches, sep=", ")
        print(', '.join(branches))
        branches.clear()


def one_department(records: namedtuple) -> (namedtuple, set):
    """Функция обрабатывает все записи одного депаратмента, извлекая данные о вилке зп,
    средней зп, численности и отделах департамента"""
    number_of_workers = len(records)
    max_salary, min_salary = -1, int(records[0].Salary)
    average_salary = 0
    branches = set()
    Info_dep = namedtuple('Info', ['Number', 'Average_salary', 'Min_salary', 'Max_salary'])
    for one_record in records:
        salary = int(one_record.Salary)
        if salary > max_salary:
            max_salary = salary
        if salary < min_salary:
            min_salary = salary
        average_salary += salary
        branches.add(one_record.Branch)
    average_salary /= number_of_workers
    info_return = Info_dep(number_of_workers, average_salary, min_salary, max_salary)
    return info_return, branches


def consolidated_report(dep: defaultdict):
    """Функция для обработки 2 пункта меню - выводит в консоль отчёт"""
    print(bcolors.OKGREEN + 'Департамент: Отделы |Численность |Средняя зп |Мин. зп |Макс. зп')
    for dep_key, records in dep.items():
        values = one_department(records)
        print(bcolors.ENDC + dep_key, end=": ")
        print(*values[1], sep=", ", end="| ")
        print(
            f'{values[0].Number} | {round(values[0].Average_salary, 2)} | {round(values[0].Min_salary, 2)} '
            f'| {round(values[0].Max_salary, 2)}')


def save_report(dep: defaultdict):
    """Функция для обработки 3 пункта меню - сохраняет отчёт в файл"""
    path = ask_for_input(bcolors.OKGREEN + "Укажите путь до файла для сохранения отчёта: ")
    f_names = ['Департамент', 'Отделы', 'Численность', 'Средняя зп', 'Мин. зп', 'Макс. зп']
    with open(path, 'w', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerow(f_names)
        for dep_key, records in dep.items():
            values = one_department(records)
            csv_writer.writerow((dep_key, values[1], values[0].Number, values[0].Average_salary,
                                 values[0].Min_salary, values[0].Max_salary))


def correct_input(argument: str) -> int:
    """Функция проверяет ввод данных на корректность"""
    if argument.isdigit() and int(argument) in range(1, 5):
        return int(argument)
    else:
        return -1


switcher = {
    1: info,
    2: consolidated_report,
    3: save_report
}


def command_to_func(cmd: int, dep: defaultdict):
    """В зависимости от введённой пользователем команды, вызывает нужную функцию"""
    func = switcher[cmd]
    return func(dep)


def print_menu():
    """Вывод в консоль главного меню"""
    print(bcolors.OKGREEN + "Меню: ")
    print(bcolors.OKGREEN + "Выберите одну из 3 команд:")
    print(bcolors.OKCYAN + "Команда 1: вывести имеющиеся департаменты и отделы")
    print("Команда 2: вывести сводный отчёт о департаментах")
    print("Команда 3: сохранить сводный отчёт об одном из департаментов в csv-файл")
    print("Команда 4: Выход из меню и завершение программы")


if __name__ == '__main__':
    print_menu()
    command = correct_input(input())
    department_ = file_processing()
    while command != 4:
        if command != -1:
            command_to_func(command, department_)
        else:
            print(bcolors.FAIL + "Некорректный ввод команды. Введите число от 1 до 4")
        print_menu()
        command = correct_input(input())
    print(bcolors.OKGREEN + "Выход из меню")
