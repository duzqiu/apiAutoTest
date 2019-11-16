import logging
from logging import handlers
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import configparser

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


class ConfigMessage(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.readfp(open('./config/config.ini'))

    def get_config(self, name, key):
        message = self.config.get(name, key)
        return message


class SendReport(object):

    def __init__(self, filename='report.html'):
        # 发件人邮箱账号
        self.sender = ConfigMessage().get_config('email', 'sender')
        # 发件人邮箱密码
        self.passwd = ConfigMessage().get_config('email', 'passwd')
        # 收件人邮箱账号
        self.receiver = ConfigMessage().get_config('email', 'receiver')
        # 发送的文件
        self.filename = filename

    def send_email(self):
        # print(self.sender, self.passwd, self.receiver, self.filename)
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("sender", 'utf-8')
        message['To'] = Header("receiver", 'utf-8')
        message['Subject'] = Header('测试报告', 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('测试报告请查看附件', 'plain', 'utf-8'))

        # 构造附件1，可构造多个附件
        report = MIMEText(open(self.filename, 'rb').read(), 'base64', 'utf-8')
        report["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        report["Content-Disposition"] = 'attachment;filename="report.html"'
        message.attach(report)

        # 发件人邮箱中的SMTP服务器，端口是465,25
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 括号中对应的是发件人邮箱账号、邮箱密码
        server.login(self.sender, self.passwd)
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(self.sender, [self.receiver, ], message.as_string())
        # 关闭连接
        server.quit()


if __name__ == '__main__':
    # print(ConfigMessage().get_config("email", "sender"))
    SendReport("./report/report.html").send_email()
