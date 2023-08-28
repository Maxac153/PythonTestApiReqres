import json
from enum import Enum

import pytest
import requests

from api.single_user.request_single_user import Request
from api.single_user.response_single_user import SingleUser
from res.csv.reader_csv_file import ReaderCsvFile
from res.url.url import BaseUrl

class ResponseStructure(Enum):
    ID = 0
    EMAIL = 1
    FIRST_NAME = 2
    LAST_NAME = 3
    AVATAR = 4
    URL = 5
    TEXT = 6


class TestSingleUsers:
    CSV_FILE_PATH = "../../res/csv/data/single_users.csv"

    @staticmethod
    def check_response(status_code: int, body, extended_result):
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

    @pytest.mark.parametrize('data_csv', ReaderCsvFile.read_csv_file(CSV_FILE_PATH))
    def test_single_users(self, data_csv):
        test_name, page = data_csv[:2]
        extended_result = data_csv[1:]

        url = BaseUrl.URL_BASE + Request.URL_SINGLE_USER + page
        response = requests.get(url)
        self.check_response(response.status_code, response.json(), extended_result)
