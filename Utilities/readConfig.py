import configparser

config = configparser.RawConfigParser()
filepath = "D:\Credence\Python\ProjectOrangeHRM\configuration\config.ini"
config.read(filepath)


class Readconfig:
    @staticmethod
    def Getusername():
        username = config.get("common data", "username")
        return username

    @staticmethod
    def Getpassword():
        password = config.get("common data", "password")
        return password
