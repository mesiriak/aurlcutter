class BaseException(Exception):
    pass


class IncorrectURLException(BaseException):
    def __init__(self, message=None):
        super().__init__(f"URL is not valid: {message}")


class CuttingErrorException(BaseException):
    def __init__(self, message=None):
        super().__init__(f"Error occured on trying to short the url: {message}")
