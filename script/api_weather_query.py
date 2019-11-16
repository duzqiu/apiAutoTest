import unittest
import requests
from api.weather_query import WeatherApi
from ddt import ddt, data
from utils import get_one_data
import app
import logging


@ddt
class WeatherQueryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
        cls.weather_api = WeatherApi()
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 测试城市天气接口
    @data(*get_one_data(app.BASE_DIR + "/data/cityData.json", "citylist", "city"))
    # @data("北京", "上海", "广州", "深圳")
    def test03_weather_query(self, city):
        response = self.weather_api.weather(self.session, city)
        logging.info(response.json())
        self.assertEqual(0, response.json().get('showapi_res_body').get('ret_code'))
        pass


if __name__ == '__main__':
    unittest.main()
