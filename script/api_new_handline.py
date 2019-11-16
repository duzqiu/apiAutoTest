import unittest
import requests
from api.new_handline import NewApi
from ddt import ddt, data
from utils import get_one_data
import app
import logging


@ddt
class NewHandlineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
        cls.new_api = NewApi()
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 测试新闻头条接口
    def test04_new_handline(self):
        response = self.new_api.news(self.session)
        logging.info(response.json())
        self.assertEqual('成功的返回', response.json().get('reason'))
        self.assertEqual('1', response.json().get('result').get('stat'))
        pass


if __name__ == '__main__':
    unittest.main()
