from requests import Session
import app


class NewApi(object):

    def __init__(self):
        self.requests_host = 'http://toutiao-ali.juheapi.com/toutiao/index'
        pass

    def news(self, session):
        """
        @type session:Session
        """
        requests_url = self.requests_host
        headers = {'Authorization': 'APPCODE ' + app.APP_CODE, 'Content-Type': app.CONTENT_TYPE}
        return session.get(requests_url, headers=headers)
        pass
