class BaseManager(object):
    def __init__(self, serverAddress):
        self.__serverAddress = serverAddress

    @property
    def serverAddress(self):
        return self.__serverAddress

