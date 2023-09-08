import json
from enum import Enum
from typing import Any

import allure
import pytest
import requests

from api.get.request_single_user import Request
from api.get.response_single_user import SingleUser
from resources.csv.reader_csv_file import ReaderCsvFile

from resources.url.url import Url


class ResponseStructure(Enum):
    ID = 0
    EMAIL = 1
    FIRST_NAME = 2
    LAST_NAME = 3
    AVATAR = 4
    URL = 5
    TEXT = 6


@allure.epic('Проверка Get метода (Single users)')
class TestSingleUsers:
    _CSV_FILE_PATH = './resources/csv/data/single_users/response_single_users.csv'

    @staticmethod
    def check_response(status_code: int, body: Any, extended_result: Any):
        if status_code == 200:
            result_data = SingleUser.from_json(json.dumps(body))
            # Data
            assert result_data.data.id == int(extended_result[ResponseStructure.ID.value])
            assert result_data.data.email == extended_result[ResponseStructure.EMAIL.value]
            assert result_data.data.first_name == extended_result[ResponseStructure.FIRST_NAME.value]
            assert result_data.data.last_name == extended_result[ResponseStructure.LAST_NAME.value]
            assert result_data.data.avatar == extended_result[ResponseStructure.AVATAR.value]
            # Support
            assert result_data.support.url == extended_result[ResponseStructure.URL.value]
            assert result_data.support.text == extended_result[ResponseStructure.TEXT.value]
        elif status_code == 404:
            assert body == {}
        else:
            raise 'Error status code!'

    @pytest.mark.parametrize('data_csv', ReaderCsvFile.read_csv_file(_CSV_FILE_PATH))
    def test_single_users(self, data_csv: tuple):
        with allure.step('Подготовка данных'):
            test_name, page = data_csv[:2]
            allure.dynamic.title(test_name)
            extended_result = data_csv[1:]
            url = Url.URL_BASE + Request.URL_SINGLE_USER + page
        with allure.step('Get запрос'):
            response = requests.get(url)
        with allure.step('Проверка ответа'):
            self.check_response(response.status_code, response.json(), extended_result)
