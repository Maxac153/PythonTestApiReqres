import json
import os
from datetime import datetime
from typing import Any

import allure
import pytest
import requests

from api.put.request_update import RequestUpdate
from api.put.response_update import ResponseUpdate
from resources.csv.reader_csv_file import ReaderCsvFile

from resources.url.url import Url


@allure.epic('Проверка Put метода (Update)')
class TestUpdate:
    _CSV_FILE_PATH_REQ = os.path.abspath('./') + '/resources/csv/data/update/request_update.csv'
    _CSV_FILE_PATH_RES = os.path.abspath('./') + '/resources/csv/data/update/response_update.csv'

    @staticmethod
    def check_response(status_code: int, result: Any, extended_result: Any):
        result_data = ResponseUpdate.from_json(json.dumps(result))
        data_now = datetime.now().strftime("%Y-%m-%d")

        if status_code == 201:
            assert result_data.createdAt.split('T')[0] == data_now
            assert result_data.id.isdigit()
        else:
            raise 'Error status code!'

    @pytest.mark.parametrize(
        'data_csv',
        ReaderCsvFile.read_two_csv_file(_CSV_FILE_PATH_REQ, _CSV_FILE_PATH_RES)
    )
    def test_update(self, data_csv):
        with allure.step('Подготовка данных'):
            data_req_csv, data_res_csv = data_csv
            _, name, job = data_req_csv
            req = RequestUpdate(name, job)
            url = Url.URL_BASE + Url.URL_UPDATE
        with allure.step('Put запрос'):
            response = requests.post(url, json.dumps(req.__dict__))
        with allure.step('Проверка ответа'):
            self.check_response(response.status_code, response.json(), data_res_csv)
