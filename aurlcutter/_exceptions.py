class BaseException(Exception):
    pass


class IncorrectURLException(BaseException):
    def __init__(self, message=None):
        super().__init__(f"URL is not valid: {message}")
