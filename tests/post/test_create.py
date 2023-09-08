import json
from datetime import datetime
from enum import Enum
from typing import Any

import allure
import pytest
import requests

from api.post.create.request_create import RequestCreate
from api.post.create.response_create import ResponseCreate
from resources.csv.reader_csv_file import ReaderCsvFile

from resources.url.url import Url


class ResponseStructure(Enum):
    ID_TEST = 0
    TEST_NAME = 1
    NAME = 2
    JOB = 3
    ID = 4
    CREATE_AT = 5


@allure.epic('Проверка Post метода (Create)')
class TestCreate:
    _CSV_FILE_PATH_REQ = './resources/csv/data/create/request_create.csv'
    _CSV_FILE_PATH_RES = './resources/csv/data/create/response_create.csv'

    @staticmethod
    def check_response(status_code: int, result: Any, extended_result: Any):
        result_data = ResponseCreate.from_json(json.dumps(result))
        date_now = datetime.now().strftime("%Y-%m-%d")

        if status_code == 201:
            # Нет возможности проверить так как генерируется случайным образом
            # assert result_data.id == extended_result[ResponseStructure.ID.value]
            assert result_data.createdAt.split('T')[0] == date_now
        else:
            raise 'Error status code!'

    @pytest.mark.parametrize(
        'data_csv',
        ReaderCsvFile.read_two_csv_file(_CSV_FILE_PATH_REQ, _CSV_FILE_PATH_RES)
    )
    def test_create(self, data_csv: tuple):
        with allure.step('Подготовка данных'):
            data_req_csv, data_res_csv = data_csv
            test_name, name, job = data_req_csv
            allure.dynamic.title(test_name)
            req = RequestCreate(name, job)
            url = Url.URL_BASE + Url.URL_CREATE
        with allure.step('Post запрос'):
            response = requests.post(url, req.__dict__)
        with allure.step('Проверка ответа'):
            self.check_response(response.status_code, response.json(), data_res_csv)
