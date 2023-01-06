import re
import urllib.parse


class LinkFile:
    __filename_pattern = r'[_a-zA-Z()0-9 -]+\.\w+\Z'
    __extension_pattern = r'\w+\Z'

    def __init__(self, url):
        self.url = url
        self.url_parsed = urllib.parse.urlparse(self.url)
        self.path = self.__path()
        self.filename = self.__filename()
        self.file_extension = self.__file_extension()

    def __path(self):
        return self.url_parsed.path

    def __filename(self):
        return re.search(self.__filename_pattern, self.path).group()

    def __file_extension(self):
        return re.search(self.__extension_pattern, self.filename).group()
