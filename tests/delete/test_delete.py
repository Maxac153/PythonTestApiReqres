import pytest
import requests

from api.delete.request_delete import Request
from resources.url.url import Url


class TestDelete:
    @staticmethod
    def check_response(status_code: int):
        if status_code == 204:
            assert status_code == 204

    def test_delete_method(self):
        url = Url.URL_BASE + Request.URL_DELETE
        response = requests.delete(url)
        self.check_response(response.status_code)
