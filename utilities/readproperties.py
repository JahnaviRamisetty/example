import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini ")

class Readconfig:
    @staticmethod
    def getApplicationurl():
        url = config.get('common info', 'baseurl')
        return url

