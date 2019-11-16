import unittest
import requests
from api.moblie_home import MoblieApi
from ddt import ddt, data
from utils import get_one_data
import app
import logging


@ddt
class MoblieHomeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
        cls.moblie_api = MoblieApi()
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 测试手机号归属地接口
    @data(*get_one_data(app.BASE_DIR + "/data/moblieData.json", "moblielist", "moblie"))
    # @data()
    def test02_moblie_home(self, moblie):
        response = self.moblie_api.moblie(self.session, moblie)
        logging.info(response.json())
        self.assertEqual(0, response.json().get('status'))
        self.assertEqual('ok', response.json().get('msg'))
        pass


if __name__ == '__main__':
    unittest.main()
