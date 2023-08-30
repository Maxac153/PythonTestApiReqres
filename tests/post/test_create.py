import json
from datetime import datetime
from enum import Enum
from typing import Any

import pytest
import requests

from api.post.request_create import RequestCreate
from api.post.response_create import ResponseCreate
from resources.csv.reader_csv_file import ReaderCsvFile
from resources.url.url import Url


class ResponseStructure(Enum):
    ID_TEST = 0
    TEST_NAME = 1
    NAME = 2
    JOB = 3
    ID = 4
    CREATE_AT = 5


class TestCreate:
    _CSV_FILE_PATH_REQ = '../../resources/csv/data/create/request_create.csv'
    _CSV_FILE_PATH_RES = '../../resources/csv/data/create/response_create.csv'

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
    def test_create(self, data_csv):
        data_req_csv, data_res_csv = data_csv
        _, _, name, job = data_req_csv

        req = RequestCreate(name, job)
        url = Url.URL_BASE + Url.URL_CREATE
        response = requests.post(url, json.dumps(req.__dict__))
        self.check_response(response.status_code, response.json(), data_res_csv)
