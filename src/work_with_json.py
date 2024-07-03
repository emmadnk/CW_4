import json
from abc import ABC, abstractmethod


class AbstractJSON(ABC):
    """
    Абстрактный класс
    """
    @abstractmethod
    def get_data(self, *args):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass

    @abstractmethod
    def add_vacancy(self, *args):
        pass


class WorkWithJSON(AbstractJSON):
    """
    Класс работы с вакансиями и записью их в файл JSON
    """
    @staticmethod
    def maintaining_vacancies(vacancies):
        """
        Меитод для записи ваканский в JSON-файл
        """
        with open("/Users/karramba/PycharmProjects/pythonProject3/data/vacancies.json", "w", encoding="utf8") as file:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False, indent=4)
            file.write(vacancies_json)

    def add_vacancy(self, name):
        """
        Метод для добавления вакансий в файл
        """
        with open("/Users/karramba/PycharmProjects/pythonProject3/data/vacancies.json", "r", encoding="utf8") as file:
            list_vacancies = json.load(file)
        with open("/Users/karramba/PycharmProjects/pythonProject3/data/my_vacancies.json", "r", encoding="utf8") as file:
            list_v = json.load(file)
        for vacancy in list_vacancies:
            if name in vacancy["name"]:
                list_v.append(vacancy)
        list_vacancies_add = json.dumps(list_v, ensure_ascii=False)
        with open("/Users/karramba/PycharmProjects/pythonProject3/data/my_vacancies.json", "w", encoding="utf8") as file:
            file.write(list_vacancies_add)
        return list_vacancies_add

    def get_data(self, criterion):
        """
        Метод для получения вакансий по заданным критериям
        """
        with open("/Users/karramba/PycharmProjects/pythonProject3/data/vacancies.json", "r", encoding="utf8") as file:
            vacancies = json.load(file)
            criterion_vacancies = []
            for vacancy in vacancies:
                if not vacancy["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vacancy["snippet"]["requirement"]:
                        criterion_vacancies.append(vacancy)
        return criterion_vacancies

    def delete_vacancies(self):
        """
        Метод для удаления вакансий
        """
        list_vacancies_del = []
        list_vac = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open("/Users/karramba/PycharmProjects/pythonProject3/data/my_vacancies.json", "w", encoding="utf8") as f:
            f.write(list_vac)
