class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, salary, name, description, url, currency):
        self.name = name
        self.description = description
        self.url = url
        self.currency = currency
        self.salary = salary

    def __str__(self):
        """
        Метод для представления объекта пользователю
        """
        return (f"Название вакансии {self.name}\n"
                f"Заработная плата {self.salary}{self.currency}\n"
                f"Описание вакансии {self.description}\n"
                f"Ссылка на вакансию {self.url}\n")

    def __repr__(self):
        """
        Метод для представления объекта разработчику
        """
        return (f"name = {self.name}\n"
                f"salary and currency = {self.salary}{self.currency}\n"
                f"description =  {self.description}\n"
                f"url = {self.url}\n")

    def __gt__(self, other):
        """
        Метод для сравнения вакансий по зарплате
        """
        if self.salary is not None and other.salary is not None:
            if self.salary["to"] > other.salary["to"]:
                return self.salary["to"]
            return other.salary["to"]
        return "Информация о зарплате отсутсвует"