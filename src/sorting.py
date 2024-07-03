from src.data_output import data_output
from src.vacancies import Vacancy

vacancies_info = data_output()


def sorting(n):
    """
    Метод для сортировки и получения запрошенного количества вакансий для вывода по зарплате
    """

    sorted_list = sorted(vacancies_info, key=lambda x: x['salary'], reverse=True)
    sorted_vac = sorted_list[:n]
    sort_vacancies = []
    for vacancy in sorted_vac:
        if not vacancy["salary"]:
            vacancy["salary"] = 0
        else:
            if vacancy["salary"] is None:
                vacancy["salary"] = 0
        sort_vacancies.append(Vacancy(vacancy['name'], vacancy['salary'], vacancy['currency'], vacancy['url'], vacancy["snippet"]['requirement']))
    print(sort_vacancies)
    return sort_vacancies

