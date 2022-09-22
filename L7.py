from datetime import datetime as dt
fio = None
number_phone = None

def Get_view_model():
    fio = input('Введите ФИО: ')
    while True:
        number_phone = input('Введите номер телефона: ')
        if number_phone.isdigit() == True:
            break
    return (fio, number_phone)


def Get_user_search():
    data_user = input('Введите ФИО или номер телефона: ')
    return data_user


def Get_user_delete():
    delete_user = input('Кого вы хотате удалить? ')
    print('Вы уверены что хотите удалить запись?')
    return delete_user


def log_data_user(fio, phone_number):
    file_log_user_data = 'phonebook.txt'
    time = dt.now().strftime("%d/%m/%Y Time %H:%M")
    with open(file_log_user_data, 'a') as file:
        file.write(f'{time} \nFIO: {fio} - NumberPhone: {phone_number}\n')


def give_the_data_user(user_data_search):
    file_log_user_data = 'phonebook.txt'
    with open(file_log_user_data, 'r') as file:
        all_data_user = file.read()
        return all_data_user


def delete_user(user):
    file_log_user_data = 'phonebook.txt'
    with open(file_log_user_data, 'r') as file:
        all_data_user = file.read().split(f'\n')
        wh = len(all_data_user)
        for i in range(0, wh):
            ind = all_data_user[i].find(user)
            if ind != -1:
                tmp = i
                break
        all_data_user.pop(tmp)
        all_data_user.pop(tmp - 1)
        for i in range(0, len(all_data_user)):
            if len(all_data_user[i]) == 0:
                all_data_user.pop(i)
                break
        with open(file_log_user_data, 'w') as file_new:
            for i in range(0, len(all_data_user)):
                file_new.write(f'{all_data_user[i]}\n')


def add_model_phonebook(user_data):
    global fio
    global number_phone
    fio = user_data[0]
    number_phone = user_data[1]
    log_data_user(fio, number_phone)


def search_phone_in_phonebook(user_data_search):
    all_data_user = give_the_data_user(user_data_search)
    if all_data_user.find(user_data_search) == -1:
        return 'По этим параметрам не найдено записей'
    else:
        all_data_user = all_data_user.split(f'\n')
        answer = -1
        answer_new = []
        for i in range(0, len(all_data_user)):
            answer = all_data_user[i].find(user_data_search)
            if answer != -1:
                answer_new.append(all_data_user[i])
        return answer_new


def delete_user(user):
    all_data_user = give_the_data_user(user)
    if all_data_user.find(user) == -1:
        return 'По этим параметрам не найдено записей'
    else:
        all_data_user = all_data_user.split(f'\n')
        answer = -1
        answer_new = []
        for i in range(0, len(all_data_user)):
            answer = all_data_user[i].find(user)
            if answer != -1:
                answer_new.append(all_data_user[i])
        if len(answer_new) != 1:
            return 'Чтобы удалить, введите более полные данные или номер телефона'
        else:
            delete_user(user)
            return 'Удаление прошло успешно!'


def Button_click():
    user_data = Get_view_model()
    add_model_phonebook(user_data)


def Button_click_search():
    user_data_search = Get_user_search()
    all_user_data = search_phone_in_phonebook(user_data_search)
    return all_user_data


def Button_click_delete():
    user_data_search = Get_user_delete()
    answer = delete_user(user_data_search)
    return answer


Button_click_delete()
# Button_click()
