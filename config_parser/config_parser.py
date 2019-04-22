import configparser

class ConfigParser:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(ConfigParser, *args, **kwargs)
        return cls._instance
        
    def __init__(self):
        self.parser = configparser.ConfigParser()
    
    def get_destination(self):
        self.parser.read("config.txt")
        return self.parser["destination"]["destination_folder"]
