def menu():
    print("Выберите действие (1 - поиск сотрудника, 2 - добавление сотрудника, 3 - редактирование, 4 - удаление)")
    res = int(input())
    return res

def get_info():
    return input("введите информацию о сотруднике: ")

def choice_info():
    pass

def change0():
    return input('введите информацию которую вы хотите заменить: ')

def change():
    return input('введите информацию на которую хотите заменить: ')



def new_emp():
    fio = input("Fio: ")
    date = input("Date: ")
    work = input("Position: ")
    salary = input("Salary: ")
    phone = input("Phone: ")

    zap ="\n" + fio + " | " + date + " | " + work + " | "  + salary + " | " + phone

    return zap

def beautiful_print():
    with open("file3.txt",'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())

def get_data():
    with open("file3.txt", 'r') as file:
         data = file.read().split(f'\n')
         return  data

def add_data(a):
    with open("file3.txt",'a') as file:
        file.write(a)


def edit_data(a, b):
    with open('file3.txt', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(a, b)

    with open('file.txt', 'w') as f:
        f.write(new_data)


def delete(a):
    with open('file.txt', 'r') as f:
        old_data = f.read()

    b = ''
    new_data = old_data.replace(a, b)

    with open('file.txt', 'w') as f:
        f.write(new_data)

def search(emp):
    book = get_data()
    ans = []
    flag = False
    for i in book:
        if i.find(emp) != -1:
            flag = True
            ans.append(i)
    if flag == True:
        return ans
    else:
        return "Сотрудник не найден"


def edit():
    emp = get_info()
    find_info = search(emp)
    print(find_info)
    n_info = change()


    for i in find_info:
        info = i.split(' | ')

    for i in range(len(info)):
        if info[i].find(emp) != -1:
            info[i] = n_info
            break

    edit_data(''.join(find_info), ' | '.join(info))


def delete_info():
    book = beautiful_print()
    print(book)
    emp = get_info()
    find_info = search(emp)
    print(find_info)

    delete(''.join(find_info))

def button():
    a = menu()
    if a == 1:
        print(search(get_info()))
    elif a == 2:
        add_data(new_emp())
        print(beautiful_print())
    elif a == 3:
        edit()
    elif a == 4:
        delete_info()

button()