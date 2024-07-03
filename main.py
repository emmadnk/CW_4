from src.hh_api import HhApi
from src.work_with_json import WorkWithJSON
from src.sorting import sorting


def main():

    """Функция для взаимодействия с пользователем"""

    user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
    hh = HhApi()
    vacancies = hh.get_response(user_vacancy)

    f = WorkWithJSON()
    f_1 = f.maintaining_vacancies(vacancies)

    name_criterion = input('Введите критерий для отбора вакансий: \n')
    f_3 = f.get_data(name_criterion)

    u = input('Введите количество вакансий для просмотра: \n')
    quantity_vacancies = sorting(int(u))

    name_exit = input('Завершим и очистим файл вакансий да/нет : \n')
    if name_exit == 'да':
        f_4 = f.delete_vacancies()
    else:
        main()


if __name__ == '__main__':
    main()