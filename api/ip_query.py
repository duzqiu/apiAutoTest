from requests import Session
import app


class QueryApi(object):

    def __init__(self):
        self.requests_host = 'https://ipquery.market.alicloudapi.com/query?ip='
        pass

    def query(self, session, ip_data):
        """
        @type session:Session
        """
        requests_url = self.requests_host + ip_data
        headers = {'Authorization': 'APPCODE ' + app.APP_CODE, 'Content-Type': app.CONTENT_TYPE}
        return session.get(requests_url, headers=headers)
        pass
