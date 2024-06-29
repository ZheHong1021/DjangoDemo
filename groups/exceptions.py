from common.exceptions import BaseException
from rest_framework import status

class InvalidGroupRequestException(BaseException):

    def __init__(self, detail):
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)