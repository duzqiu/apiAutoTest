from requests import Session
import app


class WeatherApi(object):

    def __init__(self):
        self.requests_host = 'http://ali-weather.showapi.com/day15?area='
        pass

    def weather(self, session, city_data):
        """
        @type session:Session
        """
        requests_url = self.requests_host + city_data
        headers = {'Authorization': 'APPCODE ' + app.APP_CODE, 'Content-Type': app.CONTENT_TYPE}
        return session.get(requests_url, headers=headers)
        pass
