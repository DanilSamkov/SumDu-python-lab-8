# Частина коду, створена студентом КН-32/2 Самковим Данилом Олександровичем:

# Словник для зберігання інформації про студентів
students = [
    {'group_number': 'КН-32', 'surname': 'Самков', 'name': 'Данило', 'patronymic': 'Олександрович', 'course': 2,
     'subjects': {'Математика': 2, 'Програмування': 4, 'Англ. мова': 4}},
    {'group_number': 'КН-32', 'surname': 'Святішенко', 'name': 'Дмитро', 'patronymic': 'Олександрович', 'course': 2,
     'subjects': {'Математика': 4, 'Програмування': 3, 'Англ. мова': 3}},
    {'group_number': 'КН-31', 'surname': 'Баранова', 'name': 'Марина', 'patronymic': 'Володимирівна', 'course': 2,
     'subjects': {'Математика': 4, 'Програмування': 4, 'Англ. мова': 4}},
    {'group_number': 'КН-31', 'surname': 'Сідельнік', 'name': 'Юлія', 'patronymic': 'Іванівна', 'course': 2,
     'subjects': {'Математика': 3, 'Програмування': 4, 'Англ. мова': 1}},
    {'group_number': 'КН-31', 'surname': 'Ленда', 'name': 'Микита', 'patronymic': 'Романович', 'course': 2,
     'subjects': {'Математика': 5, 'Програмування': 2, 'Англ. мова': 4}}
]


# Функція для додавання студента до словника
def add_student(students_list, group_number, surname, name, patronymic, course, subjects):
    student = {
        'group_number': group_number,
        'surname': surname,
        'name': name,
        'patronymic': patronymic,
        'course': course,
        'subjects': subjects
    }
    students_list.append(student)


# Функція для виведення словника у вигляді таблиці
def print_students_table(students_list):
    print(f"{'Група':<10}{'Прізвище':<15}{'Ім\я':<10}{'По батькові':<15}{'Курс':<10}{'Предмети':<30}")
    print("="*107)
    for student in students_list:
        subjects = ', '.join([f"{subject}: {grade}" for subject, grade in student['subjects'].items()])
        print(f"{student['group_number']:<10}{student['surname']:<15}{student['name']:<10}{student['patronymic']:<15}{student['course']:<10}{subjects:<30}")


# Головна функція
def main():
    # Додавання студента
    add_student(students, 'КН-33', 'Петров', 'Петро', 'Петрович', 2, {'Математика': 2, 'Програмування': 2, 'Англ. мова': 2})


    # Виведення словника
    print_students_table(students)


if __name__ == "__main__":
    main()
#Завдання для наступного студента: додати видалення студента зі словника