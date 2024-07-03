from abc import ABC, abstractmethod

import requests
from requests import Response


class Api(ABC):
    """
    Абстрактный класс
    """
    @abstractmethod
    def get_response(self, keyword):
        pass


class HhApi(Api):
    """
    Класс для работы с API
    """
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_response(self, keyword) -> Response:
        """
        Метод для запроса вакансий через API и получение ваканский в формате JSON
        """
        response = requests.get(self.base_url, params={'text': keyword, 'area': '1', 'per_page': 100})
        vacancies = response.json()["items"]
        return vacancies

