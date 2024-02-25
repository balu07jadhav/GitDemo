import configparser
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class readconfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserMail():
        username = config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password

