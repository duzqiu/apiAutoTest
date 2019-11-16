import unittest
import requests
from api.ip_query import QueryApi
from ddt import ddt, data
from utils import get_one_data
import app
import logging


@ddt
class IpQueryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
        cls.query_api = QueryApi()
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 测试ip归属地接口
    @data(*get_one_data(app.BASE_DIR + "/data/ipData.json", "iplist", "ip"))
    # @data("58.30.0.0", "180.101.49.12", "61.151.166.139")
    def test01_ip_location_query(self, ips):
        response = self.query_api.query(self.session, ips)
        logging.info(response.json())
        self.assertEqual(200, response.json().get('ret'))
        self.assertEqual('中国', response.json().get('data').get('country'))
        pass


if __name__ == '__main__':
    unittest.main()
