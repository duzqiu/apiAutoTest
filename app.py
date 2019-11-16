import logging
from logging import handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_KEY = "bcc5494393ba55eec2c107a45d215277"
APP_CODE = "ed14dfe2016d400eb6898f5656dcebf7"
CONTENT_TYPE = "application/json; charset=utf-8"


def init_logging():
    # 初始化日志
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 创建控制处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    log_path = BASE_DIR + "/log/apiTest.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename=log_path, when="D", interval=1, backupCount=7,
                                                   encoding="utf-8")
    # 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s %(funcName)s:%(lineno)d] - [%(message)s]"
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志
    logger.addHandler(sh)
    logger.addHandler(fh)
    pass
