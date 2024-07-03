import json


def data_output():
    """
    Метод для приведения данных для вывода
    """
    with open("/Users/karramba/PycharmProjects/pythonProject3//data/vacancies.json", "r", encoding="utf8") as file:
        vacancies = json.load(file)
    user_vacancies = []
    for vacancy in vacancies:
        if not vacancy["salary"]:
            vacancy["salary"] = 0
        else:
            if vacancy["salary"] is None:
                vacancy["salary"] = 0
            else:
                if vacancy["salary"]["currency"]:
                    vacancy["currency"] = vacancy["salary"]["currency"]
                else:
                    vacancy["currency"] = "Валюта не определена"
                if vacancy["salary"]["from"] is None and vacancy["salary"]["to"] is None:
                    vacancy["salary"] = 0
                else:
                    if vacancy["salary"]["from"] is None and vacancy["salary"]["to"] is not None:
                        vacancy["salary"] = vacancy["salary"]["to"]
                    else:
                        if vacancy["salary"]["from"] is not None and vacancy["salary"]["to"] is None:
                            vacancy["salary"] = vacancy["salary"]["from"]
                        else:
                            if vacancy["salary"]["from"] is not None and vacancy["salary"]["to"] is not None:
                                vacancy["salary"] = vacancy["salary"]["to"]

        if vacancy["snippet"]["requirement"]:
            vacancy["snippet"]["requirement"] = vacancy["snippet"]["requirement"]
        else:
            vacancy["snippet"]["requirement"] = "Информация отсутствует"
        user_vacancies.append(vacancy)
    return user_vacancies