from rest_framework.decorators import api_view
from rest_framework.response import Response
from oauth2_provider.decorators import protected_resource

@api_view(['GET'])
@protected_resource()  # Sử dụng decorator này để bảo vệ view bằng OAuth2
def hello_world(request):
    """
    Trả về một chuỗi 'Hello, world!' khi truy cập vào API endpoint.
    """
    return Response({'message': 'Hello, world!'})
