import allure
import requests

from api.delete.request_delete import Request
from resources.url.url import Url

@allure.epic('Проверка Delete метода (Delete)')
class TestDelete:
    @staticmethod
    def check_response(status_code: int):
        if status_code == 204:
            assert status_code == 204

    def test_delete_method(self):
        with allure.step('Подготовка данных'):
            url = Url.URL_BASE + Request.URL_DELETE
        with allure.step('Delete запрос'):
            response = requests.delete(url)
        with allure.step('Проверка ответа'):
            self.check_response(response.status_code)
