import unittest
from tools.HTMLTestRunner import HTMLTestRunner
from script.api_ip_location import IpQueryTest
from script.api_moblie_home import MoblieHomeTest
from script.api_weather_query import WeatherQueryTest
from script.api_new_handline import NewHandlineTest
import time

# 生成测试套件
suite = unittest.TestSuite()
# 测试用例添加到测试套件
suite.addTest(unittest.makeSuite(IpQueryTest))
suite.addTest(unittest.makeSuite(MoblieHomeTest))
suite.addTest(unittest.makeSuite(WeatherQueryTest))
suite.addTest(unittest.makeSuite(NewHandlineTest))
# 定义报告名称
# report_path = "./report/api-{}.html".format(time.strftime("%Y%m%d %H%M%S"))
report_path = "./report/apireport.html"
print(report_path)
# 使用HTMLTestRunner生成测试报告
with open(report_path, 'wb') as f:
    runner = HTMLTestRunner(f, verbosity=1, title="接口自动化测试", description="V1.0")
    runner.run(suite)
