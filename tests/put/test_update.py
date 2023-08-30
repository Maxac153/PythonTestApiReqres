import json
from datetime import datetime
from enum import Enum
from typing import Any

import pytest
import requests

from api.put.request_update import RequestUpdate
from api.put.response_update import ResponseUpdate
from resources.csv.reader_csv_file import ReaderCsvFile
from resources.url.url import Url


class TestUpdate:
    _CSV_FILE_PATH_REQ = '../../resources/csv/data/put/request_update.csv'
    _CSV_FILE_PATH_RES = '../../resources/csv/data/put/response_update.csv'

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
        data_req_csv, data_res_csv = data_csv
        _, name, job = data_req_csv

        req = RequestUpdate(name, job)
        url = Url.URL_BASE + Url.URL_UPDATE
        response = requests.post(url, json.dumps(req.__dict__))
        self.check_response(response.status_code, response.json(), data_res_csv)
