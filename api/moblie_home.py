from requests import Session
import app


class MoblieApi(object):

    def __init__(self):
        self.requests_host = 'http://jshmgsdmfb.market.alicloudapi.com/shouji/query?shouji='
        pass

    def moblie(self, session, moblie_data):
        """
        @type session:Session
        """
        requests_url = self.requests_host + moblie_data
        headers = {'Authorization': 'APPCODE ' + app.APP_CODE, 'Content-Type': app.CONTENT_TYPE}
        return session.get(requests_url, headers=headers)
        pass
