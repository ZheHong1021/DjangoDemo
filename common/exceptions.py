from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        custom_response_data = {
            'error': response.data,  # 將原始錯誤訊息放入 `error` 屬性中
            'status_code': response.status_code  # 保留狀態碼
        }

        return Response(
            custom_response_data, 
            status=response.status_code
        )

    return response



from rest_framework import status
from rest_framework.exceptions import APIException

class BaseException(APIException):
    error = None
    status_code = None

    def __init__(self, error, code):
        super().__init__(error, code)
        self.error = error
        self.status_code = code