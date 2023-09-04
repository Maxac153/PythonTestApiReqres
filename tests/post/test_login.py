import json
import os
from enum import Enum
from typing import Any

import allure
import pytest
import requests

from api.post.login.request_login import RequestLogin
from api.post.login.response_login import ResponseLoginSuccess, ResponseLoginUnsuccess
from resources.csv.reader_csv_file import ReaderCsvFile

from resources.url.url import Url


class ResponseStructure(Enum):
    TOKEN = 1
    ERROR = 1

@allure.epic('Проверка Post метода (Login)')
class TestCreate:
    _CSV_FILE_PATH_REQ = './resources/csv/data/login/request_login.csv'
    _CSV_FILE_PATH_RES = './resources/csv/data/login/response_login.csv'

    @staticmethod
    def check_response(status_code: int, result: Any, extended_result: Any):

        if status_code == 200:
            result_data = ResponseLoginSuccess.from_json(json.dumps(result))
            assert result_data.token == extended_result[ResponseStructure.TOKEN.value]
        elif status_code == 400:
            result_data = ResponseLoginUnsuccess.from_json(json.dumps(result))
            assert result_data.error == extended_result[ResponseStructure.ERROR.value]
        else:
            raise 'Error satus code!'

    @pytest.mark.parametrize(
        'data_csv',
        ReaderCsvFile.read_two_csv_file(_CSV_FILE_PATH_REQ, _CSV_FILE_PATH_RES)
    )
    def test_login(self, data_csv):
        with allure.step('Подготовка данных'):
            data_req_csv, data_res_csv = data_csv
            _, email, password = data_req_csv
            req = RequestLogin(email, password)
            url = Url.URL_BASE + Url.URL_LOGIN
        with allure.step('Post запрос'):
            response = requests.post(url, json.dumps(req.__dict__))
        with allure.step('Проверка ответа'):
            self.check_response(response.status_code, response.json(), data_res_csv)
