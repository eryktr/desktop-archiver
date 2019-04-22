import configparser

class ConfigParser:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(ConfigParser, *args, **kwargs)
        return cls._instance
        
    def __init__(self):
        self.parser = configparser.ConfigParser(open("../config.txt"))
    
    def get_destination(self):
        return self.parser["destination"]["destination_folder"]
